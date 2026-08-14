---
id: ADR-0045-absorcao-da-triagem-antigravity
titulo: Absorver a triagem do resgate antigravity — planos externos superados, fontes classificadas, poda semestral e nível de autonomia nas Cartas
tipo: adr
versao: 1.1.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-08-14
atualizado_em: 2026-08-14
revisao_prevista: 2027-02-14
decisoes_relacionadas: [ADR-0038, ADR-0039, MSG-2026-0016]
substitui: []
substituido_por: null
classe_mudanca: C2
tipo_decisao: 1
supera: []
superado_por: null
resumo: D1 declara superados os planos de ondas dos relatórios externos; D2 classifica as 3 fontes por lastro; D3 institui a poda semestral de instruções com salvaguardas fora; D4 adota o princípio do nível de autonomia nas Cartas.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: ratificada
---

# ADR-0045: Absorção da triagem do resgate antigravity

> ## ✅ ESTE ADR ESTÁ EM VIGOR POR INTEIRO — ratificado em 2026-08-14.
>
> `status: ativo` · `ratificacao: ratificada`, pelo ato registrado em
> [`MSG-2026-0016`](../memory/operacional/MSG-2026-0016-ato-soberano-ratificacao-adr-0045.md)
> (*"Ratifico o ADR-0045 em 2026-08-14"*). D1/D2 já vigoravam como registro; **D3 e D4
> vigoram desde o ato**, com os defaults `Q1` (1ª poda 2027-02, piloto no Corpo) e `Q2`
> (campo por Carta, na primeira missão que a tocar) sem objeção.
> A fonte corrente do estado é o frontmatter, nunca este bloco.

## Propósito

Instrumentar a Opção A de
[RFC-0040](../rfcs/RFC-0040-absorcao-da-triagem-antigravity.md): dar destino normativo
às quatro consequências da triagem de 2026-08-14
(`LucaX-Enterprise-Research/docs/handoffs/2026-08-14-triagem-resgate-antigravity.md`).

## 1. Contexto

Três peças externas de análise chegaram propondo planos de evolução para o
`ai-orchestrator-starter`; o fit-gap medido mostrou **15 de ~30 recomendações já
absorvidas** pelo Corpo e o único gap acionável entregue na mesma data (E6.4). Restou
para a Mente o que é governança: o estado dos planos, o lastro das fontes, e duas
práticas boas que as fontes revelaram.

## 2. Decisão

### D1 — Os planos externos estão SUPERADOS *(vigora como registro)*

O plano de 5 ondas da **auditoria de 2026-08-12** e o plano de 4 ondas da **segunda
varredura de 2026-08-13** ficam declarados **SUPERADOS** pelo checklist vivo do Corpo
(`lucax-enterprise/CLAUDE.md §7`) e pelo roadmap canônico desta Mente. Nenhuma sessão
futura os trata como plano vigente; consulta a eles é consulta a fonte histórica.
*(Ordem original preservada: as peças não são alteradas nem apagadas — o estado é
declarado AQUI, na sede normativa.)*

### D2 — As três fontes ficam classificadas por lastro *(vigora como registro)*

| Fonte | Sede | Lastro |
|---|---|---|
| Auditoria integral (2026-08-12) | `_backups\transcricoes-videos-2026-08-14-resgate-antigravity\auditoria_acervo_e_evolucao_pos_roadmap.md` | 🥈 análise secundária; números de acervo conferíveis |
| Segunda varredura (2026-08-13) | mesma pasta, `segunda_varredura_ativos_residuais.md` | 🥈 idem; percentuais de eficácia citados são 🥉 |
| Transcrições Whisper `base` (2026-08-14) | mesma pasta, `transcricoes_completas_dos_videos.md` | **🥉 — pista, nunca conclusão.** Transcrição fonética degradada: nenhum número ou nome próprio dela se cita como fato |

Contradição registrada e **não resolvida**: 175 vídeos (auditoria) × 207 (transcrição).
Reconciliar por contagem de ferramenta na fonte bruta é pendência da **Oficina**.

