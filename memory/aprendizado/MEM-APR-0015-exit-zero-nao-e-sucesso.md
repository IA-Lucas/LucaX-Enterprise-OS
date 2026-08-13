---
id: MEM-APR-0015-exit-zero-nao-e-sucesso
titulo: Exit 0 nao e sucesso — rodada automatica so termina bem com artefato materializado ou ausencia declarada
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
origem: Onda 7 — fila de admissao da triagem F51 (Oficina, ordem do Fundador de 2026-08-13, "tudo autorizado"); precedente ADR-067 do lucaX, fonte lida integral em somente-leitura na admissao
evidencia: o launcher diario do scout passava o despacho como argumento de claude -p; o texto truncava sem erro, o modelo pedia confirmacao, o CLI saia com codigo 0 e o Task Scheduler registrava sucesso SEM pesquisa nem entrega (medido em 23/07/2026); a correcao — despacho por stdin + gate de artefato (briefing.json OU status.md 'SEM POST HOJE', ausencia dos dois = exit 1 propagado) — produziu 5/5 aprovados no mesmo dia e rodada automatica limpa no dia seguinte
confianca: alta
ocorrencias: 1
ttl: permanente
aplica_se_a: [global]
resumo: Registra que codigo de saida zero e necessario e nao suficiente para automacao headless: sucesso exige artefato materializado OU declaracao explicita de ausencia, e a falta dos dois vira falha propagada ao agendador; e o controle positivo aplicado a rodada automatica.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# Exit 0 nao e sucesso

## A licao

Em automacao headless, **codigo de saida 0 e necessario, nunca suficiente**.
O processo pode morrer de um jeito que nenhum componente considera erro — e o
agendador registra sucesso sobre o nada. Rodada so termina bem com **artefato
materializado** ou **ausencia explicitamente declarada**; a falta dos dois e
falha, e falha se propaga.

## A evidencia, medida

No lucaX (ADR-067, 2026-07-23): o despacho do scout diario entrava como
*argumento* de `claude -p`; argumento longo truncava **sem erro**, o modelo
pedia confirmacao a um terminal sem ninguem, o CLI saia com 0 e o Task
Scheduler registrava `LastTaskResult = 0` — **sem pesquisa nem entrega**. A
correcao: despacho por **stdin**, e um gate de artefato — a rodada so e sucesso
se materializar `briefing.json` OU o contrato explicito `status.md` com "SEM
POST HOJE"; ausencia dos dois = `exit 1` propagado. No dia seguinte, a rodada
automatica real produziu 4 briefings sem intervencao.

## A condicao fina

O contrato tem dois lados e os dois importam: exigir artefato barra o falso
sucesso, e **a ausencia declarada ("SEM POST HOJE") e resultado legitimo** —
sem ela, o gate forcaria producao vazia para "ter artefato", que e o defeito
oposto. E o controle positivo aplicado a automacao: zero de instrumento morto e
indistinguivel de zero real, entao o sucesso precisa deixar prova positiva.

## Acao com dono

Toda rodada automatica do ecossistema (Task Scheduler, cron, headless) define
no proprio contrato qual artefato prova sucesso e qual declaracao prova
ausencia — e propaga falha na falta dos dois (`DEP-EXE`); a suite trava
transporte, gate e propagacao, como a fonte fez (`DEP-QAR`).

## Gatilho de refutacao

Processo cujo efeito e externo e nao-materializavel (ex.: side-effect remoto
sem recibo) exigiria recibo proprio — se um caso legitimo nao puder deixar
prova nem declaracao, a regra se refina ali.
