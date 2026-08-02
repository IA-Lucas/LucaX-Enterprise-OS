---
id: FIT-2026-001-meta-model
titulo: Aptidao arquitetural da adocao do Enterprise Meta Model e do Architecture Fitness Check
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
decisoes_relacionadas: [ADR-0003, ADR-0004]
substitui: []
substituido_por: null
objeto_avaliado: [ADR-0003, ADR-0004, FND-09]
classe_mudanca: C3
veredito: apto-com-ressalva
---

# FIT-2026-001: Enterprise Meta Model e Architecture Fitness Check

## Proposito
Verificar se a adocao do Meta Model (ADR-0003) e do proprio Fitness Check (ADR-0004) deixou
a arquitetura **mais apta a evoluir** — nao apenas mais correta. Primeira aplicacao do
mecanismo, sobre a mudanca que o criou.

## Escopo
| Item | Definicao |
|---|---|
| Objeto avaliado | ADR-0003, ADR-0004, FND-09 e as seis emendas em cascata (FND-01, 02, 03, 04, 06, 08) |
| Estado anterior | Fundacao de 8 documentos, 23 Capabilities, 2 ADRs, 6 portoes, 18 templates |
| Nao inclui | Corretude estrutural — objeto da [revisao arquitetural](../../foundation/revisao-arquitetural-meta-model-2026-07-28.md) |

## Responsaveis
| Papel | Quem |
|---|---|
| Executa (independente do produtor) | DEP-QAR — FND-09 foi proposto por DEP-GOV (FT-02) |
| Forma | DEP-GOV |
| Evidencia | DEP-KMS |
| Aprova | DEP-EXE |
| Ratifica (C3) | SOBERANO |

---

## Sumario

| # | Pergunta | Resposta | Sinal |
|---|---|---|---|
| F1 | Complexidade aumentou sem ganho proporcional? | **Parcialmente** | +1 documento, +1 portao, +2 entidades, +1 template contra 2 inconsistencias reais fechadas e 3 divergencias corrigidas |
| F2 | Algum conceito foi duplicado? | **Sim, um** | Grafo de transicao de estados aparece em FND-03 §5.1 e FND-09 §7.1 |
| F3 | Alguma abstracao ficou desnecessaria? | **Uma sob suspeita** | Arquetipo A2 reune 19 de 21 entidades |
| F4 | Continua mais simples de evoluir? | **Sim, com assimetria** | Criar componente: 5 documentos → 2. Criar tipo novo: 0 ritos → C3 |
| F5 | Custo de contexto subiu ou desceu? | **Desceu** na tarefa-tipo | 5 documentos → 2 para a consulta dominante; +1 documento no total da Fundacao |
| F6 | Favorece reutilizacao? | **Sim** | 6 de 6 candidatas recusadas entrariam por acrescimo, sem redesenho |

**Veredito:** `apto-com-ressalva` — tres ressalvas, todas com dono e gatilho.

---

## F1 — A complexidade aumentou sem ganho proporcional?

| Medida | Antes | Depois | Variacao |
|---|---|---|---|
| Documentos fundacionais | 8 | 9 | **+1** |
| Portoes de qualidade | 6 | 7 | **+1** |
| Tipos de entidade com identificador | 17 | 19 (+`MSG`, +`FIT`) | **+2** |
| Templates | 18 | 19 | **+1** |
| Arquetipos | 0 | 4 | **+4** |
| Relacoes declaradas entre tipos | 0 (7 so entre Capabilities) | 10 | **+10** |
| Artefatos por mudanca C2/C3 | 2 (RFC + ADR) | 3 (+ FIT) | **+1** |
| Inconsistencias reais fechadas | — | 2 | `MSG` fora da taxonomia; PI-12 (8 tipos) × FND-08 §8 (6 tipos) |
| Divergencias internas corrigidas na revisao | — | 3 | Verbos de relacao, responsabilidade × dependencia, portao como entidade |
| Regras removidas ou unificadas | — | 2 unificacoes, **0 remocoes** | Alcance de Carta e de vinculo unificados em 8 tipos |

