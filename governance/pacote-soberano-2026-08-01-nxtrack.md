---
id: PS-2026-016
titulo: Pacote soberano da admissao do nXtrack como primeiro Produto
tipo: pacote-soberano
versao: 1.2.0
status: ativo
camada_memoria: operacional
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-08-01
atualizado_em: 2026-08-01
revisao_prevista: null
decisoes_relacionadas: [ADR-0007, ADR-0027, ADR-0030]
substitui: []
substituido_por: null
resumo: Submete ao Soberano a admissao do nXtrack com G0 IDENTIDADE e G3 RECOGNIZE, com hashes por objeto, diff literal, rollback e minuta de ato redigida e nao emitida.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# PS-2026-016 — admissao do nXtrack

> **NENHUM ATO FOI EMITIDO.** A minuta de §6 esta **redigida e nao assinada**. Enquanto nao
> houver ato, `ADR-0030` permanece **`em-revisao`**, `products/` **nao existe** e o nXtrack
> permanece **`legacy-candidate` nao admitido**.

## Proposito

Submeter ao Soberano a **admissao da existencia** do nXtrack pelo portao de origem externa, com
os hashes por objeto, o diff literal, o rollback e a minuta do ato — para que a decisao seja
**verificavel por identidade criptografica**, nunca por confianca na descricao.

## 1. O que se pede, em uma frase

**Que o Soberano ratifique `ADR-0030`**, criando `PRO-nxtrack` como **primeiro Produto** do
LucaX Enterprise OS — **sem que um unico byte do candidato entre no acervo**.

## 2. Matriz dos objetos — `H-A` · `H-N` · `H-P`

> `H-A` = `sha256` do arquivo **tal como submetido** (`IR-07`). `H-N` = `sha256` com as linhas
> de `IR-03` removidas — **invariante ao `O4`** (`IR-02`). `H-P` = `sha256` **apos** a transicao
> `O4`, publicado **somente onde ha `O4`**.

| # | Objeto | Estado hoje | `H-A` | `H-N` |
|---|---|---|---|---|
| `O-1` | [ADR-0030](../decisions/ADR-0030-admissao-do-nxtrack-como-primeiro-produto.md) | `em-revisao` · `ratificacao: pendente` | `80b4989efbb1f256e4d6f9c09d64fff7d201dd9d1ec6afe3395417b34fcba89f` | `6325d9c11974b1958d64f1e0636bef8736c6e35fbb22e5e84094d30f7bd2b266` |
| `O-2` | [RFC-0025](../rfcs/RFC-0025-admissao-do-nxtrack-como-primeiro-produto.md) | `em-revisao` | `0db9536258d117a15b731e4a7bd01c683a630dca1f134b5e2155fdf260b1221c` | `adb4e4c40d00fc6cd55bb03de347f496f72b10e555eef9cc827f5af7e661305f` |
| `O-3` | [FIT-2026-023](fitness/FIT-2026-023-admissao-do-nxtrack.md) | `ativo` — parecer, **nao transiciona** | `331fcf47db35cc98d8ca5df0f3de9f1ee5b30963602dc351adade64c2bcc9cff` | — |
| `O-4` | [PT-2026-014](relatorio-transicao-2026-08-01-portao-nxtrack.md) | `ativo` — registro, **nao transiciona** | **`a6db51da4eeebf83a84f9dc88d5e05f9e0e15014a3131e54fd31a0ebf2217929`** — **REANCORADO na 1.1.0; o valor de 1.0.0 nao reproduz. Ver §2.3** | — |
| `O-5` | **Carta `PRO-nxtrack` 1.0.0** — **candidata, FORA do acervo** | **nao e artefato** (`FR-10`) | `4d4c12e0403344535ec410f4ff71353c1e7feaad6230bc33343f42018cea75c5` | — |

### 2.1 `H-P` — publicado **somente** onde ha `O4`

| Objeto | Transicao `O4` | `H-P` esperado |
|---|---|---|
| `O-1` **ADR-0030** | `status: em-revisao` → **`ativo`** · `ratificacao: pendente` → **`ratificada`** | `906dccd303c6240561a30ec5f62253d247567beb661a62b21d3f89b0e7c719fa` |
| `O-2` **RFC-0025** | `status: em-revisao` → **`aprovado`** | `eecde50420cb88e0619a30cd435506049567259753f8c01d8776ba1d844a7b63` |

