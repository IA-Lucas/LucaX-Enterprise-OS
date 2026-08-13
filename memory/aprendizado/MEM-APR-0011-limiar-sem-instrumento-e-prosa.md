---
id: MEM-APR-0011-limiar-sem-instrumento-e-prosa
titulo: Limiar sem instrumento e prosa — a norma que escreve MEDIDO sem nomear quem mede nao dispara nunca
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
origem: Onda 7 — aproveitamento por merito do lucaX (plano F50 §3 item 1, Oficina), ordem do Fundador de 2026-08-13; precedente A-013 (com o padrao anterior A-009) do acervo do lucaX, fonte lida integral em somente-leitura na admissao
evidencia: o master do lucaX escrevia o gatilho do harness externo como '$20/mes de EXECUCAO, MEDIDO, nao estimado' — e nenhum script convertia o usage real em dolar nem separava por modelo/periodo para checar contra o limiar; a lei era so prosa ate gatilho_harness.py nascer (A-013), mesmo padrao ja registrado em A-009
confianca: alta
ocorrencias: 2
ttl: permanente
aplica_se_a: [global]
resumo: Registra que norma com limiar numerico so existe operacionalmente quando nomeia o instrumento que computa o numero que a alimenta; limiar escrito sem medidor nao dispara nunca — e distinto do MEM-APR-0006, onde o instrumento existe e o defeito aparece ao exercita-lo.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# Limiar sem instrumento e prosa

## A licao

Norma com limiar numerico ("dispara quando X passar de N") so existe
operacionalmente quando **nomeia o instrumento que computa X**. Sem o medidor, o
limiar nao dispara nunca — nao porque a condicao nao ocorra, mas porque ninguem
a ve ocorrer. A lei escrita sem instrumento e prosa com aparencia de controle.

## A evidencia, medida

No lucaX (A-013, 2026-07-13), o master §15 escrevia o gatilho do harness
externo com enfase: *"$20/mes de EXECUCAO, **MEDIDO**, nao estimado"*. A palavra
MEDIDO estava na norma; **o medidor nao existia** — nenhum script convertia o
usage real em dolar nem separava por modelo/periodo para checar o limiar. A lei
ficou prosa ate `gatilho_harness.py` nascer. O proprio precedente anota: mesmo
padrao de A-009 — **duas ocorrencias** do mesmo buraco na mesma semana.

## A condicao fina

Esta licao e **distinta e complementar** ao
[MEM-APR-0006](MEM-APR-0006-exercer-o-contador-revela-o-defeito.md): la o
instrumento **existe** e o defeito so aparece ao **exercita-lo**; aqui o
instrumento **nao existe** e a norma finge que sim. A sequencia sa e: limiar
nasce com medidor nomeado (esta licao) e o medidor e exercido, nao so lido
(0006). Ha eco vivo na regra da Nota de medicao do proprio acervo: instrumento
vigente com sha256 declarado, nao "a baseline" abstrata.

## Acao com dono

Toda norma nova da Mente com limiar numerico aponta o instrumento que mede —
nome, caminho e o que ele computa (`DEP-GOV` na admissao; `DEP-QAR` confere no
FIT). No Corpo, o exemplo positivo ja e norma de fato: o teto de tokens nasceu
COM sentinela e margem medida, nunca como frase (`DEP-EXE`).

## Gatilho de refutacao

Limiar deliberadamente qualitativo (juizo humano declarado como criterio) nao
refuta — a licao vale para limiar que se declara NUMERICO e MEDIDO.