**Leitura.** O acrescimo e real e responde a problemas nomeados: as duas inconsistencias
fechadas eram verificaveis por leitura direta e nenhuma auditoria vigente as teria detectado,
porque todas verificam conformidade de instancias e nenhuma verifica coerencia entre tipos.

O que **nao** se pode afirmar: que a proporcao esta correta. Nenhuma regra foi removida, e a
plataforma acumulou tres camadas normativas em um unico dia — Fundacao, Capabilities e Meta
Model. O sinal de que o acrescimo se pagou so existira quando um Framework futuro for
construido sobre ele.

**Resposta:** parcialmente sim — o acrescimo tem contrapartida verificavel, mas a proporcao
nao esta comprovada. **→ Ressalva R1.**

## F2 — Algum conceito foi duplicado?

| Conceito | Onde ja estava definido | Como a mudanca o trata |
|---|---|---|
| Classes de mudanca C0–C3 | FND-04 §2 | Citadas por nome; **nenhuma tabela reproduzida** |
| Relacoes entre Capabilities | FND-08 §5.1 | Incorporadas por referencia, com nota explicita |
| Niveis de autonomia A0–A3 | FND-01 §7.2 | Citados como eixo ortogonal; valores nao redefinidos |
| Camadas de memoria | FND-06 §2.1 | Citadas; nenhuma tabela reproduzida |
| Autoridade por materia | FND-01 §7.3, FND-04, FND-08 §6.3 | **Derivada**, com regra de precedencia: em conflito vence a origem |
| **Grafo de transicao de estados** | **FND-03 §5.1** | **Reproduzido em FND-09 §7.1** |

**Verificacao aplicada:** varredura por definicao repetida em FND-09 contra FND-01 a FND-08.
Um caso encontrado.

O grafo de transicoes esta desenhado nos dois documentos. FND-09 §7.1 declara que nao
redefine e que apenas restringe por perfil — mas **um diagrama recolado e uma segunda fonte
de verdade**, ainda que consistente hoje. Se FND-03 §5.1 for emendado, os dois divergem em
silencio, exatamente o que MM-01 e FND-03 §7.1 existem para impedir.

**Resposta:** sim, um. **→ Ressalva R2.**

## F3 — Alguma abstracao ficou desnecessaria?

| Abstracao introduzida | Membros | Consumidor declarado | Veredito |
|---|---|---|---|
| A1 ATOR | 4 | Autoridade (§8), canais (FND-05) | Justificada |
| **A2 ARTEFATO** | **19 de 21** | Frontmatter, estados, versionamento, localizacao | **Sob suspeita** |
| A3 COMPONENTE | 8 | Carta (PI-12), vinculo (FND-08 §8) | Justificada — e o alcance que a mudanca unificou |
| A4 INSTRUMENTO | 5 | Perfil P2, imutabilidade (LV-04) | Justificada |
| 7 estratos | 21 | Direcao de dependencia (PD-11) | Justificada — sustenta a regra-mae |
| 4 perfis de ciclo de vida | 21 | Transicoes (§7.4) | Justificada, **mas 2 nunca exercitados** (P0, P3) |

**Regra aplicada:** abstracao com menos de dois membros ou sem consumidor e suspeita (AQ-03).
Nenhuma tem menos de dois membros. A suspeita sobre A2 e o **inverso**: abranger 90% do
universo classifica pouco. Seu proposito declarado — carregar as regras universais uma vez em
vez de dezenove (AQ-04) — se cumpre, mas ele nunca sera invocado para **decidir** nada.

**Resposta:** uma sob suspeita, nenhuma comprovadamente ociosa. **→ Ressalva R3.**

## F4 — O sistema continua mais simples de evoluir do que antes?