> **Diferenca de instrumento, DECLARADA e nao silenciosa.** O `H-P` de `O-1` foi calculado pelo
> instrumento padrao (`hashes.sh hp`), que implementa `O4` como *"`em-revisao`|`aprovado` →
> `ativo`; `pendente` → `ratificada`"*. **Esse instrumento nao serve para `RFC`:** o `O4` de
> `FND-10 §5.2` e *"`em-revisao` → `aprovado` → `ativo`"*, e o ciclo de `RFC` **termina em
> `aprovado`** — precedente literal: `RFC-0022` esta `aprovado`, nao `ativo`. Aplicar o
> instrumento padrao a `O-2` produziria `status: ativo`, que **nao e a transicao pedida**. Por
> isso o `H-P` de `O-2` foi calculado por **variante explicita** *(`em-revisao` → `aprovado`,
> campo unico)*, declarada aqui para que ninguem a descubra depois.

### 2.2 Provas de integridade

| Prova | Resultado |
|---|---|
| `H-N` **invariante ao `O4`** | ✅ `O4` toca **somente** chaves de `IR-03` (`status`, `ratificacao`), que o filtro remove. `H-N` de `O-1` e `O-2` **nao muda** com o ato |
| `atualizado_em` **fora do diff** | ✅ O `O4` **nao** toca `atualizado_em` — nem no instrumento padrao nem na variante |
| **`0` bytes do candidato** | ✅ **179** hashes distintos dos 183 arquivos rastreados do candidato confrontados com **todos** os arquivos do acervo: **`0` colisoes** |
| **`0` fundacionais, `0` historicos** | ✅ `FND-01`, `FND-04`, `FND-08`, `FND-09`, `FND-10`, `FND-11`, `ADR-0007`, `ADR-0026`, `ADR-0027` e `TPL-carta-produto` **byte a byte identicos** ao `H-A` do ponto de partida — **10 de 10** |
| **Candidato intacto** | ✅ `tree` `b9b36be9…fb4b` e `HEAD` `b9fbccd…3bcb` **identicos** antes e depois; `git status` da subarvore: **`0`** linhas |

### 2.3 `RD-78` — a reancoragem de `O-4`, e a perda que ela nao apaga

> **Reancorar sem declarar a perda gravaria no acervo que `O-4` sempre foi assim.** Esta
> subsecao existe para que isso nao ocorra, por determinacao soberana de 2026-08-01.

| Campo | Valor **medido** |
|---|---|
| `H-A` publicado na 1.0.0 | `f4f63f1ebedc8f5d35e44009344df27a8631e7fd09dcd7b0826061bd632a826e` |
| `H-A` medido na 1.1.0 | `a6db51da4eeebf83a84f9dc88d5e05f9e0e15014a3131e54fd31a0ebf2217929` |
| `mtime` de `PT-2026-014` | **2026-08-01 09:13:41** |
| `mtime` deste pacote na 1.0.0 | **2026-08-01 08:59:40** |
| Intervalo | **`PT-2026-014` foi alterado 14 minutos DEPOIS** de este pacote publicar o hash dele |
| Versao de `PT-2026-014` | **`1.0.0`, inalterada** — a alteracao nao trouxe bump |
| Historico de `PT-2026-014` | **uma unica entrada**, *"Registro inicial"* — a alteracao nao deixou entrada |
| Busca pelos bytes originais | **`0` arquivos** reproduzem `f4f63f1e…a826e` em **14.112** arquivos varridos, **todas as extensoes**, em **quatro** arvores: `LucaX Enterprise OS`, `lucaX`, `_missao-1-13-4-4-2026-08-01` e `_missao-1-13-4-1-2026-07-31` |
| Diff | **IMPOSSIVEL.** Sem os bytes de origem nao ha comparacao a fazer |

**O que esta subsecao NAO afirma.** Nao se afirma **o que** mudou em `PT-2026-014`: o conteudo
anterior nao existe em nenhuma arvore alcancada, e reconstrui-lo por inferencia — do texto atual,
da versao declarada ou do proposito do documento — seria **fabricar a evidencia que se perdeu**.
Nao se afirma que a alteracao tenha sido indevida, nem que tenha sido inocua: **as duas leituras
exigiriam o diff que nao existe**. Nao se afirma que `O-4` seja o unico objeto exposto a esse
mecanismo — mediu-se `O-4` porque ele reprovou; os outros quatro reproduzem **hoje**.

