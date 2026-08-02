---
id: FIT-2026-024-primeira-spec
titulo: Verificacao de aptidao da primeira Spec do acervo — SPC-001, ADR-0031 e RFC-0026
tipo: fitness
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-QAR
proprietario: DEP-QAR
aprovador: DEP-EXE
criado_em: 2026-08-02
atualizado_em: 2026-08-02
revisao_prevista: 2027-02-02
decisoes_relacionadas: [ADR-0031, ADR-0021, ADR-0022, ADR-0030]
substitui: []
substituido_por: null
objeto_avaliado: [ADR-0031, RFC-0026, SPC-001]
classe_mudanca: C2
veredito: apto-com-ressalva
---

# FIT-2026-024: A primeira `Spec` do acervo

## Proposito

Verificar se a criacao da **primeira `Spec` real do LucaX Enterprise OS** deixou a arquitetura
**mais apta a evoluir** — nao apenas correta. `FIT` **exigido**, nao opcional: a classe do objeto
e **`C2`**, e `SF-24` item **(9)** o torna item de `DoD`.

> **Independencia, e como ela e satisfeita aqui.** `FT-02` e `LV-03` proibem que a verificacao
> seja executada por quem produziu o objeto. Autor deste parecer: **DEP-QAR**. Produtor dos
> objetos: **DEP-PRD**. Forma verificada por **DEP-GOV**. **Divergencia de campo `autor` ≠
> `revisor` satisfeita.** O **segundo** criterio — independencia por fornecedor — **nao** e
> satisfeito, como nao e em **130 dos 137** artefatos do acervo que declaram os dois campos: e
> divida **declarada**, nao silenciada.

## Escopo

| Item | Definicao |
|---|---|
| **Objeto avaliado** | [`SPC-001`](../../products/nxtrack/specs/SPC-001-governanca-de-dado-pessoal-do-nxtrack.md) · [`ADR-0031`](../../decisions/ADR-0031-primeira-spec-governanca-de-dado-pessoal-do-nxtrack.md) · [`RFC-0026`](../../rfcs/RFC-0026-primeira-spec-governanca-de-dado-pessoal-do-nxtrack.md) |
| **Estado anterior** | `BL-2026-08-01-03` — **218** artefatos, **`0`** de tipo `spec`, `SF-01`–`SF-32` **determinadas e nao observadas** (`L1` de `FND-11 §14`) |
| **Nao inclui** | A corretude do **merito juridico** — que nao e materia deste acervo nem deste parecer · a corretude estrutural, do Architecture Review · o nXtrack, que **nao foi tocado** |

## Responsaveis

| Papel | Quem |
|---|---|
| Executa *(independente do produtor)* | **DEP-QAR** |
| Forma | **DEP-GOV** |
| Evidencia | **DEP-KMS** |
| Aprova | **DEP-EXE** |
| Ratifica *(se `C3`)* | **n/a** — o objeto e `C2` |

---

## Sumario

| # | Pergunta | Resposta | Sinal |
|---|---|---|---|
| **F1** | Complexidade aumentou sem ganho proporcional? | **nao** | **+3** artefatos e **+1** tipo documental instanciado, contra **10** requisitos verificaveis onde havia **`0`** |
| **F2** | Algum conceito foi duplicado? · a prevencao foi aplicada? | **nao** · **aplicada** | **`0`** conceitos redefinidos · **`1`** reproducao barrada antes de escrita |
| **F3** | Alguma abstracao ficou desnecessaria? | **nao** | **`0`** abstracoes novas; **`0`** entidades, tipos, portoes ou papeis criados |
| **F4** | Continua mais simples de evoluir? | **sim, com custo** | Criar a 2a `Spec` custa **2** artefatos, nao 5 — o `ADR` de classe **nao se repete** |
| **F5** | Custo de contexto subiu ou desceu? | **desce** *(e sobe na leitura integral)* | **13** linhas para consultar `SPC-001 RQ-3`, contra **555** que antes nao respondiam |
| **F6** | Favorece reutilizacao? | **sim** | **27 de 32** regras `SF-*` saem de *determinadas* para *observadas* — todas as `Spec`s futuras herdam o precedente |

**Veredito:** `apto-com-ressalva` — **4 ressalvas**, todas com dono e gatilho.

---

## F1 — A complexidade aumentou sem ganho proporcional?

