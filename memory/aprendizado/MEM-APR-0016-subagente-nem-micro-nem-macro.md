---
id: MEM-APR-0016-subagente-nem-micro-nem-macro
titulo: Subagente nem micro nem macro — abaixo do corte e desperdicio de boot, acima da carga destilada e degradacao importada
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
origem: Onda 7 — fila de admissao da triagem F51 (Oficina, ordem do Fundador de 2026-08-13, "tudo autorizado"); precedente ADR-058 do lucaX, fonte lida integral em somente-leitura na admissao
evidencia: a analise de eficiencia do lucaX mediu as duas armadilhas: subagente para tarefa minuscula paga ~12-15K tokens so de inicializacao (system prompt + varredura de ambiente), custando mais que a execucao direta por codigo; e despacho com historico extenso nao-destilado reproduz no subagente a mesma degradacao de janela que ele existia para evitar; a escada de custo resultante: niveis 0-2 zero token (codigo), nivel 3 subagente com carga destilada, nivel 4 julgamento
confianca: media
ocorrencias: 1
ttl: permanente
aplica_se_a: [global]
resumo: Registra o corte dos dois lados do despacho de subagente: proibido para tarefa deterministica que codigo resolve (overhead de boot supera o trabalho), e todo despacho carrega so contexto destilado (caminhos + objetivo, nunca despejo de historico) com ferramentas minimas — a janela que o subagente protege nao pode ser reproduzida dentro dele.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# Subagente nem micro nem macro

## A licao

O despacho de subagente tem **corte nos dois lados**:

- **Micro:** disparar LLM para tarefa deterministica (checar 1 arquivo, 1 grep)
  paga o boot inteiro — system prompt, varredura de ambiente — para fazer o que
  um script resolve em zero token. Abaixo do corte, **codigo, nao agente**.
- **Macro:** despejar historico nao-destilado no despacho reproduz **dentro** do
  subagente a degradacao de janela que ele existia para evitar. A carga e
  destilada: caminhos estritamente necessarios + objetivo direto + ferramentas
  minimas.

## A evidencia, medida

Analise de eficiencia do lucaX (ADR-058, 2026-07-22): overhead de inicializacao
de subagente estimado em **~12-15K tokens** antes de qualquer trabalho util —
tarefa pequena custa mais em boot que em execucao; e despacho com historico
extenso degrada o raciocinio do subagente do mesmo modo que degradaria a janela
mae. A escada de custo resultante ficou norma la: niveis 0-2 (acervo, scripts,
nucleo) **zero token**; nivel 3 (volumoso + julgamento) subagente com carga
destilada, paga 1x e morre la; nivel 4 modelo/agente especifico.

## A condicao fina

O corte micro nao proibe subagente para tarefa *pequena e de julgamento* —
proibe para tarefa *deterministica*; o criterio e "codigo resolve?", nao
tamanho. E carga destilada nao e carga minima a qualquer custo: o que o
subagente PRECISA para nao inventar contexto viaja junto — destilar e
selecionar, nao amputar. Confianca `media`: a fonte e analise de eficiencia com
numeros de ordem de grandeza, nao incidente medido em log proprio — promover a
`alta` exige medicao de despacho real do ecossistema atual.

## Acao com dono

Convocacao no ecossistema segue a escada: deterministico resolve em codigo
antes de virar despacho (`DEP-EXE` — e a familia de convocacao-por-necessidade
do Corpo); todo prompt de despacho carrega caminhos + objetivo, nunca colagem
de historico (`DEP-EXE`); revisao de custo confere a escada nas missoes
(`DEP-QAR`).

## Gatilho de refutacao

Medicao real do ecossistema atual mostrando overhead de boot muito distinto de
~12-15K, ou caso em que despacho com historico integral supere o destilado em
qualidade E custo — qualquer dos dois reabre a calibragem (nao o principio).
