---
id: FIT-2026-002-artifact-framework
titulo: Aptidao arquitetural da adocao do Enterprise Artifact Framework e das correcoes da Missao 1.3
tipo: fitness
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-QAR
proprietario: DEP-QAR
aprovador: DEP-EXE
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0005, ADR-0006]
substitui: []
substituido_por: null
objeto_avaliado: [ADR-0005, ADR-0006, FND-10, INC-2026-001]
classe_mudanca: C3
classe_avaliacao: aptidao
veredito: apto-com-ressalva
resumo: Verifica se o Artifact Framework deixou a arquitetura mais apta a evoluir; veredito apto-com-ressalva, quatro ressalvas.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-EXE
ratificacao: nao-exigida
---

# FIT-2026-002: Enterprise Artifact Framework

## Proposito
Verificar se a Missao 1.3 — contrato universal de artefato, correcao da autoverificacao e
contencao da ratificacao inferida — deixou a arquitetura **mais apta a evoluir**.

## Escopo
| Item | Definicao |
|---|---|
| Objeto avaliado | ADR-0005, ADR-0006, FND-10, INC-2026-001 e as emendas em FND-01, FND-03, FND-04, FND-08, FND-09 e `TPL-documento` |
| Estado anterior | **76 artefatos, 15.939 linhas**; 10 sem tipo declarado; nenhum perfil de contexto |
| Nao inclui | Corretude estrutural — objeto da [revisao arquitetural](../../foundation/revisao-arquitetural-artifact-framework-2026-07-28.md) |

## Responsaveis
| Papel | Quem |
|---|---|
| Executa | DEP-QAR — FND-10 e ADR-0006 foram produzidos por **DEP-GOV** (FT-02 respeitado) |
| Forma | DEP-GOV |
| Evidencia | DEP-KMS |
| Aprova | DEP-EXE |
| Ratifica (C3) | SOBERANO |

---

## Sumario

| # | Pergunta | Resposta | Sinal |
|---|---|---|---|
| F1 | Complexidade aumentou sem ganho proporcional? | **Parcialmente** | **+2.977 linhas (+18,7%)** contra 10 artefatos classificados e 2 causas corrigidas |
| F2 | Algum conceito foi duplicado? | **Sim, um** | Coluna Local da matriz §10.3 repete FND-03 §7 |
| F3 | Alguma abstracao ficou desnecessaria? | **Nao** | 33 tipos, todos com ≥1 instancia ou destino; 0 templates novos |
| F4 | Continua mais simples de evoluir? | **Sim** | Criar artefato: 1 template; classificar: 1 catalogo |
| F5 | Custo de contexto subiu ou desceu? | **Desceu no nucleo, subiu no acervo** | Nucleo **5,7%**; acervo **+18,7%** |
| F6 | Favorece reutilizacao? | **Sim** | Contrato, tipos e perfis servem a qualquer artefato futuro |

**Veredito:** `apto-com-ressalva` — quatro ressalvas, todas com dono e gatilho.

---

## F1 — A complexidade aumentou sem ganho proporcional?

| Medida | Antes | Depois | Variacao |
|---|---|---|---|
| Artefatos | 76 | **85** | **+9** |
| Linhas | 15.939 | **18.916** | **+2.977 (+18,7%)** |
| Documentos fundacionais | 9 | 10 | +1 |
| Templates | 19 | **19** | **0** — `TPL-documento` estendido, nao duplicado |
| Campos obrigatorios de frontmatter | 15 | 20 *(so para artefato novo)* | +5, todos com valor padrao |
| Arquivos do acervo reescritos | — | **0** | — |
| Artefatos sem tipo declarado | **10 (13%)** | **0** | −10 |
| Regras normativas novas | — | ~40 *(AC, CS, IX, LM, RB, CC, LN, CE, SE, RG)* | +40 |
| Regras removidas ou unificadas | — | **1 unificacao** — regra de verificacao reflexiva escrita uma vez em FND-09, apontada de FND-08 | — |
| Causas de incidente corrigidas | — | **2** — autoverificacao (ADR-0005) e ratificacao inferida (INC-2026-001, 3 frentes) | — |

