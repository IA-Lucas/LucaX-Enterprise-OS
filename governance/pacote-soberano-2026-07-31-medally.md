---
id: PS-2026-014
titulo: Pacote soberano da admissao do medAlly — matriz dos dois objetos, revisao independente e minuta do ato
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
canal: REPORTE
emissor: DEP-GOV
destinatario: SOBERANO
ttl: ate decisao do Soberano
resumo: Submete ao Soberano os dois objetos da admissao do medAlly com hashes medidos, revisao independente, ordem, rollback e minuta, e declara a questao bloqueante sobre a decisao 7.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# PS-2026-014 — Admissao do medAlly como primeiro Produto

> ## Este pacote **submete**. Nao decide, nao aprova, nao promulga e nao ativa nada.
>
> **`0` Produtos existem** no momento em que este pacote e escrito, e **continuarao a existir
> em numero `0`** ate que o Soberano pratique o ato. `products/` **nao existe** na raiz do
> acervo, e este pacote **nao o cria**.
>
> **Caminho exato:** `governance/pacote-soberano-2026-07-31-medally.md` *(`RE-01`)*.

> ### ⚠️ Questao bloqueante — leia antes dos objetos
>
> A decisao **7** de [PT-2026-009 §1](relatorio-transicao-2026-07-30-convergencia.md), registrada
> em [PS-2026-013 §7](pacote-soberano-2026-07-30-consolidado.md), diz:
>
> > *"O Soberano fixou **`S1`, com Produto real — `nXtrack`, se seguir sendo o primeiro produto
> > comercial** — e **`S2` deferida**."*
>
> **Este pacote submete outro produto.** A condicao *"se seguir sendo o primeiro produto
> **comercial**"* admite **duas leituras**, e **so o Soberano pode escolher entre elas** —
> `Q1` de §7. **Sob a leitura `L2`, este pacote inteiro e inadmissivel** sem um ato que altere
> aquela decisao. **A colisao esta declarada em primeiro lugar, e nao dissolvida em nota de
> rodape.**

## Proposito

Entregar ao Soberano **uma** peca com: os **dois** objetos da admissao, medidos; a prova de que
o portao `G1`–`G5` foi cumprido; a revisao independente de `DEP-QAR`; a ordem de aplicacao; o
plano de reversao; e a **minuta** do ato, com os objetos exatos.

## Escopo

| Item | Definicao |
|---|---|
| Inclui | Estado da fonte externa *(§2)* · a **matriz** dos dois objetos com `H-A`/`H-N`/`H-P` *(§3)* · o **diff de criacao** *(§4)* · a **revisao independente** *(§5)* · **ordem, caminhos e rollback** *(§6)* · as **questoes** *(§7)* · a **minuta** *(§8)* |
| **Nao** inclui | O **merito** do medAlly · **qualquer conteudo** do seu repositorio · a criacao de `Spec`, `Projeto` ou qualquer componente · o **inventario** de outro produto *(`FR-07`)* · o **fechamento de `RD-33`** |

---

## 1. Reproducao da baseline — **antes de qualquer escrita**

| Evidencia | Valor publicado | Valor reproduzido | Confere |
|---|---|---|---|
| Artefatos | **189** | **189** | ✅ |
| Linhas | **55.280** | **55.280** | ✅ |
| Impressao digital | `a3ca6ce33aa28c048d07831b5355e2f3ce0c83958bb5df42a092ff432655ca5d` | idem, **64 digitos** | ✅ |

**Copia datada tomada antes das edicoes** — `_backups/LucaX-Enterprise-OS_2026-07-31_pre-missao-1-13-4/`,
**567** arquivos, **fora do acervo**, com a baseline **reconferida na copia** (`PI-07`, `AF-35`).

### 1.1 O instrumento foi validado antes do uso — e a calibracao reprovou a primeira versao

`IR-02`/`IR-03` foram reimplementados e conferidos contra **hashes ja publicados**, **antes** de
medir qualquer objeto novo: `FND-01`, `FND-02`, `FND-03`, `FND-10` *(`CRLF`)*, `FND-11`,
`ADR-0022`, `ADR-0023`, `ADR-0024`, `ADR-0025` e `DEP-PRD` — **10 de 10 reproduzem**.

