---
id: FIT-2026-009-ativacao-e-endurecimento
titulo: Aptidao arquitetural da Missao 1.10 — verificacao de contrato, emendas candidatas e o ato que nao chegou
tipo: fitness
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-QAR
proprietario: DEP-QAR
aprovador: DEP-GOV
criado_em: 2026-07-29
atualizado_em: 2026-07-29
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0011, ADR-0012, ADR-0013]
substitui: []
substituido_por: null
objeto_avaliado: [PS-2026-003, PT-2026-001, IDX-departamentos, IDX-governance, IDX-fitness, artifact-registry]
classe_mudanca: C2
classe_avaliacao: aptidao
veredito: apto-com-ressalva
resumo: Verifica se a Missao 1.10 deixou a arquitetura mais apta a evoluir; veredito apto-com-ressalva, quatro ressalvas e fechamento BLOCKED por forma do ato soberano.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-GOV
ratificacao: nao-exigida
---

# FIT-2026-009: Missao 1.10 — verificacao de contrato, emendas candidatas e o ato que nao chegou

## Proposito
Verificar se a **Missao 1.10** — verificacao das treze dimensoes do contrato sobre as nove
Cartas, tres emendas candidatas, reconciliacao catalogo-fonte e a recusa de ativar sem ato
valido — deixou a arquitetura **mais apta a evoluir**.

> **Obrigatorio por QG-6** sobre mudanca **C2** (FND-01 §6.2; FND-09 §10.2).

## Escopo
| Item | Definicao |
|---|---|
| Objeto avaliado | [PS-2026-003](../pacote-soberano-2026-07-29-emendas.md) · [PT-2026-001](../relatorio-transicao-2026-07-29-departamentos.md) · `IDX-departamentos` **1.1.0** · `IDX-governance` **1.3.0** · `IDX-fitness` **1.3.0** · catalogo mestre **1.7.0** |
| Estado anterior | **131 artefatos, 35.701 linhas** *(`BL-2026-07-28-06`)*; **4 de 9** Cartas em vigor; **15** ressalvas abertas; **8** vereditos consecutivos `apto-com-ressalva` |
| **Nao** inclui | O **merito** das tres emendas *(PS-2026-003)* · o **merito** do ato que nao ocorreu · as nove Cartas como objeto de alteracao — **nenhuma foi tocada**, e entram aqui apenas como objeto de **verificacao** |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| **Executa** | **DEP-QAR** | FT-02, CV-08 — nao produziu PS-2026-003 nem PT-2026-001 |
| Forma | DEP-GOV | |
| Evidencia | DEP-KMS | Medicoes de acervo, de secao, de hash e de link |
| **Aprova** | **DEP-GOV** | **Desvio declarado.** A matriz atribui a aprovacao de `FIT` a **DEP-EXE**, impedido por ser **autor das tres emendas avaliadas** (`DEP-EXE §10, I-2`). Cenario **CX-3**; precedentes FIT-2026-003, 006, 007 e 008 |
| Ratifica | **Nao aplicavel** | Objeto **C2/Tipo 2** — e a questao **Q2**, escalada. O item 4 da minuta de PT-2026-001 §8 a alcanca **por determinacao**, se o Soberano o emitir |

> **Residuo declarado (PI-10) — quarta ocorrencia da mesma familia.** O objeto deste `FIT`
> inclui **PS-2026-003**, que contem a emenda candidata **da propria Carta de DEP-QAR**.
> **`DEP-QAR I-5`** o impede de *aprovar, revisar ou emendar* essa Carta — e **nao** o impede de
> medir hash e contagem de linhas, operacao reproduzivel por terceiro e sem juizo de merito
> (mesma distincao de [MSG-2026-0003](../../memory/operacional/MSG-2026-0003-ato-soberano-emenda-qar-e-criterio-de-consolidacao.md),
> achado **RC-02**). **A revisao de merito da emenda `DEP-QAR` 1.2.0 foi executada por DEP-GOV,
> fora desta cadeia.** Ressalva **R3**; achado **RC-08**, que segue aberto.
>
> **Alternativa recusada:** escalar a aprovacao deste `FIT` ao SOBERANO — recusada por
> proporcionalidade *(C2/Tipo 2)* e porque **sobrecarregaria o mesmo ato** que ja aguarda
> decisao sobre oito objetos.

---

## Sumario

