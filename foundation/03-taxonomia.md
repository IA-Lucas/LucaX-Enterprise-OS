---
id: FND-03
titulo: Taxonomia Oficial do LucaX Enterprise OS
tipo: fundacao
versao: 1.6.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-29
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0001, ADR-0002, ADR-0003, ADR-0004, ADR-0006, ADR-0007, ADR-0010, ADR-0022]
substitui: []
substituido_por: null
resumo: Fixa nomes, identificadores, frontmatter, estados, versionamento e localizacao de todo componente do sistema.
perfil_contexto: nucleo
confidencialidade: interno
revisor: DEP-QAR
ratificacao: ratificada
---

# Taxonomia Oficial

## Proposito

Definir o vocabulario unico e os padroes de nomenclatura, identificacao, versionamento e
localizacao de todos os componentes do LucaX Enterprise OS. Esta taxonomia elimina
ambiguidade: um mesmo conceito tem um unico nome, um unico formato de identificador e um
unico lugar onde vive.

## Escopo

| Item | Definicao |
|---|---|
| **Inclui** | Regras lexicais, esquema de identificadores, definicao canonica de cada tipo de componente, frontmatter obrigatorio, estados, versionamento, estrutura de diretorios, regras de data e idioma. |
| **Nao inclui** | Conteudo dos componentes, criterio de aprovacao (FND-04), formato de mensagem (FND-05). |
| **Subordinado a** | [FND-01 Constituicao](01-constituicao.md). |
| **Vinculante desde** | 2026-07-28. Todo artefato criado a partir desta data segue esta taxonomia sem excecao. |

## Responsaveis

| Papel | Responsavel |
|---|---|
| Proprietario | DEP-GOV |
| Aplicacao e fiscalizacao | DEP-GOV (veto sobre artefato fora do padrao) |
| Curadoria de nomes na memoria | DEP-KMS |
| Aprovador de mudanca | SOBERANO (via ADR) |

---

## 1. Regras Lexicais Universais

| # | Regra | Correto | Errado |
|---|---|---|---|
| LX-01 | Nomes de arquivo e diretorio em **minusculas**, `kebab-case`, **ASCII puro**, sem acento, sem cedilha, sem espaco. | `arquitetura-memoria.md` | `Arquitetura Memória.md` |
| LX-02 | Identificadores (IDs) em **MAIUSCULAS**, com hifens. | `ADR-0001-adocao-fundacao` | `adr_1` |
| LX-03 | Slug: apenas `a-z`, `0-9` e hifen. Sem hifen duplo, inicial ou final. Maximo 48 caracteres. | `pipeline-ingestao` | `Pipeline_Ingestão--v2` |
| LX-04 | Datas sempre **ISO-8601** (`AAAA-MM-DD`). Nunca formato local. | `2026-07-28` | `28/07/2026` |
| LX-05 | Conteudo dos documentos em **portugues do Brasil**. Nomes de arquivo e IDs sem acentuacao (LX-01). | corpo com acentos, nome sem | nome de arquivo acentuado |
| LX-06 | Numeracao sequencial com **zero a esquerda** e largura fixa por tipo. | `ADR-0007` | `ADR-7` |
| LX-07 | Um conceito, um nome. Sinonimo e proibido em documento normativo. | sempre "Carta" | "charter"/"carta"/"constitutivo" |
| LX-08 | Prefixo de tipo e obrigatorio no ID e **nunca** e reutilizado por outro tipo. | `PRO-` so para Produto | `PRD-` para produto e departamento |
| LX-09 | Nome nunca carrega estado, data ou versao. Estado vive no frontmatter. | `adr-0007-cache.md` | `adr-0007-cache-APROVADO-v2.md` |
| LX-10 | Abreviacao so e permitida se estiver no glossario deste documento. | `ADR` | `arqdec` |

### 1.1 Excecao registrada
O diretorio raiz do repositorio (`LucaX Enterprise OS`) contem espacos e antecede esta
taxonomia. E excecao herdada, registrada e tolerada. **Nenhum diretorio ou arquivo novo
pode invocar este precedente.**

## 2. Esquema de Identificadores

Todo componente tem um ID unico, imutavel e permanente. **O ID nunca muda** — nem em
renomeacao, nem em mudanca de escopo, nem em depreciacao.