**Leitura.** O acrescimo e de **18,7%** em linhas, contra tres contrapartidas verificaveis: 13% do
acervo saiu da nulidade por MT-01, duas causas de defeito foram fechadas — nao apenas as
ocorrencias — e nenhum arquivo existente precisou ser reescrito.

O que **nao** se pode afirmar: que 40 regras novas sejam a quantidade certa. Nenhuma foi
exercida. O padrao de ADR-0003 se repete — regra escrita hoje, testada amanha.

**Resposta:** parcialmente — contrapartida verificavel, proporcao nao comprovada.
**→ Ressalva R1.**

## F2 — Algum conceito foi duplicado?

| Conceito | Onde ja estava | Como FND-10 o trata |
|---|---|---|
| Estados e transicoes | FND-03 §5 | **Referencia**, sem reproduzir o grafo — aprendizado de R2 de FIT-2026-001 aplicado |
| Perfis de ciclo de vida | FND-09 §7.2 | Referencia |
| Relacoes | FND-09 §6.1 | §7.1 **mapeia** verbos, sem criar relacao |
| Matriz de autoridade | FND-09 §8.2 | §6.1 declara que nao reproduz, e a precedencia da origem |
| Classes de mudanca | FND-04 §2 | Citadas por nome |
| **Diretorio de cada tipo** | **FND-03 §7** | **Repetido na coluna Local da matriz §10.3** |

**Verificacao aplicada:** varredura de FND-10 por tabela ou diagrama reproduzido de outro
documento — a mesma verificacao que R2 de FIT-2026-001 gerou e que passou a constar da
auditoria de coerencia interna (FND-04 §8). Um caso encontrado.

A matriz §10.3 cruza quatro dimensoes, e o diretorio e uma delas — mas o **valor** e copiado
de FND-03 §7. Se a arvore mudar, os dois divergem em silencio.

**Resposta:** sim, um. **→ Ressalva R2.**

> **Nota:** a ressalva R2 de FIT-2026-001 — grafo de estados duplicado entre FND-03 e FND-09 —
> **permanece aberta**, com gatilho na 1a revisao de FND-09. Sao duas ocorrencias do **mesmo
> padrao** em duas missoes consecutivas. Registrado em §Aprendizado.

## F3 — Alguma abstracao ficou desnecessaria?

| Abstracao introduzida | Membros / instancias | Consumidor declarado | Veredito |
|---|---|---|---|
| Contrato em 3 camadas (L1/L2/L3) | 3 camadas, todas com conteudo | AC-01, §2.4 | Justificada |
| 33 tipos documentais | 21 com instancia; 12 previstos com local e template | Canon CS-01 | Justificada |
| 6 classes de tipo (§4.1–4.7) | 4 a 7 tipos cada | Matriz §10.3 | Justificada |
| 3 classes de mutabilidade | M1: 6 tipos · M2: 9 · M3: 1 | §6.2, CC-01 | **M3 com um membro** |
| 4 perfis de contexto | Todos com atribuicao padrao na matriz | CE-01 | Justificada |
| 7 sinais de especializacao | Nenhum observado ainda | SE-01, SE-02 | Justificada — sao criterios, nao membros |

**Regra aplicada:** abstracao com menos de dois membros e suspeita (AQ-03).

**M3 — Derivado** tem um unico membro: Indice. Examinado: a classe existe para carregar uma
regra que M1 e M2 nao comportam — *"reprocessa-se da fonte; nunca se edita a fonte para caber
no derivado"*. Sem ela, indices cairiam em M2 e seriam versionados como norma, que e
exatamente o defeito que IX-01 previne. **Justificada com um membro**, e registrada.