| # | Pergunta | Resposta | Sinal |
|---|---|---|---|
| F1 | Complexidade aumentou sem ganho proporcional? | **Nao** | **+1.185 linhas (3,3%)** contra **117 verificacoes de contrato**, **6 achados novos**, **2 defeitos corrigidos**, **3 emendas candidatas prontas** e **0** entidades, tipos, camadas, fundacionais ou Cartas alterados |
| F2 | Algum conceito foi duplicado? **e** a prevencao foi aplicada? | **Nao · aplicada** | **4** reproducoes barradas; a mais importante e **a segunda projecao comparativa que nao foi criada** |
| F3 | Alguma abstracao ficou desnecessaria? | **Nao — e nenhuma foi criada** | **Zero** regras novas. E o **primeiro ciclo em seis** que nao institui regime preventivo |
| F4 | Continua mais simples de evoluir? | **Sim** | O ato passou de **impossivel de emitir sem trabalho** a **assinavel**: a minuta traz os **oito** hashes integrais |
| F5 | Custo de contexto subiu ou desceu? | **DESCEU** — **13,3%** contra 18,9% | **7a medicao, 3a itemizada.** **Segunda descida consecutiva comparavel** |
| F6 | Favorece reutilizacao? | **Sim** | O metodo de verificacao das **13 dimensoes** e o de **`H-P` projetado** servem a toda Carta e a todo ato futuros |

**Veredito:** `apto-com-ressalva` — **quatro** ressalvas, todas com dono e gatilho.
**Fechamento da camada: `BLOCKED`** (§Fechamento).

---

## F1 — A complexidade aumentou sem ganho proporcional?

| Medida | Antes | Depois | Variacao |
|---|---|---|---|
| Artefatos | 131 | **134** | **+3** |
| Linhas | 35.701 | **36.886** | **+1.185 (3,3%)** |
| Entidades declaradas · instanciadas | 21 · 10 | **21 · 10** | **0** |
| Tipos documentais · com instancia | 33 · 17 | **33 · 17** | **0** |
| Documentos fundacionais | 10 | **10** | **0** — **e nenhuma foi emendada** |
| Camadas · templates · portoes · departamentos | 5 · 19 · 7 · 9 | **5 · 19 · 7 · 9** | **0** |
| **Cartas de Departamento alteradas** | — | **0** | **O numero mais importante desta tabela** |
| **Cartas em vigor** | 4 | **4** | **0** — as cinco continuam dependendo de ato |
| **Regras normativas novas** | — | **0** | **Primeiro ciclo em seis sem regime preventivo novo** |
| **Verificacoes de contrato executadas** | — | **117** | 13 dimensoes × 9 Cartas |
| Achados **novos** | — | **6** *(RD-01 a RD-06)* | **2** corrigidos · **1** tratado · **3** com dono e gatilho |
| **Ressalvas e achados fechados** | — | **0** | R4 de FIT-2026-008 **reclassificada, nao fechada** |
| **Emendas candidatas produzidas** | — | **3** | Com diff literal, `H-A` e `H-N` |
| Artefatos **M1** editados | — | **0** | Nenhum `FIT`, `REV`, `ADR` aprovado, `MSG` ou baseline anterior |
| **Documentos fundacionais emendados** | — | **0** | Verificavel por `diff` |
| Cartas de Capability alteradas | — | **0** | — |
| Agentes, skills, workflows, specs, produtos, codigo, infra | — | **0** | Conforme determinacao |
| **Consolidacoes executadas** | 0 em 8 ciclos | **0** | **9o ciclo** — ressalva R4 |
| Indices atualizados *(M3 derivado)* | — | **4** | `departments/README`, `governance/README`, `fitness/README`, catalogo mestre |

**Leitura.** E o **menor acrescimo da serie desde a Missao 1.4**, e a contrapartida nao e
cobertura nova: e **verificacao**. **117 confrontos entre declaracao e fonte**, dos quais 113
conformes e 4 achados — e **tres achados que nenhum instrumento anterior alcancava**, porque
nenhum comparava a secao 6.3 de cada Carta contra a **propria linha** da matriz de FND-02 §4.

**Contrapartida honesta:** **nenhuma Carta entrou em vigor**, **nenhuma ressalva fechou**, e o
acervo cresceu pelo **nono ciclo consecutivo**. **A missao produziu instrumento, nao vigencia.**

**Resposta:** **nao**.

