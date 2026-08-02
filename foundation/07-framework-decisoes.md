---
id: FND-07
titulo: Framework de Decisoes do LucaX Enterprise OS
tipo: fundacao
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0001]
substitui: []
substituido_por: null
---

# Framework de Decisoes

## Proposito

Definir como decisoes sao classificadas, tomadas, registradas, revisadas e superadas no
LucaX Enterprise OS. Estabelece o padrao obrigatorio de registro contendo contexto,
alternativas consideradas, justificativa, impacto, evidencias e data.

Uma decisao registrada e um ativo: evita que a mesma analise seja refeita e permite que
um erro seja rastreado ate seu raciocinio original. **Decisao nao registrada nao existe**
(PI-04).

## Escopo

| Item | Definicao |
|---|---|
| **Inclui** | O que e decisao relevante, classificacao por impacto e reversibilidade, instrumentos (ADR, RFC, Nota de Decisao), estrutura obrigatoria de registro, ciclo de vida, superacao, revisao, decisao de nao decidir. |
| **Nao inclui** | O rito de aprovacao por classe (FND-04), o formato de mensagem (FND-05), onde a decisao e memorizada (FND-06). |
| **Subordinado a** | [FND-01 Constituicao](01-constituicao.md), §7. |
| **Aplica-se a** | Toda decisao relevante, de qualquer departamento, sobre qualquer materia. |

## Responsaveis

| Papel | Responsavel |
|---|---|
| Proprietario do framework | DEP-GOV |
| Numeracao e registro oficial | DEP-GOV |
| Verificacao de risco e reversibilidade | DEP-QAR |
| Arbitragem de merito entre areas | DEP-EXE |
| Ratificacao Tipo 1 e C3 | SOBERANO |
| Preservacao na memoria | DEP-KMS |

---

## 1. O Que E Uma Decisao Relevante

Uma escolha e **decisao relevante** — e portanto exige registro — quando **qualquer uma**
das condicoes abaixo for verdadeira:

| # | Condicao |
|---|---|
| DR-1 | Alguem no futuro vai se perguntar "por que fizemos assim?" |
| DR-2 | Desfazer custa mais do que fazer de novo. |
| DR-3 | Afeta mais de um departamento, produto ou componente. |
| DR-4 | Cria, altera ou remove um componente do sistema. |
| DR-5 | Estabelece precedente que sera invocado depois. |
| DR-6 | Envolve tradeoff real entre alternativas defensaveis. |
| DR-7 | Contraria, excepciona ou tensiona uma norma vigente. |
| DR-8 | Envolve dado vivo, credencial, custo recorrente ou exposicao externa. |
| DR-9 | Adia deliberadamente algo que os criterios mandariam fazer (§9). |

**Nao sao decisoes relevantes:** execucao de procedimento ja definido, escolha sem
consequencia observavel, preferencia estetica sem impacto, ou aplicacao direta de norma
vigente.

### 1.1 Teste rapido
> Se daqui a seis meses alguem puder olhar o resultado e perguntar **"por que?"** sem
> encontrar resposta, a decisao era relevante e deveria ter sido registrada.

## 2. Classificacao da Decisao

Toda decisao relevante e classificada em **dois eixos independentes**, antes de ser tomada.

### 2.1 Eixo 1 — Reversibilidade

| Tipo | Nome | Definicao | Postura |
|---|---|---|---|
| **Tipo 1** | Porta de mao unica | Irreversivel, ou reversao cara, lenta ou arriscada | Devagar, com evidencia, com aprovacao humana |
| **Tipo 2** | Porta de mao dupla | Reversivel a custo baixo e conhecido | Rapido, no nivel mais baixo competente |

**Indicadores de Tipo 1:** perda ou migracao de dado · exposicao externa · compromisso
publico · dependencia externa nova · custo recorrente · mudanca de norma · encerramento de
componente · qualquer coisa que outros passarao a assumir como dado.

> **Regra da duvida (GV-03):** nao sabendo classificar, e **Tipo 1**. A duvida e, ela
> propria, sinal de que a reversao nao foi compreendida.

### 2.2 Eixo 2 — Impacto (classe de mudanca)