| Componente | Prefixo | Formato | Largura | Exemplo |
|---|---|---|---|---|
| Documento fundacional | `FND` | `FND-<NN>` | 2 | `FND-03` |
| **Capability** | `CAP` | `CAP-<slug>` | — | `CAP-engenharia-de-agentes` |
| Departamento | `DEP` | `DEP-<CODIGO>` | 3 letras | `DEP-ENG` |
| Produto | `PRO` | `PRO-<slug>` | — | `PRO-radar-fiscal` |
| Projeto | `PRJ` | `PRJ-<AAAA>-<NNN>` | 3 | `PRJ-2026-014` |
| Agente | `AGT` | `AGT-<DEP>-<papel>` | — | `AGT-ENG-arquiteto` |
| Subagente | `SUB` | `SUB-<DEP>-<papel>` | — | `SUB-ENG-revisor-adr` |
| Skill | `SKL` | `SKL-<dominio>-<verbo-objeto>` | — | `SKL-eng-gerar-adr` |
| Spec | `SPC` | `SPC-<NNN>-<slug>` | 3 | `SPC-004-importacao-nfe` |
| ADR | `ADR` | `ADR-<NNNN>-<slug>` | 4 | `ADR-0001-adocao-fundacao` |
| RFC | `RFC` | `RFC-<NNNN>-<slug>` | 4 | `RFC-0003-departamento-dados` |
| Template | `TPL` | `TPL-<tipo>` | — | `TPL-adr` |
| Workflow | `WFL` | `WFL-<DEP>-<slug>` | — | `WFL-QAR-revisao-entrega` |
| Memoria | `MEM` | `MEM-<CAMADA>-<NNNN>-<slug>` | 4 | `MEM-APR-0012-falha-migracao` |
| Ferramenta | `TOL` | `TOL-<classe>-<slug>` | — | `TOL-mcp-notion` |
| Excecao formal | `EXC` | `EXC-<AAAA>-<NNN>` | 3 | `EXC-2026-002` |
| Incidente de conformidade | `INC` | `INC-<AAAA>-<NNN>` | 3 | `INC-2026-005` |
| **Mensagem** | `MSG` | `MSG-<AAAA>-<NNNN>` | 4 | `MSG-2026-0031` |
| **Verificacao de aptidao** | `FIT` | `FIT-<AAAA>-<NNN>-<slug>` | 3 | `FIT-2026-001-meta-model` |
| **Revisao arquitetural** | `REV` | `REV-<ESCOPO>-<AAAA-MM-DD>` | — | `REV-META-2026-07-28` |
| **Indice / catalogo** | `IDX` | `IDX-<escopo>` | — | `IDX-decisions` |

> **`MSG` e `FIT` acrescentados por ADR-0003 e ADR-0004.** `MSG` ja operava em
> [FND-05 §3](05-framework-comunicacao.md) sem constar desta tabela — lacuna detectada na
> analise de RFC-0002 e corrigida aqui. O universo completo de entidades esta em
> [FND-09 §5](09-meta-model.md).

> **`REV` e `IDX` acrescentados por ADR-0006.** Ambos ja operavam — 2 e 8 instancias
> respectivamente — sem constar desta tabela. **Nenhum dos dois e entidade nova:** `REV` e o
> segundo tipo documental da entidade `FIT` (parecer de corretude, contra o de aptidao), e
> `IDX` e o **registro oficial da entidade que indexa** — o contador de sequencia que §2.3
> ja atribui a DEP-GOV. Prefixo distinto, mesma entidade (FND-10 §4.5 e §4.7).

### 2.1 Codigos de departamento (fechados)

`EXE` · `GOV` · `QAR` · `PRD` · `ENG` · `OPS` · `GRW` · `KMS` · `TLS`

Codigo novo so por ADR que crie departamento (FND-02, §8.1).

### 2.2 Codigos de camada de memoria (fechados)

`EST` Estrategica · `PRD` Produto · `TEC` Tecnica · `OPR` Operacional · `APR` Aprendizado

> **Atencao a colisao:** `PRD` e codigo de departamento **e** codigo de camada. A
> desambiguacao e posicional e obrigatoria: em ID de memoria, `PRD` sempre ocupa a segunda
> posicao apos `MEM-`; em ID de agente ou workflow, sempre ocupa a segunda posicao apos
> `AGT-`/`WFL-`. Fora dessas posicoes, `DEP-PRD` e a forma obrigatoria para o departamento.

### 2.3 Sequencias
| Sequencia | Escopo | Reinicia? |
|---|---|---|
| `ADR-NNNN` | Global | Nunca |
| `RFC-NNNN` | Global | Nunca |
| `MEM-<CAMADA>-NNNN` | Por camada | Nunca |
| `SPC-NNN` | Por produto | Por produto |
| `PRJ-AAAA-NNN` | Por ano | A cada ano |
| `EXC` / `INC-AAAA-NNN` | Por ano | A cada ano |
| `FIT-AAAA-NNN` | Por ano | A cada ano |
| `MSG-AAAA-NNNN` | Por ano | A cada ano |

Numero **nunca e reaproveitado**, mesmo que o artefato seja revogado ou descartado.
DEP-GOV mantem o contador oficial de cada sequencia.

### 2.4 Codigos de dominio de Capability (fechados)

`DIR` Direcao · `VAL` Descoberta e Valor · `REA` Realizacao · `GAR` Garantia ·
`SUS` Sustentacao · `MER` Mercado e Recursos · `COG` Cognicao Organizacional

Acrescentar dominio e mudanca **C3** (FND-08 §10).

## 3. Definicao Canonica dos Componentes