## F2 — Algum conceito foi duplicado? E a prevencao foi aplicada?

### F2.a — Ocorrencia

| Conceito | Onde ja estava | Como a mudanca o trata |
|---|---|---|
| **Projecao comparativa das nove Cartas** | `departments/README §2` | **Segunda projecao barrada.** A verificacao das 13 dimensoes entrou como **§2.2 da projecao existente**, e nao como artefato novo. **Era a duplicacao mais provavel desta missao** |
| Diff das tres emendas | — | **Um** lugar: `PS-2026-003 §2`. `PT-2026-001` o **referencia** e nao o reproduz |
| Hashes das cinco Cartas | `PS-2026-002 §2` | **Reconferidos, nao recopiados como fonte nova.** `PT-2026-001 §1.2` os republica **com a finalidade declarada** de compor a minuta do ato — e aponta PS-2026-002 como fonte |
| Estado das ressalvas | `fitness/README` | `governance/README` **corrigido para apontar a fonte**, em vez de manter contagem propria divergente — achado **RD-04** |
| Contagem do acervo | catalogo mestre §10 | `resumo` do proprio catalogo **corrigido** — achado **RD-06** |

**Nenhuma duplicacao nova introduzida, e duas antigas eliminadas.**

### F2.b — Prevencao *(PJ-06)*

| Verificacao | Evidencia | Resultado |
|---|---|---|
| O autor percorreu cada tabela pelo item de PJ-05? | Todas as tabelas dos 3 artefatos novos e das 4 secoes acrescidas | **Sim** |
| Alguma reproducao foi **barrada antes** de ser escrita? | **4** — a segunda projecao comparativa, o diff das emendas em PT-2026-001, a matriz de FND-02 §4 e a tabela de ressalvas | **Sim** |
| O teste encontrou algo que a auditoria posterior nao encontraria? | **3 — RD-01, RD-02 e RD-03.** Os tres so aparecem no confronto **linha a linha** entre a Carta e a **sua** linha da matriz | **Sim** |
| O instrumento foi validado contra um grupo de controle? | **Sim** — a reimplementacao de `H-N` foi rodada **primeiro** sobre as quatro Cartas ja ratificadas e reproduziu os `H-N` delas; o metodo de medicao de secao foi validado contra os valores **ja declarados** em `DEP-KMS`, `DEP-ENG` e `DEP-QAR`, reproduzindo **68 · 139 · 460**, **55 · 115 · 400** e **50 · 111** exatamente | **Sim** |

> **Setima confirmacao de [MEM-APR-0002](../../memory/aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md),
> e a familia cresceu de novo.** Ate a missao anterior o mecanismo chegara a *fontes irmas que
> divergem entre si*. Agora chega a **fonte que diverge da propria leitura obrigatoria**:
> **RD-02** nao e uma Carta contra outra, e uma **celula de FND-02 §4 contra a nota que a mesma
> tabela publica logo abaixo**. **Nenhuma Carta pode corrigir isso**, e as tres que a leram
> chegaram a **tres** conclusoes diferentes — todas defensaveis.
>
> **A licao operacional e a do grupo de controle, aplicada pela segunda vez.** O metodo de
> medicao de secao foi rodado **primeiro** contra numeros ja publicados. Ele os reproduziu — e
> **falhou** em um: `DEP-QAR`, que declara 386 onde ha 387. **Foi assim que se soube que o
> instrumento estava certo e a Carta errada**, e nao o contrario.

**Resposta:** nao houve duplicacao nova · prevencao **aplicada**, com evidencia.

## F3 — Alguma abstracao ficou desnecessaria?

| Abstracao | Membros antes | **Membros agora** | Veredito |
|---|---|---|---|
| **`DC-01` a `DC-10`** | 10 de 10 exercidas sobre 9 Cartas | **10 de 10, agora com verificacao item a item** | **Justificada, e reforcada.** As 13 dimensoes sao a **primeira aplicacao sistematica** do contrato como instrumento de auditoria |
| **`IR-01` a `IR-12`** | 6 artefatos, 3 com `IR-09` | **6 artefatos** · **`IR-07` exercido preditivamente** pela 1a vez *(`H-P` projetado antes do ato)* | **Justificada e ampliada** |
| **`HZ-01` a `HZ-08`** | 0 membros | **0 membros** | ⚠️ **Suspeita mantida.** `HZ-02` nao disparou pelo **segundo** ciclo. Ressalva **R1 de FIT-2026-008**, intacta |
| **`PR-1` · `PR-2`** *(fonte prevalece sobre projecao)* | 0 · 0 | **1 · 0** | **`PR-1` ganha o primeiro membro** — nao entre Carta e Capability, mas na **familia**: RD-04 e RD-06 foram corrigidos **na projecao**, com zero fontes tocadas |
| **Classe `M3`** | 1 membro, 6 usos | **1 membro, 8 usos** | **Justificada** — decidiu RD-04 e RD-06 |
| **Classe `inferred` · classe 4 de autoridade** | 0 | **0** | **Mantida.** Zero e o resultado bom |
| **Portao de admissao** de ADR-0007 | 0 | **0** | **Mantido** — Legacy **nao consultado**, por determinacao |

