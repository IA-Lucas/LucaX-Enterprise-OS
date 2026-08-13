---
id: MEM-APR-0021-metrica-cumulativa-prova-monotonicidade
titulo: Metrica cumulativa prova monotonicidade — campo instantaneo nao pode responder pela sessao
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
origem: Onda 7 — dedupe F53 da Oficina; precedente A-116 do lucaX, fonte lida integral em somente-leitura
evidencia: total_output_tokens mudou de comportamento e caiu de 3726 para 4 entre duas chamadas da mesma sessao; o painel o tratava como acumulado e produzia um contador que diminuia
confianca: alta
ocorrencias: 1
ttl: permanente
aplica_se_a: [global]
resumo: Registra que grandeza declarada acumulada exige teste de monotonicidade e identidade de sessao; campo instantaneo ou sem semantica versionada nao pode ser somado como total.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# Metrica cumulativa prova monotonicidade

## A licao

Se um numero se declara acumulado, **nao pode cair dentro da mesma identidade de sessao**.
Nome historico de campo e documentacao anterior nao substituem essa propriedade.

## A evidencia, medida

No `A-116`, `total_output_tokens` caiu de **3726 para 4** entre chamadas reais da mesma
sessao apos mudanca da CLI. O painel somava o valor como total, embora ele tivesse se
tornado instantaneo. O defeito so apareceu ao comparar a sequencia, nao uma amostra.

## A condicao fina

Compactacao pode reduzir tamanho de janela e reinicio pode abrir nova serie; ambos precisam
de evento/identidade explicitos. A monotonicidade vale dentro do intervalo declarado, nao
universalmente.

## Acao com dono

Toda metrica acumulada tem teste com duas observacoes diferentes, re-render identico e duas
identidades isoladas (`DEP-ENG`). Se a fonte nao garante semantica cumulativa, o Corpo
acumula eventos idempotentes ou renomeia a grandeza (`DEP-QAR`).

## Gatilho de refutacao

Uma grandeza acumulada legitimamente decrescente sem mudanca de janela ou identidade exige
redefinir o termo; enquanto isso, a queda refuta a medicao.