> **A primeira versao do filtro reprovou em `FND-03`.** Ela removia **toda** linha cujo texto
> antes do primeiro `:` fosse uma chave de `IR-03` — inclusive **linhas do corpo**. `FND-03` e
> a taxonomia: ela **fala sobre** os campos `status` e `ratificacao` no corpo, e o filtro os
> comia. Resultado: `9e020eda…cf7d` contra o publicado `1004673a…4b4e`.
>
> **`RA-4` de `ADR-0012` ja dizia como era:** *"o filtro e por chave de **frontmatter**"*.
> Corrigido para operar **somente dentro do bloco delimitado por `---`**, o instrumento passou a
> reproduzir **10 de 10**. **Foi exercer o instrumento contra um controle conhecido que revelou
> o defeito do instrumento** — o mecanismo de
> [`MEM-APR-0006`](../memory/aprendizado/MEM-APR-0006-exercer-o-contador-revela-o-defeito.md),
> pela segunda missao seguida. **Medir os objetos novos primeiro teria publicado hashes errados
> sem nenhum sinal de erro.**

## 2. A fonte externa — estado registrado, **somente leitura**

| Campo | Valor | Natureza |
|---|---|---|
| Caminho | `E:/LucasIA/Projetos/lucaX/My_WorkSpace/Meus_projetos/medally` | **observado** |
| Repositorio hospedeiro | `lucaX`, ramo **`main`** | **observado** |
| `HEAD` do hospedeiro | `e4458f29fb9e126bfe16068056c5fea05859e95c`, **2026-07-30 10:40:40 -0300** | **observado** |
| Commits que alcancam o caminho | **19**, de **2026-07-26** a **2026-07-30** | **observado** |
| Arquivos rastreados no caminho | **282** · **6** modificados na arvore | **observado** |
| Arquivos totais no caminho | **550** na abertura · **551** no fechamento | **observado**, nos **dois** instantes — §2.2 |
| Portoes clinico-juridicos | **7 declarados · `0` liberados** | **observado** |
| Trilhas de auditoria | **37 registros · 37 de 37 em `"ambiente": "simulacao"`** | **observado** |
| Licenca de software | **nenhuma** — `0` arquivos `LICENSE`/`LICENCA`/`COPYING` | **observado** |

> **A arvore nao foi exigida limpa, e nao esta.** Seis arquivos estao modificados sem commit, e
> **nenhum deles foi tocado por esta missao**: sao mudancas paralelas alheias, que **nao
> bloqueiam** (determinacao da missao). O que a missao garante e outra coisa — **`0` bytes
> escritos por ela**, provado em §9.

### 2.1 Zero escrita no candidato — como se prova

| Passo | O que foi feito |
|---|---|
| **Abertura** | Manifesto `sha256` de **527** arquivos *(exclui `.mypy_cache/` e `.pytest_cache/`, que mudam sozinhos)*, tomado **antes** de qualquer leitura de conteudo |
| **Durante** | Nenhuma escrita, nenhum `git`, nenhum script do repositorio executado. **A suite nao foi rodada** — rodar e escrever |
| **Fechamento** | Manifesto **remedido** e comparado linha a linha. **Ele NAO e identico** — §2.2 |

### 2.2 O candidato MUDOU durante a missao — reconciliacao, `RD-59`

**O manifesto de fechamento nao reproduz o de abertura, e a divergencia esta enumerada
integralmente**, caminho a caminho:

| Delta | Quantidade | Quais |
|---|---|---|
| **Novos** | **1** | `docs/demonstracao/felipe/tudo.html` |
| **Alterados** | **15** | **12** sob `docs/demonstracao/` *(seis paginas de `felipe/`, `links.json`, dois `.mp4`, `relatorio.json`, `ROTEIRO-NARRACAO.md`, e os dois de `video/web/`)* e **3** em `ferramentas/` — `montar_paginas_felipe.py`, `montar_pagina_video.py` e `gravar_video_institucional.py` |
| **Removidos** | **`0`** | — |

**Nenhuma escrita e atribuivel a esta missao**, e a prova nao e mais o manifesto — e o
**recorte**:

| # | Fato | Como se sabe |
|---|---|---|
| `Z1` | **Nenhum dos 16 caminhos foi lido, aberto ou executado pela missao.** Os tres `ferramentas/*.py` alterados sao **geradores de material de demonstracao**, e a missao **nao rodou script algum** no repositorio | A missao usou **apenas** leitura, contagem e `sha256`; **nenhum comando de escrita e nenhum `git` que escreva** foi emitido |
| `Z2` | **As CINCO fontes efetivamente consumidas estao byte a byte identicas** — `README.md`, `ESTADO-medally.md`, `CLAUDE.md`, `config/portoes.json` e `kb/entrevista-felipe-2026-07-23.md` | `sha256` de cada uma, conferido contra o manifesto de abertura: **5 de 5 inalteradas** |
| `Z3` | **Nenhuma contagem publicada mudou, exceto o total de arquivos** | Remedidas no fechamento: **9** sensores · **91** rotas · **11** telas · **76** modulos · **28.093** linhas de nucleo · **50** arquivos de teste · **1.298** funcoes `test_` · **32** `.md` · **37 de 37** trilhas em `simulacao` e **`0`** em qualquer outro ambiente — **todas identicas** |
| `Z4` | **O estado Git de referencia nao mudou** | `HEAD` continua `e4458f29fb9e126bfe16068056c5fea05859e95c`; **282** arquivos rastreados, identico. **As entradas sujas foram de 6 para 20** — **19 modificadas e 1 nao rastreada** —, e as **14 novas** sao **exatamente** os 16 caminhos acima menos os dois que ja estavam sujos na abertura |

> **`RD-59` — `G1` exige *"em que data foi observado"*, e data nao basta para repositorio vivo.**
> O candidato mudou **entre a abertura e o fechamento da mesma missao, no mesmo dia**. **A
> evidencia continua valida** — o instante esta fixado pelo manifesto de abertura, cujo `sha256`
> e `cc6fbbcf6943c731da27712870f94fec9af32e07babbdb8dda6f34e22e6baadc` —, **mas a norma nao
> pediu esse manifesto**: ele foi produzido por determinacao da missao, nao por `G1`. **Terceira
> lacuna medida do portao**, ao lado de `RD-54` e `RD-55`.
>
> **As contagens da Carta e de `ADR-0026` sao as do INSTANTE DE ABERTURA**, e os dois objetos
> **nao foram reeditados**: reescrever objeto ja hasheado para perseguir uma arvore viva
> **quebraria `H-A`, `H-N` e `H-P` sem ganho de verdade** — e recomecaria na medicao seguinte.
> **A reconciliacao vive aqui, que e o documento que pode mudar.**

## 3. Matriz dos objetos — `H-A` · `H-N` · `H-P`

| # | Objeto | Vigente | Candidato | Linhas | Bytes | `H-A` | `H-N` | `H-P` *(apos `O4`)* |
|---|---|---|---|---|---|---|---|---|
| **`O-1`** | **`PRO-medally`** *(Carta)* | *(nao existe)* | **1.0.0** | **359** | 26.291 | `e7b853f7298a76a4b5fe0c14d7930641887d5431a784e7674d628c1437c8f388` | `65b1bd9d87665466b199a63df03931694376919fd6b2a32e8b301c19b12aa384` | `4e16705338cc5e1d99165c6d00877d0eb833762fc58e2e0cc8ce11abc37ff29d` |
| **`O-2`** | **`ADR-0026`** | *(retido)* | **1.0.0** | **315** | 26.456 | `9e6a586da963412f2a5eef5c5222cbb824ea95c4d32cec39fe824f0bc3987da4` | `2934621c89edc6c8d3887363ff38380784bba7ce0d3ea162bc8c3a12e8af1867` | `265b29f73cdb08bd8e445d128175f533c958c2af45dd41f8a21fced292f8e8d0` |

**Objeto de origem, ja no acervo e sem `O4`** — nao entra na minuta:

| Objeto | Estado | Linhas | `H-A` = arquivo corrente | `H-N` |
|---|---|---|---|---|
| **`RFC-0021`** | `aprovado` — `FND-09 §8.2` linha `RFC`: **ratifica `—`** | **253** | `45535ae955b614e56c4f5babf3f176a18820248b3a17226f94474475e13e199b` | `10fe14cfb93295961b243ea4f6a261414cd4bb9d25fd503e4157d0b3acf28402` |

### 3.1 As tres provas de integridade, medidas

| # | Prova | Resultado |
|---|---|---|
| **`P1`** | **`H-N` invariante sob `O4`** (`IR-02`) | **2 de 2** — `H-N` do candidato e `H-N` do pos-transicao sao **identicos** nos dois objetos |
| **`P2`** | **`IR-09` — reconstrucao reproduz `H-A`** | **2 de 2**. Revertendo **apenas** `status` e `ratificacao` no frontmatter do arquivo pos-ato, o `sha256` volta a `e7b853f7…f388` e `9e6a586d…7da4` |
| **`P3`** | **O `O4` alcanca exatamente dois campos** | **`-3` bytes** em cada objeto: `em-revisao` → `ativo` *(`-5`)* e `pendente` → `ratificada` *(`+2`)*. **`atualizado_em` NAO e tocado** — altera-lo daria hash diferente do projetado |

