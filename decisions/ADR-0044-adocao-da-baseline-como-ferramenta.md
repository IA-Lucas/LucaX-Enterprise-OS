---
id: ADR-0044-adocao-da-baseline-como-ferramenta
titulo: Adotar TOL-local-baseline-do-acervo como a primeira Ferramenta ratificada do acervo
tipo: adr
versao: 1.1.0
status: ativo
camada_memoria: estrategica
autor: DEP-TLS
proprietario: DEP-TLS
aprovador: SOBERANO
criado_em: 2026-08-14
atualizado_em: 2026-08-14
revisao_prevista: 2027-02-14
decisoes_relacionadas: [ADR-0041, MSG-2026-0015]
substitui: []
substituido_por: null
classe_mudanca: C2
tipo_decisao: 1
supera: []
superado_por: null
resumo: Adota TOL-local-baseline-do-acervo como primeira Ferramenta vigente, sem tocar o script, sem admitir dado sensível e sem criar entidade nova.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: ratificada
---

# ADR-0044: Adoção da baseline canônica como Ferramenta

> ## ✅ ESTE ADR ESTÁ EM VIGOR — ratificado em 2026-08-14.
>
> `status: ativo` · `ratificacao: ratificada`, pelo ato registrado em
> [`MSG-2026-0015`](../memory/operacional/MSG-2026-0015-ato-soberano-ratificacao-adr-0044.md)
> (*"Ratifico o ADR-0044 em 2026-08-14"*). `tools/TOL-local-baseline-do-acervo.md` passa a
> `status: ativo` / `ratificacao: ratificada` pela mesma aplicação, e o elo de Ferramenta em
> `1.19` **conta como instanciado**.
>
> **A fonte corrente do estado é o frontmatter** (`FND-10 §5.4`, `PJ-04`), nunca este bloco.

## Propósito

Registrar a decisão de **adotar formalmente `TOL-local-baseline-do-acervo`** como Ferramenta
vigente, pelo Tool Contract de [ADR-0041](ADR-0041-framework-de-ferramentas-e-modelos.md).
A proposta não move nem altera o script `baseline.sh`; adota a ficha que já o descreve
integralmente sob os 18 blocos de `TF-09`.

## Escopo

| Item | Definição |
|---|---|
| **Inclui** | A ratificação da ficha já redigida; a mudança de `status: rascunho` para `ativo` e `ratificacao: pendente` para `ratificada`; a vigência de `tools/` como diretório canônico |
| **Não** inclui | Qualquer alteração ao script; adoção de outra Ferramenta; correção de `TPL-ferramenta` (`AF-1`/`AF-2`, rito próprio) |

## Responsáveis

| Papel | Quem |
|---|---|
| Proponente | `DEP-TLS` |
| Revisor | `DEP-QAR` |
| Aprovador/Ratificador | `SOBERANO` |

---

## 1. Contexto

O instrumento de baseline é citado em oito gerações (`IR-BL/1` a `IR-BL/8`) e mais de vinte
tokens de lease da Mente, mas nunca teve ficha de Ferramenta até
[`RFC-0039`](../rfcs/RFC-0039-adocao-da-baseline-como-ferramenta.md) submeter a questão. A
ficha `tools/TOL-local-baseline-do-acervo.md` já existe, redigida com o contrato completo de
`ADR-0041`.

## 2. Problema / Pergunta de decisão

O acervo depende, em todo lease de escrita, de um instrumento sem autoridade formal — a
lacuna entre uso real e Ferramenta adotada. **O Soberano deve ratificar a ficha existente?**

## 3. Critérios de decisão

Os mesmos `K1` a `K6` de `RFC-0039 §4`, com peso bloqueante em `K1` (sinal já observado) e
`K2` (risco de exposição de dado).

## 4. Alternativas consideradas

Ver `RFC-0039 §5` — Opção A (ratificar agora, recomendada), Opção B (manter sem ratificar) e
Opção Z (adiar). Este ADR instrumenta a **Opção A**.

## 5. Decisão

**Adotar `TOL-local-baseline-do-acervo` como Ferramenta vigente do acervo**, mediante o ato
do Soberano sobre este texto. Ao vigorar:

1. `tools/TOL-local-baseline-do-acervo.md` passa a `status: ativo` / `ratificacao:
   ratificada`, com data do ato preenchida em §11 (Rastreabilidade).