**Por que importa, embora `O-4` nao transicione.** `O-4` esta na lista de `CA-4` por ser a
evidencia de que o portao `G1`–`G5` foi exercido. Nenhum item do ato o toca, e por isso a
aplicacao nao depende dos bytes dele — mas a **decisao** se apoiou neles, e a versao que a
sustentou nao e mais recuperavel.

| Campo | Valor |
|---|---|
| **Achado** | **`RD-78`** — artefato publicado e hasheado alterado sem bump de versao e sem entrada de historico, com os bytes originais nao recuperaveis |
| **Severidade** | **Alta** — atinge a reproducao de `H-A`, que e o mecanismo pelo qual o Soberano decide por identidade e nao por confianca na descricao |
| **Dono** | **DEP-GOV** |
| **Gatilho** | Missao de catalogo, ou proxima emissao de baseline — o que ocorrer primeiro |
| **Gera missao?** | **Nao** — congelamento em vigor; achado novo e registrado com dono e gatilho |

## 3. Diff literal do que o ato altera

> **Duas linhas de frontmatter, nos dois objetos que transicionam. Nada mais.**

```diff
--- decisions/ADR-0030-admissao-do-nxtrack-como-primeiro-produto.md
@@ frontmatter @@
-status: em-revisao
+status: ativo
@@ frontmatter @@
-ratificacao: pendente
+ratificacao: ratificada

--- rfcs/RFC-0025-admissao-do-nxtrack-como-primeiro-produto.md
@@ frontmatter @@
-status: em-revisao
+status: aprovado
```

**Criacao — 1 objeto, a partir de candidato de identidade provada:**

```
+ products/nxtrack/carta.md
  origem: _missao-1-13-4-4-2026-08-01/candidatos/carta-pro-nxtrack-1.0.0.md
  H-A:    4d4c12e0403344535ec410f4ff71353c1e7feaad6230bc33343f42018cea75c5
  ajuste obrigatorio na aplicacao: `status: rascunho` -> `ativo`
                                   `ratificacao: pendente` -> `ratificada`
                                   (o H-A acima e do candidato COMO ESTA; o
                                    arquivo aplicado tera H-A proprio, e a
                                    missao de aplicacao deve publica-lo)
```

> **`DF-1`.** O `H-A` publicado e o do **candidato tal como medido**, nao o do arquivo aplicado.
> Confundir os dois foi o defeito `RD-19`: *"pacote que publica `H-A` sem declarar o caminho do
> arquivo que mediu"*. **O caminho esta declarado acima.**

**Reconciliacao na mesma mudanca — projecoes `M3` (`CV-04`):** catalogo `§2`, `§4`, `§7`, `§9`,
`§10` · `decisions/README` · `rfcs/README` · `governance/README` · `governance/fitness/README`
· `README` da raiz.

## 4. Rollback por objeto

| Objeto | Como reverter | Custo |
|---|---|---|
| `O-1` `ADR-0030` | `ADR` de retirada (`O9`) superando-o. `status` volta por ato proprio — **nao por edicao** | 1 `ADR` |
| `O-2` `RFC-0025` | Acompanha `O-1`; `RFC` sem `ADR` vigente e proposta arquivada | `0` |
| `O-3` `FIT-2026-023` | **Nao se reverte** — parecer emitido e registro historico (`BL-02`, `LV-04`) | `0` |
| `O-4` `PT-2026-014` | **Nao se reverte** — idem | `0` |
| `products/nxtrack/carta.md` | Removida; o nXtrack volta a `legacy-candidate` **nao admitido** | 1 arquivo + 1 entrada de `§9` |
| Projecoes `M3` | Reconciliadas na mesma mudanca da reversao | 5 indices |
| **Ponto de rollback integral** | `H-A` de **208** artefatos em `_missao-1-13-4-4-2026-08-01/evidencia/H-A-ponto-de-partida-1-13-4-4.txt`, `sha256` `e48f5908d8d4fbf9484ffacb564f71ee5fa1ebcc2aa99905cb5e859e1faa3caf` | — |
| **Copia datada** | `_backups/LucaX-Enterprise-OS_2026-08-01_pre-missao-1-13-4-4` — **586 arquivos**, baseline reconferida **na copia** | — |