### 3.0 Capability — `CAP`
Competencia permanente da organizacao: o que ela sabe fazer, independentemente de
departamento, agente, pessoa ou tecnologia. Definicao completa em
[FND-08](08-capability-framework.md).

| Atributo | Regra |
|---|---|
| Custodio | Exatamente um departamento (OW-01) |
| Carta | `TPL-capability` obrigatoria, com os 13 atributos |
| Vive em | `capabilities/CAP-<slug>.md` |
| Eixos | `dominio` × `classe` × `maturidade`, simultaneos e independentes |
| Regra de vinculacao | **Nenhum Departamento, Agente, Subagente, Skill, Workflow ou Produto existe sem vinculo a ao menos uma Capability** (FND-08 §8) |
| Teste de existencia | Continua verdadeira se a estrutura e a tecnologia mudarem? Se nao, nao e Capability. |

### 3.1 Produto — `PRO`
Bem digital com valor proprio, publico proprio e ciclo de vida proprio. Existe alem do
esforco que o criou.

| Atributo | Regra |
|---|---|
| Dono | DEP-PRD |
| Criado por | Decisao do Soberano (Tipo 1) |
| Carta | `TPL-carta-produto` obrigatoria |
| Vive em | `products/<slug>/` |
| Teste de existencia | Se for descontinuado, alguem perde algo? Se nao, nao e produto. |

### 3.2 Projeto — `PRJ`
Esforco temporario, com inicio, fim e resultado definido. **Projeto termina; produto
continua.**

| Atributo | Regra |
|---|---|
| Dono | DEP-EXE (alocacao) + departamento responsavel pelo resultado |
| Carta | `TPL-carta-projeto`, com criterio de encerramento explicito |
| Vive em | `projects/<PRJ-id>/` |
| Regra | Projeto sem criterio de encerramento nao e aprovado. |

### 3.3 Agente — `AGT`
Papel executor especializado, com Carta, escopo, nivel de autonomia e departamento de
origem. **Nao existe nesta fase.**

| Atributo | Regra |
|---|---|
| Pertence a | Exatamente um departamento |
| Autonomia | Igual ou inferior a do departamento; nunca superior |
| Carta | `TPL-carta-agente`, obrigatoriamente com secao "O que nao me compete" |
| Vive em | `departments/<dep>/agents/<AGT-id>.md` |
| Regra de nome | O papel no ID e substantivo de funcao, nao verbo: `arquiteto`, nao `arquitetar`. |

### 3.4 Subagente — `SUB`
Executor subordinado a um agente, com escopo mais estreito, invocado por ele para uma
parte delimitada do trabalho.

| Atributo | Regra |
|---|---|
| Declara | `agente_pai` no frontmatter, obrigatoriamente |
| Autonomia | Sempre menor ou igual a do agente pai |
| Profundidade | Maximo um nivel. **Subagente nao tem subagente.** |
| Vive em | `departments/<dep>/agents/sub/<SUB-id>.md` |

### 3.5 Skill — `SKL`
Capacidade reutilizavel e nomeada: um procedimento que pode ser invocado por mais de um
papel para produzir um resultado previsivel.

| Atributo | Regra |
|---|---|
| Formato do nome | `<dominio>-<verbo>-<objeto>` — sempre acao |
| Criterio de existencia | So vira skill o que se repete e tem resultado verificavel |
| Vive em | `skills/<SKL-id>.md` |
| Regra | Skill pertence a organizacao, nao a um agente. Se so um papel pode usar, e procedimento interno da Carta dele. |

### 3.6 Spec — `SPC`
Definicao do **que** deve existir e de como se verifica que existe. Nunca define o **como**.

| Atributo | Regra |
|---|---|
| Dono | DEP-PRD |
| Deve conter | Problema, resultado esperado, criterios de aceite verificaveis, escopo negativo ("nao inclui"), premissas |
| Nao pode conter | Decisao de arquitetura, escolha de tecnologia, detalhe de implementacao |
| Vive em | `products/<slug>/specs/<SPC-id>.md` |
| Portao | QG-1 |

### 3.7 ADR — `ADR` (Architecture Decision Record)
Registro de **decisao ja tomada** e vigente. Documento historico e imutavel apos aprovacao.

| Atributo | Regra |
|---|---|
| Uso | Decisao tomada, com consequencia estrutural |
| Imutabilidade | Apos `aprovado`, nunca e editado — apenas superado (LV-04) |
| Numeracao | Global, atribuida por DEP-GOV |
| Vive em | `decisions/<ADR-id>.md` |
| Escopo | Nao e exclusivo de arquitetura tecnica: registra decisao organizacional, de produto, de processo. |

### 3.8 RFC — `RFC` (Request For Comments)
Proposta **em aberto**, submetida a analise antes de virar decisao.