| Medida | Antes | Depois | Variacao |
|---|---|---|---|
| Entidades instanciadas | 11 de 21 | 11 de 21 | **`0`** |
| Tipos documentais com instancia | 18 de 33 | **19 de 33** | **+1** — `Spec` sai de *sem instancia* |
| Artefatos do acervo | **218** | **221** *(+`RFC`, +`ADR`, +`SPC`; o `FIT` e o `PT` entram depois)* | **+3** nesta medicao |
| Regras normativas criadas | — | **`0`** | `SF-01`–`SF-32` foram **exercidas**, nunca emendadas: **`0` bytes** em `FND-01`–`FND-11` |
| Responsabilidades orfas resolvidas | `FG-11` — *"`0` artefato governa dado pessoal de usuario final"* | **resolvida para `1` produto** | **+1** |
| Regras removidas ou unificadas | — | **`0`** | |

**Leitura.** O acrescimo corresponde a um problema **nomeado pelo proprio Soberano** no nono ato:
`LM-6(a)`, materia da primeira `Spec` **com prioridade**. O ganho e contavel: onde havia
**`0`** exigencias verificaveis sobre dado pessoal, ha **10**, com **60** campos de `SF-12`,
**`0`** ausentes, e **10 de 10** criterios verificaveis por terceiro sem consultar o autor.

**O custo tambem e contavel, e nao e pequeno:** **5** artefatos para **1** `Spec`. A causa esta
medida — a colisao de `SF-10` obrigou a classe `C2`, e `C2` puxa `RFC`, `ADR` e este `FIT`. **A
proxima `Spec` sem colisao propria custa 2.** Ressalva `R-1`.

**Resposta: nao** — o acrescimo tem problema nomeado, dono e ganho contavel.

## F2 — Algum conceito foi duplicado?

### F2.a — Ocorrencia

| Conceito | Onde ja estava definido | Como a mudanca o trata |
|---|---|---|
| Regras de privacidade do produto | `spec-tecnica-v1.md §24` do **candidato**, **fora do acervo** | **Citado como `FATO` `F-5`, com linha e arquivo** — nunca transcrito como norma. `RQ-3` e `RQ-4` **partem** dele em vez de reinventa-lo |
| Risco de aprendizado coletivo | `PRO-nxtrack §11`, risco `R2` | **`refina`** (`R-04`), declarado no Bloco 15. Nao redefine: **detalha sem contradizer** |
| Lacuna `LM-6(a)` | `PT-2026-014 §4`; `MSG-2026-0009 §2` | **Remedida**, e a remedicao **reproduz** — `0` nos seis termos. Nao ha segunda definicao da lacuna |
| Autoridade sobre `Spec` | `FND-09 §8.2`, `FND-04 §2`, `SF-10` | **Derivada e mostrada** no Bloco 5, com a fonte de cada variavel. **`0` autoridade declarada dentro da `Spec`** (`AC-01`, `SF-03`) |
| Classes de mudanca | `FND-04 §2` | **Remetida**, nunca reproduzida em tabela |

**Verificacao aplicada:** varredura por definicao repetida sobre os tres objetos; `MM-01` e
`LX-07`. **`0`** conceitos redefinidos.

### F2.b — Prevencao aplicada **antes** da submissao

| Verificacao | Evidencia | Resultado |
|---|---|---|
| O autor percorreu **cada** tabela pelo item `PJ-05`? | **Tabelas examinadas:** as 10 de requisito *(originais)*; `13.0 FATO` *(original — medicao propria)*; `13.2` e `13.3` *(derivadas de `SF-25`/`SF-17`, sao **conferencia**, nao exibicao de conteudo alheio)*; Bloco 5 *(exibe **valores apurados**, com a fonte por linha)*; Bloco 1 *(conferencia de contrato, exibe **nomes de campo**, nao conteudo)*; Bloco 16 *(exibe **estado** de dependencia — `LN-03`)* | ✅ **executado** |
| Toda tabela que exibe conteudo de outra fonte declara **projecao** com as quatro informacoes de `PJ-02`? | **Nenhuma tabela da `Spec` exibe conteudo de outra fonte.** Bloco 5 exibe **derivacao**, com fonte por linha; Bloco 16, **estado**. **`0` declaracoes `PJ-02` sao devidas**, e a ausencia e **resultado da conferencia**, nao omissao | ✅ |
| Alguma reproducao foi **barrada antes** de ser escrita? | ✅ **Uma, nomeada:** a **matriz de 50 celulas** de `SF-10 §5` **nao** foi reproduzida na `Spec`. O Bloco 5 traz **as quatro variaveis e o valor apurado de cada uma**, e remete. Reproduzir a matriz teria criado a quinta copia de uma tabela que `FND-11` ja declara **projecao** — exatamente o defeito de `RD-28`/`MEM-APR-0002` | ✅ |

