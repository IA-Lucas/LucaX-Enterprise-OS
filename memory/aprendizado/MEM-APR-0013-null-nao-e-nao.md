---
id: MEM-APR-0013-null-nao-e-nao
titulo: Null nao e nao — decisao vazia e portao aberto sem ninguem na porta, nunca recusa
tipo: memoria
versao: 1.0.0
status: ativo
camada_memoria: aprendizado
autor: DEP-KMS
proprietario: DEP-KMS
aprovador: DEP-KMS
criado_em: 2026-08-13
atualizado_em: 2026-08-13
revisao_prevista: 2027-02-13
decisoes_relacionadas: []
substitui: []
substituido_por: null
origem: Onda 7 — fila de admissao da triagem F51 (Oficina, ordem do Fundador de 2026-08-13, "tudo autorizado"); precedente ADR-079 do lucaX, fonte lida integral em somente-leitura na admissao
evidencia: o portao de ativacao do lucaX tinha 9 candidatos com 5 gates cada; 8 estavam com decisao null e o proprio ADR nomeia o estado — 'null nao e nao: e portao aberto sem ninguem na porta'; o CEO, diante da escolha entre negar em bloco e decidir item a item, decidiu os 8 item a item no mesmo dia, e a colisao do redis_kv com dois gates abertos foi resolvida fechando os gates NO MESMO lote em vez de pular degrau
confianca: alta
ocorrencias: 1
ttl: permanente
aplica_se_a: [global]
resumo: Registra que campo de decisao vazio nao equivale a recusa: e ausencia de decisao com aparencia de estado, e todo pendente exige dono e estado explicito (aprovado, recusado, ou devolvido a quem decide); a resolucao sa e item a item, com colisao de gate fechada no mesmo lote, nunca pulando degrau.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# Null nao e nao

## A licao

Campo de decisao vazio **nao e recusa** — e portao aberto sem ninguem na porta.
O sistema que trata `null` como "nao ativado" esta confundindo *ausencia de
decisao* com *decisao negativa*, e opera com um estado que ninguem tomou.

## A evidencia, medida

No portao de ativacao do lucaX (ADR-079, 2026-07-25), **8 de 9 candidatos**
estavam com `decisao: null` — e o proprio registro nomeia o estado com todas as
letras: *"null nao e 'nao': e portao aberto sem ninguem na porta"*. Chamado a
decidir, o CEO recusou o "nao ativar em bloco" e decidiu **item a item**, cada
um com escopo escrito e criterio de desligamento. Quando um pedido (redis_kv)
colidiu com dois gates ainda abertos, a saida nao foi pular degrau nem negar o
pedido: **ativar E fechar os dois gates no mesmo lote** — o contrato deixa de
mentir sem que a ordem seja desobedecida.

## A condicao fina

O oposto de `null` nao e "sim": e **estado explicito com dono** — aprovado,
recusado, ou *devolvido nominalmente a quem decide* (o proprio ADR-079 devolve
`mag_real` ao Conselho e a lista do notebooklm ao CEO, e diz que nenhum dos
dois e decisao fechada). Pendencia declarada com dono e estado legal; vazio
silencioso, nunca. E a fibra do [MEM-APR-0008](MEM-APR-0008-campo-obrigatorio-com-escape-vazio.md)
aplicada a decisao: o escape devolve, nao aceita.

## Acao com dono

Toda lista de decisao da Mente (roadmap `[!]`, filas do Fundador, gates de
ativacao no Corpo) carrega estado explicito por item — `null`/em branco conta
como ABERTO e aparece em conferencia, nunca como recusado (`DEP-GOV`). No
Corpo, gate sem decisao falha fechado e ruidoso (`DEP-EXE`).

## Gatilho de refutacao

Um caso em que tratar vazio como aberto cause dano maior que trata-lo como
recusa — com medicao — refinaria a regra; a assimetria conhecida hoje aponta
toda para o outro lado.