**Janela de reversao trivial: enquanto `RD-33` nao fechar.** Depois da primeira `Spec`
derivada, reverter exige tratar a `Spec` (`EV-06`), e o custo deixa de ser trivial.

## 5. Classe, aprovador e o que se pede

| Campo | Valor | Fundamento |
|---|---|---|
| Classe | **`C2` — Estrutural** | `FND-04 §2`: *"cria (…) um componente"*, exemplo textual *"criar produto"* |
| Reversibilidade | **`Tipo 1`** | `FND-09 E-17`: *"Criacao e encerramento sao `Tipo 1`, decididos pelo Soberano"* — **fixado por norma, nao pelo custo medido** |
| Aprovador | **SOBERANO** | `FND-04 §6`, linha **Produto** |
| Ratificacao | **EXIGIDA** | `FND-04 §2.2` + `PI-06` |
| `RFC` | **EXIGIDA** | Dispensa indisponivel: tres alternativas defensaveis (`ADR-0030 §11.2`) |
| Fitness Check | **EMITIDO** | `CV-07`; `FIT-2026-023`, `apto-com-ressalva` |

## 6. Minuta do ato soberano — **redigida e NAO emitida**

### 6.1 Condicoes ANTERIORES de eficacia — conferidas **antes** de escrever

| # | Condicao | Estado |
|---|---|---|
| `CA-1` | `ADR-0027` **`ativo`**, tornando `G0` e `RECOGNIZE` disponiveis | ✅ **conferido no frontmatter** |
| `CA-2` **INFORMATIVO** *(§6.1.1)* | **Registrar a baseline vigente no instante da aplicacao** — a que estiver publicada em `artifact-registry §10.0`, qualquer que seja | **NAO PARA, e nao abre incidente.** O trio medido entra no relatorio de transicao. Divergencia contra qualquer valor congelado e **esperada** num acervo vivo; a ancora deste ato sao os `H-A` **por objeto** de `CA-4`, nunca a arvore inteira |
| `CA-3` | `G1` a `G5` **cumpridos e registrados** | ✅ `PT-2026-014 §3` |
| `CA-4` | Os cinco objetos reproduzindo os `H-A` publicados | ✅ **5 de 5** |
| `CA-5` | Candidato **intacto** — nenhuma escrita da missao no repositorio de terceiro | ✅ `tree` e `HEAD` identicos |
| `CA-6` | **`Q2` respondida** — se a ressalva de `PS-2026-013 §7` condiciona o ato | ✅ **RESPONDIDA** por despacho soberano de **2026-08-01**: a ressalva **NAO** condiciona o ato (`RD-64`). Ver a ressalva a seguir |

> **`CA-6` e a unica condicao aberta, e ela e deliberada.** O pacote **nao presume** a resposta:
> a ressalva comercial esta em documento distinto da decisao, e quem a resolve e o Soberano.
>
> **Emenda 1.1.0 — estado das condicoes, atualizado.** `Q2` foi **respondida** por despacho
> soberano de 2026-08-01, e `CA-6` esta conferida. **A decisao ainda NAO esta gravada como
> artefato**, por determinacao do proprio despacho, que a reteve ate a reassinatura deste
> pacote — de modo que `CA-6` se apoia, neste instante, em despacho e nao em artefato do
> acervo. **`CA-4` foi reconferida sobre o `H-A` reancorado de `O-4`** (§2.3); ela era **`4` de
> `5`** contra os valores da 1.0.0.
>
> **Etiqueta, corrigida antes de gravar.** A questao respondida e o **`Q2` deste pacote, §8** —
> **nao** o `Q2` de `PS-2026-014 §7`, que e o pacote do **medAlly** e cujo `Q2` ja foi respondido
> no **oitavo ato** (`MSG-2026-0008 §2`, item I). O catalogo registra a linhagem correta em
> `artifact-registry §10.0`: *"a ressalva de `PS-2026-013 §7` vira `Q2` de `PS-2026-016`"*.

#### 6.1.1 Por que `CA-2` e INFORMATIVO — o motivo, escrito

