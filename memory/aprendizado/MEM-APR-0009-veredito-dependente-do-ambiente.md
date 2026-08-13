---
id: MEM-APR-0009-veredito-dependente-do-ambiente
titulo: Veredito dependente do ambiente nao e veredito — juiz que consulta o SO muda de opiniao com a maquina
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
origem: Onda 7 — aproveitamento por merito do lucaX (plano F50 §3 item 1, Oficina), ordem do Fundador de 2026-08-13; precedente A-244 (com o antecedente A-242) do acervo do lucaX, fonte lida integral em somente-leitura na admissao
evidencia: primeira execucao da suite do Hub fora do Windows deu 16 vermelhas de 102 sem uma regressao (A-242); a do SuperCondutor deu 8 de 133, e UMA era defeito real no proprio juiz — validar.py aplicava resolve() a caminho Windows rodando em Linux (vira caminho relativo prefixado com lixo) somado a normcase (minuscula no Windows, identidade no POSIX), de modo que estado gerado no Windows era REPROVADO em Linux
confianca: alta
ocorrencias: 2
ttl: permanente
aplica_se_a: [global]
resumo: Registra que checagem de juiz que toca sistema de arquivos ou depende de convencao do SO produz veredito que muda com a maquina, e fixa a condicao fina — comparacao entre campos do MESMO documento nao consulta disco nem SO; a garantia de integridade vive na assinatura, que roda na maquina que abriu a sessao.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# Veredito dependente do ambiente nao e veredito

## A licao

> **Juiz cujo veredito muda conforme a maquina nao e juiz.**

A frase e do proprio precedente (A-244 do lucaX, 2026-07-26) e o caso e mecanico:
a checagem cruzada do Juiz 1 comparava dois campos de um documento usando
`resolve()` + `normcase` — duas funcoes cujo resultado depende do sistema
operacional. Um `estado_sessao.json` **valido**, gerado no Windows, era
**reprovado** quando o mesmo juiz rodava em Linux. O veredito nao media o
documento; media a maquina.

## A evidencia, medida

- **A-242 (Hub):** primeira execucao da suite fora do Windows: **16 vermelhas de
  102**, zero regressao real — todas dependencia silenciosa de ambiente.
- **A-244 (SuperCondutor):** **8 vermelhas de 133** na primeira execucao em
  Linux; sete eram testes com dependencia de ambiente, **uma era defeito real no
  juiz** — a linha `os.path.normcase(str(Path(repo_estado).resolve()))`.
- A correcao trocou a pergunta: comparacao entre dois campos do MESMO documento
  normaliza separador, remove barra final, aplica `casefold` e compara — **sem
  tocar no sistema de arquivos e sem consultar o SO**.

## A condicao fina

Consultar o ambiente **nao e sempre defeito**: a garantia forte de integridade
daquele mesmo sistema (assinatura HMAC do vinculo, recomputada em
`verificar_vinculo`) roda deliberadamente **na maquina que abriu a sessao** — ali
o ambiente e parte constitutiva da garantia. O defeito e o caso em que o
ambiente entra **por acidente de implementacao** numa comparacao que se declara
documento-contra-documento.

## Acao com dono

Todo validador/contrato do Corpo que compara campos de um documento o faz sem
tocar disco nem SO (`DEP-ENG`); e nenhuma suite se declara portavel sem ter
rodado num segundo ambiente — no precedente, o Docker "se pagou no primeiro
`docker run`" exatamente por revelar o que o Windows sozinho nunca revelaria
(`DEP-QAR`).

## Gatilho de refutacao

Um caso em que a consulta ao ambiente seja constitutiva do veredito e ainda
assim indevida — o precedente ja separa os dois lados; se a separacao falhar em
caso novo, esta licao se refina.
