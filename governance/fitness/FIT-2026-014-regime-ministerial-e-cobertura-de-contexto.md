---
id: FIT-2026-014-regime-ministerial-e-cobertura-de-contexto
titulo: Aptidao arquitetural do fechamento operacional — regime ministerial de promulgacao e ativacao, cobertura de contexto e liberacao GO-TO-SPECS
tipo: fitness
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-QAR
proprietario: DEP-QAR
aprovador: DEP-EXE
criado_em: 2026-07-29
atualizado_em: 2026-07-29
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0012, ADR-0015, ADR-0019, ADR-0020]
substitui: []
substituido_por: null
objeto_avaliado: [RFC-0016, ADR-0020, PT-2026-006, MEM-APR-0005, artifact-registry]
classe_mudanca: C2
classe_avaliacao: aptidao
veredito: apto-com-ressalva
resumo: Verifica se o fechamento de RD-22 e a reconciliacao de RD-26 deixaram a arquitetura mais apta a evoluir; veredito apto-com-ressalva, duas ressalvas novas, C11 integral e fechamento GO-TO-SPECS.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-GOV
ratificacao: nao-exigida
---

# FIT-2026-014: Regime ministerial e cobertura de contexto

## Proposito
Verificar, de forma independente, se a Missao 1.12.1 deixou a arquitetura **mais apta a
evoluir** — e nao apenas correta —, e responder as seis perguntas de
[FND-09 §10.3](../../foundation/09-meta-model.md) sobre o fechamento de `RD-22`, a
reconciliacao de `RD-26` e a apuracao das oito condicoes de §X.

## Escopo
| Item | Definicao |
|---|---|
| **Objeto avaliado** | [RFC-0016](../../rfcs/RFC-0016-regime-ministerial-de-promulgacao-e-ativacao.md) · [ADR-0020](../../decisions/ADR-0020-regime-ministerial-de-promulgacao-e-ativacao.md) · [PT-2026-006](../relatorio-transicao-2026-07-29-fechamento-operacional.md) · [MEM-APR-0005](../../memory/aprendizado/MEM-APR-0005-medir-a-ausencia-na-fonte-errada.md) · [catalogo mestre](../artifact-registry.md) 2.3.0 |
| **Nao avaliado** | O merito da classe C2 *(decisao de DEP-EXE)* · `TPL-spec` *(`RD-23`)* · §10.2 do catalogo *(`RD-24`)* · a rota `PRD → TLS` *(`RD-10`)* |
| Natureza | **Parecer**, `M1`, que **nao se ratifica** — `FT-10` de [ADR-0015](../../decisions/ADR-0015-fitness-check-e-parecer-nao-decisao.md) |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| **Executa a verificacao** | **DEP-QAR** | FND-09 §10.5; `CV-08` — nao produziu nenhum dos objetos avaliados |
| **Revisa a forma** | **DEP-GOV** | FND-09 §8.2, linha `FIT` |
| **Aprova** | **DEP-EXE** | FND-09 §8.2, linha `FIT` |
| **Ratifica** | **—** | `FT-10` — parecer nao se ratifica |
| **Nao participa** | **DEP-GOV como produtor** | `PI-05`, `LV-03` — DEP-GOV e autor de RFC-0016, ADR-0020 e PT-2026-006, e por isso **nao** os verifica |

---

## Sumario

| Pergunta | Resposta |
|---|---|
| **F1** — A complexidade aumentou sem ganho proporcional? | **Nao** — 14 regras e 1 matriz, contra 10 celulas de prova que passam a nomear titular e **zero** fontes emendadas |
| **F2** — Algum conceito foi duplicado? E a prevencao foi aplicada? | **Nao** duplicou; a prevencao **foi aplicada e barrou duas reproducoes** |
| **F3** — Alguma abstracao ficou desnecessaria? | **Nao** — e uma abstracao foi **evitada**: nenhum verbo de autoridade novo |
| **F4** — O sistema continua mais simples de evoluir? | **Sim** — o bloqueio de `GO-TO-SPECS` deixou de existir sem custo normativo |
| **F5** — Reduz ou aumenta o custo de contexto? | **Reduz** — pacote de **2.522 linhas · 5,7%**, com comparabilidade declarada |
| **F6** — Favorece reutilizacao? | **Sim** — 6 metodos reutilizaveis, 1 especifico do caso |
| **C11** — Conformidade de FND-10 §11 | **13 de 13 verificacoes conformes** |
| **Veredito** | **`apto-com-ressalva`** — **duas** ressalvas novas, ambas com dono e gatilho |

