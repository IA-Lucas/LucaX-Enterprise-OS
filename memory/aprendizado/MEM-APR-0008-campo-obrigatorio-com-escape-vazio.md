---
id: MEM-APR-0008-campo-obrigatorio-com-escape-vazio
titulo: Campo obrigatorio com escape vazio e falso cumprimento — o campo que aceita o valor que o esvazia
tipo: memoria
versao: 1.0.0
status: ativo
camada_memoria: aprendizado
autor: DEP-KMS
proprietario: DEP-KMS
aprovador: DEP-KMS
criado_em: 2026-08-12
atualizado_em: 2026-08-12
revisao_prevista: 2027-02-12
decisoes_relacionadas: [ADR-0038]
substitui: []
substituido_por: null
origem: Primeira convocacao da F34 (Oficina, missoes/F42-CONVOCACAO-DO-APRENDIZADO.md, licao candidata LC-02), sobre a fila da decisao D4 do Fundador de 2026-08-12
evidencia: 5 de 17 reprovacoes fundamentadas do log veredictos.jsonl levam o motivo literal "nenhuma" — gravadas pelo UNICO julgador que tinha a pratica de fundamentar; as 72 sem motivo algum (100% do outro julgador) dao o tamanho do buraco, contadas a parte e declaradas SEM SENTIDO pela D4; reconto independente bateu digito a digito
confianca: media
ocorrencias: 5
ttl: permanente
aplica_se_a: [global]
resumo: Registra que campo obrigatorio de justificativa que aceita o valor que o esvazia produz veto sem fundamento com carimbo de forma, e fixa a condicao fina — escape legal existe e e DISTINTO de vazio disfarcado, o escape devolve em vez de aceitar — ja materializada no contrato de veredito sao.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# Campo obrigatorio com escape vazio e falso cumprimento

## Proposito
Registrar o defeito de **forma que engole o fundo**: o campo obrigatorio de justificativa que
**aceita o valor que o esvazia**. `"nenhuma"` passa no filtro *"tem motivo?"* — e o veto sai
**sem fundamento com carimbo de forma**, exatamente o que `RQ-3` *("veto sem fundamento e
devolvido")* existe para impedir, driblado pela forma.

## Escopo
| Item | Definicao |
|---|---|
| **Aplica-se a** | todo contrato de saida com **campo obrigatorio de justificativa** |
| **NAO se aplica a** | campo onde a ausencia e **resposta legal declarada** — a `F38` mediu o outro lado: campo obrigatorio **sem** valor legal de escape FORCA confabulacao. **A condicao fina:** o escape legal existe e e **DISTINTO** de vazio disfarcado — `sem-fundamento-declarado` que **devolve** e escape; `"nenhuma"` que **aceita** e fraude de forma |

## Responsaveis
| Papel | Quem |
|---|---|
| Dono do registro | **DEP-KMS** |
| Autor da licao | a primeira convocacao da `F34` *(Oficina, `F42`)*, sob `CAP-aprendizado-organizacional` e `DEP-KMS` `M-4` |
| Verificacao independente | revisao externa por **reconto independente** — bateu digito a digito |

## Situacao
**5** vetos gravados com o motivo literal **`"nenhuma"`** — pelo **unico** julgador que tinha a
pratica de fundamentar. Ao lado, **72** reprovacoes sem motivo algum *(100% do outro julgador)*
dao o tamanho do buraco: **contadas a parte, nunca somadas**, e declaradas `SEM SENTIDO` pela
decisao `D4` do Fundador — **o fundamento perdido nao se reconstroi de memoria**.

## Licao
Obrigatoriedade de **forma** nao garante presenca de **fundo**. Todo campo obrigatorio precisa
de tres coisas para nao virar teatro: **enum do que e resposta valida**, **escape explicito e
legal** para o caso sem-resposta, e **consequencia** para o escape *(devolucao, nunca
aceitacao)*. Sem as tres, o campo mede obediencia, nao verdade.

## Acao que decorre, com dono
**O contrato de veredito sao** — entregue pelo `agentops` na segunda convocacao da `F34`
*(Oficina, `_fabrica/entregas/juiz-para-o-corpo/veredicto.schema.json`)*: enum de motivos com
`"nenhuma"` **banida**, escape `sem-fundamento-declarado` que **so valida com devolucao**
*(if/then executavel)*, e **objeto julgado obrigatorio** — para a proxima fila nao nascer muda.
**Adotar no Corpo e ato da sessao de la.**

## Gatilho de refutacao
O `ADR-018` do legado *(nomeado, nunca lido)* declarar `motivo` **opcional por desenho** — ai a
licao muda de endereco: o defeito seria da regra, nao do campo. Ate la, vale como escrita.
