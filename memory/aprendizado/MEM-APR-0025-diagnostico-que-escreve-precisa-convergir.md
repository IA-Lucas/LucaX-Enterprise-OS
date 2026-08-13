---
id: MEM-APR-0025-diagnostico-que-escreve-precisa-convergir
titulo: Diagnostico que escreve precisa convergir — medir nao pode consumir o recurso finito que verifica
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
origem: Onda 7 — dedupe F53 da Oficina; precedente A-296 do lucaX, fonte lida integral em somente-leitura
evidencia: conferir_deploy criava credencial aleatoria a cada rodada num plano com teto de 5; a primeira auditoria ocupou a quinta vaga e imprimiu Tudo passou no ato em que fechava o cadastro, enquanto a segunda recebeu 402
confianca: alta
ocorrencias: 1
ttl: permanente
aplica_se_a: [global]
resumo: Registra que ferramenta de diagnostico com escrita declara recurso consumido, usa identidade idempotente e prova por contagem que repeticao converge; verde produzido enquanto a sonda causa dano e falso sucesso.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# Diagnostico que escreve precisa convergir

## A licao

Ferramenta de diagnostico que escreve nao e observadora neutra. Ela precisa declarar o que
consome e provar que a segunda execucao **converge**, em vez de acumular efeito.

## A evidencia, medida

No `A-296`, cada conferencia criava uma credencial aleatoria num plano com teto de **5**.
A primeira rodada ocupou a quinta vaga e imprimiu “Tudo passou”; a segunda recebeu **402**.
Quem mediu fechou o produto que pretendia conferir.

## A condicao fina

Sonda pode escrever quando o contrato exige prova ponta a ponta. Nesse caso usa identidade
fixa, limpa com garantia ou mede antes/depois o recurso. `409` por objeto ja existente pode
ser sucesso idempotente se o contrato o declarar.

## Acao com dono

Toda sonda com escrita lista efeitos e limites e tem teste de duas execucoes contando estado
antes/depois (`DEP-ENG`). `DEP-QAR` rejeita “verde” que nao inclui o custo material da propria
medicao.

## Gatilho de refutacao

Uma sonda destrutiva por natureza pode ser aceita em ambiente descartavel explicitamente
isolado; nunca contra o recurso vivo que ela julga.