| Mudanca-tipo | Documentos exigidos antes | Depois | Aprovacoes no caminho critico |
|---|---|---|---|
| Criar componente (departamento, agente, skill) | 5 — FND-01, 02, 03, 04, 08 | **2** — FND-09 + o especializado | Inalterado |
| Declarar relacao entre componentes | Nenhuma norma; improviso por Carta | 1 — FND-09 §6.2 | Inalterado |
| Saber quem aprova um tipo | 3 — FND-01 §7.3, FND-04, FND-08 §6.3 | **1** — FND-09 §8.2 | Inalterado |
| **Criar tipo novo** | **Nenhum rito** | **RFC + ADR + ratificacao** | **0 → 3** |
| Acrescentar atributo a tipo existente | Nenhum rito claro | C1 | 0 → 1 |
| Encerrar mudanca C2/C3 | Review opcional | **Review + Fitness obrigatorios** | +1 portao |

**Leitura.** A assimetria e deliberada e esta declarada: evoluir **dentro** do modelo ficou
mais simples; evoluir **o modelo** ficou mais caro. Era o proposito — MT-01 so tem efeito se
o rito de entidade nova for custoso.

O risco correspondente esta registrado como achado M6 da revisao arquitetural: quando o rito
parecer caro, a saida barata sera pedir excecao formal em vez de abrir RFC. A metrica de
vigilancia — excecoes formais que tocam MT-01 por horizonte, direcao desejada zero — ja tem
dono e gatilho.

**Resposta:** sim, com assimetria declarada e vigiada.

## F5 — A mudanca reduz ou aumenta o custo de contexto?

| Papel / tarefa-tipo | Material necessario antes | Depois | Direcao |
|---|---|---|---|
| Criar um componente | 5 documentos fundacionais | 2 | **desce** |
| Verificar se uma relacao e valida | Varredura de Cartas; sem norma | 1 tabela (§6.2) | **desce** |
| Saber quem aprova o que | 3 documentos | 1 tabela (§8.2) | **desce** |
| Ler a Fundacao integralmente | 8 documentos | 9 | **sobe** |
| Encerrar mudanca estrutural | Review sem forma fixa | Review + FIT com 6 perguntas | **sobe** |

**Metrica de referencia:** "Contexto por papel" (FND-01 §6.3) e "Volume de contexto por
consulta" (FND-06 §9.1). Direcao desejada: desce (PI-14).

**Leitura.** Nenhum papel precisa ler a Fundacao integralmente — a leitura integral e tarefa
de DEP-GOV na auditoria, nao do executor. A tarefa-tipo dominante da fase seguinte e "criar
um componente", e nela o custo cai de cinco documentos para dois.

**Observacao honesta:** este e o **primeiro registro** dessas duas metricas desde que foram
declaradas em ADR-0001. Nao ha serie historica; a comparacao acima e contagem de documentos,
nao medicao de volume. Isso e, em si, o ganho que ADR-0004 pretendia produzir — e tambem o
limite desta primeira aplicacao.

**Resposta:** desce na tarefa-tipo dominante; sobe na leitura integral e no encerramento de
mudanca estrutural, ambos deliberados.

## F6 — Ela favorece reutilizacao?

| Definicao produzida | Reutilizavel por | Especifica do caso? |
|---|---|---|
| 10 relacoes com pares permitidos | Qualquer Framework futuro | Nao |
| 4 perfis de ciclo de vida | Qualquer tipo novo | Nao |
| Teste de Entidade TE-1..TE-7 | Toda candidata futura | Nao |
| Gradacao de instrumento (5 degraus) | Toda proposta de crescimento | Nao |
| 6 perguntas do Fitness Check | Toda mudanca C2/C3 | Nao |
| 12 dependencias proibidas | Toda verificacao estrutural | Nao |
| Matriz de autoridade (§8.2) | Consulta permanente | Parcialmente — lista os 21 tipos atuais |

**Criterio:** DoD-8 — escrito para servir a proxima ocorrencia do problema, nao so a esta.

