---
id: IDX-foundation
titulo: Indice da Fundacao Organizacional
tipo: relatorio
versao: 1.8.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-08-02
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0001, ADR-0002, ADR-0003, ADR-0004, ADR-0006, ADR-0007, ADR-0008, ADR-0022, ADR-0032]
substitui: []
substituido_por: null
resumo: Indexa os onze documentos fundacionais, os 19 templates e a ordem de leitura, e projeta o estado de ratificacao da Fundacao.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
projecao_de: INC-2026-001 §11
---

# Fundacao Organizacional do LucaX Enterprise OS

> Ratificada por [ADR-0001](../decisions/ADR-0001-adocao-da-fundacao-organizacional.md);
> ampliada com FND-08 por [ADR-0002](../decisions/ADR-0002-adocao-da-camada-de-capabilities.md)
> e com FND-09 por [ADR-0003](../decisions/ADR-0003-adocao-do-enterprise-meta-model.md) e
> [ADR-0004](../decisions/ADR-0004-adocao-do-architecture-fitness-check.md); e com FND-10 por
> [ADR-0006](../decisions/ADR-0006-adocao-do-enterprise-artifact-framework.md).
>
> **Ratificacao concluida.** ADR-0001 a ADR-0004 e ADR-0006 foram ratificados em ato unico,
> explicito e datado do Soberano em 2026-07-28, registrado na fonte canonica
> [INC-2026-001 §11](../governance/incidents/INC-2026-001-ratificacao-inferida.md) — incidente
> **fechado**. **FND-10 esta em vigor** (`ativo`). Esta linha e projecao daquela fonte (PJ-02).
>
> A fronteira com o sistema preexistente esta declarada em
> [ADR-0007](../decisions/ADR-0007-fronteira-greenfield-legado.md): o **LucaX Enterprise OS** e
> greenfield e unica fonte normativa; o **LucaX Legacy** e externo e **nao tem autoridade**.

> **✅ O decimo primeiro documento fundacional ESTA EM VIGOR, e foi EMENDADO.**
> **[FND-11](11-framework-specifications.md) — Framework de Specifications**, **1.1.0**,
> **411 linhas**, e a **sede canonica** de `SF-01` a `SF-32`. Nasceu com **399 linhas**,
> promulgada e ratificada pelo **ato soberano de 2026-07-30** — `C3 · Tipo 1`, por
> [ADR-0022](../decisions/ADR-0022-sede-canonica-do-framework-de-specifications.md), registrado
> em [MSG-2026-0007](../memory/operacional/MSG-2026-0007-ato-soberano-vigencia-do-framework-de-specifications.md).
> **`foundation/` passa a ter onze documentos.**
> [ADR-0021](../decisions/ADR-0021-framework-de-specifications.md) permanece **vigente e
> intacto** — `0` bytes alterados —, e as emendas de **`FND-01`** *(§10, §11 e *Documentos
> derivados*)* e **`FND-03`** *(§7)* entraram em vigor no mesmo ato, como conjunto atomico.
>
> **O que este ato NAO desbloqueou:** a primeira `Spec` continua **nao criavel** — achado
> **`RD-33`** — ✅ **FECHADO em 2026-08-01**. `S1` *(ato criando Produto)* foi **consumida e
> aplicada**, e a `Spec` **de produto** passou a ser criavel; a de materia **nao-produto**
> continua dependendo de `S2`, **deferida** — achado **`RD-88`**, ABERTO.
>
> **A EMENDA de 2026-08-02 — o DECIMO ato, e ela alcanca DOIS fundacionais.**
> [MSG-2026-0010](../memory/operacional/MSG-2026-0010-ato-soberano-emenda-que-sana-rd-91.md),
> aplicado pela **Missao 1.13.5.2** em rito **MINISTERIAL**, poe **`FND-11` 1.1.0** *(411)* e
> **`FND-09` 1.6.0** *(1.278)* em vigor, `ativo` · `ratificada`, por
> [ADR-0032](../decisions/ADR-0032-separacao-de-proponente-e-aprovador-na-spec-c1.md): a
> aprovacao de `Spec` **`C1`** passa do **proprietario**, que e quem a propoe, para **DEP-EXE**,
> porque `FND-04 §3.1` declara **nula** a aprovacao com acumulo de papel (`LV-03`).
> **A sede da emenda e `FND-09 §8.2`, linha `SPC`, e a matriz de `SF-10` cascateia dela** — a
> celula que o achado nomeava, em `FND-11 §5`, **reproduzia literalmente** `FND-09 §8.2`, e por
> `PJ-03` emendar so a projecao **nao sanaria**. **`H-P` conferido `2` de `2`**, **`H-N`
> invariante `2` de `2`**, **`IR-09` `2` de `2`**. **`foundation/` continua com onze
> documentos** — **`0` criados, `0` removidos**, e **`0` bytes** nos outros nove.
> **`RD-91` fecha so quanto a `C1`:** `C0 · T2` segue aberta, por decisao expressa do item V.