---

## F1 — A complexidade aumentou sem ganho proporcional?

| O que foi acrescentado | Quantidade |
|---|---|
| Regras novas | **14** — `PA-01` a `PA-14` |
| Matrizes novas | **1** — ADR-0020 §5.2, declarada `PJ-02` |
| Entidades · arquetipos · papeis · departamentos · portoes · verbos de autoridade | **0 · 0 · 0 · 0 · 0 · 0** |
| Tipos documentais novos | **0** |
| Arquivos de `foundation/` alterados | **0**, medido por `cmp` contra a copia datada |
| Artefatos criados | **5** — 1 RFC, 1 ADR, 1 MEM-APR, 1 Reporte, este parecer |

| O que foi obtido | Quantidade |
|---|---|
| Celulas de prova que passam de *"responde por regra"* a **titular declarado** | **10** |
| Exigencias de §IX satisfeitas | de **4 de 5** para **5 de 5** |
| Condicoes de §X satisfeitas | de **6 integrais + 1 parcial + 1 falha** para **8 de 8** |
| Achados fechados | **4** — `RD-22`, `RD-26`, `RD-28`, `RD-29` |
| Atos soberanos exigidos para obter isso | **0** |

**Verificacao propria de DEP-QAR: `V1` a `V4` de `MEM-APR-0005` foram aplicados?** Sim, e a
aplicacao **e o proprio conteudo** de RFC-0016 §2.3: a funcao *"quem publica o que foi
aprovado"* foi procurada no documento de **ciclo** (`V2`), com o termo do acervo — `REGISTRO`
— e nao o da pergunta (`V1`), nas **Cartas** (`V3`), e a ausencia em FND-09 §8.2 foi
reclassificada como **consequencia de regra** e nao lacuna (`V4`). **As quatro.**

**Resposta: nao.** Quatorze regras que **remetem** e nenhuma que **institui titular** e o menor
acrescimo que responderia a §IX. **Ganho proporcional demonstrado, nao alegado.**

## F2 — Algum conceito foi duplicado? E a prevencao foi aplicada?

### a) Houve duplicacao?

| Candidato a duplicacao | Verificado | Resultado |
|---|---|---|
| A matriz de ADR-0020 §5.2 reproduz FND-09 §8.2? | Comparacao coluna a coluna | **Nao.** §8.2 distribui os **cinco verbos por entidade**; a matriz mapeia **onze atos por papel**. Objetos distintos, e a projecao esta **declarada** com as quatro informacoes de `PJ-02` |
| `PA-03` reescreve `FND-04 §4 [7]`? | Leitura literal | **Nao — remete.** `PA-03` cita a etapa; nao repete seu texto. Foi essa a razao de recusar a **Alternativa C** de ADR-0020, que **reescreveria** o ciclo |
| PT-2026-006 reproduz a matriz? | Varredura do artefato | **Nao.** §5 declara *"este relatorio nao a reproduz — `PJ-01`"* e remete a ADR-0020 §5.2 |
| PT-2026-006 reproduz as 55 celulas de PT-2026-005 §4.1? | Varredura | **Nao.** §6.1 declara a **invariancia da fonte** como fundamento e reproduz **somente as 10 celulas novas** |
| §2.1 do catalogo reproduz o frontmatter de 159 artefatos? | Leitura | **Nao** — agrega, com metodo e fonte declarados. `RG-01` preservado |

### b) A prevencao de `PJ-05` foi aplicada, com evidencia?