Usa as classes de FND-04 §2: **C0** editorial · **C1** operacional · **C2** estrutural ·
**C3** constitucional.

### 2.3 Matriz combinada

| | **C0** | **C1** | **C2** | **C3** |
|---|---|---|---|---|
| **Tipo 2** | Sem registro | Nota de Decisao | RFC → ADR | RFC → ADR → Ratificacao |
| **Tipo 1** | *(nao existe)* | **Escala para C2** | RFC → ADR → **Ratificacao** | RFC → ADR → **Ratificacao** |

**Le-se:** a linha Tipo 1 **sempre** termina em ratificacao humana explicita (PI-06). Nao
ha celula da matriz em que uma decisao irreversivel dispense o Soberano.

### 2.4 Quem decide

| Combinacao | Decide | Ratifica |
|---|---|---|
| C1 · Tipo 2 | Proprietario do dominio (A2+) | — |
| C2 · Tipo 2 | DEP-EXE, com parecer de DEP-GOV | — |
| C2 · Tipo 1 | DEP-EXE propoe | **SOBERANO** |
| C3 · qualquer | Proposta por qualquer area | **SOBERANO** (indelegavel) |
| Materia de veto (conformidade/qualidade) | DEP-GOV / DEP-QAR — vinculante | SOBERANO, so para reverter |

Ver tambem a tabela de direitos de decisao por materia: FND-01 §7.3.

## 3. Instrumentos de Registro

| Instrumento | Pergunta que responde | Estado da decisao | Onde vive |
|---|---|---|---|
| **RFC** | "Devemos fazer X? Quais as opcoes?" | **Em aberto** | `rfcs/` |
| **ADR** | "Decidimos X, por estes motivos." | **Tomada** | `decisions/` |
| **Nota de Decisao** | "Optamos por X neste caso." | Tomada, escopo local | `memory/operacional/` |

### 3.1 RFC — quando usar
- Mudanca C2 ou C3 (obrigatorio para C3)
- Existe divergencia real entre alternativas
- A decisao afeta areas que precisam se manifestar antes
- O problema ainda nao esta bem formulado

**RFC pode ser rejeitada.** RFC rejeitada vai para `arquivado` e **nunca e apagada**: saber
o que foi recusado e por que e tao valioso quanto saber o que foi aprovado.

### 3.2 ADR — quando usar
- Toda decisao C2 e C3, sem excecao
- Toda decisao Tipo 1, qualquer que seja a classe
- Decisao C1 que cria precedente (DR-5)

**ADR aprovado e imutavel** (LV-04). Nao se edita, nao se corrige, nao se atualiza. Ele e
**superado** por um novo ADR que o referencia (§7).

### 3.3 Nota de Decisao — quando usar
- Decisao C1, Tipo 2, de escopo local
- Escolha de execucao que responde a DR-1 mas nao aos demais criterios

Formato reduzido, mas com os campos irrenunciaveis: contexto, alternativa descartada,
escolha, motivo, data, responsavel. **Nota de Decisao que criar precedente vira ADR.**

## 4. Estrutura Obrigatoria do Registro de Decisao

Todo ADR contem, nesta ordem, **todas** as secoes abaixo. Secao ausente ou vazia torna o
registro **invalido** e DEP-GOV o devolve sem analise de merito.

