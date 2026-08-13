---
id: MEM-APR-0019-estado-implantado-nao-e-intencao-local
titulo: Estado implantado nao e intencao local — diagnostico identifica o artefato em execucao antes da causa
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
origem: Onda 7 — dedupe F53 da Oficina; precedente A-031 do lucaX, fonte lida integral em somente-leitura e confrontada com a Mente e o Corpo atuais
evidencia: redeploys repetidos reconstruiram o ultimo commit valido, enquanto a investigacao atribuía o 401 ao codigo/configuracao local; a causa real era autoria local invalida e o artefato servido nao era o que se imaginava diagnosticar
confianca: alta
ocorrencias: 1
ttl: permanente
aplica_se_a: [global]
resumo: Registra que diagnostico de ambiente implantado comeca identificando commit, artefato e configuracao efetivamente executados; estado local e intencao do operador nao provam o estado remoto.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# Estado implantado nao e intencao local

## A licao

Antes de explicar uma falha remota, identifique **qual artefato realmente esta rodando**.
Codigo local, ultimo commit visivel e comando de redeploy expressam intencao; nao provam o
conteudo servido.

## A evidencia, medida

No precedente `A-031`, varias rodadas investigaram variaveis de ambiente e repetiram o
redeploy. O provedor reconstruia o ultimo commit valido, não o commit bloqueado que se
pretendia testar. A causa real era a identidade local do autor; o sintoma observado vinha
de outro artefato.

## A condicao fina

Aplica-se a deploy, job, container ou agente cuja execucao possa apontar para revisao
diferente da arvore local. Nao exige acesso privilegiado ao provedor: hash de ativo,
identificador de build ou caracteristica exclusiva do commit podem provar a identidade.

## Acao com dono

Toda investigacao remota registra URL/alvo, revisao ou hash verificavel e configuracao
efetiva antes de atribuir causa (`DEP-ENG`). O Hub declara quando esse vinculo nao pode ser
medido, em vez de inferir que local e remoto coincidem (`DEP-QAR`).

## Gatilho de refutacao

Um ambiente em que a operacao prove atomicamente que a arvore local e o unico artefato
executavel delimita a excecao; a prova precisa vir do mecanismo, nao da expectativa.