**Regra aplicada:** abstracao com menos de dois membros e suspeita (AQ-03).

**Resposta:** **nao** — e o dado novo e o inverso do dos cinco ciclos anteriores: **esta missao
nao criou nenhuma regra**. Depois de `FR`, `PJ`, `CT`, `DC`, `IR` e `HZ`, e o **primeiro ciclo
que so exercita o que ja existe**.

## F4 — O sistema continua mais simples de evoluir?

| Mudanca-tipo | Antes | Depois | Aprovacoes |
|---|---|---|---|
| **Emitir o ato que poe as cinco Cartas em vigor** | Marcadores a preencher, **hash a levantar de outro arquivo** | **Minuta pronta**, com **8** hashes integrais e as clausulas de nao alcance — [PT-2026-001 §8](../relatorio-transicao-2026-07-29-departamentos.md) | Inalterado |
| **Verificar que o ato foi aplicado sem desvio** | Reconstruir o texto **depois** e comparar | **`H-P` publicado antes** — divergencia e detectavel na hora | Inalterado |
| Saber se uma Carta cumpre o contrato | Ler a Carta e julgar | **13 dimensoes com metodo reproduzivel** | Inalterado |
| Corrigir RC-01, RC-05 e RC-07 | Achado com dono e gatilho, **sem texto** | **Diff literal e hash prontos** — falta so o ato | Inalterado |
| Saber quem produz `SPC`, `PRO`, `TOL` e com que autoridade | Abrir FND-09 §8.2 e nove Cartas | **Um mapa** — [PT-2026-001 §6](../relatorio-transicao-2026-07-29-departamentos.md) | Inalterado |
| Saber o que o Specification Framework **precisa** respeitar | Julgamento | **10 requisitos, todos com a fonte que ja os obriga** | Inalterado |

**Leitura.** **Seis** operacoes ficaram mais baratas, e **nenhuma aprovacao nova foi criada**;
nenhum papel ganhou veto; nenhuma fundacional foi emendada; **nenhuma Carta foi tocada**.

**Contrapartida:** **quatro** questoes continuam dependendo do Soberano — as cinco Cartas, as
tres emendas, Q1 e Q2 — e **uma** nao depende dele e tampouco pode ser resolvida por Carta:
**RD-02**.

**Resposta:** **sim**.

## F5 — A mudanca reduz ou aumenta o custo de contexto?

| Papel / tarefa-tipo | Antes | Depois | Direcao |
|---|---|---|---|
| **Piso obrigatorio de qualquer tarefa** | 1.099 linhas | **1.099 linhas** | **inalterado** |
| **Executar uma missao de verificacao e ato** | **18,9%** — 6a medicao | **13,3%** — 7a medicao | **DESCE** |
| **Saber se uma Carta cumpre as 13 dimensoes** | **9 arquivos = 3.918 linhas** | `departments/README §2.2` — **uma tabela** | **desce** |
| **Emitir ato sobre as cinco Cartas** | PS-2026-002 §2 — **5 tabelas, 90 linhas** | `PT-2026-001 §8` — **um bloco de 35 linhas** | **desce** |
| **Decidir se um departamento pode aprovar algo** | 111–155 linhas | **Inalterado** | **inalterado** |
| Acervo total | 35.701 | **36.886** | **sobe 3,3%** |

### F5.1 A medicao, itemizada — **a terceira da serie**

**Pacote minimo medido: 4.740 linhas sobre 35.701 = 13,3%.** Composicao **itemizada**:

| Bloco | Linhas |
|---|---|
| **Artefatos integrais** — FND-02, ADR-0011, ADR-0012, ADR-0014, PS-2026-002, `departments/README`, `governance/README`, `fitness/README`, FIT-2026-008, MSG-2026-0003, e as **nove** Cartas | **3.059** |
| **Recortes normativos** — FND-09 §5.4/§8, FND-10 §4/§5.2/§10.3, FND-06 §2.1, FND-01 §6.2/§7.3, FND-04 §2 | **241** |
| **Extracoes por ferramenta** — frontmatter das 23 Cartas de Capability; secoes 5, 6.3, 9, 10 e 13.2 das nove Cartas | **850** |
| **Indices abertos para propagar (C11)** | **590** |
| **Total** | **4.740** |

**A serie observada e 23% · 33% · 30,6% · 18,5% · 21,3% · 18,9% · 13,3%.**

> ### O que esta medicao fecha — e o que ela **nao** fecha
> **E a terceira medicao itemizada, e a segunda comparavel consecutiva.** A sexta mediu **18,9%**
> com composicao declarada; esta mede **13,3%** com composicao declarada. **A comparacao e
> valida.**
>
> **R4 de FIT-2026-002 exige duas descidas consecutivas com composicao itemizada.** Esta e a
> **segunda**. **A ressalva satisfaz agora a condicao literal que ela propria escreveu** — e
> **nao e fechada aqui**, por um motivo que precisa ficar registrado: **o criterio endurecido
> por RE-08 pede duas descidas, e nao diz se descidas explicadas por natureza da missao
> contam.** A sexta medicao declarou que a queda foi **da missao, nao da arquitetura**; esta
> declara o mesmo mecanismo — **uma missao de verificacao abre menos indices que uma de
> producao**. **Fechar a ressalva com duas descidas de mesma causa seria fechar por coincidencia
> de natureza de missao, nao por ganho estrutural.**
>
> **Encaminhamento:** a ressalva permanece **aberta**, e o gatilho passa a exigir **uma descida
> em missao de producao** — o unico caso ainda nao observado. **Dono: DEP-KMS.** **Nao e criterio
> novo: e o mesmo criterio, com a variavel que ele ja pressupunha tornada explicita.**

**Resposta:** **desceu** — **e a ressalva nao fecha, pelo motivo escrito acima.**

## F6 — Ela favorece reutilizacao?

| Definicao produzida | Reutilizavel por | Especifica do caso? |
|---|---|---|
| **Verificacao das 13 dimensoes** | **Toda Carta futura** — de Departamento, e de Agente quando existir | Nao |
| **`H-P` projetado antes do ato** | **Todo ato de ratificacao futuro.** Torna a aplicacao verificavel por terceiro **no momento**, e nao depois | Nao |
| **Minuta preenchida no proprio pacote** | **Todo pacote soberano futuro** — e a resposta a **RD-05** | Nao |
| **Confronto §6.3 × propria linha da matriz** | **Toda** verificacao de interface entre componentes declarados numa matriz | Nao |
| **Candidato como diff + hash, fora do acervo** | **Toda** emenda a artefato ratificado | Nao |
| **Classificacao normativo × operacional × projecao** | **Todo** achado que exija decidir *o que se pede* | Nao |
| RD-01 a RD-06 | — | **Sim** — descrevem o estado atual |

**Criterio:** DoD-8.

**Evidencia mais forte:** **o `H-P` projetado**. Ate aqui, `IR-07` era cumprido **depois** do
ato: registrava-se o hash do arquivo ja transformado. Publica-lo **antes** transforma `IR-05` de
regra de auditoria em **regra de deteccao imediata** — se o arquivo pos-transicao nao reproduzir
o valor publicado, houve alteracao alem do diff, e sabe-se disso **no mesmo minuto**.

**Resposta:** **sim**.

---

## Ressalvas