> **`IR-10` aplicado e declarado.** Os dois objetos **nao tem `H-A` registrado por ato
> anterior**, porque **nascem nesta missao**. Este e o **primeiro vinculo** de ambos, e a
> inexistencia de alteracao anterior e provada por vias independentes: os arquivos **nao
> existiam** na copia datada de `_backups/LucaX-Enterprise-OS_2026-07-31_pre-missao-1-13-4/`,
> tomada antes da primeira escrita. **A ausencia e declarada, nunca suprida por presuncao**
> (`PI-10`, `LV-12`).

## 4. Diff de criacao

**Os dois objetos sao criacao integral.** Nao ha versao anterior, nao ha linha alterada e nao ha
linha removida — o diff **e o arquivo**.

| Objeto | Operacao | Linhas `+` | Linhas `-` | Arquivo do acervo alterado |
|---|---|---|---|---|
| **`O-1`** `PRO-medally` | `O1` **criacao** | **+359** | `0` | **nenhum** |
| **`O-2`** `ADR-0026` | `O1` **criacao**, ja executada — o arquivo esta em `decisions/` em `em-revisao` | **+315** | `0` | **nenhum** |

> **O texto nao e reproduzido aqui** (`PJ-01`). A **fonte** de `O-1` e o arquivo candidato, cujo
> caminho e hash estao em §6.1; a de `O-2` e o proprio arquivo no acervo. **Reproduzir 674
> linhas neste pacote criaria segunda fonte de verdade** e o `H-A` deixaria de discriminar.

### 4.1 Sobreposicao de diff — **zero**

| Arquivo | Objetos que o alcancam |
|---|---|
| `products/medally/carta.md` | **`O-1`**, e somente ele |
| `decisions/ADR-0026-…md` | **`O-2`**, e somente ele |

**Nenhum arquivo e alcancado por mais de um objeto**, e **cada objeto e bloqueavel isoladamente**:

| Se o Soberano bloquear | O que acontece |
|---|---|
| **`O-1`** *(Carta)* | **O ato perde o objeto.** `ADR-0026` sem Carta e decisao sem execucao: `FND-04 §6` exige a Carta como pre-condicao do Produto. **Bloquear `O-1` equivale a bloquear o ato inteiro**, e isso esta escrito para nao ser descoberto depois |
| **`O-2`** *(ADR)* | **Nada entra em `ativo`** — `G5` de `ADR-0007 §5.3`: *"sem ADR, nada entra em `ativo`"*. A Carta permanece candidata |
| **os dois** | O acervo permanece **exatamente** como esta. `RD-33` segue bloqueante, e a decisao **7** segue intacta |

> **A independencia e de forma, nao de efeito, e a diferenca esta declarada.** Diferentemente de
> `PS-2026-013`, em que catorze objetos eram bloqueaveis **com consequencia isolada**, aqui os
> dois formam **um conjunto atomico**: o Produto so existe com os dois.

## 5. Revisao independente — **DEP-QAR** *(`G4`)*

> **Impedimento conferido (`ADR-0005`, `PI-05`).** `DEP-PRD` e autor da Carta e do `ADR-0026`;
> `DEP-GOV` e autor deste pacote e executor da aplicacao futura. **`DEP-QAR` nao produziu
> nenhum dos tres**, e e quem revisa. A verificacao e **contra a norma vigente**, nunca contra a
> pratica do repositorio de origem — exigencia literal de `G4`.