> **A condicao nasceu insatisfazivel POR CONSTRUCAO, nao por desvio de ninguem.** Na forma da
> `1.0.0`, `CA-2` exigia que a baseline vigente **reproduzisse** no instante da aplicacao. **O
> pacote que publica essa condicao mora dentro do acervo que ela mede** — e por isso **qualquer
> emissao legitima a invalida**, inclusive as emendas que o proprio Soberano ordenou.

| # | O que se mediu | Resultado |
|---|---|---|
| 1 | O pacote **entra na medicao** que a condicao exige | `governance/pacote-soberano-2026-08-01-nxtrack.md` esta na raiz `governance`, **dentro da lista fechada positiva** de `baseline.sh`. Editar este arquivo **muda o numero que este arquivo exige** |
| 2 | A emenda de reancoragem (`1.1.0`), **ordenada pelo Soberano**, ja moveu o valor | `BL-2026-08-01-01` **213 · 62.250 · `4252fe47…621c`** → medido **213 · 62.300 · `b5966814…70ca`**. **`+50` linhas**, **`0` artefatos novos**, **`0` normas alteradas** |
| 3 | O delta e **integralmente atribuivel** | Varredura por `mtime` na lista fechada: **um unico** `.md` alterado — este pacote. `+50` linhas medidas no arquivo batem com `+50` no total |
| 4 | Esta emenda (`1.2.0`) **movera outra vez** | E a segunda emissao legitima a invalidar a mesma condicao **em menos de um dia**, e nenhuma delas tocou um byte dos cinco objetos |
| 5 | Os **cinco** objetos, nas duas emendas | **`0` bytes tocados.** **5 de 5** `H-A` reproduzem os publicados em §2 — **remedidos nesta emissao** |

> **Duas emendas que o Soberano ordenou, e que nao tocaram nenhum dos cinco objetos, ja teriam
> PARADO a aplicacao** pela forma anterior de `CA-2`. Nao ha conduta que corrija isso: a condicao
> fica **mais falsa a cada registro legitimo**, e assinar sob ela seria prometer que **nada mais
> sera escrito no acervo** ate a aplicacao — o que um acervo vivo nao pode prometer.

**O que protege o texto assinado e `CA-4`**, e a protecao e **por objeto consumido**:

| Ancora | Cobre | Quantos `sha256` | Efeito da divergencia |
|---|---|---|---|
| **`CA-4`** | os **5** objetos do pacote — §2 | **5** | **PARAR.** Objeto diferente do submetido |
| **`CA-5`** | o candidato, que tem de sair **intacto** — `tree` e `HEAD` | **2** objetos de commit | **PARAR.** Escrita em repositorio de terceiro |
| **Total conferido no instante da aplicacao** | os 5 objetos **mais** o candidato | — | — |

> **Se um dos cinco divergir, o ato PARA** — e foi exatamente o que ocorreu com `O-4`, que a
> `1.1.0` reancorou (§2.3). **Se a arvore andar por trabalho que nao toca nenhum deles, nada muda
> para este ato.** Ancoragem **por objeto consumido, nunca por arvore inteira**.

| O que a correcao **NAO** faz | Verificacao |
|---|---|
| **Nao afrouxa `CA-1`, `CA-3`, `CA-4`, `CA-5` nem `CA-6`** | As cinco seguem **bloqueantes**, com **`0` bytes** tocados no texto delas — exceto o estado de `CA-4` e `CA-6`, atualizado por determinacao soberana e registrado no historico |
| **Nao dispensa medir a baseline** | Ela continua **medida e registrada** no relatorio de transicao; o que cai e a exigencia de **igualdade contra valor congelado** |
| **Nao alcanca `PS-2026-015`** | Aquele pacote ja traz a correcao em `§6.1.4.1` e no item **VI** do seu ato; **`0` bytes** nele |

##### `RD-79` — a correcao soberana nao alcancou o pacote seguinte

