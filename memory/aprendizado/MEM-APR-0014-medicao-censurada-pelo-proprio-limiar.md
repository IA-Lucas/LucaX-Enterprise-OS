---
id: MEM-APR-0014-medicao-censurada-pelo-proprio-limiar
titulo: Medicao censurada pelo proprio limiar — log que so grava acima do corte transforma qualquer taxa em tautologia
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
origem: Onda 7 — fila de admissao da triagem F51 (Oficina, ordem do Fundador de 2026-08-13, "tudo autorizado"); precedente ADR-080 do lucaX, fonte lida integral em somente-leitura na admissao
evidencia: o juiz do lucaX so gravava a linha quando tokens >= 60.000: o log tinha 105 eventos e o MINIMO era 60.098 — 'teto violado por 100% das chamadas' era tautologia, o denominador nunca entrou no arquivo; recalibrar p90 sobre essa amostra daria o p90 dos estouros (sensor que nunca dispara = sensor desligado); de quebra, o teto por agente nunca resolveu uma vez (105/105 no fallback) e o campo que ele leria significava OUTRA coisa (teto: = tamanho do CLAUDE.md, deriva +7.400% se casasse)
confianca: alta
ocorrencias: 1
ttl: permanente
aplica_se_a: [global]
resumo: Registra que instrumento que so registra eventos acima do proprio limiar produz taxa de violacao tautologica e recalibracao viciada; medicao exige denominador — grava-se TODA ocorrencia mediavel com flag de estouro separando aviso de medicao, e calibracao recusa amostra censurada; nome de campo com semantica dupla e parte do mesmo buraco.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# Medicao censurada pelo proprio limiar

## A licao

Instrumento que **so grava o que passa do limiar** nao mede o limiar — mede a
propria censura. Toda taxa calculada sobre esse log ("violado por 100%") e
tautologia: o denominador — as ocorrencias que couberam — nunca entrou no
arquivo. E recalibrar o limiar a partir dessa amostra fixa o corte no p90 dos
estouros: um sensor que nunca dispara, **que e o mesmo que sensor desligado**.

## A evidencia, medida

No lucaX (ADR-080, 2026-07-25): o registro de orcamento de subagente so
escrevia linha quando `tokens >= 60.000`. O log tinha **105 eventos, minimo
60.098** — zero abaixo do corte, por construcao. A memoria institucional ja
dizia "teto de subagente e ficcao" com base nisso. Dois defeitos satelites no
mesmo exame: o teto por agente **nunca resolveu uma vez** (105/105 no
fallback, o lookup nao casava), e o campo que ele leria se casasse — `teto:` —
significava **outra grandeza** (tamanho do CLAUDE.md, 800 tokens): a deriva
sairia +7.400%, e o teste da epoca **certificava o defeito**.

## A condicao fina

A correcao tem tres pernas, e as tres sao desta licao: (1) **grava-se toda
ocorrencia mediavel**, com campo proprio (`estourou`) separando *aviso* de
*medicao*; (2) **calibracao recusa amostra censurada** — menos de N ocorrencias
ou nenhuma abaixo do limiar = sem numero novo (esperar amostra honesta e
decisao, nao omissao); (3) **um nome, uma grandeza, um dono** — campo com
semantica dupla e o mesmo buraco por outra porta. Complementar ao
[MEM-APR-0011](MEM-APR-0011-limiar-sem-instrumento-e-prosa.md): la a norma nao
tinha medidor; aqui o medidor existe e vicia a amostra.

## Acao com dono

Sensores de custo do Corpo gravam toda chamada mediavel, nao so o estouro
(`DEP-EXE` — o gate de deriva do E7.S ja nasceu com medicao pareada na trilha);
qualquer recalibracao de limiar na Mente ou no Corpo exige declarar o
denominador da amostra (`DEP-QAR` no FIT).

## Gatilho de refutacao

Registro deliberadamente amostrado por custo (gravar 1 em N, declarado) nao
refuta — a licao e sobre censura NO limiar que se quer medir, nao sobre
amostragem declarada.