**Sim, e ela barrou duas reproducoes antes da submissao** — as duas registradas acima em
PT-2026-006 §5 e §6.1. **Este e o segundo caso em que o teste preventivo tem efeito
verificavel**, e nao apenas declaracao de que foi feito.

**Resposta: nao duplicou; a prevencao foi aplicada e produziu efeito.** **Decima terceira
confirmacao** de [MEM-APR-0002](../../memory/aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md).

## F3 — Alguma abstracao ficou desnecessaria?

| Abstracao | Membros observados | Necessaria? |
|---|---|---|
| **Operacao ministerial** *(`PA-01`)* | **2** — promulgar e ativar | **Sim.** `AQ-03` exige dois membros; tem exatamente dois, e ambos com caso real medido nos seis atos |
| **Matriz de regime operacional** | **11 atos × 5 papeis** | **Sim** — e a unica forma de responder a §IX em uma leitura |
| **`PA-07` supletiva** *(custodiante)* | **0 casos reais** | **Vigiar.** Nunca foi exercida: os seis atos nomearam ou o executor era obvio. Registrada como **ressalva `R1`** |

**Uma abstracao foi deliberadamente EVITADA, e isso conta:** a Alternativa B de ADR-0020
criaria **dois verbos de autoridade novos**, ampliando o universo fechado de `FND-09 §8.1` de
cinco para sete. **Recusada.** O acervo tem historico de recusar entidade — `FND-09 §5.8`, seis
recusadas — e este e o **primeiro registro de recusa de verbo de autoridade**.

**Resposta: nao.** Uma abstracao a vigiar, com ressalva; uma evitada, com registro.

## F4 — O sistema continua mais simples de evoluir?

| Antes | **Depois** |
|---|---|
| `GO-TO-SPECS` bloqueado por lacuna **sem caminho**: nao era falta de ato, era falta de leitura | **Desbloqueado**, sem emendar fonte e sem pedir ato |
| Toda promulgacao futura reabriria a duvida de titularidade | `PA-01` a `PA-14` respondem **por regra**, uma vez |
| §2.1 do catalogo nao reproduzia; `CE-01` e `CE-02` **nao eram afirmaveis** | **Reproduz 159 · 44.539** — a propria baseline — com cobertura **100%** |
| A obrigacao de `AC-08` nunca havia sido **contada** | **Contada: 2 nao conformidades**, com instrumento e impedimento declarados *(`RD-27`)* |

**Contraprova exigida por `FT-06`:** a mudanca **acrescenta** custo em algum ponto? **Sim, um:**
as regras `PA-*` vivem em artefato **`M1`**, que **nao se emenda** — corrigi-las exige ADR
sucessor. **O tradeoff esta declarado em ADR-0020 §4** e e o mesmo de `IR-*` e `FT-*`, que ja
atravessaram tres missoes sem exigir sucessao.

**Resposta: sim, com um custo declarado.**

## F5 — A mudanca reduz ou aumenta o custo de contexto?

### F5.1 A medicao, itemizada — **a oitava da serie**

**Pacote minimo medido: 2.522 linhas sobre 44.539 = 5,7%.**

| Bloco | Linhas |
|---|---|
| **PT-2026-005 integral** — o achado sob exame, lido por inteiro | **430** |
| **`FND-10`** — §2, §5, §8, §10.3, §11 e cabecalho de vigencia | **390** |
| **Catalogo mestre** — §1 a §4.6 e §10 | **400** |
| **`MSG-2026-0006`** — §I a §X e §2.2 | **200** |
| **`DEP-GOV`** — §3 a §7 e §10 | **200** |
| **`FND-04`** — §2 a §5 | **180** |
| **`FND-09`** — §7 e §8 | **170** |
| **Extracoes por ferramenta** — varredura de frontmatter, agregacao por perfil, comparacao §4 × fonte, links, hashes | **150** |
| **`FND-07`** — §2, §3 e §5 | **110** |
| **`TPL-nota-decisao`** integral — para **recusar** a Alternativa D por incompetencia do instrumento | **102** |
| **Frontmatter dos 19 `ADR`** + recortes de `FIT-2026-013` | **120** |
| **`FND-01 §6.2`** + recorte `IR-01` a `IR-10` de `ADR-0012` | **70** |
| **Total** | **2.522** |

