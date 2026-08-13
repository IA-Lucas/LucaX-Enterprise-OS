---
id: MEM-APR-0023-referencia-operacional-resolve-desde-a-raiz
titulo: Referencia operacional resolve desde a raiz — agente isolado nao herda a intuicao de caminho do autor
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
origem: Onda 7 — dedupe F53 da Oficina; precedente A-139, reforcado pela fibra de cwd do A-031, fontes lidas integralmente em somente-leitura
evidencia: quatro definicoes de agente citavam caminhos relativos curtos; o critico isolado afirmou que tres arquivos reais nao existiam, enquanto agentes com contexto anterior os encontravam por inferencia
confianca: alta
ocorrencias: 2
ttl: permanente
aplica_se_a: [global]
resumo: Registra que toda referencia operacional de agente, hook ou runbook deve resolver do ponto de entrada real e ser exercitada isoladamente; caminho que funciona por contexto herdado e acerto por inferencia.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# Referencia operacional resolve desde a raiz

## A licao

Agente isolado nao recebe a intuicao de diretorio de quem escreveu a instrucao. Caminho
operacional precisa resolver a partir da **raiz contratada pelo executor**, em toda mencao.

## A evidencia, medida

No `A-139`, quatro definicoes usavam caminhos curtos. O critico convocado isoladamente
reprovou porque tres arquivos “nao existiam”; outros agentes os haviam achado apenas por
contexto e inferencia. No `A-031`, mudar `cwd` fez oito hooks relativos entrarem em deadlock.

## A condicao fina

Texto narrativo historico pode preservar caminho do dia. A regra vale para referencia que
sera executada, copiada ou lida por processo/agente. Caminho absoluto da maquina tambem nao
e solucao; a ancora e a raiz do repositorio ou variavel contratual equivalente.

## Acao com dono

Todo agente, hook e runbook resolve caminhos desde a raiz declarada e ganha teste a partir
de `cwd` diferente (`DEP-ENG`). Revisao rejeita caminho operacional cujo funcionamento
dependa de contexto conversacional anterior (`DEP-QAR`).

## Gatilho de refutacao

Executor que garanta por contrato um unico `cwd` pode permitir relativo a ele; o teste deve
provar a garantia, não apenas rodar no caso feliz.
