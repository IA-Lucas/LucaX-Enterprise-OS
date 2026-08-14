---
id: RFC-0039-adocao-da-baseline-como-ferramenta
titulo: A baseline canônica do acervo deve ser ratificada como Ferramenta TOL, ou continua operando sem registro formal apesar do uso real?
tipo: rfc
versao: 1.0.0
status: aprovado
camada_memoria: estrategica
autor: DEP-TLS
proprietario: DEP-TLS
aprovador: DEP-GOV
criado_em: 2026-08-14
atualizado_em: 2026-08-14
revisao_prevista: 2027-02-14
decisoes_relacionadas: [ADR-0041]
substitui: []
substituido_por: null
classe_mudanca: C2
prazo_analise: 2026-09-14
resumo: Submete ao Soberano a ratificação de TOL-local-baseline-do-acervo como primeira Ferramenta adotada do acervo, com custo quase nulo e uso já real e repetido.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# RFC-0039: Adoção da baseline canônica como Ferramenta

> **Pergunta em uma frase.** O instrumento de baseline já é invocado em toda escrita sob
> lease da Mente — oito gerações, mais de vinte tokens — mas nunca teve ficha `TOL`
> ratificada. Esta RFC pergunta se o Soberano deve **ratificar agora** a ficha já redigida
> (`TOL-local-baseline-do-acervo.md`), tornando-a a primeira Ferramenta formalmente
> adotada do acervo.

## Propósito

Submeter à análise a adoção de `TOL-local-baseline-do-acervo` como Ferramenta ratificada,
pelo Tool Contract de [ADR-0041](../decisions/ADR-0041-framework-de-ferramentas-e-modelos.md)
(`TF-05` a `TF-32`). A ficha já existe, redigida com os 18 blocos exigidos por `TF-09`; esta
RFC não propõe conteúdo novo — propõe que o Soberano decida se a proposta vira Ferramenta
vigente.

## Escopo

| Item | Definição |
|---|---|
| **Inclui** | A ratificação de `TOL-local-baseline-do-acervo`; a criação de `tools/` como diretório canônico (já ocorrida na ficha, pendente de vigência); a avaliação de se o Tool Contract de `ADR-0041` basta no primeiro caso real |
| **Não** inclui | Qualquer alteração ao script `baseline.sh` em si; adoção de qualquer outra Ferramenta; correção de `TPL-ferramenta` (`AF-1`/`AF-2`, rito próprio de `TPL`, `DEP-GOV + DEP-TLS`); avanço de `1.19` para além do elo desta Ferramenta |
| **Subordinado a** | [FND-04 §6](../foundation/04-governanca.md) linha *Ferramenta* · [FND-09 §8.2](../foundation/09-meta-model.md) linha `TOL` · [ADR-0041](../decisions/ADR-0041-framework-de-ferramentas-e-modelos.md) `TF-10` |

## Responsáveis

| Papel | Quem | Fundamento |
|---|---|---|
| Proponente | **DEP-TLS** | `TF-10`, etapa Proposta |
| Área que deve se manifestar | **DEP-EXE** | `TF-10`, etapa Aprovação |
| Revisor independente | **DEP-QAR** | `TF-10`, etapa Revisão/Avaliação de risco |
| Validação de forma | **DEP-GOV** | `FND-09 §8.2` linha `RFC` |
| Decide a matéria | **SOBERANO** | `TF-10` — Ratificação, indelegável |
| Prazo de manifestação | **2026-09-14** | — |

---

## 1. Situação atual — fatos verificáveis

| # | Fato | Medido em |
|---|---|---|
| 1 | O instrumento existe e é invocado desde `IR-BL/1`; esta sessão mediu **oito gerações** (`IR-BL/1` a `IR-BL/8`) e **mais de vinte tokens de lease** que o citam | Cabeçalho do próprio script; `_leases/LucaX-Enterprise-OS.lease` |
| 2 | `tools/` não existia até esta sessão criar `TOL-local-baseline-do-acervo.md` — `AF-3` de `ADR-0041`, agora fechado quanto ao diretório | `governance/artifact-registry.md` 2.54.0 |
| 3 | A ficha está redigida com os 18 blocos de `TF-09`, `status: rascunho`, `ratificacao: pendente` | `tools/TOL-local-baseline-do-acervo.md` |
| 4 | O instrumento é **read-only** — `0` escrita, `0` credencial, `0` chamada de rede, `0` dado sensível — medido no próprio código e nas quatro provas de inércia de cada geração | `baseline.sh` §"Uso"; §7 e §10 da ficha |
| 5 | `0` Ferramentas estão adotadas no acervo hoje; `1.19` do roadmap tem `0` elos de Ferramenta instanciados | `governance/roadmap-canonico.md` |