**Resposta: nao** a `F2.a` — `0` conceitos redefinidos, e o unico conteudo externo *(regras do
candidato)* entra **citado por arquivo e linha**. · **aplicada** a `F2.b` — com **um** caso de
reproducao barrada, nomeado.

## F3 — Alguma abstracao ficou desnecessaria?

| Abstracao introduzida | Membros | Consumidor declarado | Veredito |
|---|---|---|---|
| **Nenhuma.** `0` entidades, `0` tipos documentais, `0` portoes, `0` papeis, `0` classes, `0` verbos de autoridade | — | — | — |
| *(exame do que poderia parecer abstracao)* `SPC-001` como **categoria** | **1** membro — ela mesma | **5** consumidores nomeados no Bloco 12 | **justificada** — `AQ-03`/`RL-06` suspeitam de abstracao com **menos de dois membros ou sem consumidor**; aqui ha consumidor, e a `Spec` **nao e abstracao**: e instancia de tipo que ja existia em `FND-10 §4.4` desde a origem |

**Resposta: nao** — nada foi abstraido; um tipo que ja existia ganhou sua primeira instancia.

## F4 — O sistema continua mais simples de evoluir do que antes?

| Mudanca-tipo | Documentos exigidos antes | Depois | Aprovacoes no caminho critico |
|---|---|---|---|
| **Criar a 1a `Spec`** | **Impossivel ate 2026-08-01** *(`RD-33` bloqueante)*; depois, **indefinido** — nunca exercido | **5 artefatos**, caminho conhecido e escrito | 3 — `QG-1` *(DEP-EXE)*, aprovacao *(DEP-EXE + parecer DEP-GOV)*, registro *(DEP-GOV)* |
| **Criar a 2a `Spec`**, sem colisao propria de classe | idem | **2 artefatos** — a `Spec` e o registro. **`ADR` de classe nao se repete**: `ADR-0031 §5` declara a elevacao **restrita a esta criacao** | 3, sendo a aprovacao de `C1` *(proprietario + revisor)* — **se e quando `RD-91` for sanado** |
| **Consultar um requisito** | **Impossivel** — `0` requisitos | **1 bloco de 13 linhas**, por `SPC-001 RQ-nn` | `0` |
| **Emendar a `Spec`** | — | **1 emenda**, classe pelo efeito (`SF-27`) | conforme a classe |

**Leitura.** O custo de mudar **subiu** para a primeira, em troca de duas segurancas: uma
aprovacao que **nao e nula** e um precedente escrito. Para as seguintes, **desce** — e essa e a
direcao que `PI-14` pede.

**Resposta: sim, com custo declarado** — a 1a custou 5; a 2a custa 2.

## F5 — A mudanca reduz ou aumenta o custo de contexto?

| Papel / tarefa-tipo | Material necessario antes | Depois | Direcao |
|---|---|---|---|
| **DEP-ENG — *"o que preciso garantir sobre dado de titular?"*** | `PRO-nxtrack` **263** + `PT-2026-014` **292** = **555 linhas**, **e a resposta nao estava la** *(`0` requisitos)* | **`SPC-001 RQ-3` = 13 linhas** | **desce** — 555 sem resposta → 13 com resposta |
| **DEP-QAR — *"o que verifico?"*** | indefinido | **Bloco 19**, tabela de 10 linhas | **desce** |
| **SOBERANO — *"o que a decisao de expor pressupoe?"*** | indefinido | **Pacote minimo: `SPC-001` + Carta = 866 linhas** | **sobe**, contra 555 — e a resposta passa a existir |
| **Leitura integral do produto** | 555 | 866 | **sobe** — **+311 linhas** |

**Resposta: desce** para a consulta enderecada, que e o uso previsto por `SF-31` e `PC-01`; **e
sobe 311 linhas** para a leitura integral. As duas direcoes estao medidas, e a segunda vira
ressalva `R-2` — nao seria honesto declarar so a que favorece.

## F6 — Ela favorece reutilizacao?

| Definicao produzida | Reutilizavel por | Especifica do caso? |
|---|---|---|
| **O caminho completo de criacao de `Spec`**, exercido ponta a ponta | **Toda `Spec` futura** | **Nao especifica** — `DoR` 9/9, `DoD` 10/10 e 21 blocos servem a qualquer materia |
| **A derivacao de autoridade do Bloco 5** — quatro variaveis, quatro fontes | Toda `Spec` futura, e qualquer artefato de classe derivada | **Nao especifica** |
| **A conferencia contra `FND-04 §3.1`** antes de fixar a classe | **Qualquer** criacao de artefato | **Nao especifica** — e o achado `RD-91` em forma reutilizavel |
| **O metodo de medicao com controle positivo** antes de acreditar num zero | Qualquer medicao por varredura de termos | **Nao especifica** — generaliza `MEM-APR-0005` |
| Os **10 requisitos** | So o nXtrack | **Especifica** — e correto que seja: `SF-07` vincula a `Spec` a **um** produto |