| # | Ressalva | Custo assumido | **Dono** | **Gatilho de reavaliacao** |
|---|---|---|---|---|
| **R1** | **Cobertura vigente permanece 4/9 pelo segundo ciclo consecutivo.** A camada nao fecha por **forma do ato**, nao por defeito de conteudo | Duas missoes de trabalho verificado sem uma unica Carta entrando em vigor. **A cobertura documental e 9/9 ha dois ciclos, e a vigente nao se move** | **SOBERANO**; DEP-GOV | **Ato na forma de [PT-2026-001 §8](../relatorio-transicao-2026-07-29-departamentos.md)** |
| **R2** | **`RD-02` — a fonte fundacional e ambigua quanto ao veto da Guarda sobre a Plataforma**, e as Cartas a resolvem de tres formas | **E o unico achado aberto que toca autoridade**, e por isso o unico que **impede `GO-TO-SPECS` em qualquer cenario de ato** | **DEP-GOV** | Proxima emenda a **FND-02**, ou primeiro veto real sobre Plataforma |
| **R3** | **A segregacao opera no limite pela 4a missao seguida.** DEP-QAR executa este `FIT` com a emenda da propria Carta dentro do objeto; DEP-GOV o aprova; **DEP-EXE e autor de 9 de 9 Cartas e das 3 emendas** | **R1 de FIT-2026-006 nao fecha** e permanece agravada. A estrutura **nao comporta** segregacao completa sem agentes | **DEP-GOV** | **Primeiro agente criado**, ou **IC-3** resolvido. Achado **RC-08** |
| **R4** | **9o ciclo consecutivo de crescimento, e o 2o sem nenhuma Carta em vigor.** Zero consolidacoes em nove ciclos | O acervo cresce **3,3%** numa missao que **nao produziu cobertura nova**. **`HZ-01` retira a leitura de que crescer e falha**, e **nao** retira o fato | **DEP-EXE** | **Primeiro horizonte avaliavel sob `HZ-02`** — **mesmo gatilho de R2 de FIT-2026-008**, deliberadamente **nao contado em dobro** |

## Veredito

| Campo | Conteudo |
|---|---|
| Veredito | **`apto-com-ressalva`** |
| Fundamento | As seis perguntas tem sinal observavel. **117 verificacoes de contrato** com **113 conformes**; **seis achados novos**, dos quais **dois corrigidos** e **um tratado**; **tres emendas candidatas** com diff literal e hash, fechando o gatilho literal de R4 de FIT-2026-008; **zero regras novas** — o primeiro ciclo em seis; **zero Cartas alteradas**; **zero fundacionais emendadas**; e o custo de contexto **desce pela segunda vez consecutiva de forma comparavel**. Em contrapartida, **nenhuma Carta entrou em vigor**, **nenhuma ressalva fechou**, o acervo cresce pelo **nono** ciclo e a segregacao opera no limite pela **quarta** missao. **Nao e `inapto`** porque nenhuma falha estrutural foi encontrada e **nenhuma divida foi fechada por renomeacao**. **Nao e `apto` sem ressalva** porque quatro dividas seguem abertas, com dono e gatilho |
| Efeito | **Encerra a mudanca C2.** As quatro ressalvas viram divida declarada (FND-07 §9) |
| Data | 2026-07-29 |
| Executado por | **DEP-QAR** |
| Aprovado por | **DEP-GOV** — DEP-EXE impedido (CX-3) |
| Ratificado por | **Nao aplicavel** — objeto C2/Tipo 2. **Se isso e correto e a questao Q2**, escalada |

## Fechamento da camada — **`BLOCKED`**

> **Criterio de fechamento, herdado sem alteracao** de [FIT-2026-008 §Fechamento](FIT-2026-008-rollout-das-cartas.md):
> a camada e **pronta para consumo** somente com **(a)** cobertura 9/9, **(b)** autoridade
> inequivoca, **(c)** validacao independente, **(d)** rastreabilidade e **(e)** pacote soberano
> completo. **O criterio nao foi afrouxado nem endurecido para caber no resultado.**

| # | Condicao | Estado | Evidencia |
|---|---|---|---|
| **(a)** | **Cobertura 9/9** | ⚠️ **Documental sim · vigente NAO** | **9** Cartas escritas; **4** em vigor. **Carta que nao vigora nao pode ser consumida** (LM-02) |
| **(b)** | **Autoridade inequivoca** | ❌ **NAO — e a mudanca desta missao** | **76 de 76** linhas de autoridade citam a fonte; **0** autoridades autodeclaradas. **Mas `RD-02` mostra que a propria fonte e ambigua** num ponto que decide se a Guarda veta a Plataforma. **Ate FIT-2026-008 esta condicao estava "cumprida com ressalva"; agora nao esta cumprida** |
| **(c)** | **Validacao independente** | ✅ **Cumprida** | **117** verificacoes de contrato; **1.465** links resolvidos com **0** quebrados; **73** artefatos com autor e revisor e **0** coincidencias |
| **(d)** | **Rastreabilidade** | ✅ **Cumprida** | Cadeia **ato → versao → conteudo → estado** fechada por `H-A`, `H-N`, **`H-P` projetado** e `IR-09`; **0** artefatos M1 editados |
| **(e)** | **Pacote soberano completo** | ✅ **Cumprida, e ampliada** | PS-2026-002 *(cinco Cartas)* · **PS-2026-003** *(tres emendas)* · **minuta preenchida** em PT-2026-001 §8 |