**A serie observada e 23% · 33% · 30,6% · 18,5% · 21,3% · 18,9% · 13,3% · 15,1% · 12,0% ·
6,1% · 1,4% · 5,7%.**

> ### ⚠️ A comparabilidade e parcial, e o limite esta declarado
> **Esta missao produziu norma** — 1 RFC e 1 ADR com 14 regras —, o que a torna comparavel as
> missoes de producao *(23% a 12%)*, **e nao** a de verificacao pura de `FIT-2026-013` *(1,4%)*.
> Contra as missoes de producao, **5,7% e o menor valor da serie**.
>
> **A causa da reducao e verificavel, e nao e virtude:** **nenhuma Carta foi lida integralmente**
> *(so DEP-GOV, em recorte)*, **nenhuma fundacional foi carregada por inteiro** e **as
> 23 `CAP` e os 19 `TPL` foram classificados por varredura de frontmatter, nao por leitura** —
> **42 artefatos, 6.676 linhas, resolvidos com 0 linhas de leitura humana**. Foi `CE-02` — *custo
> e linha medida* — que permitiu isso.
>
> **Esta medicao nao e usada para fechar nenhuma ressalva.** `R4` de FIT-2026-002 permanece
> fechada por FIT-2026-012, com missoes comparaveis.
>
> **O piso obrigatorio nao mudou:** **nenhuma fundacional foi emendada**, e o nucleo **nao foi
> ampliado** — os mesmos 4 artefatos, 2 integrais e 2 por recorte.

### F5.2 O efeito sobre o custo futuro

| Consumidor | Antes | Depois |
|---|---|---|
| Quem for promulgar ou ativar qualquer artefato | Ler `FND-04 §4`, `FND-07 §5`, `FND-09 §7.5` e `§8`, `FND-10 §5` — **~600 linhas** | Ler **ADR-0020 §5.1 e §5.2** — **~80 linhas**, com remissao para o caso duvidoso |
| Quem for medir cobertura de perfil | Metodo **nao existia**; recalcular era `LV-05` | §2.1 do catalogo declara o metodo em **duas regras** |

**Resposta: reduz.** E a reducao mais util nao e a desta missao: e a de **~600 para ~80 linhas**
no consumidor recorrente.

## F6 — Ela favorece reutilizacao?

| Metodo produzido | Reutilizavel por | Especifico do caso? |
|---|---|---|
| **`V1` a `V4`: antes de afirmar ausencia, buscar a funcao no documento de ciclo, nao o termo no de autoridade** | **Toda varredura que conclua ausencia** | Nao |
| **Provar que um metodo de particao fecha, reproduzindo o total do acervo** | **Toda projecao agregada** — §2.1 e a primeira | Nao |
| **Somar as colunas da propria fonte derivada, nao so compara-la a fonte** | **Toda auditoria de catalogo** — encontrou os itens 5 e 8 de `RD-28` | Nao |
| **Rehashear os objetos de um ato ja aplicado, em vez de transcrever a prova** | **Toda apuracao de condicao de eficacia posterior** | Nao |
| **Recusar o instrumento pelo texto do proprio template** | **Toda escolha de instrumento** — foi assim que a Nota de Decisao caiu | Nao |
| **Instituir regras dentro do ADR para nao emendar fonte** | **Toda decisao interpretativa** — terceiro uso, apos `IR-*` e `FT-*` | Nao |
| `RD-27` — o impedimento de `H-N` sobre backfill de campo | — | **Sim** |

