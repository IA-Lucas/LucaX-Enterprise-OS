---
id: TPL-fitness-check
titulo: Template de Verificacao de Aptidao Arquitetural
tipo: template
versao: 1.1.0
status: ativo
camada_memoria: nao-aplicavel
autor: DEP-GOV
proprietario: DEP-QAR
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0004, ADR-0008]
substitui: []
substituido_por: null
resumo: Fixa a forma da verificacao de aptidao evolutiva, com seis perguntas de sinal observavel e veredito vinculante.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# Template — Verificacao de Aptidao Arquitetural (`FIT`)

## Proposito
Registrar, ao encerrar uma mudanca estrutural, se a arquitetura ficou **mais apta a
evoluir** — nao apenas se ficou correta. Materializa o portao QG-6 (FND-09 §10).

## Escopo
Obrigatorio em toda mudanca **C2** e **C3**, no encerramento de trabalho que produza ou
altere artefato da Fundacao, do catalogo de Capabilities ou do Meta Model, e na revisao
estrutural periodica. Opcional em C1; nao se aplica a C0.

**Nao substitui** o Architecture Review: aquele verifica corretude, este verifica aptidao
evolutiva. Em C2 e C3, os dois sao obrigatorios (FT-01).

## Responsaveis
| Papel | Quem | Regra |
|---|---|---|
| Executa | **DEP-QAR** | Nunca quem produziu o artefato avaliado (FT-02, LV-03) |
| Verifica a forma | DEP-GOV | Sinal observavel presente nas seis respostas |
| Fornece evidencia | DEP-KMS | Metricas de contexto e de reuso |
| Aprova | DEP-EXE | |
| Ratifica | **SOBERANO** | Obrigatorio quando o objeto avaliado for C3 |

## Instrucoes de uso
1. Solicite o numero a DEP-GOV e atualize o contador em `governance/fitness/README.md`.
2. Grave em `governance/fitness/FIT-<AAAA>-<NNN>-<slug>.md`.
3. **Toda resposta exige sinal observavel.** Resposta sem sinal e opiniao e a verificacao e
   devolvida sem analise de merito (FT-03, DoD-5).
4. Ressalva sem **dono** e sem **gatilho** e invalida e converte o veredito em `inapto`
   (FT-06).
5. Veredito `inapto` **bloqueia o encerramento**: a mudanca retorna a etapa [2] do ciclo de
   FND-04 §4.
6. Tres vereditos `apto` consecutivos sem uma unica ressalva escalam ao Soberano como sinal
   de complacencia (FT-04).
7. Se a verificacao revelar causa, abra registro na camada APR (FT-07, QG-5).
8. O FIT e permanente: nunca e reescrito. Veredito posterior **supera** o anterior (FT-09).
9. **F2 tem duas respostas** desde a versao 1.1.0 (ADR-0008, PJ-06): ocorrencia **e**
   prevencao. Sem evidencia de que o teste preventivo de PJ-05 foi aplicado antes da
   submissao, a verificacao e **devolvida** — nao ressalvada.

## Historico de versoes deste template
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-GOV | Criacao por ADR-0004: seis perguntas de aptidao, ressalvas com dono e gatilho, veredito vinculante. |
| 1.1.0 | 2026-07-28 | DEP-GOV | Emenda por **ADR-0008**: F2 desdobrada em F2.a (ocorrencia) e F2.b (prevencao aplicada, com evidencia). Contrato de artefato declarado no frontmatter. |

---
---
id: FIT-<AAAA>-<NNN>-<slug>
titulo: <objeto avaliado, em uma linha>
tipo: fitness
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-QAR
proprietario: DEP-QAR
aprovador: DEP-EXE
criado_em: <AAAA-MM-DD>
atualizado_em: <AAAA-MM-DD>
revisao_prevista: <AAAA-MM-DD | null>
decisoes_relacionadas: [<ADR-id>, ...]
substitui: []
substituido_por: null
objeto_avaliado: [<ADR-id | RFC-id | FND-id>, ...]
classe_mudanca: <C2 | C3>
veredito: <apto | apto-com-ressalva | inapto>
---

# FIT-<AAAA>-<NNN>: <Titulo>

## Proposito
<Que mudanca esta sendo verificada, e por que ela exige Fitness Check.>

## Escopo
| Item | Definicao |
|---|---|
| Objeto avaliado | <ADRs, RFCs e documentos alterados> |
| Estado anterior | <a que se compara> |
| Nao inclui | <corretude estrutural — isso e do Architecture Review> |

## Responsaveis
| Papel | Quem |
|---|---|
| Executa (independente do produtor) | DEP-QAR |
| Forma | DEP-GOV |
| Evidencia | DEP-KMS |
| Aprova | DEP-EXE |
| Ratifica (se C3) | SOBERANO |

---

## Sumario