**Criterio `DoD-8`:** escrito para servir a proxima ocorrencia. **4 de 5** definicoes produzidas
sao reutilizaveis; a 5a e especifica por norma, nao por descuido.

**Resposta: sim** — **27 de 32** regras `SF-*` deixam de ser *determinadas* e passam a
*observadas*, e o precedente e o que a segunda `Spec` vai consumir.

---

## Ressalvas

| # | Ressalva | Custo assumido | **Dono** | **Gatilho de reavaliacao** |
|---|---|---|---|---|
| **`R-1`** | **A primeira `Spec` custou 5 artefatos**, e a causa e uma colisao de norma *(`RD-91`)*, nao a materia. Ha risco de o numero virar expectativa | **+3 artefatos** sobre o minimo teorico *(`RFC`, `ADR`, `FIT`)* | **SOBERANO** *(so ele emenda `FND-11`)* | **Segunda `Spec` real.** Se ela tambem for `C2` **pelo mesmo motivo**, a colisao virou norma de fato |
| **`R-2`** | **`SPC-001` tem 603 linhas — `2,23×` a mediana do acervo *(270)* e `+311` sobre o material que antes se lia.** `CE-05` manda comparar com **o dobro da mediana do proprio tipo**, e **a populacao do tipo e `1`**: o teste e **inaplicavel por ausencia de populacao**, nao satisfeito | Leitura integral mais cara | **DEP-PRD** | **Terceira `Spec` do acervo** — com `n=3` a mediana do tipo passa a existir e `CE-05` se torna aplicavel |
| **`R-3`** | **`DEP-QAR` e custodiante da materia *(via `CAP-juridico`)* e revisor do tipo *(via `FND-09 §8.2`)* na mesma mudanca.** Nao e incompatibilidade de `FND-04 §3.1`, e por isso **nao anula** — mas a independencia e menor do que a tabela sugere | Independencia reduzida, declarada | **DEP-GOV** | **Segunda `Spec` custodiada por DEP-QAR** — achado `RD-92` |
| **`R-4`** | **`H-1` nao esta validada.** A `Spec` assume que `RQ-1`–`RQ-8` **bastam** para uma assessoria juridica humana concluir sem novo levantamento, e **isso nao foi testado** — `0` assessorias consultadas | Risco de o levantamento estar incompleto na dimensao que importa | **DEP-PRD** | **Primeira consulta a assessoria juridica humana.** Metrica: quantos levantamentos adicionais ela pede. `0` ⇒ `H-1` confirmada |

## Veredito

| Campo | Conteudo |
|---|---|
| **Veredito** | **`apto-com-ressalva`** |
| **Fundamento** | A arquitetura ficou **mais apta**: um tipo documental inerte ganhou instancia, **27 de 32** regras sairam de *determinadas* para *observadas*, e o caminho ficou escrito para as seguintes — ao custo, **declarado e medido**, de 5 artefatos e de uma colisao de norma que **este parecer nao pode sanar** |
| **Efeito** | **Encerra com divida declarada.** As **4** ressalvas tem dono e gatilho (`FT-06`) |
| **Data** | 2026-08-02 |
| **Executado por** | **DEP-QAR** |
| **Aprovado por** | **DEP-EXE** |
| **Ratificado por** | **n/a** — objeto `C2` |

> **`FT-04` conferido:** este **nao** e o terceiro `apto` consecutivo sem ressalva. `FIT-2026-023`
> foi `apto-com-ressalva` *(4 ressalvas)*, e este tambem. **Nao ha sinal de complacencia a
> escalar.**

## Aprendizado gerado

| Registro `APR` | Licao |
|---|---|
| **nenhum registro novo** *(congelamento em vigor: achado nao gera missao, e criar `MEM-APR` seria trabalho novo)* | A licao esta **nomeada e localizada**, para a missao que a promover: **exercer a matriz de autoridade revela o que le-la nao revela** — o mesmo padrao de `MEM-APR-0006` *(*"exercer o contador revela o defeito"*)* e de `MEM-APR-0005` *(*"medir a ausencia na fonte errada"*)*, agora na **terceira** ocorrencia. **Gatilho de promocao:** proxima missao que toque a camada `APR` |

## Historico de vereditos sobre este objeto

| `FIT` | Data | Veredito | Relacao |
|---|---|---|---|
| **FIT-2026-024** | 2026-08-02 | `apto-com-ressalva` | **primeiro** — nao supera nenhum |