**Resposta:** nao — nenhuma comprovadamente ociosa; M3 sob observacao. **→ Ressalva R3.**

## F4 — O sistema continua mais simples de evoluir do que antes?

| Mudanca-tipo | Antes | Depois | Aprovacoes |
|---|---|---|---|
| Criar artefato novo | Escolher entre 19 templates, sem regra de escolha | 1 template universal + teste T1–T4 | Inalterado |
| Saber que tipo um artefato e | Nao havia registro — 10 sem tipo | 1 consulta ao catalogo | Inalterado |
| Saber o que carregar para uma tarefa | Nao havia regra | 1 consulta ao perfil | Inalterado |
| Verificar se `revisor` = `autor` | Leitura de cada arquivo | Varredura de frontmatter — **so em artefato novo** | Inalterado |
| Criar tipo documental novo | Nao havia rito | **C2** — degrau 1 da escada (FND-09 §11.2) | 0 → 2 |
| Encerrar mudanca C2/C3 | Review + Fitness | Review + Fitness + entrada no catalogo | +1 passo |

**Leitura.** A assimetria repete a de FIT-2026-001 e e deliberada: evoluir **dentro** do
modelo ficou mais simples; acrescentar tipo ficou mais caro — mas **C2**, nao C3, o que e
proporcional. O passo novo no encerramento — atualizar o catalogo — e o preco de RG-02.

**Resposta:** sim.

## F5 — A mudanca reduz ou aumenta o custo de contexto?

| Papel / tarefa-tipo | Antes | Depois | Direcao |
|---|---|---|---|
| Executar tarefa qualquer | Sem regra — na pratica, tudo | **Nucleo: 1.087 linhas + 2 recortes = 5,7%** | **desce** |
| Descobrir se um artefato e relevante | Abrir o artefato | Ler 1 linha de resumo no catalogo | **desce** |
| Ler a Fundacao integralmente | 9 documentos | 10 documentos | sobe |
| Acervo total | 15.939 linhas | **18.916 linhas** | **sobe 18,7%** |

**Metrica de referencia:** "Contexto por papel" (FND-01 §6.3), "Volume de contexto por
consulta" (FND-06 §9.1). Direcao desejada: desce (PI-14).

**Leitura honesta.** O acervo cresceu **18,7%**; o que caiu foi o **contexto necessario por
tarefa**, de "indeterminado" para **5,7%** declarado. As duas coisas sao verdadeiras ao mesmo
tempo, e apresentar so a segunda seria maquiagem (PI-10).

**Observacao critica:** este e o **segundo** registro da metrica; ainda nao ha serie. E, como
em FIT-2026-001, **nenhum trabalho foi executado sob os perfis** — a reducao e razao entre
numeros, nao medicao de uso.

**Resposta:** desce por tarefa; sobe no acervo. **→ Ressalva R4.**

## F6 — Ela favorece reutilizacao?

| Definicao produzida | Reutilizavel por | Especifica do caso? |
|---|---|---|
| Contrato de artefato em 3 camadas | Todo artefato futuro | Nao |
| 33 tipos documentais com local e template | Todo artefato futuro | Parcialmente — lista os tipos atuais |
| 9 operacoes de ciclo com rollback | Todo tipo | Nao |
| 3 classes de mutabilidade | Todo tipo | Nao |
| 7 sinais de especializacao de documento | Toda proposta de divisao | Nao |
| 4 perfis de contexto | Todo papel e toda missao | Nao |
| Regra LM-02 a LM-06 (ratificacao) | Toda decisao C3/Tipo 1 futura | Nao |

**Criterio:** DoD-8.

**Evidencia mais forte:** `TPL-documento` foi **estendido em vez de duplicado**, e os 19
templates vigentes passaram nos testes T1–T4 sem que nenhum novo fosse criado. Um framework
sobre artefatos que nao produz artefato redundante e a demonstracao do proprio principio.