```markdown
# ADR-<NNNN>: <Titulo — a decisao em uma frase afirmativa>

## Proposito
## Escopo
## Responsaveis

## 1. Contexto
Qual e a situacao, o que a torna um problema agora, e o que muda se nada for feito.
Fatos, nao justificativas. Estado do mundo antes da decisao.

## 2. Problema / Pergunta de decisao
A pergunta exata que este ADR responde. Uma unica pergunta.

## 3. Criterios de decisao
Os criterios usados para comparar as opcoes, **declarados antes** da escolha, com peso
relativo. Criterio inventado depois da escolha e racionalizacao, nao criterio.

## 4. Alternativas consideradas
Minimo: **duas alternativas reais + a opcao "nao fazer nada"**.
Para cada uma: descricao, a favor, contra, custo, risco, e por que foi ou nao escolhida.
Alternativa de palha (criada so para perder) invalida o registro.

## 5. Decisao
O que foi decidido, em frase afirmativa e inequivoca. Sem hedge, sem "provavelmente".

## 6. Justificativa
Por que esta opcao vence pelos criterios da secao 3. Explicitar o tradeoff aceito:
o que se esta abrindo mao ao escolher isto.

## 7. Impacto
| Dimensao | Impacto |
|---|---|
| Departamentos afetados | |
| Componentes afetados | |
| Camadas de memoria a atualizar | |
| Decisoes superadas | |
| Documentos a atualizar | |
| Custo e dependencia criados | |
| Ganho de PI-14 (organizacao/reuso/contexto) | |

## 8. Evidencias
O que sustenta a decisao: dados, testes, registros de memoria (por ID), experiencia
anterior (registro APR), fonte externa. Para cada evidencia, o grau de confianca.
**"Parece melhor" nao e evidencia.** Ausencia de evidencia deve ser declarada como tal.

## 9. Riscos e mitigacao
O que pode dar errado, qual a probabilidade e o impacto, e o que ja esta previsto
para cada risco. Incluir o risco de a propria decisao estar errada.

## 10. Plano de reversao
Como desfazer, a que custo, dentro de qual janela, e quem executa.
Obrigatorio para Tipo 1. Para Tipo 2, declarar por que a reversao e trivial.

## 11. Classificacao
| Campo | Valor |
|---|---|
| Classe de mudanca | C0 / C1 / C2 / C3 |
| Tipo de reversibilidade | 1 / 2 |
| Decisor | |
| Ratificador | |
| Data da decisao | AAAA-MM-DD |
| Data de vigencia | AAAA-MM-DD |

## 12. Revisao
Quando esta decisao sera reavaliada, sob qual gatilho, e qual sinal indicaria que
ela deu errado. Decisao sem gatilho de revisao vira dogma.

## 13. Rastreabilidade
Origem (RFC, incidente, escalada), decisoes superadas, decisoes relacionadas,
registros de memoria gerados.
```

### 4.1 Regras de validade

| # | Regra | Consequencia se violada |
|---|---|---|
| VD-01 | Minimo de 2 alternativas reais + "nao fazer nada" | Registro invalido (PI-04, FND-01 §7.1.4) |
| VD-02 | Criterios declarados antes da escolha | Registro devolvido: e racionalizacao |
| VD-03 | Alternativa de palha e proibida | Registro invalido |
| VD-04 | Tradeoff aceito deve estar explicito | Registro incompleto |
| VD-05 | Evidencia ausente e declarada como ausente | Omissao = violacao de PI-10 |
| VD-06 | Plano de reversao obrigatorio em Tipo 1 | Aprovacao vetada por DEP-QAR |
| VD-07 | Impacto em cascata mapeado | Mudanca incompleta (CV-04) |
| VD-08 | Data e responsavel presentes | Decisao nula (GV-01) |
| VD-09 | Gatilho de revisao definido | Devolvido por DEP-GOV |

### 4.2 Por que "nao fazer nada" e obrigatorio
Porque o custo de agir e frequentemente invisivel, e porque comparar so entre acoes esconde
que o status quo as vezes vence. A opcao nula tambem forca a explicitar o custo real da
inacao — que e o argumento mais honesto a favor de agir.

## 5. Ciclo de Vida da Decisao

```
 [1] GATILHO       problema, escalada, incidente, gatilho de revisao, gatilho PI-14
       |
 [2] ENQUADRAMENTO qual e a pergunta exata? (§4, secao 2)
       |
 [3] CLASSIFICACAO impacto (C0-C3) x reversibilidade (Tipo 1/2)
       |           DEP-GOV valida                              <-- veto
       |
 [4] CRITERIOS     definidos e pesados ANTES de olhar as opcoes
       |
 [5] ALTERNATIVAS  >= 2 reais + "nao fazer nada"
       |
 [6] EVIDENCIA     consulta obrigatoria a memoria (FND-06 §8.1)
       |           EST + APR + camada do dominio
       |
 [7] ESCOLHA       comparacao pelos criterios de [4]
       |
 [8] REVISAO       revisor independente + DEP-QAR (risco/reversao)  <-- veto
       |
 [9] APROVACAO     conforme §2.4
       |           SOBERANO ratifica se Tipo 1 ou C3               <-- indelegavel
       |
[10] REGISTRO      DEP-GOV atribui numero e publica o ADR
       |
[11] PROPAGACAO    documentos dependentes atualizados; superados marcados
       |
[12] MEMORIA       DEP-KMS grava na camada correta (QG-5)
       |
[13] VIGENCIA      decisao passa a valer e vincula
       |
[14] REVISAO       na data ou no gatilho definidos em §4, secao 12
```

