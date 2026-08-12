---
id: MEM-APR-0007-plausibilidade-nao-e-verificacao
titulo: Plausibilidade nao e verificacao — coerencia usada como evidencia e a causa numero um de reprovacao medida
tipo: memoria
versao: 1.0.0
status: ativo
camada_memoria: aprendizado
autor: DEP-KMS
proprietario: DEP-KMS
aprovador: DEP-KMS
criado_em: 2026-08-12
atualizado_em: 2026-08-12
revisao_prevista: 2027-02-12
decisoes_relacionadas: [ADR-0038]
substitui: []
substituido_por: null
origem: Primeira convocacao da F34 (Oficina, missoes/F42-CONVOCACAO-DO-APRENDIZADO.md, licao candidata LC-01), sobre a fila da decisao D4 do Fundador de 2026-08-12
evidencia: 9 de 17 reprovacoes fundamentadas do log veredictos.jsonl do lucaX levam o motivo literal "pareceu-razoavel" — 6 numa unica tarde (2026-07-26); reconto independente da revisao externa bateu digito a digito; corroboracao em corpus distinto contada a parte (familia "escrito antes de o instrumento rodar", 5 arq/10 occ em missoes/ da Oficina)
confianca: alta
ocorrencias: 9
ttl: permanente
aplica_se_a: [global]
resumo: Registra que aceitar como verdadeiro o que parece razoavel — coerencia usada como evidencia — foi a causa numero um de reprovacao fundamentada medida no legado, e fixa a regra derivada, toda afirmacao verificavel com fonte ou contagem ao lado, ja com dono na camada de execucao.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# Plausibilidade nao e verificacao

## Proposito
Registrar a causa numero um de reprovacao fundamentada medida na organizacao — **coerencia
usada como evidencia** — para que ela deixe de se repetir por desconhecimento: **9** das **17**
reprovacoes com motivo do log do legado levam, literal, o motivo **`pareceu-razoavel`**.

## Escopo
| Item | Definicao |
|---|---|
| **Aplica-se a** | toda entrega que contenha **afirmacao verificavel** — numero, existencia, estado de coisa |
| **NAO se aplica a** | juizo sem fato verificavel *(estilo, preferencia)* — ai plausibilidade e o que ha |

## Responsaveis
| Papel | Quem |
|---|---|
| Dono do registro | **DEP-KMS** |
| Autor da licao | a primeira convocacao da `F34` *(Oficina, `F42`)*, sob `CAP-aprendizado-organizacional` `R1`–`R4` |
| Verificacao independente | revisao externa por **reconto independente** contra a fonte — bateu digito a digito |

## Situacao
O log `veredictos.jsonl` do legado guarda **188** registros, **89** reprovacoes, **17** com
motivo. **9** delas — mais da metade — levam o motivo literal **`pareceu-razoavel`**, **6 numa
unica tarde** (2026-07-26). O produtor aceitou como verdadeiro o que **parecia** razoavel, sem
confrontar a fonte.

## Licao
**O sintoma seria "entrega errada"; a causa e o criterio de aceitacao errado.** Coerencia
narrativa nao e evidencia: e a familia de `LV-12` *(fabricar evidencia)* na forma branda — e a
forma branda e a que escala, porque nao parece fraude para quem a comete. A propria fabrica
cometeu o padrao **duas vezes na mesma sessao** que o mediu *(MEDICOES 1 de `F39`/`F40`,
escritas antes de o contador rodar — declaradas la, nao aqui)*.

## Acao que decorre, com dono
**A instrucao de execucao de todo papel exige fonte ou contagem AO LADO de toda afirmacao
verificavel** — `Q-7`/`LV-12` descendo a camada de execucao. **Dono: o setor `agentops`**
*(decisao `1` e `D1` do Fundador)*, que ja a materializou: `INSTRUCAO-CAMADA-2.md` na entrega
`juiz-para-o-corpo` da Oficina, e o motivo **`afirmacao-sem-fonte`** no enum do contrato de
veredito sao.

## Gatilho de refutacao
O desmonte do legado (Onda 7) cruzar os objetos julgados — o log **nao os grava** — e mostrar
outra causa comum nos 9 vetos: a causa aqui e a **melhor leitura do motivo literal**, refutavel
por evidencia nova *(correcao append-first, `MM-09`)*.
