---
id: MEM-APR-0017-handoff-urgente-nasce-na-sessao-viva
titulo: Handoff urgente nasce na sessao viva — processo cego automatiza formulario, nao contexto
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
origem: Onda 7 — fila de admissao da triagem F51 (Oficina, ordem do Fundador de 2026-08-13, "entao vamos terminar a onda 7"); precedente ADR-066 do lucaX, fonte lida integral em somente-leitura na admissao
evidencia: o controlador de contexto do lucaX cruzava 120k tokens e chamava um handoff headless; por contrato, o processo nao via o despacho original nem conseguia escrever o resumo executivo, e a serie chegou a 14+ handoffs cegos consecutivos ate 2026-07-23; a correcao conservou o limiar e trocou o executor pela sessao viva, solicitada uma unica vez por hook
confianca: alta
ocorrencias: 1
ttl: permanente
aplica_se_a: [global]
resumo: Registra que handoff cujo valor depende do contexto vivo nao pode ser delegado a processo que nao enxerga esse contexto; o automato mede e sinaliza, e a sessao que viveu o trabalho materializa despacho e resumo. Automacao continua valida quando o contrato de entrada e integralmente fornecido.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# Handoff urgente nasce na sessao viva

## A licao

Quando o valor do handoff e explicar **o que aconteceu nesta conversa**, processo
headless sem essa conversa so consegue automatizar o formulario. Ele nao produz
despacho original nem resumo executivo verdadeiros.

## A evidencia, medida

No lucaX (ADR-066, 2026-07-24), o controlador cruzava o limiar de **120k**
tokens e disparava `claude -p` para produzir o handoff. O processo nao via a
janela da sessao e, por contrato, deixava vazias as duas secoes de maior valor.
Houve **14+ handoffs cegos consecutivos** ate 2026-07-23. A correcao manteve o
limiar: o controlador apenas classifica `normal`/`aviso`/`urgente`, e um hook
pede UMA vez que a **sessao viva** execute a skill e solicite nova sessao.

## A condicao fina

Isto nao proibe automacao de handoff: ela e apropriada se todo o contrato de
entrada ja existe, e verificavel, fora da conversa. Aplica-se quando o produto
do handoff depende de contexto experiencial que o processo nao recebe. A sessao
abandonada apos o limiar continua sendo custo declarado; inventar resumo cego
para cobrir esse caso custa mais que declarar a lacuna.

## Acao com dono

Todo limite automatico de contexto mede, registra o nivel e **sinaliza** a
sessao que possui o contexto; essa sessao materializa o handoff completo antes
de encerrar (`DEP-EXE`). `DEP-QAR` testa tanto a instrucao unica por sessao
quanto a presenca de despacho e resumo no resultado.

## Gatilho de refutacao

Um handoff composto por dados completos e verificaveis, entregue por processo
headless sem perda de informacao material, delimita a excecao e preserva a
automacao naquele contrato.