## 2. Problema

O acervo tem uma norma completa sobre Ferramenta (`ADR-0041`, 32 regras) e **zero
Ferramentas adotadas**, enquanto um instrumento real já opera sob a autoridade **implícita**
de estar citado em CLAUDE.md e no catálogo mestre — nunca sob a autoridade **formal** que
`FND-09 §8.2` linha `TOL` exige. A ficha redigida fecha a lacuna de registro; falta a
ratificação para fechar a lacuna de autoridade.

**Quem perde com o estado atual:** o próprio protocolo de lease, que depende deste
instrumento para medir `estado_fenceado`/`estado_no_fechamento`, sem que o instrumento em
si tenha status normativo formal — a mesma classe de risco que motivou `ADR-0041 §1` a
medir o defeito do template antes de qualquer regra.

## 3. Pergunta de decisão

**O Soberano deve ratificar `TOL-local-baseline-do-acervo` agora, tornando-a a primeira
Ferramenta vigente do acervo, ou a ficha permanece `rascunho` indefinidamente enquanto o
script continua em uso de fato?**

## 4. Critérios de avaliação

| # | Critério | Peso | Como se mede |
|---|---|---|---|
| `K1` | Uso real já observado, não previsto (`PI-14`) | **Bloqueante** | Oito gerações, 20+ tokens — ver §1 |
| `K2` | Risco de exposição de dado | **Bloqueante** | `dado_trafegado: nenhum`; `0` rede; §4/§5 da ficha |
| `K3` | Custo de adoção | Alto | `0` bytes de código mudam; só o ato formal |
| `K4` | Reversibilidade | Alto | Ver §9 (Plano de reversão) |
| `K5` | Coerência com o Tool Contract de `ADR-0041` | Alto | 18 blocos presentes na ficha, `TF-05` a `TF-30` |
| `K6` | Desbloqueia elo de `1.19` | Médio | Sim, um dos dez elos passa a ter instância vigente |

## 5. Opções

### Opção A — **Ratificar agora** *(recomendada)*

| Campo | Conteúdo |
|---|---|
| Descrição | O Soberano assina o ato sobre `ADR-0044`; `TOL-local-baseline-do-acervo.md` passa a `status: ativo` / `ratificacao: ratificada` |
| A favor | Único candidato com uso já medido e repetido; risco mínimo (`0` dado sensível, `0` rede, `0` escrita); fecha a lacuna entre uso de fato e autoridade formal; desbloqueia um elo real de `1.19` |
| Contra | Formaliza um script que já "funcionava" sem ficha — alguém pode ler a adoção como burocracia sobre algo que não estava quebrado |
| Custo | 2 artefatos novos nesta RFC/ADR, `0` bytes no script, `0` fontes normativas emendadas |
| Risco | `RR-1` abaixo |
| Avaliação | `K1` ✔ · `K2` ✔ · `K3` ✔ · `K4` ✔ · `K5` ✔ · `K6` ✔ |

### Opção B — **Não ratificar; manter como instrumento não-governado**

| Campo | Conteúdo |
|---|---|
| Descrição | A ficha permanece `rascunho`; o script continua em uso, citado no `CLAUDE.md`, mas sem Ferramenta formalmente adotada |
| A favor | Nenhum ato é gasto agora |
| Contra | **Mantém a assimetria que motivou esta RFC:** uso real sem autoridade formal. Nenhum elo de `1.19` avança por esta via |
| Custo | Zero agora; custo permanente de governança informal |
| Risco | O instrumento mais citado do protocolo de lease continua sem status normativo — se um dia falhar ou for questionado, não há ADR/ratificação a que apelar |
| Avaliação | `K1` ✔ mas irrelevante sob esta opção · `K6` **falha** |

### Opção Z — **Adiar (não decidir agora)**

| Campo | Conteúdo |
|---|---|
| Consequência de manter o estado atual | Idêntica à Opção B, mas sem fechar a pergunta — revisitada depois |
| Custo da inação | Nenhum novo, mas a pergunta permanece em aberto sem prazo |
| Por que não venceu | Não há nova evidência a esperar — o sinal (`K1`) já está observado; adiar não produz informação nova, só posterga uma decisão de baixo risco |

## 6. Recomendação do proponente

**Opção A.** O risco é o mais baixo possível entre os componentes que exigem ratificação
(`0` dado sensível, `0` rede, `0` escrita), o sinal de uso já está observado cinco vezes mais
do que o mínimo exigido por qualquer precedente de adoção neste acervo, e o custo de
formalizar é, literalmente, um ato — nenhuma linha de código muda.