| Atributo | Regra |
|---|---|
| Uso | Mudanca estrutural (C2) ou constitucional (C3), antes do ADR |
| Relacao com ADR | RFC aceita gera ADR. RFC rejeitada e arquivada, **nunca apagada**. |
| Vive em | `rfcs/<RFC-id>.md` |
| Regra | RFC sem alternativas analisadas e devolvida por DEP-GOV. |

**ADR x RFC:** RFC pergunta, ADR responde. RFC pode ser rejeitada; ADR aprovado so pode ser
superado.

### 3.9 Template — `TPL`
Estrutura padronizada e vazia para producao de um tipo de artefato.

| Atributo | Regra |
|---|---|
| Dono | DEP-GOV (forma) + departamento dono do tipo (conteudo) |
| Vive em | `foundation/templates/<TPL-id>.md` |
| Regra | Se um tipo de artefato existe, ele tem template. Sem template, o tipo nao esta pronto para uso. |

### 3.10 Workflow — `WFL`
Sequencia definida de etapas, com entradas, saidas, responsaveis e portoes, para produzir
um resultado recorrente. **Nao existe nesta fase.**

| Atributo | Regra |
|---|---|
| Deve declarar | Gatilho, entradas, etapas, responsavel por etapa, portoes, saidas, criterio de falha |
| Vive em | `workflows/<WFL-id>.md` |
| Regra | Workflow que atravessa departamentos declara o dono do resultado final (FND-02, §6). |

### 3.11 Memoria — `MEM`
Unidade de conhecimento organizacional persistente, alocada em exatamente uma das cinco
camadas. Detalhamento em [FND-06](06-arquitetura-memoria.md).

| Atributo | Regra |
|---|---|
| Camada | Exatamente uma. Registro em duas camadas e erro de curadoria. |
| Proveniencia | Origem, autor e data sao obrigatorios |
| Vive em | `memory/<camada>/<MEM-id>.md` |
| Curador | DEP-KMS |

### 3.12 Ferramenta — `TOL`
Capacidade externa ao sistema que a organizacao usa: servico, API, integracao, MCP, base
externa.

| Classe | Uso |
|---|---|
| `mcp` | Servidor MCP conectado |
| `api` | Servico consumido por API |
| `saas` | Aplicacao de terceiros |
| `local` | Recurso da maquina do Soberano |
| `dados` | Fonte de dados externa |
| `modelo` | Modelo de IA consumido como capacidade externa *(acrescentado por ADR-0003; absorve a candidata `Model`, FND-09 §5.8 X-08)* |

| Atributo | Regra |
|---|---|
| Dono | DEP-TLS |
| Ficha | Finalidade, classe, dado que trafega, custo, dependencia, alternativa, criterio de descarte |
| Vive em | `tools/<TOL-id>.md` |
| Regra | Credencial **nunca** aparece na ficha — apenas o nome da variavel de ambiente (PI-08). |

### 3.13 Mensagem — `MSG`
Unidade de comunicacao formal entre atores, com envelope e contrato. Definicao operacional
completa em [FND-05 §3](05-framework-comunicacao.md); registrada como entidade em
[FND-09 §5.7](09-meta-model.md).

| Atributo | Regra |
|---|---|
| Canal | Exatamente um: DIRETIVA, HANDOFF, REPORTE, CONSULTA ou ALERTA |
| Vive em | `memory/operacional/` enquanto vale (FND-05 §9) |
| Ciclo de vida | Efemero. Mensagem com decisao, aprendizado ou fato duravel e **promovida** ao instrumento proprio (FND-05 §9.1) |
| Regra | Referencia por ID, nunca por copia de conteudo (CM-09). Silencio nao e mensagem (CM-07). |

### 3.14 Verificacao de Aptidao Arquitetural — `FIT`
Registro do veredito sobre a **aptidao evolutiva** de uma mudanca estrutural. Mecanismo em
[FND-09 §10](09-meta-model.md); portao correspondente e QG-6 (FND-01 §6.2).

| Atributo | Regra |
|---|---|
| Dono | DEP-QAR — **nunca** quem produziu o artefato avaliado (FT-02, LV-03) |
| Obrigatorio em | Toda mudanca C2 e C3; opcional em C1; nao se aplica a C0 |
| Vive em | `governance/fitness/<FIT-id>.md` |
| Veredito | `apto` · `apto-com-ressalva` · `inapto`. `inapto` **bloqueia o encerramento** |
| Regra | Toda resposta exige sinal observavel. Nunca reescrito: veredito posterior **supera** o anterior (FT-09). |

### 3.15 Revisao Arquitetural — `REV`
Parecer datado sobre a **corretude estrutural** de uma camada. Segundo tipo documental da
entidade `FIT` (FND-10 §4.5), distinguido pelo eixo `classe_avaliacao: corretude`.

| Atributo | Regra |
|---|---|
| Dono | DEP-QAR — nunca quem produziu a camada revisada (RM-06b) |
| Vive em | **Ao lado do que revisa**: `foundation/` ou `capabilities/` |
| Mutabilidade | **M1** — imutavel apos eficacia; corrige-se superando |
| Regra | Achado sem severidade, dono e gatilho e observacao sem destino, proibida por FND-04 §8 |

