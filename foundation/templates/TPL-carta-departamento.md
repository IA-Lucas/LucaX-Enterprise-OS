---
id: TPL-carta-departamento
titulo: Template de Carta de Departamento
tipo: template
versao: 1.2.0
status: ativo
camada_memoria: nao-aplicavel
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0001, ADR-0011]
substitui: []
substituido_por: null
resumo: Fixa a forma obrigatoria da Carta de Departamento, com os doze blocos do contrato e as dez regras de desenho de ADR-0011.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# Template — Carta de Departamento

## Proposito
Dar existencia formal a um departamento, com escopo exclusivo, fronteiras, autoridade
rastreada e criterio de sucesso, conforme [FND-02 §8.1](../02-estrutura-organizacional.md) e
o **Contrato de Carta de Departamento** de
[ADR-0011](../../decisions/ADR-0011-contrato-de-carta-de-departamento.md).

## Escopo
Criacao e alteracao de Carta de Departamento. Mudanca **C2**. **Nao** se aplica a Carta de
Agente, Subagente, Produto, Projeto, Capability ou Ficha de Ferramenta.

## Responsaveis
Proprietario: DEP-GOV · Autor da Carta: **DEP-EXE** · Revisor: **DEP-GOV** ·
Aprova e ratifica: **SOBERANO** *(FND-09 §8.2, linha `DEP`)*.

## Instrucoes de uso

1. Grave em `departments/<dep>/carta.md`, onde `<dep>` e o **codigo do departamento em
   minusculas** (`qar`, `eng`) — LX-01. O ID no frontmatter permanece `DEP-<CODIGO>`.
2. Preceda de RFC + ADR. Departamento sem ADR de criacao nao existe (PI-12). Departamento ja
   criado por ADR anterior cita **esse** ADR em B12.
3. **Os doze blocos de ADR-0011 §5.2 sao obrigatorios.** Bloco ausente ou vazio torna a Carta
   nao conforme e DEP-GOV a devolve sem analise de merito (AC-06).
4. **A secao 4 — "O que NAO me compete" — e obrigatoria**: e ela que impede sobreposicao
   (ES-01, DC-05). Exclusao generica e devolvida; cada item nomeia o dono real.
5. **A secao 9 — impedimentos — e obrigatoria** (DC-03). Departamento que nao declare em que
   materia esta impedido de aprovar ou verificar nao tem Carta valida.
6. **Custodia e exercicio sao colunas distintas** na secao 2 (DC-02). A fonte de ambos e o
   frontmatter das Cartas de Capability; esta Carta e **projecao** (ADR-0011 §5.5, PR-1).
7. **Indicador sem valor medido declara-se `definido, sem valor`** (DC-07). Afirmar
   desempenho sem medida e LV-12.
8. **O perfil minimo de carregamento e medido em linhas**, com data (DC-10). Nao se estima.
9. **Nenhuma tabela reproduz norma de outro documento** sem declaracao de projecao com as
   quatro informacoes de PJ-02 (DC-08). Aplique o teste preventivo do checklist de
   [`TPL-documento`](TPL-documento.md) tabela a tabela, **antes** de submeter.
10. **A Carta nao entra em vigor por si** (DC-09): sem ato explicito e datado do Soberano ela
    permanece em `em-revisao`, com `ratificacao: pendente`. Declarar `aprovado` sem o ato
    repete a causa de [INC-2026-001](../../governance/incidents/INC-2026-001-ratificacao-inferida.md).
11. Registre a Carta no [catalogo mestre](../../governance/artifact-registry.md) — sem
    entrada, o artefato e nao localizavel (RG-02, DoD-7).

## Historico de versoes deste template
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-GOV | Criacao por ADR-0001: 13 secoes, com "O que nao me compete" obrigatoria. |
| 1.2.0 | 2026-07-28 | DEP-GOV | **Conclusao da propagacao da correcao M1**, decidida e declarada aplicada em [REV-DEPARTAMENTO §3.7](../revisao-arquitetural-cartas-de-departamento-2026-07-28.md) e que **nunca chegou a este arquivo**. O checklist passa a exigir a **conferencia cruzada B4 × B9**. Nao e decisao nova: e mudanca **incompleta** de ADR-0011 sendo completada (CV-04, RG-03). Achado **IC-1** de [REV-INTERCLASSES](../revisao-arquitetural-validacao-interclasses-2026-07-28.md). |
| 1.1.0 | 2026-07-28 | DEP-GOV | Emenda **MENOR** por **ADR-0011**: materializa os doze blocos do contrato — secao 2 passa a separar **custodia** de **exercicio**; novas secoes **6 Artefatos e registros**, **10 Riscos, impedimentos e segregacao**, **13 Resumo operacional e perfil minimo de carregamento**; secao 9 passa a declarar **politica de contexto**; secao 11 separa indicador **definido** de **medido**; secao 12 acrescenta gatilhos de **especializacao** e **fusao**; checklist do contrato acrescentado. Frontmatter passa a declarar os cinco campos do contrato de artefato (AC-08, ADR-0009). |