### 5.1 Regras do ciclo
| # | Regra |
|---|---|
| CD-01 | Etapa 4 antes da 5, sempre. Criterio definido depois de ver as opcoes e viesado. |
| CD-02 | Etapa 6 e obrigatoria: decidir sem consultar a memoria repete analise ja feita e desperdica o ativo (MM-04). |
| CD-03 | Etapa 10 precede a execucao para C2 e C3 (CV-02). |
| CD-04 | Mudanca de escopo entre [7] e [9] reabre o ciclo em [3]. |
| CD-05 | Decisao vigente ([13]) vincula todos, inclusive quem discordou. Discordancia registrada, execucao integral. |

## 6. Estados da Decisao

| Estado | Significado | Vincula? |
|---|---|---|
| `rascunho` | Em elaboracao | Nao |
| `em-revisao` | Sob analise independente | Nao |
| `aprovado` | Aceito; aguarda vigencia | Sim, a partir da vigencia |
| `ativo` | Em vigor | **Sim** |
| `depreciado` | Ainda vale; substituicao ja decidida | Sim, com ressalva |
| `superado` | Substituido por outro ADR | Nao — valor historico |
| `revogado` | Anulado sem substituto | Nao |
| `arquivado` | RFC nao aceita | Nao — valor historico |

## 7. Superacao de Decisoes

**Um ADR aprovado nunca e editado** (LV-04). Ele e superado.

### 7.1 Rito de superacao

| Etapa | Acao |
|---|---|
| 1 | Novo ADR e aberto, declarando `supera: [ADR-XXXX]` |
| 2 | O novo ADR explica **por que a decisao anterior deixou de servir** — nao basta apresentar a nova |
| 3 | O que mudou desde entao e explicitado: contexto, evidencia, criterio ou resultado observado |
| 4 | O ADR antigo passa a `superado`, com `superado_por` preenchido — **texto original intacto** |
| 5 | Dependentes do ADR antigo sao migrados (CV-04) |
| 6 | Se a decisao anterior estava errada, abre-se registro APR sobre a causa do erro |

### 7.2 Regras
| # | Regra |
|---|---|
| SU-01 | Superacao sem explicar o que mudou e substituicao de opiniao, nao decisao. E devolvida. |
| SU-02 | Superar decisao ratificada pelo Soberano exige nova ratificacao do Soberano. |
| SU-03 | Superacao frequente da mesma materia indica que o problema esta mal enquadrado (etapa 2) — DEP-GOV escala. |
| SU-04 | Decisao revogada sem substituto exige declaracao explicita do que passa a valer no lugar. |

## 8. Revisao Programada

Toda decisao carrega o gatilho da propria reavaliacao (§4, secao 12).

| Tipo de gatilho | Exemplo |
|---|---|
| **Temporal** | "Reavaliar em 2027-01-28" |
| **Por evento** | "Reavaliar quando o produto passar de 1.000 usuarios" |
| **Por sinal de falha** | "Reavaliar se o tempo de build passar de 5 minutos" |
| **Por confirmacao de ganho (PI-14)** | "Reavaliar se a divisao reduziu o contexto necessario" |

### 8.1 Resultado da revisao
Sempre um destes tres, sempre registrado:

| Resultado | Acao |
|---|---|
| **Confirmar** | Nota registrando que foi revista e mantida, com novo gatilho |
| **Ajustar** | Novo ADR que supera parcialmente o anterior |
| **Superar** | Novo ADR pelo rito de §7 |

Revisao vencida e nao realizada e achado de auditoria (FND-04 §8).

## 9. Decisao de Nao Decidir

Adiar e uma decisao, e a mais facil de tornar invisivel. Quando um gatilho existe e a acao
e adiada, registra-se (DR-9):

