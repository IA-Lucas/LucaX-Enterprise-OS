---
id: RFC-0040-absorcao-da-triagem-antigravity
titulo: A Mente absorve a triagem do resgate antigravity — planos externos superados, fontes classificadas, poda semestral e nível de autonomia nas Cartas?
tipo: rfc
versao: 1.0.0
status: aprovado
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-GOV
criado_em: 2026-08-14
atualizado_em: 2026-08-14
revisao_prevista: 2027-02-14
decisoes_relacionadas: [ADR-0038, ADR-0039]
substitui: []
substituido_por: null
classe_mudanca: C2
prazo_analise: 2026-09-14
resumo: Submete as 4 decisões da triagem de 2026-08-14 — superar os planos de ondas dos relatórios externos, classificar as 3 fontes por lastro, instituir a poda semestral de instruções (salvaguardas fora) e dar nível de autonomia às Cartas.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: pendente
---

# RFC-0040: Absorção da triagem do resgate antigravity

> **Pergunta em uma frase.** Chegaram três peças externas de análise (auditoria
> 2026-08-12, segunda varredura 2026-08-13, transcrições Whisper 2026-08-14) propondo
> planos de evolução para um alvo que já evoluiu; a triagem do Corpo mediu o fit-gap.
> Esta RFC pergunta se a Mente **absorve as quatro consequências normativas** da
> triagem — ou deixa dois planos concorrentes vivos e as fontes sem classificação.

## Propósito

Dar destino normativo ao que a triagem
(`LucaX-Enterprise-Research/docs/handoffs/2026-08-14-triagem-resgate-antigravity.md`)
apontou como matéria da Mente (§2 dela). O que era matéria do Corpo já foi executado
na mesma data (E6.4, commit `ca3b826` do Corpo); o que é da Oficina ficou registrado
lá como pendência. Aqui entram só as decisões de governança.

## Escopo

| Item | Definição |
|---|---|
| **Inclui** | D1 superação dos planos externos · D2 classificação das fontes por lastro · D3 rito semestral de poda de instruções · D4 princípio do nível de autonomia nas Cartas |
| **Não** inclui | O registro de entrada físico das peças (pendência da Oficina, §3 da triagem) · a reconciliação 175×207 vídeos (idem) · qualquer mudança de código no Corpo · a redação material da emenda de cada Carta (fica para a manutenção das Cartas, sob rito próprio) |
| **Subordinado a** | Hierarquia normativa do Padrão Ouro (matéria 🔒 nunca é derrogada por poda) · [ADR-0039] (contrato fábrica↔acervo e Cartas) · protocolo de conteúdo hostil (CLAUDE.md da Mente) |

## Responsáveis

| Papel | Quem | Fundamento |
|---|---|---|
| Proponente | **DEP-GOV** | Absorção de fonte externa é matéria de governança |
| Revisor independente | **DEP-QAR** | `FND-09 §8.2` linha `RFC` |
| Decide D1/D2 | **DEP-GOV** | Registro e estado, sem emenda normativa |
| Decide D3/D4 | **SOBERANO** | Criam rito e emendam contrato ratificado por ato |
| Prazo de manifestação | **2026-09-14** | — |

---

## 1. Situação atual — fatos verificáveis