2. `tools/` deixa de ser "fase futura" (`FND-03 §7`) e passa a diretório canônico com
   instância vigente.
3. `1.19` do roadmap ganha o elo de Ferramenta instanciado — de `3/10` para `4/10`.
4. **`0` bytes do script `baseline.sh` mudam.** A adoção é do registro de governança, nunca
   do código.
5. **`0` entidades, classes, tipos, templates, papéis ou portões são criados** — `TOL` e o
   contrato de `ADR-0041` já existem integralmente.

## 6. Justificativa

O instrumento tem o perfil de risco mais baixo possível entre os componentes que exigem
ratificação: `dado_trafegado: nenhum`, `0` chamada de rede, `0` escrita (`§7` da ficha,
"read-only" declarado no próprio script), `0` credencial. O sinal de uso (`PI-14`) é o mais
forte já medido no acervo para uma Ferramenta — oito gerações reais, não uma hipótese.
Adotar fecha a assimetria entre autoridade de fato e autoridade formal antes que ela vire
achado de auditoria por conta própria.

## 7. Avaliação do portão — `TF-10` basta?

O ciclo de dez etapas de `TF-10` foi seguido: Proposta e Autoria (`DEP-TLS`, a ficha e esta
RFC/ADR), Revisão e Avaliação de risco (`DEP-QAR`, manifestação em `RFC-0039 §10`),
Aprovação (`SOBERANO`, pendente), Ratificação (`SOBERANO`, indelegável, pendente), Registro
(`DEP-GOV`, após o ato). **Uma lacuna medida:** `DEP-EXE` não se manifestou — declarada em
`RFC-0039 §10`, não suprida (`PI-10`, `LM-03`), e não bloqueante porque `TF-10` não lista
`DEP-EXE` como consulta obrigatória para adoção de Ferramenta (diferente do que `FND-01
§7.3` exige para Produto).

## 8. Evidências

| # | Evidência | Fonte |
|---|---|---|
| `E1` | Uso real em oito gerações do instrumento | Cabeçalho de `baseline.sh` |
| `E2` | 20+ tokens de lease citando o instrumento | `_leases/LucaX-Enterprise-OS.lease` |
| `E3` | Ficha completa com os 18 blocos de `TF-09` | `tools/TOL-local-baseline-do-acervo.md` |
| `E4` | Quatro provas de inércia por geração, incluindo a mais recente (`IR-BL/8`) | Cabeçalho de `baseline.sh`, seção `IR-BL/8` |
| `A1` | **Evidência ausente, declarada:** manifestação formal de `DEP-EXE` | `RFC-0039 §10` |

## 9. Riscos e mitigação

| # | Risco | Prob. | Impacto | Mitigação |
|---|---|---|---|---|
| `RA-1` | Precedente de adoção apressada de Ferramentas de maior risco | Baixa | Médio | Este caso é atípico (risco quase nulo); cada adoção futura segue `TF-10` por inteiro, sem atalho |
| `RA-2` | Ratificação ocorrer sem revisão integral da ficha | Baixa | Médio | A ficha de 18 blocos acompanha este ADR por referência direta; nenhum conteúdo é resumido ou ocultado |

## 10. Plano de reversão

| Campo | Conteúdo |
|---|---|
| **Reversível?** | **Sim, trivialmente.** Reverter é mudar `status`/`ratificacao` de volta a `rascunho`/`pendente` — `0` dependente é criado por esta adoção, porque o script já era usado antes dela |
| **O que a reversão NÃO desfaz** | O uso factual do script continua (ele já era invocado antes desta ficha existir); reverter tira a autoridade formal, não o uso |
| **Quem executa** | `DEP-GOV`, sob ato do Soberano |
| **Backup necessário** | Cópia datada do acervo antes da aplicação (`PI-07`) |

## 11. Classificação

| Campo | Valor |
|---|---|
| **Classe de mudança** | `C2` — Estrutural |
| **Tipo de reversibilidade** | `Tipo 1` |
| **Aprovador/Ratificador** | `SOBERANO` — indelegável (`TF-10`) |
| Instrumento | RFC → ADR → Ratificação ([RFC-0039](../rfcs/RFC-0039-adocao-da-baseline-como-ferramenta.md)) |
| Data da decisão | **2026-08-14** — [`MSG-2026-0015`](../memory/operacional/MSG-2026-0015-ato-soberano-ratificacao-adr-0044.md) |
| Data de vigência | **2026-08-14** |