| # | Verificacao | Metodo | Resultado |
|---|---|---|---|
| `V1` | Baseline anterior reproduz antes da escrita | Comando publicado em §10.9 do catalogo | ✅ **189 · 55.280 · `a3ca6ce3…ca5d`** |
| `V2` | Instrumento de hash validado contra controles publicados | 10 controles | ✅ **10 de 10**, apos correcao de um defeito real |
| `V3` | `H-N` invariante sob `O4` | `IR-02` | ✅ **2 de 2** |
| `V4` | `IR-09` reconstroi `H-A` | `IR-09` | ✅ **2 de 2** |
| `V5` | Contrato de artefato completo nos dois objetos | `AC-06`, os 15 campos + os 5 de `FND-10 §2.2` | ✅ **2 de 2** |
| `V6` | `revisor` ≠ `autor` | `AC-03` | ✅ DEP-PRD × DEP-QAR nos dois |
| `V7` | `ratificacao` coerente com a classe | `LM-02` | ✅ `pendente` nos dois; `status` maximo respeitado |
| `V8` | Vinculo a Capability **ativa** | `VC-01`, `FND-08 §8` | ✅ **5 de 5** `ativo`, conferidas no catalogo |
| `V9` | Pre-condicoes de Produto de `FND-04 §6` | *"Decisao do Soberano; publico e problema definidos; criterio de sucesso e de encerramento"* | ✅ **3 de 4 satisfeitas; a 4a e o proprio ato** |
| `V10` | Teste de existencia de `FND-03 §3.1` | *"se descontinuado, alguem perde algo?"* | ✅ **passa** — e a resposta declara que passa **pelo motivo mais fraco**: um usuario nomeado |
| `V11` | Evidencia separada por natureza | observado / alegado / inferido / desconhecido | ✅ **12** evidencias e **5** ausencias declaradas |
| `V12` | **`0` bytes admitidos do repositorio de origem** | `G3` = `REWRITE`, `AM-01` | ✅ **`0`** |
| `V13` | **`0` bytes escritos no repositorio de origem** | Manifesto `sha256`, 527 arquivos | ✅ **§9** |
| `V14` | Nenhuma `Spec`, Produto ativo, Projeto ou componente criado | Restricao da missao | ✅ **`0`** — nada entra em vigor |
| `V15` | Links relativos dos objetos resolvem no destino | Conferencia arquivo a arquivo | ✅ — **com a ressalva `R2`** abaixo |

### 5.1 Ressalvas de `DEP-QAR`

| # | Ressalva | Severidade |
|---|---|---|
| **`R1`** | **O publico primario tem um membro.** O teste de existencia passa, e passa pela margem minima. **Nao e defeito do candidato nem da Carta** — a Carta o declara em §2 e o testa em `H1` com prazo —, mas e o fato mais fragil da admissao, e a ressalva existe para que ele **nao seja lido como validado** | **Media** |
| **`R2`** | **Os links relativos da Carta candidata apontam para o DESTINO, nao para onde ela esta hoje.** Isso e **deliberado e necessario**: o `H-A` submetido tem de ser byte a byte o arquivo que sera aplicado em `products/medally/carta.md`. **Consequencia: os 9 links da Carta nao resolvem enquanto ela estiver em `_candidatos/`**, e passam a resolver **no instante da aplicacao**. **A Carta esta fora do acervo e por isso fora da varredura de links** — a prova de *"zero links quebrados"* de §9 nao a inclui, e isso esta dito em vez de suposto | Baixa |
| **`R3`** | **A evidencia `E1` da Carta — a entrevista — e `alegada`, nao `observada`.** O documento foi lido e tem proveniencia declarada; **o entrevistado nao foi consultado por esta missao**. Todo o publico primario repousa sobre ele | **Media** |
| **`R4`** | **A alegacao de *"1440 testes verdes"* nao foi reexecutada**, porque rodar a suite seria escrever no candidato. O que se mediu foi a **estrutura**: 50 arquivos, 1.298 funcoes `test_` | Baixa |

**Parecer:** os **15** controles sao conformes e as quatro ressalvas **nao impedem a submissao**.
`R1` e `R3` sao **fatos sobre a evidencia**, declarados na propria Carta; `R2` e consequencia
necessaria da regra de integridade; `R4` e limite da vedacao de escrita. **A decisao e do
Soberano, e `Q1` a precede.**

## 6. Caminhos, ordem e rollback

### 6.1 Caminhos exatos

| Objeto | Origem *(candidato)* | Destino *(acervo)* |
|---|---|---|
| **`O-1`** | `E:/LucasIA/Projetos/_candidatos-LucaX-Enterprise-OS-2026-07-31-M1.13.4/products/medally/carta.md` | `products/medally/carta.md` |
| **`O-2`** | *(ja em `decisions/`, `em-revisao`)* | `decisions/ADR-0026-admissao-do-medally-como-primeiro-produto.md` |

