---
id: FND-05
titulo: Framework de Comunicacao do LucaX Enterprise OS
tipo: fundacao
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-EXE
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0001]
substitui: []
substituido_por: null
---

# Framework de Comunicacao

## Proposito

Definir como departamentos e, futuramente, agentes trocam informacao: quais canais existem,
qual o formato obrigatorio de cada mensagem, como o contexto e transferido sem perda, como
resultados sao reportados, como divergencias sao escaladas e o que precisa ficar registrado.

Comunicacao no LucaX nao e conversa: e **transferencia de responsabilidade com contrato**.

## Escopo

| Item | Definicao |
|---|---|
| **Inclui** | Principios de comunicacao, canais, envelope padrao de mensagem, contrato de handoff, pacote de contexto, formatos de reporte, escalonamento, cadencias, regras de registro. |
| **Nao inclui** | Protocolo tecnico, implementacao, ferramenta de mensageria, automacao (fases futuras). |
| **Subordinado a** | [FND-01 Constituicao](01-constituicao.md), [FND-02 Estrutura](02-estrutura-organizacional.md). |
| **Consumido por** | Todos os departamentos hoje; todos os agentes quando existirem. |

## Responsaveis

| Papel | Responsavel |
|---|---|
| Proprietario | DEP-EXE |
| Guardiao do formato | DEP-GOV |
| Custodia dos registros de comunicacao | DEP-KMS |
| Aprovador de mudanca | SOBERANO (via ADR) |

---

## 1. Principios de Comunicacao

| # | Principio | Consequencia pratica |
|---|---|---|
| CM-01 | **Escrito e assincrono por padrao.** | Nada relevante existe apenas em uma sessao ou conversa. |
| CM-02 | **Mensagem carrega contrato.** | Toda solicitacao declara o que se espera e como se verifica. |
| CM-03 | **Contexto viaja com o trabalho.** | Quem recebe nao precisa reconstruir o que quem enviou ja sabia. |
| CM-04 | **Contexto minimo suficiente (PI-14).** | Envia-se o que a tarefa usa, nao tudo o que existe sobre o tema. |
| CM-05 | **Uma mensagem, um pedido.** | Multiplos pedidos viram multiplas mensagens rastreaveis. |
| CM-06 | **Remetente e destinatario sao papeis, nao pessoas.** | Endereca-se `DEP-ENG`, nao "quem estiver livre". |
| CM-07 | **Silencio nao comunica nada.** | Ausencia de resposta nunca significa aceite, recusa ou conclusao (GV-05). |
| CM-08 | **Ma noticia viaja primeiro.** | Falha, bloqueio e incerteza sao comunicados antes do relatorio de rotina (PI-10). |
| CM-09 | **Referencia por ID, nunca por copia.** | Cita-se `ADR-0007`; nao se recola o conteudo dele (FND-03 §7.1). |
| CM-10 | **Toda mensagem e potencialmente memoria.** | O formato ja e o formato do registro; nao se "traduz depois". |

## 2. Canais de Comunicacao

Cinco canais. Cada mensagem pertence a exatamente um.

| Canal | Direcao | Finalidade | Resposta obrigatoria? |
|---|---|---|---|
| **DIRETIVA** | De cima para baixo | Determinar o que sera feito | Sim — aceite ou objecao |
| **HANDOFF** | Lateral | Transferir trabalho e responsabilidade entre areas | Sim — aceite ou devolucao |
| **REPORTE** | De baixo para cima | Informar estado, resultado ou conclusao | Nao, salvo se pedir decisao |
| **CONSULTA** | Qualquer direcao | Obter parecer sem transferir responsabilidade | Sim — parecer ou declinio |
| **ALERTA** | Qualquer direcao, prioritaria | Comunicar risco, bloqueio, violacao ou incidente | Sim — imediata |

### 2.1 Regras de canal

| # | Regra |
|---|---|
| CN-01 | **DIRETIVA** so desce pela cadeia de autoridade de FND-02. Area de Linha nao emite diretiva a outra area de Linha — usa HANDOFF ou escala a DEP-EXE. |
| CN-02 | **CONSULTA nao transfere responsabilidade.** Quem consulta continua dono do resultado. Parecer nao vincula, salvo parecer de Guarda em materia de conformidade ou qualidade. |
| CN-03 | **HANDOFF transfere responsabilidade** apenas quando aceito. Enquanto nao ha aceite, o trabalho continua com o remetente. |
| CN-04 | **ALERTA interrompe.** Tem precedencia sobre qualquer outro canal e nao pode ser enfileirado. |
| CN-05 | **REPORTE nao pede.** Se ha pedido embutido, e DIRETIVA, HANDOFF ou CONSULTA — e deve ser separado (CM-05). |
| CN-06 | Veto de Guarda circula como **ALERTA**, nunca como reporte de rotina. |