| # | Pergunta | Resposta | Sinal |
|---|---|---|---|
| F1 | Complexidade aumentou sem ganho proporcional? | <sim/nao> | <numero> |
| F2 | Algum conceito foi duplicado? **e** a prevencao foi aplicada? | <sim/nao> · <aplicada/nao> | <numero> |
| F3 | Alguma abstracao ficou desnecessaria? | <sim/nao> | <numero> |
| F4 | Continua mais simples de evoluir? | <sim/nao> | <numero> |
| F5 | Custo de contexto subiu ou desceu? | <subiu/desceu> | <numero> |
| F6 | Favorece reutilizacao? | <sim/nao> | <numero> |

**Veredito:** `<apto | apto-com-ressalva | inapto>`

---

## F1 — A complexidade aumentou sem ganho proporcional?

| Medida | Antes | Depois | Variacao |
|---|---|---|---|
| Entidades / componentes | | | |
| Regras normativas | | | |
| Artefatos a manter | | | |
| Responsabilidades orfas resolvidas | | | |
| Regras removidas ou unificadas | | | |

**Leitura:** <o acrescimo corresponde a um problema nomeado? qual?>

**Resposta:** <sim/nao> — <uma frase>

## F2 — Algum conceito foi duplicado?

> **Duas respostas obrigatorias (PJ-06, FND-10 §2.6).** Responder so a primeira e responder
> pela metade: deteccao posterior nao substitui prevencao.

### F2.a — Ocorrencia: houve duplicacao?

| Conceito | Onde ja estava definido | Como a mudanca o trata |
|---|---|---|
| | | <referencia por ID / projecao declarada / redefinicao> |

**Verificacao aplicada:** <varredura por definicao repetida, MM-01 e LX-07>

### F2.b — Prevencao: o teste preventivo foi aplicado antes da submissao?

| Verificacao | Evidencia exigida | Resultado |
|---|---|---|
| O autor percorreu **cada** tabela do artefato pelo item de PJ-05 do checklist de `TPL-documento`? | Quais tabelas foram examinadas, e o que resultou de cada uma — nao a marca no checklist | |
| Toda tabela que exibe conteudo de outra fonte declara **projecao** com as quatro informacoes de PJ-02? | A declaracao, citada | |
| Alguma reproducao foi **barrada antes** de ser escrita? | O caso, nomeado. "Nenhuma" e resposta valida e deve ser declarada | |

> Item marcado sem evidencia da execucao e reporte de verificacao que nao ocorreu (LV-05).
> Nesse caso a verificacao e **devolvida**, nao ressalvada.

**Resposta:** <sim/nao> a F2.a — <uma frase> · <aplicado/nao aplicado> a F2.b — <uma frase>

## F3 — Alguma abstracao ficou desnecessaria?

| Abstracao introduzida | Membros | Consumidor declarado | Veredito |
|---|---|---|---|
| | | | <justificada / ociosa> |

**Regra aplicada:** abstracao com menos de dois membros ou sem consumidor e suspeita
(AQ-03, RL-06).

**Resposta:** <sim/nao> — <uma frase>

## F4 — O sistema continua mais simples de evoluir do que antes?

| Mudanca-tipo | Documentos exigidos antes | Depois | Aprovacoes no caminho critico |
|---|---|---|---|
| | | | |

**Leitura:** <o custo de mudar subiu? em troca de que seguranca?>

**Resposta:** <sim/nao> — <uma frase>

## F5 — A mudanca reduz ou aumenta o custo de contexto?

| Papel / tarefa-tipo | Material necessario antes | Depois | Direcao |
|---|---|---|---|
| | | | <sobe/desce> |

**Metrica de referencia:** "Contexto por papel" (FND-01 §6.3) e "Volume de contexto por
consulta" (FND-06 §9.1). Direcao desejada: **desce** (PI-14).

**Resposta:** <sobe/desce> — <uma frase>

## F6 — Ela favorece reutilizacao?

| Definicao produzida | Reutilizavel por | Especifica do caso? |
|---|---|---|
| | | |

**Criterio:** DoD-8 — escrito para servir a proxima ocorrencia do problema, nao so a esta.

**Resposta:** <sim/nao> — <uma frase>

---

## Ressalvas

| # | Ressalva | Custo assumido | **Dono** | **Gatilho de reavaliacao** |
|---|---|---|---|---|
| | | | | |

> Ressalva sem dono e sem gatilho e invalida e converte o veredito em `inapto` (FT-06).

## Veredito

| Campo | Conteudo |
|---|---|
| Veredito | `<apto \| apto-com-ressalva \| inapto>` |
| Fundamento | <por que, em uma frase> |
| Efeito | <encerra / encerra com divida declarada / bloqueia e retorna a FND-04 §4 etapa 2> |
| Data | <AAAA-MM-DD> |
| Executado por | DEP-QAR |
| Aprovado por | DEP-EXE |
| Ratificado por (se C3) | SOBERANO |

## Aprendizado gerado

| Registro APR | Licao |
|---|---|
| <MEM-APR-id ou "nenhum"> | |

## Historico de vereditos sobre este objeto

| FIT | Data | Veredito | Relacao |
|---|---|---|---|
| | | | <primeiro / supera FIT-...> |