---
---
id: DEP-<CODIGO>
titulo: <Nome do Departamento>
tipo: carta
versao: 1.0.0
status: em-revisao
camada_memoria: estrategica
autor: DEP-EXE
proprietario: DEP-EXE
aprovador: SOBERANO
criado_em: <AAAA-MM-DD>
atualizado_em: <AAAA-MM-DD>
revisao_prevista: <AAAA-MM-DD>
decisoes_relacionadas: [<ADR de criacao do departamento>, ADR-0011]
substitui: []
substituido_por: null
classe: <comando|guarda|linha|plataforma>
nivel: <1|2>
nivel_autonomia: <A0|A1|A2|A3>
responde_a: <SOBERANO | DEP-EXE>
capabilities: [<CAP-slug>, ...]   # custodiadas ∪ exercidas; nunca vazio (FND-08 §8.1)
# contrato de artefato (FND-10 §2.2)
resumo: <uma linha, ate 200 caracteres, em voz ativa — o que este departamento faz>
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-GOV
ratificacao: pendente
# NAO declarar `projecao_de`: a Carta nao e majoritariamente projecao (FND-10 §2.2).
# A projecao da secao 2 declara-se no corpo, com as quatro informacoes de PJ-02.
---

# <Nome do Departamento> (DEP-<CODIGO>)

## Proposito
<Por que este departamento existe. Ate 3 frases. Nao repete a missao — a missao e a secao 1.>

## Escopo
| Item | Definicao |
|---|---|
| Classe | comando / guarda / linha / plataforma |
| Nivel | |
| Responde a | |
| Nivel de autonomia | |
| Poder de veto | sim / nao *(apenas classe Guarda — FND-02 §2.1)* |
| **Nao** inclui | <o que este documento nao trata; remete a secao 4> |
| Subordinado a | FND-01 · FND-02 · ADR-0011 |

## Responsaveis
| Papel | Quem |
|---|---|
| Autor da Carta | DEP-EXE |
| Proprietario | DEP-EXE |
| Guardiao normativo / revisor | DEP-GOV |
| Aprovador e ratificador | **SOBERANO** |

---

## 1. Missao e mandato  *(bloco B1)*

**Missao:** <uma frase — o resultado permanente pelo qual este departamento responde.>

**Mandato:** <uma frase — a autoridade que a missao exige, e nada alem dela.>

## 2. Capabilities custodiadas e exercidas  *(bloco B2 · DC-01, DC-02)*

> **Declaracao de projecao (PJ-02).** **Fonte:** frontmatter das Cartas de Capability em
> `capabilities/CAP-<slug>.md`, campos `custodio` e `exercentes`. **Campos projetados:** apenas
> as linhas deste departamento. **Finalidade:** responder "o que custodio e o que exerco" sem
> percorrer 23 arquivos. **Atualizacao:** pela mesma mudanca que altera a Carta de Capability
> (CV-04). Em divergencia, prevalece a Carta de Capability (ADR-0011 PR-1).

| Capability | Dominio · Classe | **Custodia** *(zelo, unica)* | **Exercicio** *(pratica, nao exclusiva)* | Por que este departamento |
|---|---|---|---|---|
| | | sim / nao | sim / nao | |

**Capabilities que exerco sem custodiar:** <lista, ou "nenhuma">
**Capabilities que custodio e sao exercidas por outros:** <lista, ou "nenhuma">

> Custodia **nao** e exclusividade de exercicio (OW-02, RM-05). Acrescentar exercente e
> mudanca na **Carta de Capability**, nunca declaracao unilateral aqui (PR-3).

## 3. O que possuo — escopo exclusivo  *(bloco B3 · DC-05)*
> Cada item aqui tem exatamente um dono: este departamento (ES-01).

| # | Responsabilidade | Como se verifica que esta sendo cumprida | Capability correspondente |
|---|---|---|---|