## 3. Envelope Padrao de Mensagem

Toda comunicacao formal usa este envelope. Campo obrigatorio ausente torna a mensagem
**invalida**: nao gera obrigacao para o destinatario, e este deve devolve-la.

```yaml
---
msg_id: MSG-<AAAA>-<NNNN>
canal: DIRETIVA | HANDOFF | REPORTE | CONSULTA | ALERTA
de: <DEP-xxx | AGT-xxx | SOBERANO>
para: <DEP-xxx | AGT-xxx | SOBERANO>
com_copia: [<papel>, ...]
assunto: <uma linha, sem ambiguidade>
prioridade: rotina | alta | critica
referencias: [<ADR-xxxx>, <SPC-xxx>, <MSG-xxxx>, ...]
prazo: <AAAA-MM-DD | null>
nivel_autonomia_concedido: A0 | A1 | A2 | A3
resposta_esperada: aceite | parecer | entrega | ciencia
criado_em: <AAAA-MM-DD>
---
```

### 3.1 Corpo obrigatorio

```markdown
## Contexto
O que o destinatario precisa saber para agir — e apenas isso (CM-04).

## Pedido
Uma frase imperativa. Exatamente um pedido (CM-05).

## Criterio de aceite
Como se verifica objetivamente que o pedido foi atendido.

## Fora de escopo
O que explicitamente nao se pede. Evita ampliacao silenciosa (PI-09).

## Restricoes
Normas, limites, riscos e dependencias aplicaveis.

## Contexto anexo
Referencias por ID. Nunca copia de conteudo (CM-09).
```

### 3.2 Campos por canal

| Canal | Campos adicionais obrigatorios |
|---|---|
| DIRETIVA | `nivel_autonomia_concedido`, `prazo` |
| HANDOFF | `estado_do_trabalho`, `o_que_falta`, `criterio_de_devolucao` |
| REPORTE | `estado`, `evidencia`, `desvios`, `nao_entregue` |
| CONSULTA | `pergunta_precisa`, `decisao_que_depende_disso` |
| ALERTA | `severidade`, `norma_ou_risco`, `efeito_atual`, `acao_imediata_tomada` |

### 3.3 Regra do pedido unico
Se o corpo precisar de "e tambem", "aproveitando" ou "de quebra", ha mais de um pedido. A
mensagem e dividida. Pedidos empacotados destroem a rastreabilidade do aceite.

## 4. Contrato de Handoff

Handoff e o instrumento mais critico do sistema: e onde o contexto se perde e onde a
responsabilidade fica orfa. Por isso e contrato, nao aviso.

### 4.1 Clausulas obrigatorias

| Clausula | Pergunta que responde |
|---|---|
| **Objeto** | O que exatamente esta sendo transferido? |
| **Estado** | Em que ponto o trabalho esta agora? |
| **Feito** | O que ja foi concluido e verificado? |
| **Nao feito** | O que falta, e o que foi deliberadamente deixado de fora? |
| **Decisoes tomadas** | Que escolhas ja estao fechadas e nao devem ser reabertas? (por ID) |
| **Decisoes em aberto** | O que o receptor precisa decidir? |
| **Premissas** | O que se assumiu sem confirmar? |
| **Riscos conhecidos** | O que pode dar errado, e o que ja se sabe sobre isso? |
| **Criterio de aceite** | Como o receptor sabe que terminou? |
| **Criterio de devolucao** | Em que condicao o receptor pode recusar o handoff? |
| **Contexto minimo** | Quais referencias sao necessarias — e somente elas (CM-04). |

### 4.2 Ciclo do handoff

```
EMISSAO -> RECEPCAO -> [ ACEITE   -> responsabilidade transferida
                       [ DEVOLUCAO -> responsabilidade permanece com o emissor
                       [ SILENCIO  -> responsabilidade permanece com o emissor (CM-07)
```

| # | Regra |
|---|---|
| HO-01 | **Silencio nunca transfere responsabilidade.** Sem aceite explicito, o dono continua sendo o emissor. |
| HO-02 | Devolucao exige motivo em uma das categorias: escopo insuficiente, contexto insuficiente, fora do dominio do receptor, conflito com norma, dependencia nao resolvida. |
| HO-03 | Handoff devolvido duas vezes pelo mesmo motivo escala a DEP-EXE — ha defeito de fronteira (FND-02 §9.2). |
| HO-04 | Handoff que atravessa portao QG so e emitido apos a liberacao do portao. |
| HO-05 | Handoff que apenas transporta, sem transformar o trabalho, e sinal de consolidacao (FND-02 §9.3). |

## 5. Pacote de Contexto

