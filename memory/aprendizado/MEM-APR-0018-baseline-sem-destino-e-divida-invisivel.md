---
id: MEM-APR-0018-baseline-sem-destino-e-divida-invisivel
titulo: Baseline sem destino e divida invisivel — falha medida precisa de proximo responsavel ou limite declarado
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
origem: Onda 7 — fila de admissao da triagem F51 (Oficina, ordem do Fundador de 2026-08-13, "entao vamos terminar a onda 7"); precedente ADR-071 do lucaX, fonte lida integral em somente-leitura na admissao
evidencia: o lucaX tinha 76 testes sem runner integral; a baseline criada para as falhas passou a exigir destino por item, pois listar sem decidir era omissao. Na mesma medicao, runner que alterava PYTHONIOENCODING fabricou 10 vermelhas falsas e --jobs 8 gerou 8 vermelhas fantasma que --jobs 1 nao reproduziu; o estado confiavel exige nova medicao no ambiente herdado e serial por padrao
confianca: alta
ocorrencias: 1
ttl: permanente
aplica_se_a: [global]
resumo: Registra que baseline nao e deposito de falhas: cada entrada precisa de destino acionavel ou fronteira declarada, e so medicao nova no ambiente que se pretende julgar pode alterar seu estado. Listagem sem destino e relato sem veredito.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# Baseline sem destino e divida invisivel

## A licao

Falha medida sem **destino** e apenas divida que ganhou arquivo. Baseline util
declara quem ou qual fronteira decide o proximo passo; nao usa a lista para
adiar a decisao indefinidamente.

## A evidencia, medida

No lucaX (ADR-071, 2026-07-24), havia **76** arquivos de teste e nenhum runner
integral. A baseline de suites passou a recusar item sem `destino`; destinos
legitimos incluem "CEO decide" e "bloqueado por fronteira". A mesma fonte
mediu por que o veredito precisa ser novo e limpo: runner que injetava
`PYTHONIOENCODING=utf-8` fabricou **10 vermelhas falsas**, e `--jobs 8`
produziu **8 vermelhas fantasma** que `--jobs 1` nao reproduziu.

## A condicao fina

Destino nao significa promessa de consertar tudo agora: pode ser autoridade
nomeada ou limite real declarado. O que nao vale e item sem responsavel. E a
mudanca de estado exige nova execucao que herde o ambiente medido; paralelo e
evidencia de menor confianca ate reconfirmacao serial.

## Acao com dono

Toda baseline de falhas exige `destino` nao vazio por entrada e recusa a lista
incompleta (`DEP-QAR`). O executor mede sem mutar o ambiente e usa serial como
padrao; so depois de rodada nova pode baixar ou encerrar uma entrada
(`DEP-EXE`). Item que sarou e permaneceu listado vira atencao de faxina.

## Gatilho de refutacao

Uma classe de falha para a qual nao exista dono, fronteira ou autoridade
legitima para decidir exige ampliar a taxonomia de destinos antes de aceitar a
entrada; nao autoriza aceitar vazio.