**Evidencia mais forte: a soma das proprias colunas.** O risco **`RG-2`** da Carta de DEP-GOV
declara, desde a Missao 1.9, que *"a auditoria confere projecao contra fonte e nao confere a
fonte contra si mesma"*, com mitigacao escrita: *"`G-7` passa a exigir somar as tabelas da
fonte"*. **A mitigacao existia e nunca havia sido exercida.** Exercida uma vez, encontrou **um
subtotal que nao fecha** *(§4.4: 2.952 declarado, 2.958 somado)* e **um ordinal errado**
*(§2.2)*. **Custo: uma execucao. Achados: dois.**

**Resposta: sim.**

---

## C11 — Conformidade de [FND-10 §11](../../foundation/10-artifact-framework.md)

| # | Verificacao | Resultado |
|---|---|---|
| 1 | Contrato **L1** completo nos artefatos novos | ✅ **5 de 5** declaram os **cinco** campos do contrato estendido |
| 2 | `revisor` ≠ `autor` | ✅ **98 artefatos com ambos · 0 coincidencias**, remedido apos as edicoes |
| 3 | `ratificacao` coerente com a classe | ✅ ADR-0020 e **C2 · Tipo 2** → `nao-exigida`. **Nenhum artefato novo e C3 ou Tipo 1** |
| 4 | Tipo documental consta de FND-10 §4 | ✅ `RFC` §4.2 · `ADR` §4.2 · `Memoria APR` §4.6 · `Reporte` §4.6 · `Fitness Check` §4.5 |
| 5 | Atributo **derivavel** declarado em frontmatter | ✅ **0** — nenhum artefato novo declara consumidores, relacoes, autoridade, custo ou dependencia transitiva (`AC-01`) |
| 6 | Cadeia **origem → estado → substituicao** percorrivel | ✅ **5 de 5** — `decisoes_relacionadas`, `status` e o par `substitui`/`substituido_por` presentes |
| 7 | Custo de contexto **medido**, nao estimado | ✅ Linhas de cada artefato novo medidas por `wc -l` e registradas no catalogo §4 |
| 8 | Entrada no catalogo mestre presente | ✅ **5 de 5** — §4.2, §4.5 e §4.7 |
| 9 | Divisao com menos de dois sinais | ✅ **Nao aplicavel** — nenhuma divisao proposta |
| 10 | Tabela reproduzida **sem** declaracao de projecao | ✅ **0** — a unica matriz nova declara `PJ-02` com as quatro informacoes |
| 11 | **Teste preventivo de projecao aplicado, com evidencia** | ✅ **Aplicado, e com efeito**: barrou **duas** reproducoes — F2.b |
| 12 | Conteudo de origem externa fora do portao | ✅ **0** — **LucaX Legacy nao foi consultado** nesta missao, por vedacao expressa |
| 13 | Alteracao de conteudo **sem** incremento de versao | ✅ **0** — a correcao de `memory/operacional/README` declarou **CORRECAO 1.2.1**, conforme `AC-11` |

**13 de 13 conformes.**

---

## Ressalvas

| # | Ressalva | Custo assumido | **Dono** | **Gatilho** |
|---|---|---|---|---|
| **R1** | **`PA-07` supletiva nunca foi exercida.** A regra que designa o **custodiante** como executor na ausencia de nomeacao no ato tem **zero casos observados** — e determinada, nao verificada. Se a primeira invocacao real revelar ambiguidade de custodia, a regra precisara de ADR sucessor | Uma regra em vigor sem membro observado. `PI-10` exige que isso esteja escrito, e esta | **DEP-GOV** | **Primeira invocacao real de `PA-07`**, ou o primeiro ato soberano que **nao nomeie** executor |
| **R2** | **`RD-27` deixa duas fundacionais em nao conformidade declarada.** `FND-01` e `FND-02` vigoram sem quatro e sem cinco campos do contrato, e a correcao **altera `H-N`** — so cabe em ato soberano. Enquanto isso, `AC-06` esta descumprido por dois documentos de **nivel 2 da hierarquia normativa** | O acervo passa a ter nao conformidade **conhecida e nao corrigivel sem ato**. O atenuante — valores padrao declarados em §2.2 — e real, **e nao e cumprimento** | **DEP-GOV** | **Proximo ato soberano que alcance `FND-01`, `FND-02` ou `FND-10`** |