Instrumento de DEP-KMS para entregar contexto sem inundar o destinatario. Aplica CM-04 e
PI-14 (reducao de contexto).

| Camada do pacote | Conteudo | Regra |
|---|---|---|
| **Nucleo** | O minimo indispensavel para agir corretamente | Sempre enviado, sempre curto |
| **Suporte** | Referencias por ID, consultaveis sob demanda | Enviado como lista, nunca como conteudo |
| **Historico** | O que ja foi tentado e por que nao serviu | Enviado quando ha risco de repetir erro |
| **Fronteira** | O que esta fora do escopo e nao deve ser tocado | Sempre enviado |

### 5.1 Regras do pacote
| # | Regra |
|---|---|
| PC-01 | Contexto e **curado**, nao despejado. Enviar tudo e falha de curadoria, nao zelo. |
| PC-02 | Todo item do nucleo justifica sua presenca: se a tarefa nao o usa, ele nao entra. |
| PC-03 | Contexto tem proveniencia: cada afirmacao aponta a origem (PI-03). |
| PC-04 | Contexto que precisa ser reconstruido pelo receptor indica handoff mal formado, e o receptor deve devolver (HO-02). |
| PC-05 | Pacote recorrente para o mesmo tipo de tarefa vira Skill (FND-02 §9.1, degrau 2). |

## 6. Reporte de Resultados

### 6.1 Estrutura obrigatoria

```markdown
## Estado
concluido | concluido-com-ressalva | parcial | bloqueado | cancelado

## Entregue
O que foi produzido, com localizacao por ID ou caminho.

## Evidencia
Como se sabe que funciona: verificacao, saida, teste, fonte. (DoD-5)

## Nao entregue
O que estava no escopo e nao foi feito — e por que. (PI-10)

## Desvios
Onde a execucao divergiu do que foi pedido ou aprovado, e sob qual autorizacao.

## Decisoes tomadas
Escolhas feitas durante a execucao, com o ID do registro correspondente.

## Riscos e pendencias
O que fica em aberto e quem passa a ser o dono disso.

## Aprendizado
O que a proxima ocorrencia deste trabalho deveria saber. (alimenta camada APR)
```

### 6.2 Regras de reporte

| # | Regra |
|---|---|
| RP-01 | Reporte sem secao **Evidencia** e invalido. "Feito" nao e evidencia (DoD-5, LV-05). |
| RP-02 | Reporte sem secao **Nao entregue** presume escopo integral. Se algo ficou de fora e nao foi declarado, e violacao de PI-10. |
| RP-03 | Estado `concluido` exige verificacao independente ja realizada (QG-3). Sem ela, o estado e `concluido-com-ressalva`. |
| RP-04 | `bloqueado` exige nomear o bloqueio, o dono do desbloqueio e o que ja foi tentado. |
| RP-05 | Reporte de trabalho encerrado sem secao **Aprendizado** nao fecha QG-5. |
| RP-06 | Reporte otimista desmentido depois gera incidente de conformidade. |

### 6.3 Reporte ao Soberano
Consolidado por DEP-EXE, com regras adicionais:

| # | Regra |
|---|---|
| SB-01 | Comeca pelo que exige decisao humana, nao pelo que foi feito. |
| SB-02 | Separa **fato verificado** de **estimativa** de forma explicita. |
| SB-03 | Toda decisao Tipo 1 pendente aparece com alternativas e recomendacao — nunca so a pergunta. |
| SB-04 | Ma noticia vem antes de boa noticia (CM-08). |
| SB-05 | Nao contem credencial, dado sensivel ou segredo em texto (PI-08). |

## 7. Escalonamento

### 7.1 Niveis

| Nivel | Gatilho | Escala para | Prazo |
|---|---|---|---|
| **E0** | Duvida rotineira, resolvivel por premissa declarada | Ninguem — decide e registra a premissa | Imediato |
| **E1** | Bloqueio dentro do proprio dominio | Proprietario do dominio | Mesmo ciclo |
| **E2** | Conflito de escopo, prioridade ou recurso entre areas | DEP-EXE | Mesmo ciclo |
| **E3** | Duvida de conformidade, qualidade ou risco | DEP-GOV / DEP-QAR | Imediato, bloqueante |
| **E4** | Decisao Tipo 1, norma, portfolio, dado vivo, credencial | SOBERANO | Imediato, bloqueante |

### 7.2 Regras

| # | Regra |
|---|---|
| EC-01 | Escalar e obrigacao, nao fraqueza. Improvisar em materia de E3/E4 e violacao (PI-09). |
| EC-02 | Escalonamento nao pula nivel, **exceto** violacao de Linha Vermelha, que vai direto a E4. |
| EC-03 | Toda escalada carrega: o que se tentou, o que se sabe, quais as opcoes, qual a recomendacao. Escalada sem recomendacao e devolvida. |
| EC-04 | Escalonamento E3/E4 **bloqueia a execucao** ate haver resposta explicita (CM-07). |
| EC-05 | O mesmo tema escalado repetidamente indica norma ausente ou fronteira mal desenhada; DEP-GOV abre proposta de ajuste. |