> **Por que `C2` e não `C3`.** Cria um componente (`FND-04 §2`), não altera princípio
> imutável, linha vermelha, hierarquia normativa ou a Fundação. `0` fundacionais emendadas.
>
> **Por que `Tipo 1`.** `FND-04 §6` linha *Ferramenta* já fixa adoção como `C2 · Tipo 1` com
> ratificação do Soberano — **a classificação é derivada de norma, não escolhida**
> (`TF-10`).

## 12. Questões submetidas ao Soberano

| # | Questão | Bloqueia? |
|---|---|---|
| `Q1` | Confirmar `criticidade: média` da ficha, ou ajustar para `baixa`/`alta` | ❌ Não — segue o valor da ficha sem objeção |
| `Q2` | O instrumento deve ganhar dono distinto de `DEP-TLS`? | ❌ Não |

## 13. Revisão

| Campo | Conteúdo |
|---|---|
| **Gatilho por evento** | A primeira falha *plausível e errada* observada no instrumento (`L4` de `ADR-0041`) |
| **Gatilho por evento** | A primeira emenda de `TPL-ferramenta` que sane `AF-1`/`AF-2` — reavaliar se a ficha precisa de ajuste de forma |
| **Gatilho temporal** | 2027-02-14 |
| **Responsável pela revisão** | `DEP-QAR` |

## 14. Rastreabilidade

| Campo | Conteúdo |
|---|---|
| Origem | [RFC-0039](../rfcs/RFC-0039-adocao-da-baseline-como-ferramenta.md) |
| Ato de ratificação | [MSG-2026-0015](../memory/operacional/MSG-2026-0015-ato-soberano-ratificacao-adr-0044.md) — "Ratifico o ADR-0044 em 2026-08-14" |
| Artefatos criados pelo ato | *(nenhum novo — a ficha já existe; o ato só muda `status`/`ratificacao` dela)* |
| Artefatos do acervo alterados pelo ato | `tools/TOL-local-baseline-do-acervo.md` (`status`, `ratificacao`, `atualizado_em`) |
| Bytes do script alterados | `0` |
| Achados fechados por esta decisão | `AF-3` de `ADR-0041` (quanto à vigência; o diretório já existia desde a criação da ficha) |
| Achados que permanecem abertos | `AF-1`/`AF-2` de `ADR-0041` (defeitos de `TPL-ferramenta`) — não tocados por esta adoção |

---

## Checklist de validade (`FND-07 §4.1`)

- [x] `VD-01` — 2 alternativas reais + "não fazer nada" (`RFC-0039 §5`)
- [x] `VD-02` — critérios declarados antes das alternativas
- [x] `VD-03` — nenhuma alternativa de palha
- [x] `VD-04` — tradeoff aceito explícito (§9)
- [x] `VD-05` — ausência de evidência declarada (`A1`, §8)
- [x] `VD-06` — reversão declarada, trivial (§10)
- [x] `VD-07` — impacto mapeado (`RFC-0039 §7`)
- [x] `VD-08` — data e responsável presentes
- [x] `VD-09` — gatilhos de revisão definidos (§13)
- [x] Proponente ≠ aprovador · revisor ≠ autor

## Histórico de versões

| Versão | Data | Autor | Mudança |
|---|---|---|---|
| 1.0.0 | 2026-08-14 | DEP-TLS | Decisão inicial, **`em-revisao`, não vigente**. Instrumenta a Opção A de `RFC-0039`: adota a ficha já redigida, `0` bytes do script alterados, `0` entidades criadas. Uma ausência de evidência declarada (`DEP-EXE`). Duas questões não bloqueantes ao Soberano. |
| 1.1.0 | 2026-08-14 | DEP-GOV | **RATIFICADO** — `MSG-2026-0015`, *"Ratifico o ADR-0044 em 2026-08-14"*. `status: ativo`, `ratificacao: ratificada`. Nenhuma das duas questões (`Q1`/`Q2`) recebeu objeção — permanecem no valor original da ficha. `tools/TOL-local-baseline-do-acervo.md` aplicado na mesma mudança. |