### 3.16 Indice / Catalogo — `IDX`
Registro oficial e contador de uma sequencia. **Vista derivada**: seu conteudo existe
integralmente em outros artefatos.

| Atributo | Regra |
|---|---|
| Dono | DEP-GOV |
| Entidade | **A que ele indexa** — nao e entidade propria (FND-10 §4.7) |
| Vive em | `README.md` do diretorio da entidade indexada |
| Mutabilidade | **M3** — derivado; reprocessa-se da fonte |
| Regra IX-01 | **Nao contem informacao original.** Informacao que so exista no indice deve ser movida para a fonte e referenciada |
| Regra IX-02 | Indice desatualizado apos mudanca aprovada e **mudanca incompleta** (CV-04), nunca norma nova |

## 4. Frontmatter Obrigatorio

Todo artefato em Markdown do sistema comeca com este bloco. Campo ausente ou vazio =
artefato nao conforme = veto de DEP-GOV.

```yaml
---
id: <ID canonico>
titulo: <titulo legivel, sem acentos no nome do arquivo>
tipo: <fundacao|carta|spec|adr|rfc|template|workflow|memoria|ferramenta|skill|relatorio|fitness>
versao: <semver>
status: <ver secao 5>
camada_memoria: <estrategica|produto|tecnica|operacional|aprendizado|nao-aplicavel>
autor: <DEP-xxx ou SOBERANO>
proprietario: <DEP-xxx>
aprovador: <DEP-xxx ou SOBERANO>
criado_em: <AAAA-MM-DD>
atualizado_em: <AAAA-MM-DD>
revisao_prevista: <AAAA-MM-DD ou null>
decisoes_relacionadas: [<ADR-id>, ...]
substitui: [<id>, ...]
substituido_por: <id ou null>
# extensao do contrato de artefato (FND-10 §2.2)
resumo: <uma linha, ate 200 caracteres, em voz ativa>
perfil_contexto: <nucleo|missao|sob-demanda|arquivo>
confidencialidade: <publico|interno|restrito|soberano>
revisor: <DEP-xxx — obrigatoriamente distinto de `autor`>
ratificacao: <nao-exigida|pendente|ratificada>
---
```

> **Extensao acrescentada por ADR-0006.** Os cinco campos valem para artefato **criado ou
> emendado a partir de 2026-07-28**. O acervo anterior e atendido por valor padrao e pelo
> [catalogo mestre](../governance/artifact-registry.md) — **nenhum arquivo existente e
> reescrito** (FND-10 §2.3). Atributo **derivavel** — consumidores, relacoes, autoridade,
> custo de contexto — **nao entra no frontmatter** (AC-01).

### 4.1 Campos adicionais por tipo

| Tipo | Campos extras obrigatorios |
|---|---|
| **Carta de Capability** | `dominio`, `classe`, `maturidade`, `custodio`, `exercentes`, `depende_de`, `consumida_por`, `especializa` |
| **Departamento, agente, subagente, skill, workflow, produto, projeto, ferramenta** | `capabilities: [...]` — ao menos uma, nunca vazio (FND-08 §8.1). *Alcance estendido a projeto e ferramenta por ADR-0003, unificando com PI-12* |
| Carta de agente | `departamento`, `nivel_autonomia`, `agente_pai` (se subagente) |
| Spec | `produto`, `criterios_aceite_count` |
| ADR | `classe_mudanca`, `tipo_decisao` (1 ou 2), `supera`, `superado_por` |
| RFC | `classe_mudanca`, `prazo_analise` |
| Memoria | `origem`, `evidencia`, `ttl`, `confianca` |
| Ferramenta | `classe`, `dado_trafegado`, `custo`, `criticidade` |
| Workflow | `gatilho`, `portoes` |
| Excecao formal | `norma_excepcionada`, `escopo`, `prazo`, `motivo`, `vigencia` |
| Incidente | `norma_violada`, `severidade`, `efeito`, `causa`, `situacao` |
| Verificacao de aptidao | `objeto_avaliado`, `classe_mudanca`, `veredito` |
| Mensagem | Envelope completo de FND-05 §3 + campos por canal de §3.2 |

> Os campos `vigencia` e `situacao` foram declarados por ADR-0003: sao **eixos ortogonais de
> estado** (FND-09 §7.3) que ja existiam implicitamente em FND-04 §9 e §10.2 e nao tinham
> nome no frontmatter. `status` continua descrevendo o estado do **documento**; o eixo
> proprio descreve o estado da **coisa**. Os dois sao declarados sempre que ambos existirem.

### 4.2 Corpo obrigatorio
Apos o frontmatter, **todo documento** contem, nesta ordem:

```markdown
# <Titulo>

## Proposito     — para que este documento existe, em ate 3 frases
## Escopo        — o que inclui, o que nao inclui, a que se subordina
## Responsaveis  — quem possui, quem aprova, quem e obrigado
```