### A decisao, e por que **piorou** em relacao ao ciclo anterior

| Campo | Conteudo |
|---|---|
| **Decisao** | **`BLOCKED`** |
| **Causa imediata** | **Pre-condicao 1 nao satisfeita:** o ato consumido traz `[VERSAO]` e `[HASH INTEGRAL]` em vez de enumerar as cinco Cartas |
| **Por que nao `READY-FOR-RATIFICATION`**, como no ciclo anterior | Porque **a condicao (b) deixou de estar cumprida**. Em FIT-2026-008 a ressalva de autoridade era **IC-2**, *contido por `IR-11` com 0 violacoes*. Agora ha **`RD-02`**, que **nenhuma contencao alcanca**: nao e termo ambiguo em artefato novo, e **celula ambigua na fonte** |
| **Por que nao `ADJUST`** | Nenhuma correcao delimitada resta **dentro do mandato**. As correcoes possiveis foram feitas *(RD-04, RD-06)*; as impossiveis estao declaradas com dono e gatilho |
| **Por que nao `STOP`** | **Zero** falhas estruturais: 113 de 117 conformes, 0 links quebrados, 0 autoverificacoes, integridade do acervo **byte a byte identica** a `BL-2026-07-28-06` na abertura |
| **A camada esta pronta para consumo?** | **NAO.** E a resposta e **mais firme** que a do ciclo anterior: alem de 5 Cartas fora de vigor, ha **um ponto de autoridade que a fonte nao resolve** |
| **Desempenho** | **Nao exercido, logo nao comprovado.** **41 de 123** indicadores `definido, sem valor`; os **82** medidos descrevem **o acervo**. **Nenhuma Carta foi exercida em operacao real** — inalterado |

## Pendencias para o SOBERANO — **quatro**

> Esta secao **informa e pergunta**; nao decide, nao presume e nao antecipa (LM-03, LM-06).

| # | Pendencia | Origem | Se nao houver ato |
|---|---|---|---|
| **PS-2** | **As cinco Cartas em `em-revisao`** | DC-09 | Cobertura vigente permanece **4/9**. **Terceiro ciclo** |
| **PS-3** | **Emenda C3 a FND-01 §7.3** | Q1; ADR-0014 | **IC-2 permanece contido** por `IR-11`, quinto ciclo |
| **PS-4** | **`FIT` exige ratificacao?** | Q2 | **G1/G2 permanece aberta.** O **item 4** da minuta a alcanca por **determinacao** — [PT-2026-001 §8](../relatorio-transicao-2026-07-29-departamentos.md) |
| **PS-5** | **As tres emendas locais** — `DEP-KMS` 1.1.0, `DEP-ENG` 1.1.0, `DEP-QAR` 1.2.0 | R4 de FIT-2026-008 | **RC-01, RC-05 e RC-07 permanecem abertos** em Cartas **em vigor**. Nada quebra; a divida envelhece |

### Nota sobre FT-04 — vigilancia de complacencia

| Verificacao | Estado |
|---|---|
| Vereditos emitidos | **9** |
| Consecutivos `apto` **sem nenhuma ressalva** | **0** — os nove com ressalvas |
| `inapto` emitidos | **0** — **em nove oportunidades** |
| Ressalvas fechadas neste ciclo | **0** |
| Achados novos | **6** |
| **Recomendacoes de APROVAR nos pacotes soberanos** | **3 de 3** neste; **8 de 8** acumulado |

FT-04 exige tres `apto` **sem ressalva** para disparar; nao e o caso.

