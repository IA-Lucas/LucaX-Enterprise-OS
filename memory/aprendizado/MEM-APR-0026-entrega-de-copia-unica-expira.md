---
id: MEM-APR-0026-entrega-de-copia-unica-expira
titulo: Entrega de copia unica expira — repositorio sem remoto precisa de segunda custodia ou lacuna explicita
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
origem: Onda 7 — dedupe F53 da Oficina; precedente A-297 do lucaX, fonte lida integral em somente-leitura e comparada com o Hub atual do Corpo
evidencia: repositorio separado, backup do split e ambiente local existiam apenas num caminho sem remoto e ficaram ausentes apos mudanca de arvore; o Hub atual mede a mesma classe em seis produtos sem origin e declara posicao contra remoto como desconhecida
confianca: alta
ocorrencias: 2
ttl: permanente
aplica_se_a: [global]
resumo: Registra que commit local prova historia, nao durabilidade; entrega com um unico exemplar precisa de segunda custodia verificavel ou deve aparecer como lacuna com dono, sem fingir que esta publicada ou perdida.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# Entrega de copia unica expira

## A licao

Commit local protege contra edicao acidental, mas nao contra perda ou ausencia da maquina.
Uma entrega com um unico exemplar precisa de **segunda custodia verificavel**; sem ela, o
estado correto e lacuna explicita, nao “publicado” nem “perdido”.

## A evidencia, medida

No `A-297`, repositorio separado, backup do split e ambiente local viviam num unico caminho
sem remoto e ficaram ausentes depois da mudanca da arvore. No projeto novo, o Hub encontra
seis produtos sem `origin` e responde corretamente que a posicao contra remoto **nao se
sabe**, em vez de inventar “em dia”.

## A condicao fina

Segunda custodia pode ser remoto, backup externo verificado ou bundle em outra sede. Criar
remoto e publicar continuam atos do Fundador; a licao nao amplia essa autoridade. Ausente
nesta maquina tambem nao significa perdido — exige medir a outra custodia.

## Acao com dono

O Hub mantem procedencia e estado de remoto por repositorio (`DEP-EXE`). Entrega de repositorio
sem segunda custodia fica na mesa do Fundador com dono e nao fecha como duravel (`DEP-GOV`).

## Gatilho de refutacao

Uma sede cujo armazenamento unico tenha durabilidade e restauracao independentemente
provadas pode satisfazer a segunda custodia; a afirmacao do provedor sem ensaio nao basta.