> **Os candidatos vivem FORA do acervo, deliberadamente.** O comando que reproduz a baseline
> **nao exclui** `_candidatos/`; manter candidatos dentro da raiz faria a contagem publicada
> deixar de reproduzir — foi o que ocorreu com `BL-2026-07-30-01`, e e o achado **`RD-53`**.

### 6.2 Ordem de aplicacao — e por que **nao** e indiferente

| Etapa | Objeto | Por que nesta posicao |
|---|---|---|
| **1** | **`O-2`** — `ADR-0026` → `ativo` · `ratificada` | **Decisao antes de execucao** (`CV-02`, `GV-06`). A Carta **so tem fundamento** depois do ADR que a autoriza; `G5` exige o ADR para que algo entre em `ativo` |
| **2** | **`O-1`** — criar `products/`, gravar a Carta e aplicar `O4` | O caminho canonico so nasce sob autorizacao da etapa 1 |
| **3** | Reconciliacao `M3` — catalogo, indices e contadores | `CV-04`, `IX-02`: **parte da mesma mudanca**, nunca trabalho posterior |
| **4** | `FIT` de aplicacao, relatorio e **nova baseline** | `BL-02`: a baseline se mede **depois** da ultima escrita |

**A dependencia 1 → 2 e real.** Inverter deixaria uma Carta de Produto em vigor sem decisao que
a fundamente — a hipotese que `INC-2026-001` registrou e `ADR-0012` fechou.

### 6.3 Como aplicar

1. **Conferir `H-A` do candidato ANTES de escrever.** Divergencia = **parar**.
2. **Aplicar por copia binaria.** Os dois objetos sao **`LF`**; conversao invalida o ato quanto a eles.
3. **`O4` apenas em `status` e `ratificacao`.** **`atualizado_em` nao entra.**
4. **Conferir `H-P` contra o projetado.** Divergencia = **`IR-05`**, incidente.
5. **`IR-09`** por **DEP-QAR**.
6. **So entao** reconciliacao, `FIT` e nova baseline.

### 6.4 Rollback

| Campo | Conteudo |
|---|---|
| **Janela barata** | **Enquanto nenhuma `Spec` existir e nenhum artefato depender de `PRO-medally`.** Nessa janela: `O8` sobre os dois objetos, remocao de `products/` **somente se a Carta nunca esteve `ativo`**, e reconciliacao dos indices |
| **Apos a primeira `Spec`** | **Remocao fisica proibida** (`RB-05`). O caminho e **`O9` — retirada**, declarando o que passa a valer no lugar (`SU-04`), com **todos** os dependentes tratados (`LC-05`, `RB-04`) |
| **Conjunto atomico** | **A reversao e por bloco.** Reverter `O-2` sem `O-1` deixaria Carta sem decisao; reverter `O-1` sem `O-2` deixaria decisao sem execucao |
| **Backup** | Copia datada de **2026-07-31**, ja tomada, **567** arquivos |
| **O que a reversao NAO desfaz** | O exercicio do portao e os achados `RD-54`/`RD-55` — eles permanecem validos ainda que o Produto seja revertido. **E `0` bytes do repositorio do medAlly**, que nunca foram tocados |
| **Quem executa** | **DEP-GOV**, sob ato do Soberano |

## 7. Questoes ao Soberano

| # | Questao | Bloqueia? |
|---|---|---|
| **`Q1`** | **A decisao 7 fixou o nXtrack como primeiro produto *comercial* (`L1`), ou como primeiro Produto *do acervo* (`L2`)?** Sob **`L1`**, este pacote **nao contraria** decisao alguma — a decisao 7 fica intacta e `PRO-nxtrack` nasce quando houver evidencia. Sob **`L2`**, este pacote **e inadmissivel** sem ato que altere a decisao 7 | ✅ **SIM** |
| `Q2` | **Emendar `ADR-0007`** para fechar as duas lacunas do portao — `RD-54` *(identidade × conteudo)* e `RD-55` *(`G3` sem classificacao para admissao de existencia)* — **ou mante-las declaradas**, com dono e gatilho? | ❌ Nao |
| `Q3` | **Confirmar o SOBERANO como aprovador de `ADR-0026`**, e nao DEP-EXE, resolvendo a colisao entre `FND-07 §2.4` e `FND-01 §7.3` + `FND-09 §8.2` a favor da autoridade mais alta (`GV-03`)? | ❌ Nao |
| `Q4` | **Confirmar o estagio `construcao`** para um produto que roda com **`0`** usuarios reais? | ❌ Nao |
| `Q5` | **`RD-56` — `TPL-carta-produto` nao preve `capabilities` no frontmatter nem os cinco campos de `FND-10 §2.2`**, embora `FND-09` E-17 os exija como atributo minimo. A Carta candidata **os declara assim mesmo**, por norma superior. **Emendar o template** *(`C2`, aprovador DEP-GOV)* ou manter declarado? | ❌ Nao |