## 7. Impacto previsto

| Dimensão | Impacto |
|---|---|
| Departamentos | `DEP-TLS` passa a ter a primeira Ferramenta sob custódia formal |
| Componentes | `+1` Ferramenta vigente. `tools/` deixa de ser "fase futura" |
| Normas afetadas | `0` fundacionais emendadas |
| Entidades e tipos novos | `0` — `TOL` já existe |
| Camadas de memória | Técnica (a ficha já grava o instrumento) |
| `1.19` | Passa a ter **um elo de Ferramenta instanciado** — de `3/10` para `4/10` (Skill, Workflow, aresta, Ferramenta) |
| Ganho `PI-14` pretendido e sinal que o comprova | Organização e autoridade formal sobre um instrumento crítico já em uso — sinal observado em oito gerações e vinte tokens |

## 8. Riscos

| # | Risco | Impacto | Mitigação |
|---|---|---|---|
| `RR-1` | Ratificar sem o Soberano ter revisado a ficha inteira (18 blocos) | Médio | A ficha completa acompanha esta RFC; o ADR (§12) lista as questões submetidas, nenhuma delas oculta conteúdo |
| `RR-2` | O ato ser lido como precedente para adoção apressada de outras Ferramentas | Baixo | Este caso é atípico (risco quase nulo, uso já medido); cada adoção futura tem rito próprio (`TF-10`), este RFC não o abrevia |

## 9. Perguntas em aberto

| # | Questão | Quem responde | Bloqueia? |
|---|---|---|---|
| `Q1` | Confirmar `criticidade: média` da ficha — o Soberano concorda, ou é `baixa`/`alta`? | **SOBERANO** | ❌ Não — o ADR segue com o valor da ficha se não houver objeção |
| `Q2` | O instrumento deve ganhar `dono` distinto de `DEP-TLS` (ex.: `DEP-GOV`, que hoje o mantém de fato)? | **SOBERANO** | ❌ Não |

## 10. Manifestações

| Área | Posição | Fundamento | Data |
|---|---|---|---|
| `DEP-TLS` | apoia a Opção A | Proponente; §6 | 2026-08-14 |
| `DEP-QAR` | apoia | Risco mínimo medido em §4/§5/§7 da ficha, sem dado sensível nem rede | 2026-08-14 |
| `DEP-GOV` | apoia quanto à forma | Contrato completo (`TF-05`/`TF-09`), rastreabilidade presente | 2026-08-14 |
| `DEP-EXE` | *(consulta obrigatória — não registrada nesta sessão)* | `TF-10`, etapa Aprovação | — |
| `SOBERANO` | *(não ocorrido)* | — | — |

## 11. Resultado

| Campo | Conteúdo |
|---|---|
| Decisão | **aceita, quanto à forma** — gera `ADR-0044`, que **não entra em vigor** sem ato |
| ADR gerado | [`ADR-0044`](../decisions/ADR-0044-adocao-da-baseline-como-ferramenta.md) — `em-revisao`, `ratificacao: pendente` |
| Data | 2026-08-14 |
| Responsável | DEP-TLS, com validação de forma por DEP-GOV |

---

## Checklist de validade

| # | Item | Estado |
|---|---|---|
| 1 | Pergunta clara | ✅ §3 |
| 2 | Alternativas analisadas — 2 reais + "não fazer nada" | ✅ A, B, Z |
| 3 | Nenhuma alternativa de palha | ✅ B é status quo real, não descartada por construção |
| 4 | Critérios antes das opções | ✅ §4 antes de §5 |
| 5 | Recomendação obrigatória presente | ✅ §6 |
| 6 | Prazo de análise definido | ✅ 2026-09-14 |
| 7 | Evidência ausente declarada | ✅ §10, linha `DEP-EXE` |
| 8 | Impacto mapeado | ✅ §7 |
| 9 | `revisor` ≠ `autor` | ✅ `DEP-TLS` × `DEP-QAR` |
| 10 | Nenhuma entidade, tipo, camada ou norma criada | ✅ §7 |

## Histórico de versões

| Versão | Data | Autor | Mudança |
|---|---|---|---|
| 1.0.0 | 2026-08-14 | DEP-TLS | Proposta inicial. Submete a ratificação da primeira Ferramenta do acervo, com risco mínimo medido e uso já real (oito gerações, 20+ tokens). Recomenda a Opção A. Declara a ausência de manifestação de `DEP-EXE`. |