### D3 — Rito semestral de poda de instruções *(exige ato)*

A cada **6 meses**, teste de necessidade sobre as instruções **comportamentais** da
fábrica (CLAUDE.md, skills, hooks): remover o patch, observar o modelo vigente,
recolocar só o que degradar. **Fora da poda, sempre:** matéria 🔒 da hierarquia
normativa — segurança, backup, credencial, escopo e honestidade — e todo bloqueio de
comando destrutivo. Poda é para *patch de comportamento de modelo antigo*, nunca para
*salvaguarda*. Primeira execução: **2027-02**, começando pelo Corpo como piloto
(RFC-0040 `Q1`, default). Lastro: prática exercida pelo próprio fabricante
(Anthropic removeu ~80% do system prompt do Claude Code para a família 5) e
recomendação pública de Boris Cherny, criador do Claude Code (YC Startup School,
jul/2026) — fonte 🥈, ressalva declarada: a primária (vídeo da talk) não foi
localizada nesta sessão.

### D4 — Nível de autonomia nas Cartas *(exige ato)*

Toda missão de Carta criada ou emendada a partir da vigência declara
`nivel_de_autonomia`: **conduzido-por-humano · assistido-por-humano · autônomo** —
o princípio da matriz de delegação observada no acervo (`10_APLICACOES`). Cartas
paradas **não** são reabertas só para ganhar o campo (RFC-0040 `Q2`, default:
por Carta, na primeira missão que a tocar). A redação material do campo no template
das Cartas segue o rito próprio de manutenção das Cartas.

## 3. Justificativa

D1/D2 custam zero e fecham o defeito de controle de autoridade no dia em que nasceu.
D3 é a regra de zero desperdício aplicada ao próprio contexto, com o único risco real
(podar salvaguarda) bloqueado por desenho. D4 dá às Cartas a pergunta que a operação
com clientes reais vai fazer primeiro: *quem decide — o humano ou o agente?*

## 4. Evidências

| # | Evidência | Fonte |
|---|---|---|
| `E1` | Fit-gap: 15 de ~30 recomendações já absorvidas; gap único entregue (E6.4) | Triagem §1a/§1b; Corpo `ca3b826` |
| `E2` | Corte de ~80% do system prompt do Claude Code pela Anthropic (jul/2026) | Fonte 🥈 verificada em 2026-08-14 |
| `E3` | Recomendação de poda semestral, com exceção de salvaguardas | Boris Cherny, YC Startup School — 🥈 |
| `E4` | Matriz de delegação em 3 níveis no acervo | `10_APLICACOES` (xlsx + vídeos) — 🥉/🥈 |
| `A1` | **Ausente, declarado:** fonte primária da talk de D3 | RFC-0040 §5 fato 5 |

## 5. Riscos e mitigação

| # | Risco | Prob. | Impacto | Mitigação |
|---|---|---|---|---|
| `RA-1` | Poda remover instrução ainda necessária | Média | Médio | Remover→observar→recolocar; piloto antes da fábrica; salvaguardas fora por desenho |
| `RA-2` | Campo de autonomia virar decoração | Baixa | Baixo | Só em missão nova/emendada; nunca reabre Carta parada |

## 6. Plano de reversão

| Campo | Conteúdo |
|---|---|
| **Reversível?** | **Sim.** D1/D2 são registro (revoga-se por ADR); D3 revoga-se cancelando o rito antes da 1ª execução; D4 revoga-se antes da 1ª emenda de Carta |
| **Quem executa** | `DEP-GOV`, sob ato do Soberano para D3/D4 |
| **Backup** | Cópia datada pré-t79 (1164/1164), ponto de rollback `4e0bcb6` |

## 7. Classificação

