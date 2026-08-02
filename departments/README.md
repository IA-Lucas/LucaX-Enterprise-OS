---
id: IDX-departamentos
titulo: Indice e Projecao Comparativa das Nove Cartas de Departamento
tipo: relatorio
versao: 1.6.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-07-28
atualizado_em: 2026-07-30
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0001, ADR-0002, ADR-0008, ADR-0011, ADR-0018, ADR-0023, ADR-0025]
substitui: []
substituido_por: null
projecao_de: [departments/*/carta.md, capabilities/CAP-*.md, foundation/02-estrutura-organizacional.md]
resumo: Indexa as nove Cartas de Departamento e projeta a comparacao unica entre elas — classes, custodia, exercicio, portoes, memoria, impedimentos e lacunas.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# Cartas de Departamento — indice e projecao comparativa

> **✅ Cinco Cartas 1.1.0 ESTAO EM VIGOR, e `QG-1` tem uma unica resposta em todo o acervo.**
> O **ato soberano de 2026-07-30**
> ([MSG-2026-0007](../memory/operacional/MSG-2026-0007-ato-soberano-vigencia-do-framework-de-specifications.md))
> aprovou e ratificou **`DEP-PRD`** *(429 → 445 linhas)*, **`DEP-EXE`** *(481 → 506)*,
> **`DEP-OPS`** *(437 → 438)*, **`DEP-GRW`** *(443 → 444)* e **`DEP-TLS`** *(424 → 425)* —
> por [ADR-0023](../decisions/ADR-0023-propagacao-de-qg-1-e-aprovacao-de-spec-nas-cartas.md)
> e [ADR-0025](../decisions/ADR-0025-extensao-da-propagacao-de-qg-1-as-cartas-restantes.md).
>
> **Medicao no acervo em vigor, `RD-31` e `RD-37` FECHADOS:** a familia das **nove** Cartas
> passou de **11 afirmacoes falsas em 4 Cartas** para **`0` em `0`**, com **63 ocorrencias** de
> `QG-1` e **5 de 9** Cartas nomeando **`DEP-EXE`** como titular — onde antes **nenhuma** o
> nomeava. **`DEP-ENG` nunca teve afirmacao falsa:** menciona `QG-1` duas vezes, e **nenhuma
> atribui titularidade**. `DEP-GOV`, `DEP-KMS` e `DEP-QAR` **nao o mencionam**.
>
> **Os cinco caminhos de titularidade concordam:** `FND-01 §6.2` *(fonte)*, `FND-09 §8.2`
> *(por remissao a classe)*, `FND-10 §10.3` *(cascata)*, a tabela **Portoes que libera** deste
> indice, e as **nove** Cartas. **Nenhum contradiz outro.**

## Proposito
Responder, em **uma leitura**, o que distingue e o que iguala os nove departamentos — e
**fechar o achado DR-4**, cujo gatilho literal era *"a quinta Carta"*.

## Escopo
| Item | Definicao |
|---|---|
| Inclui | As **nove** Cartas; a comparacao entre elas nas dimensoes que ADR-0011 torna obrigatorias; as lacunas encontradas |
| **Nao** inclui | O **merito** de cada Carta *(objeto de [REV-ROLLOUT](../foundation/revisao-arquitetural-rollout-cartas-2026-07-28.md))*; o **ato** que as poe em vigor *(objeto de [MSG-2026-0004](../memory/operacional/MSG-2026-0004-ato-soberano-cartas-emenda-constitucional-e-regime-do-fitness-check.md))* |
| Natureza | **Projecao**, nunca fonte. Divergencia e defeito **deste** indice (PJ-03, RG-03) |

> **Declaracao de projecao (PJ-02, [ADR-0008](../decisions/ADR-0008-uma-fonte-multiplas-projecoes.md)).**
> **Fonte:** o frontmatter e as secoes 2, 5, 9, 10, 11 e 13 das **nove** Cartas em
> `departments/<dep>/carta.md`; o frontmatter das **23** Cartas de Capability; e
> [FND-02 §2.1 e §3](../foundation/02-estrutura-organizacional.md).
> **Campos projetados:** classe, nivel, autonomia, subordinacao, custodia, exercicio, portoes,
> papel por camada de memoria, contagem de impedimentos e de indicadores, e custo medido de
> carregamento.
> **Finalidade:** responder *"o que distingue um departamento do outro"* sem abrir nove
> arquivos — pergunta que nenhuma Carta responde sozinha, porque cada uma declara **apenas as
> proprias linhas** (DC-08).
> **Metodo de atualizacao:** pela mesma mudanca que altera qualquer Carta (CV-04).

---

## 1. As nove Cartas

| # | Departamento | Classe | Arquivo | Versao | Estado | Ratificacao |
|---|---|---|---|---|---|---|
| 1 | **DEP-EXE** — Gabinete Executivo | Comando | [`exe/carta.md`](exe/carta.md) | **1.1.0** | **`ativo`** | **ratificada** — [MSG-2026-0007](../memory/operacional/MSG-2026-0007-ato-soberano-vigencia-do-framework-de-specifications.md) |
| 2 | **DEP-GOV** — Governanca e Conformidade | Guarda | [`gov/carta.md`](gov/carta.md) | 1.0.0 | **`ativo`** | **ratificada** — [MSG-2026-0004](../memory/operacional/MSG-2026-0004-ato-soberano-cartas-emenda-constitucional-e-regime-do-fitness-check.md) |
| 3 | **DEP-QAR** — Qualidade e Risco | Guarda | [`qar/carta.md`](qar/carta.md) | **1.2.0** | **`ativo`** | **ratificada** — [MSG-2026-0005](../memory/operacional/MSG-2026-0005-ato-soberano-aplicacao-dep-qar.md) |
| 4 | **DEP-PRD** — Produto e Estrategia | Linha | [`prd/carta.md`](prd/carta.md) | **1.1.0** | **`ativo`** | **ratificada** — [MSG-2026-0007](../memory/operacional/MSG-2026-0007-ato-soberano-vigencia-do-framework-de-specifications.md) |
| 5 | **DEP-ENG** — Engenharia | Linha | [`eng/carta.md`](eng/carta.md) | **1.1.0** | **`ativo`** | **ratificada** — [MSG-2026-0006](../memory/operacional/MSG-2026-0006-ato-soberano-aplicacao-integral.md) |
| 6 | **DEP-OPS** — Operacoes | Linha | [`ops/carta.md`](ops/carta.md) | **1.1.0** | **`ativo`** | **ratificada** — [MSG-2026-0007](../memory/operacional/MSG-2026-0007-ato-soberano-vigencia-do-framework-de-specifications.md) |
| 7 | **DEP-GRW** — Crescimento e Receita | Linha | [`grw/carta.md`](grw/carta.md) | **1.1.0** | **`ativo`** | **ratificada** — [MSG-2026-0007](../memory/operacional/MSG-2026-0007-ato-soberano-vigencia-do-framework-de-specifications.md) |
| 8 | **DEP-KMS** — Conhecimento e Memoria | Plataforma | [`kms/carta.md`](kms/carta.md) | **1.1.0** | **`ativo`** | **ratificada** — [MSG-2026-0006](../memory/operacional/MSG-2026-0006-ato-soberano-aplicacao-integral.md) |
| 9 | **DEP-TLS** — Ferramentas e Integracoes | Plataforma | [`tls/carta.md`](tls/carta.md) | **1.1.0** | **`ativo`** | **ratificada** — [MSG-2026-0007](../memory/operacional/MSG-2026-0007-ato-soberano-vigencia-do-framework-de-specifications.md) |

**Cobertura: 9 de 9 departamentos com Carta escrita, e 9 de 9 em vigor.** A cobertura
**vigente** alcancou a **documental** pelo ato soberano de 2026-07-29 —
[MSG-2026-0004](../memory/operacional/MSG-2026-0004-ato-soberano-cartas-emenda-constitucional-e-regime-do-fitness-check.md),
com `H-P` de cada Carta conferido contra o valor **projetado antes do ato** e `IR-09`
reproduzindo `H-A` nas cinco (DC-09, IR-07 a IR-09).

**Cinco Cartas foram emendadas a 1.1.0 pelo ato de 2026-07-30**
([MSG-2026-0007](../memory/operacional/MSG-2026-0007-ato-soberano-vigencia-do-framework-de-specifications.md)),
sob o **mesmo regime de prova**: `H-P` **projetado antes** e reproduzido nos **64 digitos** nas
cinco, `H-N` **invariante** nas cinco, e `IR-09` reconstruindo `H-A` nas cinco. **Seis das nove
Cartas ja passaram por `O4` com `H-P` publicado antes da escrita.**

## 2. Projecao comparativa — a leitura unica

| Dimensao | EXE | GOV | QAR | PRD | ENG | OPS | GRW | KMS | TLS |
|---|---|---|---|---|---|---|---|---|---|
| **Classe** | Comando | Guarda | Guarda | Linha | Linha | Linha | Linha | Plataforma | Plataforma |
| **Nivel** | **1** | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| **Autonomia** | **A3** | A2 | A2 | A2 | A2 | A2 | **A1** | A2 | **A1** |
| **Responde a** | SOBERANO | **SOBERANO** | **SOBERANO** | DEP-EXE | DEP-EXE | DEP-EXE | DEP-EXE | DEP-EXE | DEP-EXE |
| **Veta?** | nao | **sim** | **sim** | nao | nao | nao | nao | nao | nao |
| **Custodia** | 4 | **1** | 3 | 3 | **5** | 2 | 2 | 2 | **1** |
| **Exerce** | 4 | 1 | 3 | 3 | 5 | 2 | 2 | **3** | 1 |
| **Portoes que libera** | QG-0 · **QG-1** | QG-2 · QG-6 | QG-3 · QG-4 · QG-6 | **nenhum** | QG-2 | **nenhum** | **nenhum** | QG-5 | **nenhum** |
| **Camada de memoria que possui** | — | **EST** | — | **PRD** | **TEC** | **OPR** | — | **APR** | — |
| **Impedimentos declarados** | **10** | **12** | 7 | **12** | **9** | 11 | **13** | **11** | 11 |
| **Indicadores** *(def / medidos / sem valor)* | 14/9/5 | **17**/14/3 | 11/8/3 | 13/7/6 | 12/7/5 | 14/9/5 | 14/8/6 | 16/13/3 | 12/7/5 |
| **Carta integral** *(linhas)* | **506** | 457 | **388** | 445 | **402** | 438 | 444 | **464** | 425 |
| **Recorte de decisao** *(linhas)* | **172** | 133 | **111** | 145 | **116** | 136 | 144 | **141** | 125 |

**Totais medidos:** **23** custodias · **24** vinculos de exercicio · **7** portoes cobertos ·
**5** camadas de memoria com dono · **96** impedimentos declarados · **123** indicadores
definidos, **82** com valor medido · **3.969** linhas de Carta.

> **`Carta integral` e medido por `wc -l`; `Recorte de decisao` e projetado de §13.2 de cada
> Carta.** Em **`DEP-OPS`, `DEP-GRW` e `DEP-TLS`** as duas fontes **divergem** — §13.2 declara
> **437 · 443 · 424** e o arquivo tem **438 · 444 · 425**. **Esta linha exibe o valor medido**,
> nao o declarado: achado **`RD-49`**, **aberto**, familia de `RC-01` e `RD-46`. **Nao e
> corrigivel por edicao** — as tres Cartas foram **ratificadas** em 2026-07-30 (`LV-04`), e a
> correcao exige **ato novo**.

### 2.1 O que a comparacao mostra — e nao mostraria Carta a Carta

| # | Observacao | Leitura |
|---|---|---|
| **C-1** | **Quatro departamentos nao liberam nenhum portao** — OPS, GRW, TLS e, **desde o ato de 2026-07-29**, tambem **PRD** | Nao e lacuna: os sete portoes de FND-01 §6.2 **seguem integralmente cobertos**, e liberar portao nao e propriedade de toda classe. **`QG-1` passou de `DEP-PRD` para `DEP-EXE`** por `ADR-0018`, justamente porque **PRD produz a Spec** e a **regra de portao** veda liberar o que se produz. **Nenhum portao ficou sem dono; nenhum ganhou dois donos indevidos** |
| **C-2** | **As cinco camadas de memoria tem dono, e os cinco donos sao departamentos distintos** | EST→GOV · PRD→PRD · TEC→ENG · OPR→OPS · APR→KMS. **Reproduz exatamente FND-06 §2.1**, sem divergencia |
| **C-3** | **DEP-GRW declara 13 impedimentos — o maior numero do sistema** | E o unico departamento cujo produto **sai da organizacao**. Seis gatilhos **E4**, tambem o maior numero. **Diferenca fundamentada** |
| **C-4** | **DEP-QAR declara 7 impedimentos — o menor** | E tambem a **primeira** Carta escrita e a unica **emendada**. Diferenca **de maturidade do instrumento**, nao de classe — achado **RC-06** |
| **C-5** | **DEP-GOV custodia 1 Capability e declara 12 impedimentos** | Menor custodia, maior alcance de verificacao — a assimetria **P7**, agora com o contrapeso escrito |
| **C-6** | **Dois departamentos operam em A1: GRW e TLS** | Ambos por **natureza do objeto**, nao por desconfianca: saida externa e adocao de ferramenta sao **Tipo 1** (PI-06). **Um e de Linha, outro de Plataforma** — A1 nao e propriedade de classe |
| **C-7** | **DEP-KMS e o unico que exerce sem custodiar** | `CAP-comunicacao`, custodiada por DEP-EXE. **Unico membro de OW-02** no acervo — achado **P1**, ainda com **1** membro |
| **C-8** | **A Guarda responde ao Soberano; todo o resto responde a DEP-EXE** | ES-02 integralmente refletido nas nove. **Zero** excecoes |
| **C-9** | **A menor Carta e a de DEP-QAR (388) e a maior e a de DEP-EXE (506) — variacao de 30%** | A variacao acompanha **numero de custodias e de interfaces**, nao a classe. **A distancia cresceu de 24% para 30% com `DEP-EXE` 1.1.0**, que recebeu a titularidade de `QG-1` |
| **C-10** | **O recorte de decisao custa entre 29% e 34% da Carta nas nove** | **Faixa estreita**, medida com o mesmo metodo em todas. O instrumento de DC-10 e **reproduzivel entre autores e entre classes**. O teto subiu de 33% para **34%** *(`DEP-EXE`)* |

### 2.2 Verificacao das treze dimensoes do contrato — **as nove, uma a uma**

> **Executada na Missao 1.10**, sobre a cobertura **documental** 9/9 — e **antes** do ato
> soberano de 2026-07-29, quando cinco Cartas ainda nao vigoravam. Esta secao verifica
> **conformidade ao contrato**, nunca vigencia: conformidade de Carta que nao vigora **nao a
> coloca em vigor** (LM-02), e o ato que a colocou **nao altera nenhum dos 117 resultados** —
> a transicao **O4** nao tocou nenhuma linha de corpo e `H-N` ficou invariante nas cinco.
> **Metodo:** contagem por ferramenta sobre os nove arquivos, e confronto de cada declaracao
> contra a **fonte** — FND-02 §2.1, §3 e §4; FND-06 §2.1; FND-09 §8.2; e o frontmatter das 23
> Cartas de Capability. **Nenhum numero desta tabela foi estimado.**

| # | Dimensao | Bloco | Verificacao executada | Resultado |
|---|---|---|---|---|
| D-1 | **Identidade** | B1 | `id`, `titulo`, `classe`, `nivel`, `nivel_autonomia`, `responde_a` presentes no frontmatter | **9 de 9** ✅ |
| D-2 | **Classe** | B1 | Classe declarada × FND-02 §2.1 | **9 de 9** ✅ — 1 Comando · 2 Guarda · 4 Linha · 2 Plataforma |
| D-3 | **Mandato** | B1 | Frase unica de mandato em §1 | **9 de 9** ✅ |
| D-4 | **Autoridade** | B4 | **Toda** linha de §5 cita a fonte (DC-04, AU-09) | **76 linhas · 76 com fonte · 0 sem** ✅ |
| D-5 | **Capabilities** | B2 | Custodia e exercicio × frontmatter das 23 Cartas de Capability (PR-1) | **23 custodias · 24 vinculos de exercicio · 0 divergencias** ✅ |
| D-6 | **Fronteiras** | B3 | §4 nomeia o **dono real** de cada exclusao (DC-05) | **9 de 9** ✅ |
| D-7 | **Interfaces** | B5 | §6.3 de cada Carta × a **propria linha** de FND-02 §4 | **9 de 9 reproduzem a propria linha** ✅ — **1 ressalva: RD-03** |
| D-8 | **Memoria** | B7 | §9 × FND-06 §2.1 — dono, escritor, leitor, curador | **9 de 9** ✅ — 5 camadas, 5 donos distintos, **0 divergencias** |
| D-9 | **Incidentes** | B3 · B9 | Ocorrencias do termo *incidente*, e se a Carta declara o **proprio papel** | **9 de 9** ✅ — `DEP-KMS` **1.1.0** declara em §4, §7 e `I-11`. **`RC-05` FECHADO** pelo ato de 2026-07-29 |
| D-10 | **Impedimentos** | B9 | Contagem item a item, com materia, substituto e fonte (DC-03) | **94** — 9·12·7·11·**9**·11·13·**11**·11. **9 de 9** declaram sobre a propria Carta: `DEP-ENG` **1.1.0** declara `I-9`. **`RC-07` FECHADO** |
| D-11 | **Handoffs** | B10 | §8.2 presente, com criterio de aceite **e** de devolucao | **9 de 9** ✅ · gatilhos **E4** em §8: 6·6·5·4·4·5·6·4·5 |
| D-12 | **Contexto** | B12 | §13.2 com custo **medido** e data (DC-10), reproduzido por `sed`+`wc -l` | **6 de 9** ⚠️ **remedido em 2026-07-30** — `DEP-OPS`, `DEP-GRW` e `DEP-TLS` **1.1.0** declaram **437 · 443 · 424** contra **438 · 444 · 425** medidos: as tres receberam a linha de historico **sem remedir §13.2**. Achado **`RD-49`**, **aberto**. `RC-01` *(`DEP-QAR`, 2026-07-29)* permanece **fechado** — nota abaixo |
| D-13 | **Ciclo** | B11 | §12 com gatilhos, sinal observado e destino de cada custodia na extincao | **9 de 9** ✅ |

> **Estado posterior a medicao, declarado sem reescreve-la.** A verificacao acima e a da
> **Missao 1.10** e **nao e refeita aqui**. Desde entao, **`RC-01` fechou** com a aplicacao de
> `DEP-QAR` **1.2.0** *(2026-07-29)*: **D-12 passaria a 9 de 9**. Os demais **113 conformes e
> 3 achados permanecem exatos**. **A medicao historica nao foi editada** — MEM-APR-0004.

**Resultado: 117 verificacoes — 13 dimensoes × 9 Cartas. 113 conformes · 4 achados, todos ja
declarados ou novos com dono e gatilho. 0 violacoes de Principio Imutavel ou Linha Vermelha.**

> **A dimensao que mais rendeu foi a que nenhum instrumento anterior media: D-7.** Confrontar
> §6.3 de cada Carta contra a **propria linha** da matriz — e nao contra a matriz inteira —
> encontrou **RD-03**, em Carta **em vigor desde a Missao 1.7**, e expos **RD-02**, que **nao e
> defeito de Carta nenhuma**: e ambiguidade da propria FND-02 §4. **Quarta confirmacao de
> [MEM-APR-0004](../memory/aprendizado/MEM-APR-0004-projecao-revela-divergencia-antiga.md).**

## 3. Custodia e exercicio — as 23 Capabilities

> **Projecao de segunda ordem.** A fonte e o frontmatter das 23 Cartas de Capability; a
> projecao **primaria** vive em [`capabilities/README §10`](../capabilities/README.md), e esta
> tabela e a leitura **por departamento com Carta**. Em divergencia, prevalece a Carta de
> Capability (PR-1); a divergencia e defeito **desta** tabela.

| Departamento | Custodia | Exerce sem custodiar |
|---|---|---|
| **DEP-EXE** | estrategia · coordenacao · financeiro · comunicacao | — |
| **DEP-GOV** | governanca | — |
| **DEP-QAR** | qualidade · seguranca · juridico | — |
| **DEP-PRD** | produto · pesquisa · design | — |
| **DEP-ENG** | arquitetura · engenharia · dados · inteligencia-artificial · engenharia-de-agentes | — |
| **DEP-OPS** | operacoes · infraestrutura | — |
| **DEP-GRW** | marketing · comercial | — |
| **DEP-KMS** | conhecimento · aprendizado-organizacional | **comunicacao** |
| **DEP-TLS** | integracao | — |

**Verificacao: 23 custodias, 23 Capabilities, 9 departamentos.** **0** Capabilities sem
custodio · **0** custodias duplas · **0** departamentos sem custodia · **1** exercicio sem
custodia.

### 3.1 As quatro classes exercidas, e o que cada uma declara de proprio

| Classe | Departamentos | Propriedade que **so** ela declara | Verificado em |
|---|---|---|---|
| **Comando** | EXE | **Nivel 1** e **A3**; unico que arbitra entre areas de Linha; libera QG-0 | `DEP-EXE §1, §5` |
| **Guarda** | GOV, QAR | **Poder de veto**; responde ao **SOBERANO**; impedimento de ser instruida por outra classe | `DEP-GOV I-6` · `DEP-QAR I-6` |
| **Linha** | PRD, ENG, OPS, GRW | Produz e entrega; **e vetada**, nunca veta; responde a DEP-EXE | as quatro §6.3 |
| **Plataforma** | KMS, TLS | **Serve sem decidir pela Linha** (ES-07); habilita quem atravessa os portoes | `DEP-TLS I-6` · `DEP-KMS I-6` |

**As quatro classes tem, agora, ao menos uma Carta escrita em cada** — e **Guarda**,
**Linha** e **Plataforma** tem duas ou mais, o que permite comparar **dentro** da classe.

### 3.2 Diferenca fundamentada × diferenca sem fundamento

> **Regra aplicada:** diferenca de classe **com** fundamento declarado e valida; diferenca
> **sem** fundamento e achado (ADR-0011; Missao 1.9, entregavel 6).

| Diferenca observada | Fundamentada? | Fundamento ou achado |
|---|---|---|
| Guarda responde ao Soberano; Linha e Plataforma a DEP-EXE | ✅ **Sim** | ES-02, IV-01 |
| So a Guarda veta | ✅ **Sim** | FND-02 §2.1 |
| So EXE e nivel 1 e A3 | ✅ **Sim** | FND-02 §2 |
| GRW e TLS em A1, os demais em A2 | ✅ **Sim** | FND-02 §3, notas de autonomia — Tipo 1 por natureza do objeto |
| OPS, GRW e TLS sem portao | ✅ **Sim** | FND-01 §6.2 atribui os sete a outros; **C-1** |
| Numero de impedimentos varia de **7** a **13** | ⚠️ **Parcialmente** | A variacao acompanha exposicao externa e alcance de verificacao — **exceto DEP-QAR**, cuja diferenca e de **maturidade do instrumento**. Achado **RC-06** |
| Numero de indicadores varia de **11** a **17** | ⚠️ **Parcialmente** | Mesma causa e mesmo achado |
| DEP-KMS nao menciona **incidente** em nenhuma linha | ✅ **Deixou de valer** | **`RC-05` FECHADO** — `DEP-KMS` **1.1.0** declara o proprio papel em §4, §7 e `I-11`, aplicada pelo ato de 2026-07-29 |
| DEP-ENG nao declara impedimento sobre a **propria Carta** | ✅ **Deixou de valer** | **`RC-07` FECHADO** — `DEP-ENG` **1.1.0** declara `I-9`, como as outras oito |

## 4. Interfaces e fronteiras — o cruzamento

> Cada Carta declara **apenas as proprias linhas** (DC-08). Esta secao verifica se as
> declaracoes **fecham entre si** — o que nenhuma Carta pode verificar sozinha.

| # | Par | O que a primeira declara | O que a segunda declara | Fecha? |
|---|---|---|---|---|
| F-1 | PRD → ENG | *"entrega spec"* | *"recebe spec de DEP-PRD"* | ✅ |
| F-2 | ENG → OPS | *"emite componente para operacao"* | *"recebe componente de DEP-ENG"* | ✅ |
| F-3 | OPS → PRD | *"emite sinal de uso real"* | *"recebe sinal de uso de DEP-OPS"* | ✅ |
| F-4 | GRW → PRD | *"emite objecao e motivo de perda"* | *"recebe sinal de mercado de DEP-GRW"* | ✅ |
| F-5 | GRW ↔ ENG | *"sem interacao estrutural direta"* | *"sem interacao estrutural direta"* | ✅ **Ambas declaram a ausencia**, e a fonte e a mesma: FND-02 §4 |
| F-6 | TLS → ENG | *"entrega ferramenta oficial e limite"* | *"recebe ferramenta oficial de DEP-TLS"* | ✅ |
| F-7 | QAR → GOV | *"revisa o produto de DEP-GOV"* | *"recebe revisao independente de DEP-QAR"* | ✅ **RM-06b fechado dos dois lados** |
| F-8 | GOV → QAR | *"registra incidente; nao fecho"* | *"fecho incidente; nao registro nem numero"* | ✅ **Complementares, sem sobreposicao** |
| F-9 | OPS → QAR | *"emite confirmacao de backup"* | *"recebe verificacao de backup"* | ✅ |
| F-10 | KMS → todos | *"entrega pacote de contexto"* | as oito declaram receber de KMS | ✅ |
| F-11 | PRD ↔ TLS | *"emito a DEP-TLS via DEP-ENG ou DEP-EXE"* | *"sem interacao estrutural direta"* | ✅ **Coerentes**: FND-02 §4 declara `—`, e PRD declara a mediacao |

**11 pares verificados · 11 fecham · 0 divergencias · 0 sobreposicoes de escopo.**

### 4.1 Dependencias entre departamentos — **derivadas, nunca declaradas**

> `DEP → DEP` **nao consta** dos pares permitidos de **R-04** ([FND-09 §6.2](../foundation/09-meta-model.md));
> declarar dependencia entre departamentos seria relacao **nula** (RM-02). A leitura abaixo e
> **derivada** de `depende-de` entre Capabilities, e vive integralmente em
> [`capabilities/README §10.2`](../capabilities/README.md) — **nao e reproduzida aqui**.

| Verificacao | Resultado |
|---|---|
| Alguma Carta declara `depende-de` sobre outro departamento? | **Nao — 0 ocorrencias nas nove** |
| Alguma Carta declara autoridade sobre departamento que a fonte nao concede? | **Nao — 0 ocorrencias** (DC-04, AU-09) |
| Ciclo em `depende-de` entre Capabilities | **Sem ciclo** — nenhuma Carta de Capability foi tocada |
| Dependencia ascendente (PD-11) | **Conforme** — estrato 3 `DEP` → estrato 2 `CAP` |

## 5. Segregacao — o mapa dos 92 impedimentos

> Contagem executada **item a item** sobre as 92 linhas de impedimento das nove secoes 10, em
> 2026-07-28. Nenhum numero desta tabela foi estimado.

| Materia do impedimento | Quantos declaram | Quem **nao** declara, e por que |
|---|---|---|
| **Aprovar ou verificar o proprio produto** *(entrega, veredito, ADR, spec, ficha, evidencia)* | **9 de 9** | — |
| **Alterar Carta de Capability** para acomodar a propria Carta | **9 de 9** | — |
| **Aprovar, revisar ou emendar a propria Carta** | **8 de 9** | ❌ **DEP-ENG nao declara.** As outras oito declaram; DEP-ENG cobre apenas *"a propria entrega"* e *"o proprio ADR tecnico"*. **Achado RC-07** |
| **Autoridade fora da cadeia** — instruir a Guarda, ou ser instruido por quem nao coordena | **8 de 9** | **DEP-KMS** declara o equivalente de Plataforma em outra forma: *"decidir por qualquer area servida"* (I-6, ES-07). **Diferenca de redacao, nao de cobertura** |
| **Julgar merito fora do proprio dominio** | **6** — EXE, GOV, PRD, ENG, GRW, TLS | QAR, OPS e KMS delimitam o merito na secao **4**, e nao na 10. **Diferenca de local, nao de cobertura** |
| **Comunicar externamente, ou expor dado** | **4** — PRD, OPS, GRW, TLS | EXE, GOV, QAR, ENG e KMS **nao produzem saida externa**; QAR a **verifica** em QG-4, e verificar nao e produzir |
| **Executar acao destrutiva sem backup verificado** | **1** — OPS | **Unico impedimento do acervo sem substituto possivel**: a acao **nao ocorre** |
| **Executar `IR-09` sobre artefato proprio** | **1** — GOV | Criado por **RC-02** nesta missao |
| **Revisar Carta cuja revisao estrutural produziu** | **1** — GOV | Criado por **RE-03**, condicao de saida do rollout de FIT-2026-007 |

**Verificacao de PI-05 nas nove: nenhuma Carta concede a si propria autoridade de aprovar o
que produz — 9 de 9 declaram o impedimento correspondente. 0 violacoes.**

> **A lacuna de DEP-ENG e de outra natureza, e por isso e achado e nao violacao.** DEP-ENG
> **nao pode** aprovar a propria Carta — a matriz de FND-09 §8.2 atribui a aprovacao ao
> **SOBERANO**, e a autoridade que a fonte nao concede **nao existe** (AU-09). O que falta e a
> **declaracao** do impedimento, que DC-03 exige e que as outras oito fazem. **O efeito e nulo;
> a assimetria e real** — e so aparece quando as nove sao lidas juntas.

## 6. Lacunas — o que as nove Cartas **nao** cobrem

> Lacuna declarada e divida visivel; lacuna omitida e defeito (PI-10).

| # | Lacuna | Natureza | Dono | Gatilho |
|---|---|---|---|---|
| ~~**L-1**~~ | ~~**Cinco Cartas nao estao em vigor** — GOV, PRD, OPS, GRW, TLS~~ | ✅ **FECHADA** — ato soberano de 2026-07-29 | — | Cumprida: [MSG-2026-0004 §6](../memory/operacional/MSG-2026-0004-ato-soberano-cartas-emenda-constitucional-e-regime-do-fitness-check.md). **Cobertura vigente 9/9** |
| **L-2** | **Nenhum agente existe** — as nove descrevem dominios, nao executores | **Determinada** — proibido nesta fase | DEP-EXE | Fase futura; **IC-3** |
| **L-3** | **82 de 123 indicadores tem valor medido; 41 nao tem** | **Determinada** — dependem de ciclo de produto inexistente | cada custodio | Primeiro produto |
| **L-4** | **Nenhuma das nove foi escrita por autor distinto de DEP-EXE** | **Estrutural** — **R1 de FIT-2026-006 nao fecha** | DEP-EXE | Primeiro agente; **IC-3** |
| **L-5** | **`DEP-KMS` nao declara papel diante de incidente** | **Defeito** — achado **RC-05** | DEP-EXE | Proxima emenda a `DEP-KMS`; e **M1 quanto ao texto ratificado** |
| ~~**L-6**~~ | ~~**`DEP-QAR §13.2` declara 386 linhas; o arquivo tem 387**~~ | ✅ **FECHADA** — achado **RC-01** fechado pela aplicacao de `DEP-QAR` **1.2.0**: §13.2 declara **388** e `wc -l` conta **388** | — | Cumprida: [MSG-2026-0005 §4](../memory/operacional/MSG-2026-0005-ato-soberano-aplicacao-dep-qar.md), Z4 |
| **L-7** | **`DEP-ENG` nao declara impedimento sobre a propria Carta** | **Defeito** — achado **RC-07** | DEP-EXE | Proxima emenda a `DEP-ENG` |
| **L-8** | **Nenhuma Carta foi exercida em operacao real** | **Determinada** | — | Primeiro produto; **desempenho nao exercido permanece nao comprovado** |
| **L-9** | **`DEP-KMS §6.3` declara *"entrega a sete departamentos e consulta dois"*; a linha KMS de FND-02 §4 tem **6** `E`, **2** `C` e **1** `—`.** A mesma secao cita *"KMS entrega a todos (FND-02 §4, linha KMS)"*, quando a leitura obrigatoria da fonte e *"**Todos entregam a KMS**"* — a **coluna**, nao a linha | **Defeito** — achado **RD-03**; Carta **ratificada** | DEP-EXE | Proxima emenda a `DEP-KMS`; **nao** incluida em [PS-2026-003](../governance/pacote-soberano-2026-07-29-emendas.md) |
| ~~**L-10**~~ | ~~**Os campos `GOV→KMS` e `QAR→KMS` de FND-02 §4 declaram `E`; a leitura obrigatoria da mesma tabela declara que a Guarda veta Linha **e Plataforma****~~ | ✅ **FECHADA** — achado **RD-02** fechado **na fonte** pela promulgacao de **FND-02 1.3.0**: as **quatro** celulas *(`GOV→KMS`, `QAR→KMS`, `GOV→EXE`, `QAR→EXE`)* declaram `V`, §4.1 define os **seis codigos**, `MI-01` a `MI-06` fixam a semantica e a leitura obrigatoria **R2** passa a *"GOV e QAR vetam qualquer departamento"* | — | Cumprida: [MSG-2026-0006 §2.2](../memory/operacional/MSG-2026-0006-ato-soberano-aplicacao-integral.md) |
| **L-12** | **`DEP-TLS §6.3` declara *"sem interacao estrutural direta"* com `DEP-PRD` e `DEP-GRW` e diz que o pedido de capacidade chega *"por DEP-ENG ou DEP-EXE"*; `DEP-PRD §6.3` e `DEP-GRW §6.3` declaram **consulta direta**, e a fonte declara `C` nos dois casos** | **Defeito** — achado **RD-10**. **Duas Cartas em vigor descrevem caminhos operacionais incompativeis** | DEP-EXE | Proxima emenda a `DEP-TLS` |
| **L-13** | **Quatro celulas de FND-02 1.3.0 — agora em vigor — declaram mais do que a Carta do proprio emissor**: `EXE→KMS`, `GOV→EXE`, `QAR→EXE` e `QAR→KMS` | **Residuo de propagacao** (CV-04) — achado **RD-11**. **Agrava-se com a promulgacao:** deixou de ser divergencia entre Carta e *candidato* e passou a ser divergencia entre Carta e **fonte vigente**. `MI-01` resolve o conflito — **prevalece a celula** —, logo **nao ha ambiguidade normativa**; o que resta e **projecao desatualizada em tres Cartas** | DEP-EXE | Proxima emenda a `DEP-EXE`, `DEP-GOV` e `DEP-QAR` |
| ~~**L-14**~~ | ~~**`QG-1` e liberado por `DEP-PRD`, que produz a Spec**, contra a regra literal de **FND-01 §6.2**~~ | ✅ **FECHADA** — achado **RD-14** fechado **na fonte** pela promulgacao de **FND-01 1.5.0**: §6.2 declara **`DEP-EXE`** e recebe nota normativa que distingue **liberar portao** de **aprovar artefato**. **A autoverificacao de portao deixou de existir**, e `RP-1` de `DEP-PRD` **perde objeto** | — | Cumprida: [MSG-2026-0006 §2.2](../memory/operacional/MSG-2026-0006-ato-soberano-aplicacao-integral.md) |
| **L-11** | **`DEP-PRD §8.2` cita *"FND-02 §4 declara `—` entre PRD e TLS"*; a matriz declara `C` no sentido PRD→TLS e `—` apenas no sentido TLS→PRD** | **Defeito de citacao** — achado **RD-01**; substancia preservada. Carta em **`em-revisao`** | DEP-EXE | **Apos** a decisao sobre PS-2026-002 — corrigir agora mudaria o `H-A` submetido |

> **L-5, L-6, L-7 e L-9 tem a mesma natureza e o mesmo bloqueio: as quatro estao em Cartas ja
> ratificadas.** Corrigi-las altera `H-N` e exige **ato novo** do Soberano (IR-01, IR-05).
> **Nenhuma e corrigida nesta missao.** Tres delas — L-5, L-6 e L-7 — tem emenda candidata
> pronta em [PS-2026-003](../governance/pacote-soberano-2026-07-29-emendas.md); **L-9 nao**, para
> nao inflar um pacote cujo objeto o Soberano ja conhece.

> **L-11 e de outra especie, e a diferenca decide o que se faz com ela.** A Carta de `DEP-PRD`
> **nao esta em vigor** e poderia, em tese, ser corrigida sem ato. **Nao foi** — porque o seu
> `H-A` ja consta de [PS-2026-002 §2.3](../governance/pacote-soberano-2026-07-28-cartas.md) e
> corrigi-la trocaria, sem ato, o objeto que o Soberano vai decidir. **Divergencia se declara;
> correcao silenciosa e o que a missao proibiu por escrito.**

## 7. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Contrato das nove Cartas | [ADR-0011](../decisions/ADR-0011-contrato-de-carta-de-departamento.md) |
| Template | [`TPL-carta-departamento`](../foundation/templates/TPL-carta-departamento.md) **1.2.0** |
| ADR que cria os nove departamentos | [ADR-0001](../decisions/ADR-0001-adocao-da-fundacao-organizacional.md), que adota FND-02 |
| Validacao independente | [REV-ROLLOUT](../foundation/revisao-arquitetural-rollout-cartas-2026-07-28.md) |
| Verificacao de aptidao | [FIT-2026-008](../governance/fitness/FIT-2026-008-rollout-das-cartas.md) |
| Pacote de decisao soberana | [PS-2026-002](../governance/pacote-soberano-2026-07-28-cartas.md) |
| Fonte da custodia e do exercicio | frontmatter de `capabilities/CAP-*.md`; projecao primaria em [`capabilities/README §10`](../capabilities/README.md) |
| Achado que este indice fecha | **DR-4** — *"`departments/` sem indice"*, gatilho *"a quinta Carta"*, **disparado** |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-GOV | Criacao na **Missao 1.9**, com a cobertura **9/9** alcancada. Indexa as nove Cartas e projeta a comparacao unica: quatro classes, 23 custodias, sete portoes cobertos, cinco camadas com dono, **92** impedimentos e **11** pares de interface verificados. **Fecha DR-4.** Registra **sete lacunas** e tres achados novos — **RC-05**, **RC-06** e a reincidencia de **RC-01**. |
| 1.1.0 | 2026-07-29 | DEP-GOV | Emenda **MENOR** da **Missao 1.10**: acrescenta **§2.2**, a verificacao das **treze dimensoes do contrato** sobre as nove Cartas — **117** verificacoes, **113** conformes, **4** achados —, e **tres lacunas novas**: **L-9** *(RD-03)*, **L-10** *(RD-02)* e **L-11** *(RD-01)*. **Nenhuma Carta foi alterada** e **nenhuma linha da projecao anterior foi removida**; a cobertura permanece **9/9 documental** e **4/9 vigente**. Esta continua sendo a **unica** projecao comparativa das nove — nenhuma segunda foi criada. |
| 1.3.0 | 2026-07-29 | DEP-GOV | Emenda **MENOR** da **Missao 1.11**: `DEP-QAR` passa a **1.2.0** · **388** linhas, pela aplicacao do ato de 2026-07-29 — **`RC-01` fechado** e **L-6 fechada**, com `wc -l` e §13.2 declarando o mesmo numero. Total de linhas de Carta: **3.918 → 3.919**. §2.2 recebe **nota de estado posterior** que **nao reescreve** a medicao da Missao 1.10 (MEM-APR-0004). **L-10 passa a *tratada pelo rito*** — RFC-0012 → ADR-0016 → PS-2026-004 —, e a medicao mostrou que a lacuna e de **quatro** celulas, nao duas. **Tres lacunas novas: L-12 *(RD-10)*, L-13 *(RD-11)* e L-14 *(RD-14, severidade Alta)*.** **Nenhuma Carta alem de `DEP-QAR` foi alterada.** |
| 1.2.0 | 2026-07-29 | DEP-GOV | Emenda **MENOR** apos o **ato soberano de 2026-07-29**: `DEP-GOV`, `DEP-TLS`, `DEP-PRD`, `DEP-OPS` e `DEP-GRW` passam a **`ativo` · `ratificada`**, e a **cobertura vigente alcanca 9/9** — o valor que a documental tinha ha dois ciclos. **Fecha L-1**, a lacuna mais antiga desta projecao. **Nenhuma outra linha alterada:** as contagens de §2, §3, §4 e §5 permanecem exatas, porque a transicao **O4 nao tocou nenhuma linha de corpo** e `H-N` ficou invariante nas cinco. **L-9, L-10 e L-11 seguem abertas.** |
| 1.4.0 | 2026-07-29 | DEP-GOV | Emenda **MENOR** da aplicacao do **sexto ato soberano** ([MSG-2026-0006](../memory/operacional/MSG-2026-0006-ato-soberano-aplicacao-integral.md)): `DEP-KMS` passa a **1.1.0 · 464** linhas e `DEP-ENG` a **1.1.0 · 402** linhas, ambas **`ativo` · `ratificada`**. **`RC-05` e `RC-07` FECHADOS** — as duas ultimas lacunas de contrato de Carta —, e **D-9 e D-10 passam a 9 de 9**. Impedimentos declarados: **92 → 94**; linhas de Carta: **3.919 → 3.925**; recortes de decisao de `DEP-ENG` **115 → 116** e `DEP-KMS` **139 → 141**. **Nenhuma das outras sete Cartas foi tocada**, e **nenhuma linha de medicao anterior foi reescrita** (MEM-APR-0004). Cobertura permanece **9/9 documental e 9/9 vigente**. A desordem do proprio historico desta projecao — `1.3.0` antes de `1.2.0` — **nao foi corrigida**: e defeito preexistente, da mesma familia de `RD-13`, e corrigi-lo nao foi autorizado por este ato. |
| 1.6.0 | 2026-07-30 | DEP-GOV | Emenda **MENOR** da aplicacao do **setimo ato soberano** ([MSG-2026-0007](../memory/operacional/MSG-2026-0007-ato-soberano-vigencia-do-framework-de-specifications.md)): **cinco** Cartas passam a **1.1.0 · `ativo` · `ratificada`** — `DEP-PRD` **445**, `DEP-EXE` **506**, `DEP-OPS` **438**, `DEP-GRW` **444** e `DEP-TLS` **425**. **`RD-31` e `RD-37` FECHADOS:** a familia das nove vai de **11 afirmacoes falsas em 4 Cartas** para **`0` em `0`**, com **63** ocorrencias de `QG-1` e **5 de 9** nomeando `DEP-EXE` — medido no acervo **em vigor**, nao em candidato. Total de linhas de Carta: **3.925 → 3.969**; impedimentos **94 → 96** *(`DEP-EXE` `I-10`, `DEP-PRD` `I-12`)*; recorte de decisao passa a **29%–34%**. **Abre `RD-49`:** `DEP-OPS`, `DEP-GRW` e `DEP-TLS` declaram em §13.2 **437 · 443 · 424** contra **438 · 444 · 425** medidos — as tres receberam a linha de historico **sem remedir §13.2**. **`D-12` cai de 8/9 para 6/9.** **Nao corrigido:** as Cartas estao ratificadas (`LV-04`) e a correcao exige **ato novo**. |