| Campo | Valor |
|---|---|
| **Achado** | **`RD-79`** — o Soberano ja emitira esta mesma correcao em `PS-2026-015 §6.1.4.1` e no item **VI** daquele ato, em **2026-07-31**. Ela **nao alcancou** `PS-2026-016`, emitido no dia seguinte, porque **viveu num pacote e nao no molde de pacote soberano**: cada pacote redige as suas condicoes do zero, e um defeito corrigido num deles renasce no proximo |
| **Regra que o achado fixa** | **Toda condicao anterior de eficacia que meca a arvore inteira nasce insatisfazivel e deve nascer INFORMATIVA.** Ancoragem de ato e **por objeto consumido** |
| **Severidade** | **Alta** — reincidencia de defeito ja corrigido pelo Nivel 0, em **um dia**, no instrumento que submete decisao ao Soberano |
| **Dono** | **DEP-GOV** |
| **Gatilho** | Proxima emissao de pacote soberano, ou missao que tocar o molde/`TPL` de pacote soberano — o que ocorrer primeiro |
| **Gera missao?** | **Nao** — congelamento em vigor; achado novo e registrado com dono e gatilho |

### 6.2 Ordem de aplicacao

1. Conferir os **5** `H-A` publicados em §2.
2. `O4` em `RFC-0025`: `status` → `aprovado`.
3. `O4` em `ADR-0030`: `status` → `ativo`; `ratificacao` → `ratificada`.
4. Criar `products/nxtrack/carta.md` a partir do candidato `4d4c12e0…75c5`, com `status: ativo`
   e `ratificacao: ratificada`; **publicar o `H-A` do arquivo aplicado**.
5. Reconciliar catalogo `§2`, `§4`, `§7`, `§9`, `§10` e as projecoes `M3` — **na mesma mudanca**.
6. Acrescentar `products` a lista fechada positiva de `baseline.sh` — **a raiz nova precisa ser
   declarada, ou o portao de raiz recusa medir** *(e essa recusa e o comportamento correto)*.
7. Emitir nova baseline e reproduzi-la em **duas** execucoes.

> **`OA-1` — o passo 6 nao e detalhe de ferramenta.** `baseline.sh` mede por **lista fechada
> positiva** e **para com erro** diante de raiz nao declarada. Criar `products/` sem declara-la
> **impede medir a baseline** — e isso e o portao funcionando, nao falha.

### 6.3 Limites deste ato — o que ele **NAO** faz

| # | O ato **nao** |
|---|---|
| `LA-1` | Admite **conteudo** algum do candidato. `G0` e `IDENTIDADE`; **`0` bytes**. Admitir conteudo depois e **passagem nova pelo portao** (`FR-07`, `AD-02`) |
| `LA-2` | Autoriza inventariar o repositorio do candidato |
| `LA-3` | Cria `Spec`, nem fecha `RD-33` — que **so fecha apos a vigencia**, por missao propria |
| `LA-4` | Decide `E2`. `RFC-0023`, `ADR-0028` e `FIT-2026-021` seguem **intactos**; fila de retidos: **2** |
| `LA-5` | Altera `ADR-0007`, `ADR-0026` ou qualquer fundacional — **`0` bytes** |
| `LA-6` | Afirma merito tecnico do nXtrack. `RECOGNIZE` **declara que nao avaliou** |
| `LA-7` | Resolve a custodia do candidato (`RD-71`), a lacuna de politica de dado pessoal (`LM-6`) ou `VC-03` (`RD-74`) — **os tres sao trabalho da primeira `Spec`** |

### ATO SOBERANO — ADMISSAO DO nXtrack *(minuta, NAO emitida)*