| Campo | Valor |
|---|---|
| **Classe de mudança** | `C2` — cria rito (D3) e princípio de contrato (D4); `0` fundacionais emendadas |
| **Tipo de reversibilidade** | `Tipo 1` |
| **Aprovador/Ratificador** | `SOBERANO` para D3/D4; `DEP-GOV` para D1/D2 |
| Instrumento | RFC → ADR → Ratificação ([RFC-0040](../rfcs/RFC-0040-absorcao-da-triagem-antigravity.md)) |
| Data da decisão | **2026-08-14** — D1/D2 na emissão; D3/D4 pelo ato [`MSG-2026-0016`](../memory/operacional/MSG-2026-0016-ato-soberano-ratificacao-adr-0045.md) |
| Data de vigência | **2026-08-14** |

> **Por que `C2` e não `C3`.** Nenhum princípio imutável, linha vermelha ou hierarquia
> é alterado — D3 explicitamente se subordina à matéria 🔒, e D4 não muda quem decide
> (o Soberano continua ratificando Carta); cria-se rito e campo, não autoridade.

## 8. Questões submetidas ao Soberano

| # | Questão | Bloqueia? |
|---|---|---|
| `Q1` | 1ª poda: piloto no Corpo (default) ou fábrica inteira? | ❌ |
| `Q2` | Campo de autonomia: por Carta na primeira missão (default) ou nas 8 de uma vez? | ❌ |

## 9. Revisão

| Campo | Conteúdo |
|---|---|
| **Gatilho por evento** | A 1ª poda executada (medir: o que saiu, o que voltou, o que degradou) |
| **Gatilho por evento** | A 1ª Carta emendada com `nivel_de_autonomia` |
| **Gatilho temporal** | 2027-02-14 |
| **Responsável** | `DEP-QAR` |

## 10. Rastreabilidade

| Campo | Conteúdo |
|---|---|
| Origem | [RFC-0040](../rfcs/RFC-0040-absorcao-da-triagem-antigravity.md) · triagem de 2026-08-14 (Oficina, handoffs) |
| Execução-irmã no Corpo | E6.4 golden runs, commit `ca3b826` (mesma triagem, matéria técnica) |
| Ato de ratificação | [MSG-2026-0016](../memory/operacional/MSG-2026-0016-ato-soberano-ratificacao-adr-0045.md) — "Ratifico o ADR-0045 em 2026-08-14" (décimo sexto ato) |
| Achados/pendências que permanecem abertos | Registro de entrada físico das 3 peças (Oficina) · reconciliação 175×207 (Oficina) |

---

## Checklist de validade (`FND-07 §4.1`)

- [x] `VD-01` — alternativas reais + "não fazer nada" (`RFC-0040 §5`)
- [x] `VD-02` — critérios antes das alternativas
- [x] `VD-03` — nenhuma alternativa de palha
- [x] `VD-04` — tradeoff aceito explícito (§5, `RA-1`)
- [x] `VD-05` — ausência de evidência declarada (`A1`)
- [x] `VD-06` — reversão declarada (§6)
- [x] `VD-07` — impacto mapeado (`RFC-0040 §7`)
- [x] `VD-08` — data e responsável presentes
- [x] `VD-09` — gatilhos de revisão definidos (§9)
- [x] Proponente ≠ aprovador · revisor ≠ autor

## Histórico de versões

| Versão | Data | Autor | Mudança |
|---|---|---|---|
| 1.0.0 | 2026-08-14 | DEP-GOV | Decisão inicial: D1/D2 vigentes como registro; D3/D4 `em-revisao`, ratificação pendente. Lastro de D3 elevado a 🥈 por verificação da mesma data, com a primária declarada ausente. |
| 1.1.0 | 2026-08-14 | DEP-GOV | **RATIFICADO** — `MSG-2026-0016`, *"Ratifico o ADR-0045 em 2026-08-14"* (décimo sexto ato). `status: ativo`, `ratificacao: ratificada`. `Q1`/`Q2` sem objeção — valem os defaults (piloto no Corpo; por Carta). Compromissos criados: 1ª poda **2027-02**; `nivel_de_autonomia` obrigatório em missão de Carta criada/emendada. |