> **Somente `Q1` bloqueia.** As outras quatro tem desfecho definido nos candidatos, com o
> fundamento escrito, e **nenhuma delas impede o ato**.

## 8. Minuta do ato — **os dois objetos, integralmente enumerados**

> ### Esta secao **nao e um ato**. Nada aqui produz efeito. **Nenhum objeto entrou em vigor.**

```
ATO SOBERANO DO FUNDADOR — <data do ato>

Apos revisar governance/pacote-soberano-2026-07-31-medally.md, a RFC-0021, o
ADR-0026, a Carta candidata de PRO-medally, os hashes, a revisao independente de
DEP-QAR com as suas quatro ressalvas, o FIT-2026-019, os riscos e as ausencias de
evidencia declaradas:

0 - RESOLVO A QUESTAO Q1, QUE PRECEDE TUDO O MAIS:

  A decisao 7 de PT-2026-009 §1 — "S1 com Produto real (nXtrack), se seguir sendo
  o primeiro produto comercial" — deve ser lida na forma
  <L1: primeiro produto COMERCIAL> ou <L2: primeiro Produto DO ACERVO>.

  Escolhida L1: a decisao 7 permanece INTACTA, e este ato pode prosseguir.
  Escolhida L2: este ato PARA AQUI, e nenhum dos itens seguintes tem efeito.

I - APROVO E RATIFICO EXPRESSAMENTE:

- ADR-0026, versao 1.0.0, C2 Tipo 1,
  SHA-256 9e6a586da963412f2a5eef5c5222cbb824ea95c4d32cec39fe824f0bc3987da4,
  cujo SHA-256 apos a transicao de estado devera ser
  265b29f73cdb08bd8e445d128175f533c958c2af45dd41f8a21fced292f8e8d0.

II - APROVO E RATIFICO A CARTA, E AUTORIZO A SUA GRAVACAO:

- PRO-medally, Carta de Produto versao 1.0.0, 359 linhas,
  SHA-256 e7b853f7298a76a4b5fe0c14d7930641887d5431a784e7674d628c1437c8f388,
  cujo SHA-256 apos a transicao de estado devera ser
  4e16705338cc5e1d99165c6d00877d0eb833762fc58e2e0cc8ce11abc37ff29d,

  gravada em products/medally/carta.md, criando-se o diretorio products/, que e o
  caminho canonico que FND-03 §3.1, FND-09 §5.6 e FND-10 §4.4 ja declaravam.

III - ORDEM OBRIGATORIA: (1) ADR-0026; (2) products/ e a Carta; (3) reconciliacao
  dos indices na MESMA mudanca; (4) Fitness Check de aplicacao, relatorio e nova
  baseline. A etapa 2 NAO precede a 1.

IV - DECLARACOES EXPRESSAS DESTE ATO:

1. O portao de ADR-0007 §5.3 foi exercido pela PRIMEIRA VEZ, sobre UM candidato
   nomeado. A classificacao G3 e REWRITE: NADA do repositorio do medAlly entra no
   acervo, e a proveniencia do que nasce e native.
2. Nenhum byte, arquivo, schema, ADR, base de conhecimento, teste ou documento do
   repositorio de origem e admitido. Cada admissao futura tera portao proprio
   (FR-07). Conteudo que entrar fora do portao e NULO (FR-03).
3. Este ato NAO autoriza operar o medAlly com paciente real, dado real de
   paciente, ambiente de producao, chamada externa nova, cobranca nova, alteracao
   de regra clinica ou alegacao regulatoria. Os SETE portoes clinico-juridicos
   permanecem FECHADOS, o unico ambiente operavel continua sendo simulacao,
   somente o medico valida e assina, e NENHUM desses portoes se abre por decisao
   deste acervo.
4. NENHUMA Spec nasce deste ato. A Carta torna SF-23 item (9) satisfazivel;
   criar a primeira Spec e mudanca PROPRIA, com DoR de nove itens e DoD de dez.
5. RD-33 NAO e fechado por este ato. Ele so fecha APOS a vigencia da Carta, por
   verificacao de missao ministerial separada, e NUNCA por inferencia.
6. As duas lacunas do portao — RD-54 e RD-55 — nascem DECLARADAS, com dono
   DEP-GOV e gatilho "segunda admissao pelo portao, ou emenda a ADR-0007". Este
   ato NAO emenda ADR-0007.
7. A entrada em vigor depende de verificacao independente de identidade, versao,
   hash integral, diff, revisao e inexistencia de alteracao entre o candidato
   revisado e o objeto aplicado. A aplicacao e por copia binaria.

V - O QUE ESTE ATO NAO FAZ:

Nao cria titular, portao, papel, classe, verbo de autoridade, entidade ou tipo
documental novo — PRO e entidade E-17 e tipo documental JA existentes, e o que
muda e a cardinalidade, de zero instancias para uma; nao altera direito de decisao
de FND-01 §7.3, principio imutavel, linha vermelha ou nivel da hierarquia
normativa; nao emenda nenhuma das onze fundacionais; nao emenda ADR-0007,
ADR-0021 nem qualquer artefato historico, MSG, FIT ou baseline; nao inventaria,
nomeia ou classifica nenhum outro produto; nao resolve RD-49, RD-47, RD-48,
RD-43, RD-13 nem RD-36; e nao alcanca qualquer objeto nao enumerado expressamente
nas secoes I e II.

VI - NENHUM Projeto, Spec, Skill, Tool, Command, Workflow, Agente, codigo ou
infraestrutura e criado, autorizado ou tornado criavel por este ato. O UNICO
efeito e a existencia formal de UM Produto.
```