## 8. Cadencias

Ritmos fixos da organizacao. Cadencia nao substitui comunicacao por evento — organiza-a.

| Cadencia | Quando | Quem | Produz |
|---|---|---|---|
| **Abertura de ciclo** | Inicio de cada ciclo de trabalho | DEP-EXE | Prioridades, alocacao, portao QG-0 |
| **Sincronizacao de linha** | Durante o ciclo | Areas de Linha | Estado, bloqueios, dependencias |
| **Revisao de qualidade** | Ao concluir entregavel | DEP-QAR | Parecer, defeitos, veto ou liberacao |
| **Fechamento de ciclo** | Fim de cada ciclo | DEP-EXE + DEP-GOV | Reporte ao Soberano, auditoria, excecoes vencidas |
| **Colheita de aprendizado** | Fim de cada ciclo | DEP-KMS | Registros na camada APR, QG-5 |
| **Revisao estrutural** | Fim de horizonte, min. semestral | DEP-GOV + DEP-EXE + DEP-KMS | Proposta de especializacao ou consolidacao (PI-14) |
| **Revisao da Fundacao** | Semestral | DEP-GOV + SOBERANO | Emendas propostas, aderencia verificada |

**Regra:** ciclo nao fecha com portao pendente sem excecao formal, nem com aprendizado nao
colhido.

## 9. Registro da Comunicacao

| O que | Registra? | Onde | Retencao |
|---|---|---|---|
| DIRETIVA | Sim | Memoria Operacional | Ate o ciclo fechar; decisao embutida promove-se |
| HANDOFF | Sim | Memoria Operacional | Ate aceite + conclusao |
| REPORTE de entrega | Sim | Memoria Operacional; aprendizado promove-se a APR | Ciclo |
| CONSULTA com parecer relevante | Sim | Camada correspondente ao tema | Enquanto o parecer valer |
| ALERTA | **Sempre** | Memoria Operacional; incidente vai a `governance/incidents/` | Permanente |
| Decisao contida em qualquer mensagem | **Sempre** | ADR ou Nota de Decisao | Permanente |
| Conversa exploratoria sem conclusao | Nao | — | — |

### 9.1 Regra de promocao
Mensagem que contem **decisao, aprendizado ou fato duravel** nao permanece como mensagem:
e promovida ao instrumento proprio (ADR, registro de memoria) por DEP-KMS. Decisao que fica
so na mensagem viola PI-04.

### 9.2 Regra de nao duplicacao
Mensagem referencia por ID (CM-09). Conteudo recolado em mensagem cria segunda fonte de
verdade e e erro de conformidade (FND-03 §7.1).

## 10. Comunicacao Externa

| Regra | Detalhe |
|---|---|
| EX-01 | Toda comunicacao para fora do sistema passa por DEP-GRW (forma) e DEP-QAR (risco). |
| EX-02 | Publicacao externa exige aprovacao explicita do Soberano (LV-08). Nao ha delegacao. |
| EX-03 | Envio de dado a servico externo e ato de exposicao: exige autorizacao especifica para aquele envio, nao autorizacao geral. |
| EX-04 | Nenhuma comunicacao externa contem credencial, dado sensivel ou informacao nao verificada (PI-08, LV-12). |
| EX-05 | O que sai para fora e arquivado internamente, com data e autorizacao correspondente. |

## 11. Aplicacao a Agentes (fase futura)

Este framework foi escrito para valer sem alteracao quando existirem agentes. Quando
chegarem, aplicam-se adicionalmente:

| # | Regra |
|---|---|
| AG-01 | Agente se comunica pelos mesmos cinco canais, com o mesmo envelope. |
| AG-02 | Agente nunca opera acima do `nivel_autonomia_concedido` na mensagem, ainda que sua Carta permita mais. |
| AG-03 | Agente que recebe pedido fora do proprio escopo devolve (HO-02); nao executa por conveniencia (PI-09). |
| AG-04 | Subagente comunica-se com o agente pai, nao com outros departamentos. |
| AG-05 | Contexto entregue a agente segue o Pacote de Contexto (§5): nucleo curto, suporte por referencia. |
| AG-06 | Reporte de agente segue §6 integralmente, inclusive **Nao entregue** e **Evidencia**. |

---

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-GOV | Framework inicial: 5 canais, envelope padrao, contrato de handoff, 5 niveis de escalonamento. Ratificado por ADR-0001. |