| # | Fato | Medido em |
|---|---|---|
| 1 | As três peças vivem em `_backups\transcricoes-videos-2026-08-14-resgate-antigravity\` e propõem, cada uma, um plano de ondas para o `ai-orchestrator-starter` | As próprias peças |
| 2 | **15 das ~30 recomendações já estavam absorvidas** pelas ondas 2–7 do Corpo antes de as peças chegarem — os planos foram escritos contra um alvo que não existe mais | Triagem §1a, conferida item a item contra o checklist do Corpo |
| 3 | O único gap com consumidor ativo (golden dataset de runs) foi **entregue na mesma data** como E6.4 | Corpo, commit `ca3b826`, suíte 297→307 |
| 4 | As transcrições são Whisper `base`, fonéticas, PT severamente degradado; os relatórios se contradizem em contagem (175 vs 207 vídeos) | Triagem, veredito; soma por pasta confere 207 |
| 5 | A fala "a cada 6 meses, delete CLAUDE.md/skills/hooks" é de **Boris Cherny (criador do Claude Code), YC Startup School, jul/2026**, dias após a Anthropic remover ~80% do system prompt do Claude Code para os modelos da família 5 — com a ressalva de que **salvaguardas não entram na poda** | Fonte 🥈 (múltiplas secundárias convergentes, 2026-08-14); vídeo do acervo era só a pista 🥉 |
| 6 | As Cartas dos 8 setores migrados (ADR-0039, token 44) **não declaram nível de autonomia por missão** — a matriz human-led/assisted/autonomous aparece no acervo (xlsx e vídeos de `10_APLICACOES`) e não tem equivalente aqui | Cartas vigentes; triagem §2 P4 |

## 2. Problema

Dois planos de evolução externos permanecem tecnicamente "vivos" para o mesmo alvo que
o roadmap canônico já governa — **exatamente o defeito de controle de autoridade**
(dois nomes/planos para o mesmo conceito) que a Parte 3B do Padrão Ouro descreve. E as
fontes que os carregam não têm classificação de lastro registrada: qualquer sessão
futura que as leia pode citar "-65% de tokens" ou "260 mil estrelas" como fato.

## 3. Pergunta de decisão

**A Mente declara os planos externos SUPERADOS, classifica as fontes, institui a poda
semestral de instruções (salvaguardas fora) e adota o princípio do nível de autonomia
nas Cartas — ou mantém o estado atual?**

## 4. Critérios de avaliação

| # | Critério | Peso | Como se mede |
|---|---|---|---|
| `K1` | Elimina plano concorrente do roadmap canônico | **Bloqueante** | D1: os dois planos ficam com estado declarado |
| `K2` | Fonte fraca não pode virar conclusão em sessão futura | **Bloqueante** | D2: classificação registrada onde as sessões leem |
| `K3` | Custo de adoção | Alto | 2 artefatos novos + 2 alterados; `0` código |
| `K4` | Poda não pode alcançar salvaguarda | **Bloqueante** | D3: matéria 🔒 explicitamente fora do rito |
| `K5` | Reversibilidade | Alto | Tudo é registro e rito; reverter é revogar por ADR |

## 5. Opções

### Opção A — **Absorver as quatro decisões** *(recomendada)*

| Campo | Conteúdo |
|---|---|
| Descrição | D1+D2 vigoram como registro (DEP-GOV); D3+D4 vigoram com o ato do Soberano sobre `ADR-0045` |
| A favor | Fecha o plano concorrente no mesmo dia em que nasceu; a classificação de fonte vira consulta obrigatória; a poda ganha rito com salvaguarda protegida; as Cartas ganham o campo que a operação real vai cobrar |
| Contra | D3 institui rito com base em fonte 🥈 (a primária — vídeo da talk — não foi localizada); D4 gera trabalho futuro de emenda nas 8 Cartas |
| Custo | 2 criados + 2 alterados nesta sessão; emendas de Carta em sessão própria |
| Avaliação | `K1` ✔ · `K2` ✔ · `K3` ✔ · `K4` ✔ · `K5` ✔ |

### Opção B — **Absorver só D1+D2 (registro), recusar D3+D4**

| Campo | Conteúdo |
|---|---|
| Descrição | Planos superados e fontes classificadas; nenhum rito novo, Cartas intocadas |
| A favor | Zero compromisso novo; nada depende de fonte 🥈 |
| Contra | A poda que a própria Anthropic praticou (80% do prompt) fica sem rito — o acervo de instruções da fábrica só cresce, contra a regra de zero desperdício; as Cartas seguem sem declarar o que a matriz de delegação já mostrou ser a pergunta operacional central |
| Avaliação | `K1` ✔ · `K2` ✔ · `K4` vazio (não há rito) |

### Opção Z — **Adiar**

| Campo | Conteúdo |
|---|---|
| Consequência | Os dois planos externos permanecem sem estado; próxima sessão que ler as peças pode tratá-los como vigentes |
| Por que não venceu | `K1` é bloqueante e não precisa de informação nova: o fit-gap já está medido |

## 6. Recomendação do proponente

**Opção A.** D1/D2 são urgentes e de custo zero; D3 tem o lastro mais forte que uma
prática de harness pode ter hoje (o próprio fabricante a exerceu sobre si) e a
ressalva `K4` remove o único risco real; D4 decide só o princípio — a emenda material
fica para o rito das Cartas.

## 7. Impacto previsto

| Dimensão | Impacto |
|---|---|
| Normas afetadas | `0` fundacionais emendadas; ADR-0039 ganha decisão relacionada (D4, princípio) |
| Entidades novas | `0` — poda é rito recorrente registrado em ADR, não entidade |
| Roadmap | Seção de conferências ganha o registro da absorção; nenhum épico muda |
| Camadas de memória | Estratégica (esta RFC/ADR) |
| Trabalho futuro gerado | 1 sessão de emenda das Cartas (D4) · 1ª poda em 2027-02 (D3) |

## 8. Riscos

| # | Risco | Impacto | Mitigação |
|---|---|---|---|
| `RR-1` | Poda semestral remover instrução que ainda era necessária | Médio | O rito exige teste de necessidade ANTES de remover (remover → observar → recolocar se degradar), e salvaguardas 🔒 nunca entram |
| `RR-2` | D4 virar burocracia nas Cartas (campo decorativo) | Baixo | O campo só é obrigatório em missão nova ou emendada; Cartas paradas não são reabertas só para isso |

## 9. Perguntas em aberto

| # | Questão | Quem responde | Bloqueia? |
|---|---|---|---|
| `Q1` | A 1ª poda (2027-02) roda sobre os CLAUDE.md da fábrica inteira ou começa por um repositório piloto? | **SOBERANO** | ❌ — sem resposta, começa por piloto (o Corpo) |
| `Q2` | D4: o campo entra nas 8 Cartas de uma vez ou por Carta, na primeira missão que a tocar? | **SOBERANO** | ❌ — sem resposta, por Carta |

## 10. Manifestações

| Área | Posição | Fundamento | Data |
|---|---|---|---|
| `DEP-GOV` | apoia a Opção A | Proponente; §6 | 2026-08-14 |
| `DEP-QAR` | apoia, com a ressalva registrada | Fonte de D3 é 🥈; a ressalva vive no próprio ADR | 2026-08-14 |
| `SOBERANO` | *(não ocorrido)* | — | — |

## 11. Resultado

| Campo | Conteúdo |
|---|---|
| Decisão | **aceita, quanto à forma** — gera `ADR-0045`; D1/D2 vigoram como registro, D3/D4 **não entram em vigor** sem ato |
| ADR gerado | [`ADR-0045`](../decisions/ADR-0045-absorcao-da-triagem-antigravity.md) — `em-revisao`, `ratificacao: pendente` |
| Data | 2026-08-14 |
| Responsável | DEP-GOV, revisão DEP-QAR |

---

## Checklist de validade

| # | Item | Estado |
|---|---|---|
| 1 | Pergunta clara | ✅ §3 |
| 2 | Alternativas reais + "não fazer nada" | ✅ A, B, Z |
| 3 | Nenhuma alternativa de palha | ✅ B é absorção parcial legítima |
| 4 | Critérios antes das opções | ✅ §4 |
| 5 | Recomendação presente | ✅ §6 |
| 6 | Prazo de análise | ✅ 2026-09-14 |
| 7 | Evidência ausente declarada | ✅ §5 (fonte primária de D3 não localizada) e §10 |
| 8 | Impacto mapeado | ✅ §7 |
| 9 | `revisor` ≠ `autor` | ✅ DEP-GOV × DEP-QAR |

## Histórico de versões

| Versão | Data | Autor | Mudança |
|---|---|---|---|
| 1.0.0 | 2026-08-14 | DEP-GOV | Proposta inicial: as 4 decisões da triagem do resgate antigravity, com o lastro de D3 elevado de 🥉 (transcrição) a 🥈 (Boris Cherny/YC + corte de 80% pela Anthropic) por verificação da mesma data. Recomenda Opção A. |