## 9. Provas de fechamento — a preencher na aplicacao

| # | Prova | Estado nesta submissao |
|---|---|---|
| `F1` | `H-P` reproduzido em 2 de 2 | **projetado**; conferir na aplicacao |
| `F2` | `H-N` invariante em 2 de 2 | ✅ **medido** |
| `F3` | `IR-09` em 2 de 2 | ✅ **medido** |
| `F4` | `0` bytes fora dos diffs autorizados | conferir na aplicacao, contra a copia datada |
| `F5` | **`0` bytes escritos no repositorio do medAlly ATRIBUIVEIS A MISSAO** | ✅ **medido, e o resultado NAO e um manifesto identico** — o candidato mudou por **mudanca paralela alheia**, enumerada em **16** caminhos, **`0`** deles lidos ou executados pela missao, e as **5** fontes consumidas **inalteradas**. §2.2, `RD-59` |
| `F6` | `0` links quebrados no acervo | ✅ **medido no fechamento desta missao** |
| `F7` | `0` autoverificacoes · `0` credenciais | ✅ **medido no fechamento desta missao** |
| `F8` | Nova baseline reproduzivel | ✅ **`BL-2026-07-31-01`** — catalogo §10.10 |

## 10. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Origem | [RFC-0021](../rfcs/RFC-0021-admissao-do-medally-como-primeiro-produto.md) → [ADR-0026](../decisions/ADR-0026-admissao-do-medally-como-primeiro-produto.md) |
| Portao | [ADR-0007 §5.3](../decisions/ADR-0007-fronteira-greenfield-legado.md) — `G1`–`G4` **comprovados**, `G5` **preparado** |
| Verificacao de aptidao | [FIT-2026-019](fitness/FIT-2026-019-admissao-do-medally.md) |
| Relatorio da missao | [PT-2026-011](relatorio-transicao-2026-07-31-admissao-medally.md) |
| Achados abertos por esta missao | **`RD-53`** · **`RD-54`** · **`RD-55`** · **`RD-56`** · **`RD-57`** · **`RD-58`** — [catalogo §7](artifact-registry.md) |
| Baseline de abertura | `BL-2026-07-30-02` — **reproduzida** |
| Baseline de fechamento | **`BL-2026-07-31-01`** |

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-31 | DEP-GOV | Pacote inicial. **Dois** objetos submetidos, com `H-A`/`H-N`/`H-P` **medidos** e `IR-09` **2 de 2**; instrumento validado em **10 de 10** controles **apos** a calibracao reprovar a primeira versao; revisao independente de `DEP-QAR` com **15** controles e **4** ressalvas; ordem, caminhos e rollback declarados; **5** questoes ao Soberano, sendo **`Q1` bloqueante**; minuta com item **`0`** que resolve `Q1` **antes** de qualquer objeto. **`0` objetos em vigor.** |