| Campo | Conteudo |
|---|---|
| O que se decidiu **nao** decidir agora | |
| Por que adiar e melhor que decidir agora | |
| O custo assumido pelo adiamento | |
| O que precisa acontecer para decidir | |
| Ate quando o adiamento vale | |
| Quem e o dono do adiamento | |

Aplica-se especialmente a PI-14: gatilho de especializacao constatado e divisao adiada
exige este registro (FND-04 §6.2). **Custo assumido conscientemente e divida declarada;
custo invisivel e defeito de governanca.**

Adiamento sem prazo e invalido: vira decisao por omissao, que viola PI-04.

## 10. Qualidade da Decisao

### 10.1 Separar decisao de resultado
Uma boa decisao pode ter mau resultado; uma decisao ruim pode dar certo por sorte. A
organizacao avalia **o processo decisorio**, nao apenas o desfecho.

| Pergunta de avaliacao | O que revela |
|---|---|
| Os criterios foram definidos antes? | Vies de racionalizacao |
| As alternativas eram reais? | Decisao encenada |
| A memoria foi consultada? | Desperdicio de ativo |
| A evidencia sustentava a confianca declarada? | Excesso de confianca |
| O risco identificado foi o que se materializou? | Calibracao de risco |
| A reversao funcionou como previsto? | Realismo do plano |

### 10.2 Antipadroes que invalidam o registro

| Antipadrao | Como reconhecer |
|---|---|
| **Alternativa de palha** | Todas as opcoes descartadas sao obviamente ruins |
| **Criterio retroativo** | Os criterios descrevem exatamente a opcao escolhida |
| **Evidencia decorativa** | Dados citados nao discriminam entre as alternativas |
| **Decisao sem dono** | "Foi decidido que..." sem responsavel nomeado |
| **Escopo elastico** | A decisao cresce durante a execucao sem reabrir o ciclo |
| **Consenso presumido** | Ausencia de objecao tratada como concordancia (CM-07) |
| **Reversao teorica** | Plano de reversao que ninguem verificou ser executavel |

DEP-QAR verifica esses antipadroes em QG-3; DEP-GOV, na auditoria de coerencia normativa.

### 10.3 Calibracao
Decisoes com resultado observado alimentam a camada APR (FND-06 §3.5): acerto de
estimativa, risco que se materializou, reversao que funcionou ou nao. Isso torna a proxima
decisao mensuravelmente melhor — que e a definicao operacional da Visao V2.

## 11. Decisao sob Urgencia

Urgencia altera o **instrumento**, nunca o **registro** (GV-08).

| Regra | Detalhe |
|---|---|
| UR-01 | Urgencia real exige excecao formal (FND-01 §8.3) autorizada pelo Soberano. |
| UR-02 | Decisao urgente Tipo 1 continua exigindo aprovacao humana. Urgencia **nao** dispensa PI-06. |
| UR-03 | Registro pode ser **abreviado no momento** e completado depois — em prazo declarado na propria excecao. |
| UR-04 | Registro pendente vencido e incidente de conformidade. |
| UR-05 | Toda decisao urgente gera registro APR: por que a organizacao foi surpreendida. |

**Nunca dispensavel, mesmo sob urgencia:** o que foi decidido, quem decidiu, quando, e qual
o plano de reversao.

---

## Documentos e artefatos relacionados

| Referencia | Relacao |
|---|---|
| [FND-01 §7](01-constituicao.md) | Regras invariantes de decisao e direitos por materia |
| [FND-04 §2](04-governanca.md) | Classes de mudanca e rito de aprovacao |
| [FND-06 §8.1](06-arquitetura-memoria.md) | Consulta obrigatoria a memoria antes de decidir |
| [TPL-adr](templates/TPL-adr.md) | Template do registro de decisao |
| [TPL-rfc](templates/TPL-rfc.md) | Template de proposta |
| [TPL-nota-decisao](templates/TPL-nota-decisao.md) | Template do registro leve |

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-GOV | Framework inicial: 2 eixos de classificacao, 3 instrumentos, 13 secoes obrigatorias de ADR. Ratificado por ADR-0001. |
