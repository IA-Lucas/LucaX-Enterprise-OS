---
id: MEM-APR-0020-similaridade-lexical-nao-e-equivalencia
titulo: Similaridade lexical nao e equivalencia — dedupe textual declara o que nao consegue reconhecer
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
origem: Onda 7 — dedupe F53 da Oficina; precedente A-077 do lucaX, fonte lida integral em somente-leitura e confrontada com a regua atual de RAG e dedupe da Mente
evidencia: SequenceMatcher encontrou reformulacao leve e quase copia, mas nao reconheceu um resumo curto do A-067 contra a entrada longa do mesmo assunto; diferenca de comprimento derrubou o pareamento sem negar a equivalencia semantica
confianca: alta
ocorrencias: 1
ttl: permanente
aplica_se_a: [global]
resumo: Registra que similaridade de caracteres e detector de quase copia, nao juiz de equivalencia semantica; limiar, unidade comparada e falsos negativos conhecidos acompanham todo veredito de dedupe.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# Similaridade lexical nao e equivalencia

## A licao

Um algoritmo de similaridade textual responde **quanto duas strings se parecem**. Ele nao
responde se duas formulacoes carregam a mesma regra. Usar seu `nao bateu` como `nao duplica`
transforma limite do instrumento em decisao semantica.

## A evidencia, medida

Em `A-077`, o detector reconheceu pares quase verbatim, mas nao pareou um resumo curto do
`A-067` com sua entrada longa, embora fossem o mesmo assunto. A proporcao de comprimento,
nao a diferenca de significado, dominou o resultado.

## A condicao fina

O metodo continua valido para copy-paste e reformulacao leve. Para dedupe de conceito,
serve como candidato de leitura, nunca como aprovador final. Alterar o limiar muda recall e
precisao e precisa de gabarito congelado, como a avaliacao RAG atual.

## Acao com dono

Todo dedupe declara algoritmo, limiar, unidade e classe de equivalencia que mede
(`DEP-KMS`). Resultado negativo lexical nao encerra dedupe sem comparacao de funcao e
consumidor (`DEP-QAR`).

## Gatilho de refutacao

Um instrumento que prove equivalencia semantica no dominio por gabarito independente pode
assumir esse papel; a mera troca de embedding ou limiar nao basta.