> **Dois numeros a vigiar, e eles apontam em direcoes opostas.** **Zero ressalvas fechadas** e o
> pior resultado da serie desde o 4o ciclo — e a causa esta escrita: a ressalva que esta missao
> existia para fechar **depende de ato**. **Seis achados novos** e o segundo maior da serie — e a
> causa tambem: pela primeira vez o contrato foi usado **como instrumento de auditoria**, e nao
> so como criterio de producao.
>
> **O alarme real desta verificacao e outro, e nao aparece em nenhuma das duas contagens: a
> missao encerrou `BLOCKED` por um defeito de forma que o proprio sistema podia ter evitado.**
> **PS-2026-002 §2 publicava, ha um ciclo, todos os hashes que a minuta pedia** — e o pacote
> entregou os dados sem entregar a minuta preenchida. **Achado RD-05.** Corrigido para o futuro:
> todo pacote soberano passa a entregar o **texto do ato**, e nao apenas os insumos dele.

## Aprendizado gerado

| Registro APR | Licao |
|---|---|
| [MEM-APR-0002](../../memory/aprendizado/MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md) | **Setima confirmacao, com alcance ampliado pela sexta vez:** o mecanismo chegou a **fonte que diverge da propria leitura obrigatoria** — uma celula de FND-02 §4 contra a nota publicada logo abaixo dela. Acao: **toda tabela normativa com "leituras obrigatorias" exige conferencia celula × nota antes de ser projetada.** Dono: DEP-GOV |
| [MEM-APR-0004](../../memory/aprendizado/MEM-APR-0004-projecao-revela-divergencia-antiga.md) | **Quarta confirmacao:** a verificacao das 13 dimensoes revelou **RD-01, RD-02 e RD-03**, um deles em Carta em vigor desde a Missao 1.7. Acao: **contrato tambem e instrumento de auditoria, e nao so criterio de producao.** Dono: DEP-KMS |
| A gravar por DEP-KMS *(QG-5)* | **Pacote de decisao entrega o texto do ato, nao so os insumos.** Esta missao parou porque o ato chegou com marcadores, embora os valores estivessem publicados ha um ciclo. Acao: **todo pacote soberano anexa a minuta com ID, versao e hash integral ja preenchidos.** Dono: DEP-GOV |
| A gravar por DEP-KMS *(QG-5)* | **Publicar o hash do estado futuro torna a violacao detectavel na hora.** `H-P` projetado antes do ato transforma `IR-05` de auditoria posterior em deteccao imediata. Acao: **todo pacote de ratificacao publica o `H-P` projetado.** Dono: DEP-QAR |
| A gravar por DEP-KMS *(QG-5)* | **Descida de custo com a mesma causa duas vezes nao e tendencia.** Duas quedas consecutivas explicadas por *"missao que abre poucos indices"* nao demonstram ganho estrutural. Acao: **o gatilho de R4 de FIT-2026-002 passa a exigir uma descida em missao de producao.** Dono: DEP-KMS |

## Historico de vereditos sobre este objeto

| FIT | Data | Veredito | Relacao |
|---|---|---|---|
| FIT-2026-005 | 2026-07-28 | `apto-com-ressalva` | Contrato de Carta; **R1** *(autor distinto)* **mantida** |
| FIT-2026-006 | 2026-07-28 | `apto-com-ressalva` | Validacao interclasses; **R1** **mantida e agravada** |
| FIT-2026-007 | 2026-07-28 | `apto-com-ressalva` | Revisao estrutural; **R4** *(Q1 e Q2)* **mantida** |
| FIT-2026-008 | 2026-07-28 | `apto-com-ressalva` | Rollout; **R4** **reclassificada** aqui, **nao fechada** |
| **FIT-2026-009** | 2026-07-29 | **`apto-com-ressalva`** | **Nao supera nem edita nenhum anterior** (M1, LV-04, FT-09). **Fecha zero ressalvas** e e o **primeiro do sistema a rebaixar uma condicao de fechamento** — a **(b)**, de *cumprida com ressalva* para **nao cumprida** |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-29 | DEP-QAR | Verificacao de aptidao da **Missao 1.10**: seis perguntas com sinal observavel; **117 verificacoes de contrato** com **113 conformes**; **seis achados novos** *(RD-01 a RD-06)*, dois corrigidos e um tratado; **zero regras novas** — primeiro ciclo em seis; **zero Cartas alteradas**; **F5 desce pela segunda vez consecutiva** na **3a medicao itemizada**, e **R4 de FIT-2026-002 nao fecha**, com o motivo escrito; **quatro ressalvas** novas; **zero ressalvas fechadas**; e fechamento **`BLOCKED`** — o **primeiro veredito do sistema a rebaixar uma condicao de fechamento**, a **(b)**, por causa de **RD-02**. |