Essa e a exigencia da Constituicao (§6.1, DoD-2). Documento sem os tres blocos e nulo
como norma.

## 5. Estados (ciclo de vida)

Todo artefato tem exatamente um estado. Estados sao os mesmos para todos os tipos.

| Estado | Significado | Pode ser usado como referencia? |
|---|---|---|
| `rascunho` | Em elaboracao. Nao vincula ninguem. | Nao |
| `em-revisao` | Submetido a revisao independente. | Nao |
| `aprovado` | Revisado e aceito; aguarda entrada em vigor. | Sim |
| `ativo` | Em vigor. Norma corrente. | Sim |
| `depreciado` | Ainda valido, mas substituicao ja definida. | Sim, com ressalva |
| `superado` | Substituido por outro artefato, indicado em `substituido_por`. | Apenas como historico |
| `revogado` | Anulado sem substituto. | Nao |
| `arquivado` | Encerrado sem ter vigorado (ex.: RFC rejeitada). | Nao |

### 5.1 Transicoes permitidas

```
rascunho -> em-revisao -> aprovado -> ativo -> depreciado -> superado
                |                       |                 \
                +-> arquivado           +-> revogado       -> revogado
```

Transicoes proibidas: `ativo -> rascunho`, `superado -> ativo`, `revogado -> qualquer`.
Reativar conteudo revogado exige **novo artefato com novo ID**.

## 6. Versionamento

Versionamento semantico `MAIOR.MENOR.CORRECAO`:

| Incremento | Quando |
|---|---|
| **MAIOR** | Mudanca que quebra compatibilidade: remove regra, inverte decisao, altera principio, muda escopo exclusivo. |
| **MENOR** | Acrescimo compativel: nova secao, nova regra que nao contradiz as existentes. |
| **CORRECAO** | Correcao editorial: redacao, tipografia, link, exemplo. Sem efeito normativo. |

Regras:
- Mudanca MAIOR sempre exige ADR. Mudanca MENOR exige registro. CORRECAO dispensa ADR mas
  atualiza `atualizado_em`.
- ADR aprovado **nao versiona**: ele e superado (LV-04).
- Toda mudanca MAIOR ou MENOR acrescenta linha na tabela "Historico de versoes" do proprio
  documento.

## 7. Estrutura Canonica de Diretorios

```
LucaX Enterprise OS/
├── README.md                     indice mestre do sistema
│
├── foundation/                   [FND] a Fundacao — fonte oficial de verdade
│   ├── README.md
│   ├── 01-constituicao.md
│   ├── 02-estrutura-organizacional.md
│   ├── 03-taxonomia.md
│   ├── 04-governanca.md
│   ├── 05-framework-comunicacao.md
│   ├── 06-arquitetura-memoria.md
│   ├── 07-framework-decisoes.md
│   ├── 08-capability-framework.md
│   ├── 09-meta-model.md
│   ├── 10-artifact-framework.md
│   ├── 11-framework-specifications.md
│   ├── revisao-arquitetural-*.md [REV] parecer de corretude, ao lado do revisado
│   └── templates/                [TPL]
│
├── capabilities/                 [CAP] competencias permanentes
│   ├── README.md                 catalogo e mapa oficial de dependencias
│   └── CAP-<slug>.md
│
├── decisions/                    [ADR] decisoes tomadas
│   └── README.md                 indice e contador oficial
│
├── rfcs/                         [RFC] propostas em analise
│   └── README.md
│
├── memory/                       [MEM] memoria organizacional, 5 camadas
│   ├── README.md
│   ├── estrategica/
│   ├── produto/
│   ├── tecnica/
│   ├── operacional/
│   └── aprendizado/
│
├── departments/                  [DEP] cartas e, no futuro, agentes
│   └── <dep>/
│       ├── carta.md
│       └── agents/               (fase futura)
│
├── products/                     [PRO]
│   └── <slug>/
│       ├── carta.md
│       └── specs/                [SPC]
│
├── projects/                     [PRJ]
│   └── <PRJ-id>/
│
├── skills/                       [SKL]   (fase futura)
├── workflows/                    [WFL]   (fase futura)
├── tools/                        [TOL]   (fase futura)
│
└── governance/
    ├── artifact-registry.md      [IDX] catalogo mestre do acervo
    ├── exceptions/               [EXC] excecoes formais vigentes
    ├── incidents/                [INC] incidentes de conformidade
    └── fitness/                  [FIT] verificacoes de aptidao arquitetural
```

> Revisoes arquiteturais vivem **ao lado do que revisam** — em `foundation/` ou
> `capabilities/` —, com id `REV-<ESCOPO>-<AAAA-MM-DD>` (§3.15). Nao sao norma: sao parecer
> datado, imutavel apos eficacia.