## Proposito
Indexar os onze documentos fundacionais e seus templates, e explicar em que ordem devem ser
lidos. Este conjunto e a **unica fonte oficial de verdade** do sistema (PI-02), ratificada
por [ADR-0001](../decisions/ADR-0001-adocao-da-fundacao-organizacional.md).

## Escopo
Todo o LucaX Enterprise OS. Nao existe area do sistema fora do alcance da Fundacao.

## Responsaveis
| Papel | Responsavel |
|---|---|
| Guardiao | DEP-GOV |
| Ratificador | SOBERANO |
| Obrigados | Todos os departamentos, agentes e componentes |

---

## Os onze documentos

| # | Documento | Responde a pergunta | Proprietario |
|---|---|---|---|
| [FND-01](01-constituicao.md) | **Constituicao** | O que nunca pode ser violado? | DEP-GOV |
| [FND-02](02-estrutura-organizacional.md) | **Estrutura Organizacional** | Quem e dono de que? | DEP-EXE |
| [FND-03](03-taxonomia.md) | **Taxonomia Oficial** | Como as coisas se chamam e onde vivem? | DEP-GOV |
| [FND-04](04-governanca.md) | **Governanca** | Como algo muda, e quem responde? | DEP-GOV |
| [FND-05](05-framework-comunicacao.md) | **Framework de Comunicacao** | Como a informacao circula? | DEP-EXE |
| [FND-06](06-arquitetura-memoria.md) | **Arquitetura da Memoria** | Como a organizacao lembra? | DEP-KMS |
| [FND-07](07-framework-decisoes.md) | **Framework de Decisoes** | Como se decide e se registra? | DEP-GOV |
| [FND-08](08-capability-framework.md) | **Enterprise Capability Framework** | O que a organizacao sabe fazer? | DEP-EXE |
| [FND-09](09-meta-model.md) | **Enterprise Meta Model** | O que pode existir, e como as coisas se ligam? | DEP-GOV |
| [FND-10](10-artifact-framework.md) | **Enterprise Artifact Framework** | O que todo artefato deve carregar, custar e obedecer? | DEP-GOV |
| [FND-11](11-framework-specifications.md) | **Framework de Specifications** | O que uma `Spec` deve conter, quem a aprova e quando ela esta pronta? | DEP-GOV |

## Ordem de leitura recomendada

```
FND-01  Constituicao        <- comece aqui: define o que e inegociavel
   |
FND-02  Estrutura           <- quem responde por que
   |
FND-03  Taxonomia           <- o vocabulario que os demais usam
   |
   +--> FND-04  Governanca              como algo nasce e muda
   +--> FND-05  Comunicacao             como a informacao circula
   +--> FND-06  Memoria                 como o conhecimento persiste
   +--> FND-07  Decisoes                como se escolhe e se registra
   +--> FND-08  Capabilities            o que a organizacao sabe fazer
   +--> FND-09  Meta Model              o que pode existir e como se liga
   +--> FND-10  Artifact Framework      o que todo artefato deve carregar
   +--> FND-11  Framework de Specs      o que uma Spec deve conter e quem a aprova
```

Os oito ultimos sao independentes entre si e podem ser lidos em qualquer ordem — mas
todos pressupoem FND-01, FND-02 e FND-03.

> **Atalho para quem vai criar um componente:** FND-09 §5 (o tipo existe?), §6.2 (que
> relacoes sao validas?) e §8.2 (quem aprova?) respondem em um documento o que antes exigia
> cinco.

## Templates

| Template | Para que serve |
|---|---|
| [TPL-documento](templates/TPL-documento.md) | Estrutura base de qualquer documento |
| [TPL-capability](templates/TPL-capability.md) | Constituir Capability |
| [TPL-adr](templates/TPL-adr.md) | Registro de decisao tomada |
| [TPL-rfc](templates/TPL-rfc.md) | Proposta em analise |
| [TPL-nota-decisao](templates/TPL-nota-decisao.md) | Decisao local, reversivel |
| [TPL-carta-departamento](templates/TPL-carta-departamento.md) | Constituir departamento |
| [TPL-carta-agente](templates/TPL-carta-agente.md) | Constituir agente ou subagente |
| [TPL-carta-produto](templates/TPL-carta-produto.md) | Constituir produto |
| [TPL-carta-projeto](templates/TPL-carta-projeto.md) | Constituir projeto |
| [TPL-spec](templates/TPL-spec.md) | Definir o que deve existir |
| [TPL-memoria](templates/TPL-memoria.md) | Registro nas 5 camadas |
| [TPL-handoff](templates/TPL-handoff.md) | Transferir trabalho entre areas |
| [TPL-reporte](templates/TPL-reporte.md) | Relatar resultado |
| [TPL-skill](templates/TPL-skill.md) | Capacidade reutilizavel |
| [TPL-workflow](templates/TPL-workflow.md) | Sequencia recorrente |
| [TPL-ferramenta](templates/TPL-ferramenta.md) | Ficha de capacidade externa |
| [TPL-excecao](templates/TPL-excecao.md) | Excecao formal do Soberano |
| [TPL-incidente](templates/TPL-incidente.md) | Incidente de conformidade |
| [TPL-fitness-check](templates/TPL-fitness-check.md) | Verificacao de aptidao arquitetural (QG-6) |