**Resposta:** sim.

---

## Ressalvas

| # | Ressalva | Custo assumido | **Dono** | **Gatilho de reavaliacao** |
|---|---|---|---|---|
| R1 | 40 regras novas, nenhuma exercida; proporcao do acrescimo nao comprovada | Se o ganho nao se confirmar, o acervo carrega mais um documento normativo sem contrapartida | DEP-EXE | 1a revisao estrutural: aplicar EV-08 a FND-10 se nenhum artefato tiver sido criado sob o contrato |
| R2 | Coluna Local da matriz §10.3 repete o diretorio de FND-03 §7 | Mudanca na arvore faz os dois divergirem em silencio | DEP-GOV | 1a revisao de FND-10: substituir valor por referencia |
| R3 | Classe de mutabilidade **M3** tem um unico membro | Abstracao com um membro e suspeita (AQ-03) | DEP-GOV | 1a revisao estrutural: se continuar com um membro e sem uso, fundir em M2 com regra propria |
| R4 | Reducao de contexto **calculada**, nao observada — segunda missao consecutiva | O numero pode nao corresponder ao uso real | DEP-KMS | Primeiro trabalho executado sob os perfis, apos a ratificacao |

## Veredito

| Campo | Conteudo |
|---|---|
| Veredito | **`apto-com-ressalva`** |
| Fundamento | As seis perguntas tem sinal observavel; quatro revelam degradacao ou incerteza aceitas conscientemente, todas com dono e gatilho. Nenhuma revela degradacao sem contrapartida |
| Efeito | Encerra. As quatro ressalvas viram **divida declarada** com data de reavaliacao (FND-07 §9) |
| Data | 2026-07-28 |
| Executado por | DEP-QAR |
| Aprovado por | DEP-EXE |
| Ratificado por (C3) | **Pendente** — mesma pendencia de ADR-0006 §14 |

### Nota sobre FT-04 — vigilancia de complacencia

| Verificacao | Estado |
|---|---|
| Vereditos emitidos | 2 |
| Consecutivos `apto` **sem nenhuma ressalva** | **0** — ambos com ressalvas |
| `inapto` emitidos | **0** |

Dois vereditos `apto-com-ressalva` consecutivos **nao** disparam FT-04, que exige tres `apto`
sem ressalva. Registra-se, porem, que **nenhum `inapto` foi emitido em duas oportunidades**.
Isso ainda nao e sinal de criterio frouxo — mas e o numero a vigiar: se a terceira verificacao
tambem terminar em `apto-com-ressalva` sem que nenhuma ressalva anterior tenha sido fechada,
o mecanismo estara produzindo divida em vez de correcao.

### Nota de conflito de interesse (PI-10)

Ao contrario de FIT-2026-001, **nao ha conflito nesta verificacao**: FND-10 e ADR-0006 foram
produzidos por DEP-GOV, e a verificacao e executada por DEP-QAR. O precedente de excecao
aberto em FIT-2026-001 nao foi invocado — como aquele documento determinou.

## Aprendizado gerado

| Registro APR | Licao |
|---|---|
| A gravar por DEP-KMS (QG-5) | **Duplicacao por reproducao de tabela e o defeito recorrente deste acervo.** Duas missoes consecutivas produziram a mesma classe de ressalva — R2 de FIT-2026-001 (grafo de estados) e R2 desta (coluna Local). A auditoria de coerencia interna criada na missao anterior **detectou** o segundo caso, o que confirma que o instrumento funciona; mas nao o **preveniu** na redacao. Acao: o checklist de `TPL-documento` passa a incluir a verificacao antes da submissao, nao so na auditoria. Dono: DEP-GOV |

## Historico de vereditos sobre este objeto

| FIT | Data | Veredito | Relacao |
|---|---|---|---|
| FIT-2026-002 | 2026-07-28 | `apto-com-ressalva` | Primeiro sobre este objeto |