> Todo `README.md` de diretorio e um **indice** (`IDX`, §3.16): o registro oficial e o
> contador da sequencia daquela entidade. O [catalogo mestre](../governance/artifact-registry.md)
> nao o substitui — aquele conta a sequencia, este da a visao transversal do acervo (RG-04).

### 7.1 Regra de localizacao
**Um artefato existe em exatamente um lugar.** Copia nao e permitida — apenas referencia
por ID ou link relativo. Duplicata detectada e incidente de conformidade e a copia e
removida em favor do original.

### 7.2 Diretorios ainda nao materializados
`skills/`, `workflows/`, `tools/`, `projects/` e `departments/<dep>/agents/` estao previstos
mas **nao sao criados nesta fase** — a fundacao nao cria componente de execucao. Eles nascem
quando o primeiro artefato do tipo for aprovado.

## 8. Vocabulario Controlado

Termos com significado fixo. Uso divergente e erro de conformidade.

| Termo oficial | Significa | Nao confundir com |
|---|---|---|
| **Entidade** | Tipo de coisa que **pode existir** (FND-09 §5) | Instancia, componente, artefato |
| **Tipo documental** | Forma que uma entidade assume (FND-10 §4) | Entidade, classe, categoria |
| **Perfil de contexto** | Regra de carregamento do artefato (FND-10 §8) | Confidencialidade, prioridade |
| **Vista derivada** | Artefato cujo conteudo existe integralmente em outro | Copia, resumo, duplicata |
| **Arquetipo** | Classe abstrata que carrega regra comum; nunca instanciada | Entidade, categoria, tag |
| **Estrato** | Camada de natureza que ordena a direcao das dependencias | Nivel hierarquico, camada de memoria, degrau da escada |
| **Capability** | O que a organizacao **sabe fazer** | Departamento (quem responde), agente (quem executa), skill (procedimento) |
| **Custodio** | Departamento que zela por uma Capability | Exercente, dono exclusivo, executor |
| **Maturidade** | Estado da **competencia** | `status`, que e o estado do **documento** |
| **Carta** | Documento constitutivo de um componente | Spec, briefing, descricao |
| **Spec** | O que deve existir e como verificar | Carta, plano, tarefa |
| **Decisao** | Escolha registrada com alternativas e justificativa | Opiniao, preferencia, plano |
| **Portao (QG)** | Parada obrigatoria com liberacao registrada | Revisao informal, checagem |
| **Handoff** | Transferencia formal de trabalho entre areas | Aviso, mensagem, pedido |
| **Camada** | Uma das 5 divisoes da memoria | Diretorio, categoria, tag |
| **Promocao** | Movimento de registro para camada mais estavel | Copia, duplicacao |
| **Veto** | Bloqueio vinculante da Guarda | Discordancia, ressalva |
| **Excecao formal** | Autorizacao temporaria registrada | Improviso, jeitinho |
| **Nulo** | Sem efeito organizacional; deve ser revertido | Errado, ruim, indesejado |
| **Tipo 1 / Tipo 2** | Irreversivel / reversivel barato | Urgente / nao urgente |
| **Soberano** | O humano, autoridade final | Usuario, cliente, stakeholder |
| **LucaX Enterprise OS** | **Este** sistema: greenfield e unica fonte normativa (ADR-0007 §5.1) | LucaX Legacy; "LucaX" sem qualificacao |
| **LucaX Legacy** | O sistema preexistente, **externo**, sem autoridade normativa (ADR-0007 §5.1) | Este sistema; versao anterior deste acervo |
| **Programa de Migracao** | Eventual esforco temporario de admitir conteudo do Legacy — **nao iniciado** (ADR-0007 §5.1) | Projeto existente; fase planejada |
| **Proveniencia** | Origem do artefato quanto a fronteira greenfield/legado: `native` · `legacy-candidate` · `adapted` · `migrated` · `rejected` (ADR-0007 §5.5) | Autoria, custodia, `origem` de memoria |
| **Projecao** | Exibicao declarada de conteudo cuja fonte e outro documento (FND-10 §2.6) | Copia, reproducao, duplicata |
| **Contexto do Soberano** | Conhecimento operacional registrado **sobre** o Soberano — visao, criterios, linguagem e forma de trabalho —, com proveniencia por afirmacao e **sem autoridade normativa**. Regra em [ADR-0010 §5](../decisions/ADR-0010-contrato-de-conhecimento-do-soberano.md) | Ato soberano *(que obriga)*; decisao registrada *(ADR)*; instrucao de sessao |

## 9. Regras de Nomeacao por Situacao