> **`TPL-documento` e o template universal** (v1.1.0): carrega a estrutura minima **e** o
> contrato de artefato de FND-10 §2. Template especializado so se justifica pelos testes
> T1–T4 de FND-10 §10.2 — os 19 vigentes passam nos quatro.

## O essencial em uma pagina

### Nao negociavel
| # | Regra |
|---|---|
| PI-01 | Soberania humana — nenhum agente amplia a propria autoridade |
| PI-02 | A Fundacao prevalece sobre qualquer prompt, memoria ou saida de agente |
| PI-04 | Decisao sem registro nao existe |
| PI-05 | Quem produz nao aprova o proprio trabalho |
| PI-06 | Mudanca irreversivel exige aprovacao humana explicita |
| PI-07 | Sem backup datado, nao se sobrescreve, apaga, migra ou expoe |
| PI-08 | Credencial nunca em texto — apenas referencia a variavel de ambiente |
| PI-10 | Sucesso nao verificado nunca e reportado como sucesso |
| PI-14 | Especializar quando houver ganho de organizacao, reuso ou contexto |
| MT-01 | Nenhuma entidade existe fora do Meta Model — universo fechado (FND-09) |
| LM-02 | Ratificacao ausente e **impedimento**, nao ressalva: o artefato nao entra em vigor (FND-10) |
| CE-01 | Nenhum papel carrega o acervo por padrao — nucleo medido em **2,2%** em `BL-2026-07-29-10` (FND-10 §8.5). **O valor so se le contra a baseline em que foi medido** |
| PJ-01 | Tabela normativa vive em **uma** fonte; toda outra exibicao e projecao declarada (FND-10 §2.6) |
| FR-03 | Nada do **LucaX Legacy** entra sem passar pelo portao de admissao (ADR-0007) |

### As 21 entidades
O universo e **fechado**. Entidade nova exige RFC, ADR e ratificacao do Soberano (C3).

| Estrato | Entidades |
|---|---|
| 0 Raiz | `ORG` · `SOBERANO` |
| 1 Normativo | `FND` · `ADR` · `RFC` · `EXC` · `INC` · `FIT` |
| 2 Competencia | `CAP` |
| 3 Estrutural | `DEP` · `AGT` · `SUB` |
| 4 Execucao | `SKL` · `WFL` · `TOL` · `TPL` |
| 5 Valor | `PRO` · `PRJ` · `SPC` |
| 6 Cognitivo | `MEM` · `MSG` |

Dependencia dura so aponta para o mesmo estrato ou para numero menor. Nunca para cima.

### As 23 Capabilities
Nenhum componente existe sem vinculo a ao menos uma. Catalogo em
[`../capabilities/`](../capabilities/).

| Dominio | Qtd |
|---|---|
| `DIR` Direcao · `VAL` Valor · `GAR` Garantia · `SUS` Sustentacao · `MER` Mercado · `COG` Cognicao | 3 cada |
| `REA` Realizacao | 5 |

### Os nove departamentos
| Classe | Departamentos |
|---|---|
| Comando | DEP-EXE |
| Guarda *(pode vetar)* | DEP-GOV · DEP-QAR |
| Linha | DEP-PRD · DEP-ENG · DEP-OPS · DEP-GRW |
| Plataforma | DEP-KMS · DEP-TLS |

### Os sete portoes
`QG-0` iniciar · `QG-1` especificar · `QG-2` arquitetar · `QG-3` revisar ·
`QG-4` liberar · `QG-5` aprender · `QG-6` **aptidao arquitetural**

`QG-0` a `QG-5` verificam **corretude**; `QG-6` verifica **aptidao evolutiva** ao encerrar
mudanca C2 ou C3.

### As cinco camadas de memoria
`EST` estrategica · `PRD` produto · `TEC` tecnica · `OPR` operacional · `APR` aprendizado

### As quatro classes de mudanca
`C0` editorial · `C1` operacional · `C2` estrutural · `C3` constitucional
× `Tipo 1` irreversivel / `Tipo 2` reversivel

## Como alterar a Fundacao

| Alteracao | Instrumento |
|---|---|
| Correcao editorial (C0) | Direta, incrementa CORRECAO |
| Acrescimo compativel (C2) | RFC → ADR → atualizacao MENOR → **QG-6** |
| Mudanca de principio, linha vermelha ou hierarquia (C3) | RFC → analise de impacto → ADR → **ratificacao do Soberano** → versao MAIOR → **QG-6** |
| Criar tipo de entidade novo | Teste TE (FND-09 §11.1) → RFC → ADR → **ratificacao** — sempre C3 |
| Criar tipo **documental** novo | Teste CS-01 (FND-10 §4) → ADR — **C2**, degrau 1 da escada |

> **Sem ato explicito do Soberano, C3 nao entra em vigor** — permanece `aprovado` (LM-02).
> Instrucao generica anterior, precedente e silencio **nao ratificam** (CV-09).

O texto anterior **nunca e apagado** — e preservado como versao superada (FND-01 §9).