### Ressalvas anteriores — situacao

| Ressalva | Origem | Situacao |
|---|---|---|
| `R4` de FIT-2026-002 *(custo de contexto)* | FIT-2026-002 | **Permanece fechada** por FIT-2026-012. **Esta medicao nao e usada para nada** |
| Familia **`RC-02`** *(DEP-GOV produz e a verificacao independente e do mesmo ciclo)* | REV-ESTRUTURAL-I | **DECLARADA, NAO RESOLVIDA — sexta ocorrencia.** Mitigacao possivel exercida: `PA-08`, `I-7`, e **este parecer, produzido por DEP-QAR sobre objetos de DEP-GOV**. O residuo so desaparece com agentes *(`IC-3`)* |
| `RD-10` *(rota `PRD → TLS`)* | RFC-0015 | **Aberta.** Materia de Carta; **nao alcancada** por esta missao |
| `RD-13` *(historico de FND-10 fora de ordem)* | PS-2026-008 | **Aberta.** Corrigir exige editar fonte ratificada — mesmo impedimento de `RD-27` |

---

## Veredito

> ## **`apto-com-ressalva`**
>
> **A arquitetura ficou mais apta a evoluir.** O bloqueio de `GO-TO-SPECS` foi removido **sem
> emendar uma linha de fonte, sem criar um titular e sem pedir um ato** — e o que o removeu foi
> **medir no lugar certo**, nao acrescentar norma. Isso e o oposto do padrao que `FIT-2026-002`
> temia: complexidade acrescentada para resolver problema de leitura.
>
> **Duas ressalvas, ambas com dono e gatilho.** `R1` e uma regra sem membro observado; `R2` e
> uma nao conformidade real que **este ciclo nao podia corrigir** — e o registro diz **por que**,
> com a regra criptografica citada, em vez de silenciar.
>
> **O que este parecer NAO afirma:** nao julga a **classe C2** — isso e de DEP-EXE; nao afirma
> que `PA-12` e `PA-14` funcionam — **nunca foram exercidos**, e ADR-0020 §8 `A1` e `A2` dizem
> isso; e nao converte a apuracao de §X em decisao — `FT-10` e `FT-11` proibem que parecer
> adquira autoridade normativa.

## Fechamento — **`GO-TO-SPECS`**

| Condicao de §X | Verificada por DEP-QAR |
|---|---|
| 1 · 2 · 5 | ✅ **10 de 10 objetos rehasheados** hoje, reproduzindo nos 64 digitos — PT-2026-006 §2. **DEP-QAR executa `IR-09`; DEP-GOV nao e a unica prova** (`I-7`) |
| 3 · 4 | ✅ Ordem literal de §V em PT-2026-005 §1; **0 fontes alteradas** nesta missao, por `cmp` |
| **6** | ✅ **55/55 e as cinco exigencias de §IX** — a quinta fecha por ADR-0020, e a refutacao de `RD-22` foi **conferida linha a linha** contra `FND-04 §4 [7]` e `FND-07 §5 [10]` |
| **7** | ✅ §2.1 **reproduz o total do acervo**; **9** valores corrigidos na projecao; **0** fontes alteradas |
| 8 | ✅ **`BL-2026-07-29-08`**, com **metodo de contagem de links declarado** — atende `RD-30` |

**As oito condicoes estao satisfeitas, e a verificacao e independente de quem as apurou.**

### A decisao

**`GO-TO-SPECS`** — nos termos de §X do sexto ato soberano, que **ja o autorizou sob condicao
objetiva**. DEP-QAR confirma que as condicoes estao satisfeitas; **a liberacao decorre do ato**.

> **Com uma pre-correcao obrigatoria, e ela nao e negociavel.** **`RD-23` — `TPL-spec`
> contradiz `ADR-0019` vigente** — deve ser corrigido **antes da primeira Spec**, nao depois. O
> esqueleto fixa `aprovador: DEP-PRD` e nao tem campo `ratificacao`; usa-lo produziria Spec
> **nao conforme desde a criacao** (`AC-06`), e a primeira Spec e exatamente o que
> `GO-TO-SPECS` libera. **Registrado como pre-correcao da Missao 1.13, com dono DEP-GOV.**