> Eu, Soberano do LucaX Enterprise OS, no exercicio da competencia que `FND-04 §6` me atribui
> sobre a criacao de Produto (`C2` · `Tipo 1`), e tendo conferido as condicoes anteriores de
> eficacia de `PS-2026-016 §6.1`:
>
> **I.** **RATIFICO** `ADR-0030`, que admite a **existencia** do nXtrack pelo portao de
> origem externa de `ADR-0007 §5.3`, com **`G0` = `IDENTIDADE`** e **`G3` = `RECOGNIZE`**, nos
> termos de `ADR-0027 §5.1` e `§5.2`.
>
> **II.** **APROVO** `RFC-0025`, instrumento de origem da decisao.
>
> **III.** **CRIO** o Produto **`PRO-nxtrack`**, em `products/nxtrack/carta.md`, a partir do
> candidato de `H-A` `4d4c12e0403344535ec410f4ff71353c1e7feaad6230bc33343f42018cea75c5`, com
> as **cinco** Capabilities declaradas e o criterio de encerramento de §6 da Carta.
>
> **IV.** **DECLARO** que este ato admite **identidade e nada mais**: **`0` bytes** do
> repositorio do candidato entram no acervo, e cada peca dele que um dia queira entrar tera
> **portao proprio**.
>
> **V.** **DECLARO** que este ato **nao afirma merito tecnico** do nXtrack, **nao valida** a
> hipotese central `H1`, **nao mede** usuarios reais e **nao resolve** a custodia fora do
> acervo — as quatro ressalvas de `FIT-2026-023` seguem **abertas, com dono e gatilho**.
>
> **VI.** **DETERMINO** que a aplicacao siga a ordem de `PS-2026-016 §6.2`, reconciliando
> catalogo e indices **na mesma mudanca** e declarando `products` na lista fechada do medidor
> **antes** de reemitir a baseline. **`CA-1`, `CA-3`, `CA-4`, `CA-5` e `CA-6` sao BLOQUEANTES:**
> falha em qualquer uma **para a aplicacao**. **`CA-2` e INFORMATIVO e nao para nada:** a
> baseline vigente e **medida e registrada**, jamais exigida como igualdade contra valor
> congelado, porque **o pacote mora dentro do acervo que ela mede** e toda emissao legitima a
> invalidaria — inclusive as emendas que ordenei. **A ancora deste ato sao os `5` `sha256` por
> objeto de `CA-4`, mais o `tree` e o `HEAD` do candidato em `CA-5`** — **nunca a arvore
> inteira** (§6.1.1).
>
> **VII.** **DECLARO** que este ato **nao cria `Spec`, nao fecha `RD-33` e nao decide `E2`**.
>
> `_______________________________`
> **Soberano** · data: `__________`

## 7. Rastreabilidade — decisao → portao → instrumento → minuta

| Elo | Objeto |
|---|---|
| Decisao do Soberano que originou | `PT-2026-009 §1`, decisao **7** — *"Via futura e `S1` com Produto real (`nXtrack`)"* |
| Portao aplicado | `PT-2026-014 §3` — `G0` a `G5` |
| Proveniencia | `ITEM-0-proveniencia-nxtrack.md` — 17 de 17 atribuiveis; `tree` `b9b36be9…fb4b` |
| Instrumento de origem | `RFC-0025` |
| Decisao | `ADR-0030` |
| Parecer independente | `FIT-2026-023` — `apto-com-ressalva` |
| Objeto criado pelo ato | Carta `PRO-nxtrack`, `H-A` `4d4c12e0…75c5` |
| Minuta | §6 — **redigida e nao assinada** |

## 8. Questoes ao Soberano

| # | Questao | Por que so o Soberano responde |
|---|---|---|
| **`Q2`** | **A ressalva *"se seguir sendo o primeiro produto comercial"* de `PS-2026-013 §7` condiciona este ato?** A decisao **7** de `PT-2026-009` nomeia o nXtrack **sem ressalva**, e a oracao mora em **artefato distinto** — a palavra `comercial` tem **`0`** ocorrencias no arquivo de `PT-2026-009`. **O executor nao pode escolher qual dos dois textos prevalece** | É interpretacao de ato proprio do Nivel 0 |
| **`Q3`** | **Qual e a meta do criterio de sucesso?** O candidato define **o que medir** *(% de sessoes com recomendacao aceita e salva em playlist)* e **nao define quanto**. A Carta deixou a meta **em aberto** em vez de inventar numero | Criterio de sucesso de Produto e decisao de Soberano (`FND-04 §6`) |
| **`Q4`** | **A admissao deve esperar politica de dado pessoal?** O candidato tem **dado real**, **dado pessoal por desenho** e **aprendizado coletivo entre usuarios**, e o acervo tem **`0`** artefato que governe isso (`LM-6`, `FG-11`). Hoje o risco esta contido pelo **loopback**; ele se realiza **na publicacao** | É tradeoff de exposicao, nao de forma |