## 4. O que NAO me compete  *(bloco B3 · DC-05)*
> **Secao obrigatoria.** Sem ela a Carta nao e aprovada. Exclusao generica e devolvida:
> cada linha nomeia o **dono real**.

| Materia | Dono real | Fonte |
|---|---|---|

## 5. O que decido — autoridade e portoes  *(bloco B4 · DC-04)*

> **Autoridade nao declarada na fonte nao existe** (AU-09). Linha sem fonte e removida.

| Materia | Autonomia | Consulta obrigatoria | **Fonte da autoridade** |
|---|---|---|---|

### 5.1 O que **nao** decido
| Materia | Quem decide | Fonte |
|---|---|---|

### 5.2 Portoes sob minha responsabilidade
| Portao | O que verifico | Criterio de liberacao | Fonte |
|---|---|---|---|

> Portao novo **nao** se cria aqui: os sete sao de FND-01 §6.2 e acrescentar e **C3**.

## 6. Interfaces — entradas, saidas e consumidores  *(bloco B5)*

### 6.1 Entradas
| De quem | O que recebo | Em que forma | Gatilho |
|---|---|---|---|

### 6.2 Saidas
| Entrega | Destinatario | Formato | Cadencia | Consumidor final |
|---|---|---|---|---|

### 6.3 Natureza da interacao
| Departamento | Natureza *(entrega / consulta / veto / aprovacao)* | O que trafega |
|---|---|---|

> A matriz completa de interacao vive em **FND-02 §4** e **nao** e reproduzida aqui: esta
> secao declara apenas as linhas deste departamento (DC-08).

## 7. Artefatos e registros mantidos  *(bloco B6)*

| Tipo documental | Entidade | Sou autor / proprietario / revisor? | Onde vive |
|---|---|---|---|

> Tipo documental que nao conste de **FND-10 §4** nao existe (CS-01, MT-01).

## 8. Quando escalo  *(bloco B10)*

| Gatilho | Escala para | Nivel *(FND-05 §7.1)* | Bloqueia execucao? |
|---|---|---|---|

### 8.1 Cadencias de que participo
| Cadencia | Meu papel | O que produzo |
|---|---|---|

### 8.2 Handoffs
| Handoff | Emito / recebo | Criterio de aceite | Criterio de devolucao |
|---|---|---|---|

## 9. Memoria autorizada e politica de contexto  *(bloco B7)*

| Camada | Meu papel *(dono / escritor / leitor obrigatorio / sem acesso de escrita)* | Sob que condicao |
|---|---|---|
| EST | | |
| PRD | | |
| TEC | | |
| OPR | | |
| APR | | |

### 9.1 Politica de contexto
| Item | Valor |
|---|---|
| Pacote minimo para operar | <artefatos, por ID> |
| Custo medido do pacote | <N linhas, medido em AAAA-MM-DD> |
| Gatilho para carregar alem do minimo | <declarado; carregamento sem gatilho e falha de curadoria, PC-01, CE-01> |

## 10. Riscos, impedimentos e segregacao  *(bloco B9 · DC-03)*

> **Secao obrigatoria.** Departamento nao aprova nem verifica materia em que esteja impedido.

| # | Materia em que estou impedido | Por que | **Quem me substitui** | Fonte |
|---|---|---|---|---|

### 10.1 Riscos proprios do dominio
| # | Risco | Probabilidade | Impacto | Mitigacao declarada |
|---|---|---|---|---|

### 10.2 Incompatibilidades de papel
| Papel A | Papel B | Por que nao se acumulam na mesma mudanca |
|---|---|---|

## 11. Indicadores  *(bloco B8 · DC-07)*

> Indicador **sem valor medido** declara-se `definido, sem valor`. Afirmar desempenho sem
> medida e LV-12.

| # | Indicador | Definicao | Direcao | **Valor medido** | **Data da medicao** |
|---|---|---|---|---|---|
| | | | ↑ / ↓ / estavel | `<valor>` ou **`definido, sem valor`** | |

**Contagem:** <N> definidos · <M> com valor medido.

## 12. Ciclo de vida — especializacao, fusao e retirada  *(bloco B11 · DC-06)*

### 12.1 Gatilhos de especializacao
| Gatilho *(FND-02 §9.2)* | Aplica-se a mim? | **Sinal ja observado** *(valor e data)* | Movimento previsto |
|---|---|---|---|