**Evidencia mais forte:** a simulacao de §6.2 da revisao arquitetural mostrou que **6 de 6**
candidatas recusadas entrariam pelo rito de §11.1 **por acrescimo**, sem alterar estratos,
arquetipos ou relacoes existentes. Um modelo que absorve seis extensoes futuras sem redesenho
e reutilizavel por construcao, nao por declaracao.

**Resposta:** sim.

---

## Ressalvas

| # | Ressalva | Custo assumido | **Dono** | **Gatilho de reavaliacao** |
|---|---|---|---|---|
| R1 | O acrescimo liquido — 1 documento, 1 portao, 2 entidades, 1 artefato por mudanca — nao tem proporcao comprovada. Nenhuma regra foi removida | Se o ganho nao se confirmar, a plataforma carrega uma camada normativa a mais sem contrapartida | DEP-EXE | 1a revisao estrutural: se nenhum Framework tiver sido construido sobre o Meta Model, aplicar EV-08 ao modelo inteiro |
| R2 | O grafo de transicao de estados esta reproduzido em FND-03 §5.1 e FND-09 §7.1 — segunda fonte de verdade, consistente hoje | Emenda a FND-03 §5.1 faria os dois divergirem em silencio | DEP-GOV | 1a revisao de FND-09: substituir o grafo por link, mantendo apenas a tabela de perfis |
| R3 | O arquetipo A2 ARTEFATO reune 19 de 21 entidades e nunca sera invocado para discriminar | Uma abstracao que nao decide nada e peso de leitura | DEP-GOV | 1a revisao estrutural: se A2 nao tiver sido invocado para decidir nenhum caso, consolidar em regra geral (EV-08, AQ-03) |

## Veredito

| Campo | Conteudo |
|---|---|
| Veredito | **`apto-com-ressalva`** |
| Fundamento | As seis perguntas tem sinal observavel; tres revelam degradacao aceita conscientemente, todas com dono e gatilho. Nenhuma revela degradacao sem contrapartida |
| Efeito | Encerra. As tres ressalvas viram **divida declarada**, com data de reavaliacao — nao custo invisivel (FND-07 §9) |
| Data | 2026-07-28 |
| Executado por | DEP-QAR |
| Aprovado por | DEP-EXE |
| Ratificado por (C3) | SOBERANO |

### Nota de conflito de interesse (PI-10)

Este `FIT` avalia, entre outros objetos, o **ADR-0004 que o criou**. DEP-QAR e simultaneamente
o proponente de RFC-0003 e o executor desta verificacao — situacao que FT-02 proibe para o
artefato produzido, e que aqui ocorre porque o mecanismo ainda nao existia quando foi
proposto.

| Campo | Conteudo |
|---|---|
| Mitigacao aplicada | O objeto principal — FND-09 — foi produzido por **DEP-GOV**, nao por DEP-QAR. A independencia esta preservada para a maior parte do escopo |
| Residuo nao mitigado | A avaliacao de aptidao do proprio ADR-0004 e, em rigor, autoavaliacao |
| Consequencia | **A partir de FIT-2026-002, FT-02 se aplica sem excecao.** Nenhuma verificacao futura pode invocar este precedente |
| Registro | Declarado aqui em vez de omitido (PI-10, LV-05) |

## Aprendizado gerado

| Registro APR | Licao |
|---|---|
| A gravar por DEP-KMS (QG-5) | **Duplicacao de diagrama e invisivel a auditoria de conformidade.** As tres divergencias internas de FND-09 e a ressalva R2 sao do mesmo tipo: coerencia **dentro** de um documento normativo, e entre documentos, nao e verificada por nenhum controle que verifique apenas instancias. Condicao de aplicacao: documentos normativos extensos que citam outros. Acao: a auditoria de coerencia normativa (FND-04 §8) passa a verificar tabela ou diagrama reproduzido de outro documento. Dono: DEP-GOV |

## Historico de vereditos sobre este objeto

| FIT | Data | Veredito | Relacao |
|---|---|---|---|
| FIT-2026-001 | 2026-07-28 | `apto-com-ressalva` | Primeiro |