## Pendencias para o SOBERANO — **tres**

| # | Materia | Natureza |
|---|---|---|
| 1 | **`RD-27`** — backfill dos campos de contrato em `FND-01`, `FND-02` e `FND-10 §8.5`, que **altera `H-N`** | Exige **RFC + ADR + diff + pacote + ato**. **Nao urgente**: nenhuma condicao de §X depende disso |
| 2 | **A classe de `ADR-0020`** — se o SOBERANO entender que declarar o regime e **C3** | Basta a manifestacao; RFC-0016 serve de peca instrutoria **sem reescrita** |
| 3 | **A leitura de §X** — se a liberacao exige **ato proprio** em vez de apuracao ministerial | Sob qualquer das duas leituras, **8 de 8 condicoes estao satisfeitas** — muda **quem enuncia**, nao o estado |

**Nenhuma das tres bloqueia trabalho.** Esta e a primeira vez que a lista de pendencias do
Soberano **nao contem nada que impeca a proxima missao**.

## Aprendizado gerado

| # | Licao | Registro |
|---|---|---|
| 1 | **Achado de ausencia deve declarar o que foi varrido, e buscar a funcao antes do termo** | [MEM-APR-0005](../../memory/aprendizado/MEM-APR-0005-medir-a-ausencia-na-fonte-errada.md) — `ocorrencias: 3` |
| 2 | **Um metodo de particao que reproduz o total do acervo nao pode ter dupla contagem nem omissao** — foi o que tornou §2.1 afirmavel | PT-2026-006 §3.5; candidato a `MEM-APR` proprio na proxima missao que o reutilize |
| 3 | **Mitigacao escrita e nao exercida nao e mitigacao** — `RG-2` estava mitigado no papel desde a Missao 1.9 e produziu 2 achados na primeira execucao | Esta secao; dono **DEP-GOV**, gatilho **proxima auditoria documental** |

## Historico de vereditos sobre este objeto

**Primeiro parecer** sobre o regime de promulgacao e ativacao. Nao supera nem contesta
`FIT-2026-013`, cujo objeto era outro.

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-QAR | Verificacao de aptidao do **fechamento operacional**. Veredito **`apto-com-ressalva`**, com **duas** ressalvas novas — **`R1`** *(`PA-07` supletiva sem membro observado)* e **`R2`** *(`RD-27` deixa `FND-01` e `FND-02` em nao conformidade declarada, corrigivel so por ato, porque o backfill altera `H-N`)*. **F1:** 14 regras e 1 matriz contra **10 celulas** que passam a nomear titular, **0 fontes emendadas** e **0 atos exigidos**; `V1` a `V4` de MEM-APR-0005 aplicados, as quatro. **F2:** nenhuma duplicacao, e o teste preventivo de `PJ-05` **barrou duas reproducoes** — decima terceira confirmacao de MEM-APR-0002. **F3:** primeira **recusa registrada de verbo de autoridade** no acervo. **F4:** o consumidor recorrente passa de **~600 para ~80 linhas**. **F5:** oitava medicao da serie — **2.522 linhas · 5,7%**, o menor valor entre missoes **de producao**, com comparabilidade declarada e **42 artefatos resolvidos por varredura de frontmatter, com 0 linhas de leitura**. **F6:** 6 metodos reutilizaveis; o mais forte foi **somar as colunas da propria fonte derivada**, mitigacao de `RG-2` escrita desde a Missao 1.9 e **nunca exercida** — exercida uma vez, produziu **2 achados**. **`C11`: 13 de 13 conformes.** Fechamento **`GO-TO-SPECS`**, com **`RD-23` como pre-correcao obrigatoria e nao negociavel** da Missao 1.13. **Tres pendencias para o SOBERANO, e nenhuma delas bloqueia trabalho — a primeira vez que isso ocorre no acervo.** |