> **Ganho previsto nao autoriza divisao** (SE-01). Sinal declarado sem valor medido nao conta.

### 12.2 Gatilhos de fusao ou consolidacao
| Sinal *(FND-02 §9.3)* | Com quem | O que indicaria |
|---|---|---|

### 12.3 Criterio de extincao
<Como saberemos que este departamento deixou de ser necessario. Na extincao, **cada
responsabilidade e cada custodia recebem destino explicito** (IV-07, FND-02 §8.3).>

| Responsabilidade / custodia | Destino declarado na extincao |
|---|---|

### 12.4 Funcoes internas nomeadas
> Responsabilidades hospedadas aqui que ainda nao merecem departamento proprio (ES-04).

| Funcao | Responsabilidade | Gatilho de promocao |
|---|---|---|

## 13. Resumo operacional, carregamento e rastreabilidade  *(bloco B12 · DC-10)*

### 13.1 Resumo operacional
<Uma linha, ate 200 caracteres, em voz ativa. E o mesmo valor do campo `resumo` — aqui ele
serve a quem le a Carta; la, a quem decide se abre a Carta (FND-10 §8.3).>

### 13.2 Perfil minimo de carregamento
| Recorte | Para que serve | Custo **medido** | Data |
|---|---|---|---|
| Secoes 1, 2 e 4 | Saber o que este departamento faz e o que nao faz | <N linhas> | <AAAA-MM-DD> |
| + secoes 5 e 10 | Decidir se ele pode aprovar ou verificar algo | <N linhas> | <AAAA-MM-DD> |
| Carta integral | Auditoria, revisao estrutural, extincao | <N linhas> | <AAAA-MM-DD> |

> Carregar alem do recorte aplicavel exige **gatilho declarado** (CE-01, PC-01).

### 13.3 Rastreabilidade
| Campo | Conteudo |
|---|---|
| ADR de criacao do departamento | |
| ADR do contrato desta Carta | ADR-0011 |
| RFC de origem | |
| Alteracoes (ADRs) | |
| Fonte da custodia e do exercicio | frontmatter de `capabilities/CAP-*.md` |

---

## Checklist do contrato (ADR-0011 §5.2 e §5.3)
- [ ] **B1** identidade, classe, nivel, autonomia, `responde_a`, proposito e mandato
- [ ] **B2** custodia e exercicio em **colunas separadas**, com declaracao de projecao *(DC-02, DC-08)*
- [ ] **B3** escopo exclusivo **e** "o que nao me compete", cada exclusao com dono real *(DC-05)*
- [ ] **B4** cada linha de autoridade com **Fonte**; nenhuma autoridade autodeclarada *(DC-04)*
- [ ] **B5** entradas, saidas, consumidores e natureza da interacao
- [ ] **B6** artefatos e registros mantidos, por tipo documental de FND-10 §4
- [ ] **B7** memoria autorizada por camada **e** politica de contexto com custo medido
- [ ] **B8** indicadores com valor medido **ou** marca `definido, sem valor` *(DC-07)*
- [ ] **B9** impedimentos declarados, com substituto nomeado *(DC-03)*
- [ ] **B10** escalonamento com nivel E0–E4, cadencias e handoffs
- [ ] **B11** gatilhos de especializacao com **sinal observado**, fusao e destino na extincao *(DC-06)*
- [ ] **B12** resumo operacional, perfil de carregamento **medido** e rastreabilidade *(DC-10)*
- [ ] **B4 × B9 — conferencia cruzada** *(correcao **M1**, REV-DEPARTAMENTO §3.7)*: **cada** linha
      de autoridade de B4 e lida contra o impedimento correspondente de B9. Autoridade concedida
      em B4 sem o impedimento vizinho declarado em B9 e devolvida. Foi este par que distinguiu
      *escolher* de *adotar* no cenario CN-1; sem a conferencia, a distincao depende de leitura
      atenta em vez de verificacao
- [ ] **DC-01** nenhuma Capability e definida, criada, dividida ou aposentada nesta Carta
- [ ] **DC-09** `status: em-revisao` e `ratificacao: pendente` enquanto nao houver ato do Soberano
- [ ] Nenhum conteudo proibido de ADR-0011 §5.4
- [ ] Checklist de conformidade de [`TPL-documento`](TPL-documento.md) aplicado, **inclusive o
      teste preventivo de projecao (PJ-05)**
- [ ] Entrada criada no [catalogo mestre](../../governance/artifact-registry.md) *(RG-02)*