> **As tres sao perguntas, nao pedidos de aprovacao.** O ato de §6 pode ser assinado com
> qualquer resposta a `Q3` e `Q4` — **so `Q2` e condicao anterior de eficacia** (`CA-6`).

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.2.0 | 2026-08-01 | DEP-GOV | **Despacho do Fundador: `CA-2` passa de bloqueante a INFORMATIVO, ANTES da assinatura.** A condicao e **insatisfazivel por construcao** — o pacote mora dentro do acervo que ela mede, e a propria emenda `1.1.0`, ordenada pelo Soberano, ja a invalidou: `213 · 62.250 · 4252fe47…621c` → `213 · 62.300 · b5966814…70ca`, **`+50` linhas** integralmente atribuidas a este arquivo. **§6.1.1, nova**, escreve o motivo, mede as cinco provas e declara a ancora correta — **por objeto consumido, nunca por arvore inteira**. **A correcao alcanca as DUAS metades:** a tabela de §6.1 **e** o item **VI** do ato, que agora enumera quais condicoes sao bloqueantes e diz que `CA-2` nao para nada. Corrigir so a tabela deixaria o guarda vivo na metade assinada — foi o que se verificou. Verificado tambem que o efeito **nao** se repete em outro ponto: §6.2 passo 7 pede **reproduzir a nova baseline em duas execucoes** *(autoconsistencia, nao igualdade contra valor congelado)*, e este pacote **nao declara condicoes posteriores**. Abre **`RD-79`** *(dono DEP-GOV; gatilho: proxima emissao de pacote soberano ou missao que toque o molde; **nao gera missao**)*: a mesma correcao ja emitida em `PS-2026-015 §6.1.4.1` e no item VI daquele ato **nao alcancou este pacote porque viveu num pacote e nao no molde**. **`0` bytes** em `O-1`, `O-2`, `O-3`, `O-5`, em `PS-2026-015` e em qualquer fundacional. Dentro de §6: **itens I a V e VII identicos**; mudaram **§6.1** e **o item VI**, ambos por determinacao expressa. |
| 1.1.0 | 2026-08-01 | DEP-GOV | **Emenda de reancoragem, por determinacao soberana de 2026-08-01.** A conferencia de `CA-4` **lendo os `H-A` do proprio arquivo, e nao da transcricao** — ordenada pelo despacho de emissao — mediu **`4` de `5`**: `O-4` (`PT-2026-014`) **nao reproduzia** o `H-A` publicado na 1.0.0. §2 reancora `O-4` no `H-A` vigente `a6db51da…7929`, e a **§2.3, nova**, caracteriza a perda e abre **`RD-78`** *(dono DEP-GOV; gatilho: missao de catalogo ou proxima baseline; **nao gera missao**, congelamento em vigor)*. A caracterizacao e **condicao** da reancoragem: reancorar em silencio gravaria que `O-4` sempre foi assim. **Os bytes originais de `O-4` nao existem** em **14.112** arquivos de **quatro** arvores — **nao ha diff, e nada foi reconstruido por inferencia**. §6.1 registra `CA-6` **respondida** por despacho *(decisao ainda nao gravada como artefato)* e corrige a **etiqueta** da questao: e o `Q2` **deste** pacote §8, nao o de `PS-2026-014 §7`, ja respondido no oitavo ato. **`0` bytes** em `O-1`, `O-2`, `O-3`, `O-5` e em qualquer fundacional. **O que mudou dentro de §6, com precisao:** o bloco **`ATO SOBERANO`, itens I a VII, e byte a byte IDENTICO** *(sha256 do bloco: `647f835d…e309`)*, e **§6.2** e **§6.3** tambem; **§6.1 mudou** — e so ele —, porque a reconferencia das condicoes foi ordenada pelo mesmo despacho. Toda a minuta **mudou de faixa de linhas**: era **148–224**, e a nova faixa vai ao Soberano junto com o `H-A` novo do pacote. **O ato emitido sobre a 1.0.0 nao foi gravado**, por determinacao do mesmo despacho, que reteve o registro ate a reassinatura. |
| 1.0.0 | 2026-08-01 | DEP-GOV | Pacote inicial. Submete a admissao do nXtrack com **5** objetos hasheados, `H-P` publicado **so onde ha `O4`** — com a **diferenca de instrumento entre `ADR` e `RFC` declarada** —, diff literal de **duas** linhas de frontmatter, rollback objeto a objeto, minuta **redigida e nao emitida** e **tres** questoes ao Soberano, das quais **so `Q2`** e condicao anterior de eficacia. |
