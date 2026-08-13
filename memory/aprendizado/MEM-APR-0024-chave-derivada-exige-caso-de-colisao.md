---
id: MEM-APR-0024-chave-derivada-exige-caso-de-colisao
titulo: Chave derivada exige caso de colisao — unicidade presumida produz falso verde em massa
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
origem: Onda 7 — dedupe F53 da Oficina; precedente A-204 do lucaX, fonte lida integral em somente-leitura
evidencia: sensor agregava por stem; um unico link README marcava como ligados cerca de 89 READMEs e escondia 110 orfaos reais, porque nenhum dos seis testes originais continha chave repetida
confianca: alta
ocorrencias: 1
ttl: permanente
aplica_se_a: [global]
resumo: Registra que agregacao por nome, slug, id ou outra chave derivada exige fixture com colisao; se a origem nao garante unicidade, a chave precisa incluir identidade suficiente ou recusar ambiguidades.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# Chave derivada exige caso de colisao

## A licao

Toda agregacao por chave derivada precisa de um teste com **duas entidades diferentes que
geram a mesma chave**. Caso feliz com nomes unicos apenas repete a suposicao do algoritmo.

## A evidencia, medida

Em `A-204`, o sensor indexava por `stem`. Um unico `[[README]]` fazia cerca de **89** arquivos
homonimos parecerem ligados e reportava zero, escondendo **110** orfaos reais. Os seis testes
originais tinham apenas nomes unicos.

## A condicao fina

Chave derivada e valida quando a fonte garante unicidade e essa garantia tambem e testada.
Se a resolucao aceita ambiguidades por desenho, o veredito precisa declará-las em vez de
escolher silenciosamente.

## Acao com dono

Indices, caches, agrupamentos e sensores do Corpo incluem caso de colisao para cada chave
derivada (`DEP-ENG`). `DEP-QAR` compara pelo menos uma medicao independente quando o proprio
sensor ja produziu falso verde.

## Gatilho de refutacao

Uma chave criptograficamente ou contratualmente unica dispensa colisao sintetica apenas se
a propriedade de unicidade for verificada no portao de entrada.