| Situacao | Regra |
|---|---|
| Nome ja existe | Nome deve ser unico dentro do tipo. Colisao resolve-se por qualificacao (`SPC-004-importacao-nfe-lote`), nunca por sufixo numerico vazio (`-2`). |
| Artefato renomeado | O **ID nao muda**. Muda o slug do arquivo, e o antigo caminho e registrado no frontmatter (`substitui`). |
| Artefato movido de departamento | ID preservado. Muda `proprietario`, com ADR registrando a transferencia. |
| Rascunho descartado | Numero da sequencia **nao e devolvido**; o artefato vai para `arquivado`. |
| Artefato importado de fora | Recebe ID novo do sistema e declara a origem em `origem`. **A forma nao autoriza a entrada:** admissao de conteudo externo exige o portao de [ADR-0007 §5.3](../decisions/ADR-0007-fronteira-greenfield-legado.md) — G1 a G5, cumulativas. Fora dele, o artefato e nulo (FR-03). |
| Nome em ingles | Permitido apenas quando for termo tecnico consagrado sem traducao aceita (`workflow`, `handoff`, `backup`). Fora disso, portugues. |

## 10. Conformidade

| Verificacao | Resultado se falhar |
|---|---|
| Frontmatter completo e valido | Veto de DEP-GOV; artefato nao referenciavel |
| ID no formato canonico | Correcao obrigatoria antes de aprovacao |
| Localizacao conforme §7 | Movimentacao obrigatoria; nao gera novo ID |
| Blocos Proposito/Escopo/Responsaveis | Documento nulo como norma |
| Estado valido e transicao legal | Estado revertido; incidente registrado |
| Ausencia de duplicata | Copia removida; original preservado |
| Ausencia de credencial em texto | Incidente critico (LV-02); rotacao obrigatoria |
| **Vinculo a Capability presente e valido** | Elo quebrado; bloqueia aprovacao (VC-01) |
| **Tipo consta do Meta Model** (FND-09 §5) | Entidade **nula**; o uso e incidente de conformidade (MT-01) |
| **Relacao consta dos pares permitidos** (FND-09 §6.2) | Relacao nula (RM-02) |
| **Verificacao de aptidao emitida em C2/C3** | Mudanca nao encerra (QG-6, FT-05) |
| **`revisor` distinto de `autor`** | Aprovacao **nula** (AC-03, LV-03) |
| **Ratificacao coerente com a classe** | Artefato retido em `aprovado` (LM-02) |
| **Entrada no catalogo mestre presente** | Artefato nao localizavel; falha DoD-7 (RG-02) |

DEP-GOV audita conformidade a cada fechamento de ciclo e a cada portao QG.

---

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-GOV | Taxonomia inicial. Ratificada por ADR-0001. |
| 1.1.0 | 2026-07-28 | DEP-GOV | Emenda por ADR-0002: tipo `CAP`, dominios de Capability, campo `capabilities` obrigatorio, diretorio `capabilities/`, vocabulario e conformidade. |
| 1.2.0 | 2026-07-28 | DEP-GOV | Emenda por ADR-0003 e ADR-0004: identificadores `MSG` e `FIT`; classe `modelo` de ferramenta; §3.13 Mensagem e §3.14 Verificacao de aptidao; eixos `vigencia` e `situacao` no frontmatter; `capabilities` estendido a projeto e ferramenta; diretorio `governance/fitness/`; vocabulario acrescido de Entidade, Arquetipo e Estrato; tres verificacoes de conformidade. |
| 1.3.0 | 2026-07-28 | DEP-GOV | Emenda por ADR-0006: identificadores `REV` e `IDX`, ambos **sem criar entidade**; §3.15 Revisao arquitetural e §3.16 Indice; extensao do frontmatter com cinco campos e valor padrao; `governance/artifact-registry.md` na arvore; vocabulario acrescido de Tipo documental, Perfil de contexto e Vista derivada; tres verificacoes de conformidade. **Ratificacao pendente.** |
| 1.5.0 | 2026-07-28 | DEP-GOV | Emenda C2 por **ADR-0010**: §8 acrescido de `Contexto do Soberano` como termo oficial — a **regra** vive em ADR-0010 §5, este e a fonte do **termo** (PJ-01). Nenhum identificador, estado, versao ou diretorio novo. Frontmatter passa a declarar os cinco campos do contrato de artefato (AC-08, **ADR-0009**), fechando o achado C13 quanto a este artefato. |
| 1.4.0 | 2026-07-28 | DEP-GOV | Emenda C2 por **ADR-0007**: §8 acrescido de `LucaX Enterprise OS`, `LucaX Legacy`, `Programa de Migracao`, `Proveniencia` e `Projecao` como termos oficiais; §9 passa a remeter ao portao de admissao — forma de importacao nao autoriza entrada. **Ratificacao de ADR-0001 registrada em INC-2026-001 §11.** |
| 1.6.0 | 2026-07-29 | DEP-GOV | Emenda **C3** por **ADR-0022**: **§7** acrescenta `11-framework-specifications.md` a arvore canonica de `foundation/`, unica alteracao do documento. **Nenhum identificador, estado, versao, diretorio, tipo documental ou termo novo.** **§3.6 nao e tocada:** a `Spec` continua vivendo em `products/<slug>/specs/<SPC-id>.md`, com sequencia por produto — o vinculo `Spec` x `Produto` permanece integralmente vigente, e **RD-33 permanece aberto e bloqueante**. |
