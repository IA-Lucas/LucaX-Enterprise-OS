> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO

# SÍNTESE — ÁREA 09 — SEGURANÇA E QUALIDADE

**Frente:** Programa de Inteligência do Acervo · **Fase 3 — Síntese** (missão **A3**) · **Data:** 2026-07-29 · **Avaliador:** Claude Opus 5 (Fase 3)

**Origem:** external-evidence · **Autoridade:** nenhuma · **Estado:** provisório · **Normativo:** não · **Adoção:** não-decidida

**Base:** 10 fichas de `07_FICHAS-DE-EVIDENCIA/09_SEGURANCA-E-QUALIDADE.md` — 1 REPO · 2 PRINT · 7 VÍDEO · 0 PLANILHA. Pergunta central da área (base de E01): *como saber que o sistema funciona e que é seguro instalar o que se instala.*

---

## 1. O que sabemos

- A área é a mais pequena do acervo: **10 itens e um único repositório**, contra 43 repositórios no acervo inteiro — fato contável do manifesto, registrado na ficha de abertura da área (`AC-09-REP-001`, nota de contexto). O juízo do catálogo ("a pasta mais vazia — e isso é em si um achado") **não é confirmado nem negado** por esta frente.
- Existe **um único item que verifica os demais** em vez de produzir capacidade: `AC-09-REP-001` (`SkillSpector-main`), scanner de skills com 242 arquivos, `LV = 4`, licença Apache-2.0 íntegra, 96 arquivos de teste **nomeados por ameaça** (`test_mcp_least_privilege.py`, `test_mcp_rug_pull.py`, `test_mcp_tool_poisoning.py`, `test_multi_skill.py`), `SECURITY.md`, `Dockerfile` para execução isolada e ganchos de pré-commit (`AC-09-REP-001`, E02 = 4, E06 = 4, E13 = 4).
- Os dois percentuais que sustentam a razão de existir de `AC-09-REP-001` — "26,1% das skills contêm vulnerabilidades e 5,2% mostram intenção provavelmente maliciosa" — **citam pesquisa não nomeada** e não são verificáveis no trecho lido (`AC-09-REP-001`, E15 = 1). Os números "68 padrões / 17 categorias" são conferíveis dentro da própria fonte (`src/`), mas **não foram conferidos** sob o teto de leitura (`AC-09-REP-001`, alegações registradas).
- Nenhuma taxa de detecção ou de falso positivo de `AC-09-REP-001` foi lida: a ficha registra explicitamente que "um scanner sem essa medida é instrumento não calibrado" (`AC-09-REP-001`, restrições).
- O restante da área é **material de quadros**: 9 itens em `LV3` (2 PRINT, 7 VÍDEO), dos quais 3 têm transcrição automática bruta (`AC-09-VID-001`, `AC-09-VID-002`, `AC-09-VID-007`, `pt`, ALTA AUTOMÁTICA) e 4 não têm fala lexical confiável (`AC-09-VID-003` a `AC-09-VID-006`). Fala permanece desconhecida onde não revisada; só quadros sustentam afirmação.
- Dos quadros, os conteúdos concretos observados são: uma regra de parada com limiar numérico — após duas ou três tentativas fracassadas, limpar contexto e reabrir sessão (`AC-09-VID-001`, E02 = 2); uma demonstração de agente de observabilidade com sinais nomeados, hipótese, confiança exibida subindo de 33% para 92% **sem método de cálculo**, e plano final "aguardando aprovação" (`AC-09-VID-002`, E02 = 2, E15 = 1); um laço fazer → avaliar → criticar → reescrever, só carrossel (`AC-09-VID-003`, E02 = 1); um prompt de revisão **exibido por inteiro**, com separação entrada/saída e a instrução "não editar a entrada" (`AC-09-VID-004`, E02 = 2); um protocolo Grill → Review → Verdict → Build com veredito binário e teto de cinco rodadas (`AC-09-VID-005`, E02 = 1 — "só carrossel", salvo pela especificidade do protocolo); quatro perguntas para colar num agente (`AC-09-VID-006`, E02 = 1); e uma **busca de skills por catálogo** com dois candidatos devolvidos (`AC-09-VID-007`, E02 = 2).
- `AC-09-VID-007` (**NC = 0**): o catálogo diz "varredura de segurança de skills"; a inspeção (`94`) mostra **busca em catálogo, sem varredura**. A síntese **não credita varredura** a este item — a descrição do catálogo corresponde a `AC-09-REP-001`, não a este vídeo; descoberta e verificação são operações diferentes (ficha `AC-09-VID-007`, bloco Catálogo).
- `AC-09-VID-003` (**E06 = 1**): a tela exibe instalação de ferramenta por **download encadeado a execução em shell** — padrão observado na tela; **o que ele instala não foi inspecionado**. É risco **declarado** por terceiro (`94`), **não confirmado**; o item não foi rejeitado porque rejeitar por suspeita é proibido pela rubrica (`AC-09-VID-003`, portas de veto V1).
- `AC-09-PRT-001` (**NC = 2**): o mapa Blue/Red confere na estrutura, mas o catálogo colocou **Nessus sob Red Teaming** onde o diagrama o põe sob **Vulnerability Management**; usa-se só a parte confirmada, e a hierarquia do catálogo fica fora (`AC-09-PRT-001`, bloco Catálogo).
- `AC-09-PRT-002` (**NC = 3**, confirmado em `109`): infográfico de nove blocos — laços agênticos, evals (entradas → resposta → camada de avaliação → pass/fail → métricas), guardrails de entrada/saída, observabilidade com traces/logs/métricas — que o catálogo e a ficha registram como **o primeiro material do acervo a pôr evals e observabilidade explicitamente no fluxo de produção**; é mapa de cobertura, sem dataset, métrica ou limiar (`AC-09-PRT-002`, E02 = 2, E01 = 3).
- A área tem **30,0% de células ND** (45 de 150), a maior taxa da rodada registrada na Fase 2, e **zero disparos de V7** — nenhuma relevância depende de alegação sem prova (fechamento da área 09; `00_PRE-CORRECOES` §3.5).

## 2. Fontes mais fortes e por quê

- **`AC-09-REP-001` é a fonte mais forte da área, por distância larga.** É o único `LV = 4` (artefato completo e inspecionável), `NF = 4` com apenas **1 ND** (E05, manutenção), `E06 = 4` (superfície declarada com controles documentados: `SECURITY.md`, `.env.example` em vez de credencial embutida, `Dockerfile` para isolar a varredura de material não confiável), `E07 = 4` (Apache-2.0 íntegra com avisos de terceiros), `E13 = 4` (suíte executável com testes nomeados por ameaça) e `NC = 3` (descrição do catálogo confere em todos os detalhes verificáveis). O ponto fraco é declarado e estreito: `E15 = 1` pelos dois percentuais sem fonte nomeada — e V7 foi **avaliada explicitamente e não disparou**, porque a relevância se sustenta pela pergunta da área e pelo artefato, não pelos percentuais (`AC-09-REP-001`, bloco A e portas de veto).
- **Segundo patamar: `AC-09-VID-002` e `AC-09-VID-004`.** `AC-09-VID-002` tem `NC = 5` (título confirmado por `94`) e é "a mais concreta dos sete vídeos" — sinais nomeados, plano de três passos e porta de aprovação humana; limita-se por `E15 = 1` (confiança 33%→92% exibida sem método) e 5 ND (`AC-09-VID-002`). `AC-09-VID-004` tem `NC = 5` e o **único conteúdo literalmente copiável** da área em vídeo — o prompt de revisão exibido por inteiro, com a fonte protegida de escrita (`AC-09-VID-004`, E02 = 2, E04 = 3). Ambos são `LV3-V`: demonstração, não artefato.
- **`AC-09-PRT-002`** é o print mais forte: `NC = 3` confirmado em `109`, nove blocos nomeados e conferidos; limita-se por ser mapa de cobertura, sem implementação (`AC-09-PRT-002`, E02 = 2).
- Os demais são fontes fracas por dados de ficha, não por juízo: `AC-09-VID-003`, `AC-09-VID-005`, `AC-09-VID-006` e `AC-09-PRT-001` têm `E02 = 1` (só carrossel ou só listagem) e 4–5 ND cada (`AC-09-VID-003`; `AC-09-VID-005`; `AC-09-VID-006`; `AC-09-PRT-001`).

## 3. Padrões recorrentes

- **Menor privilégio antes de correção automática**, aparecendo por três caminhos independentes: o prompt "não editar a entrada" com entrada e saída separadas (`AC-09-VID-004`); a condição de segurança "sandbox somente leitura" — afirmada, não demonstrada (`AC-09-VID-005`, E15 = 1); e os testes de menor privilégio em MCP de `AC-09-REP-001` (`test_mcp_least_privilege.py`).
- **Porta de aprovação antes de ação**: o plano de `AC-09-VID-002` termina em "aguardando aprovação"; o protocolo de `AC-09-VID-005` impõe veredito aprovado/revisar com teto de cinco rodadas antes do build; o bloco de evals de `AC-09-PRT-002` desenha camada de avaliação com pass/fail antes das métricas.
- **Laço com critério de parada** como mecanismo de qualidade: limiar de duas a três tentativas em `AC-09-VID-001`; laço fazer → avaliar → criticar → reescrever em `AC-09-VID-003`; teto de cinco rodadas em `AC-09-VID-005`. O mesmo mecanismo de `AC-09-VID-001` reaparece no acervo por outro caminho, em `AC-08-VID-008` e no item `ralph-main` da área 03 — a própria ficha registra (`AC-09-VID-001`, E14 = 2).
- **Avaliação e observabilidade no fluxo, não ao redor**: os nove blocos de `AC-09-PRT-002`; o pipeline coleta → correlação → hipótese → confiança → plano → aprovação de `AC-09-VID-002`.
- **A cadeia descoberta → verificação está presente, mas partida em dois itens**: a descoberta aparece em `AC-09-VID-007` (busca em catálogo de terceiro, com a própria resposta exibida avisando que as opções "não são de fonte oficial e não devem ser tratadas como totalmente confiáveis") e a verificação em `AC-09-REP-001` — e o erro do catálogo sobre `AC-09-VID-007` consiste exatamente em fundir as duas operações (`AC-09-VID-007`, bloco Catálogo).
- **Vídeo da área quase todo sem artefato e sem medição**: 7 de 7 vídeos em `LV3`, nenhum com procedimento verificável de resultado; onde há número exibido (33%→92% em `AC-09-VID-002`; "1,49M pessoas viram" em `AC-09-VID-003`; "700.000 skills" em `AC-09-VID-007`), ele entra como **alegação não verificada**, não como fato.

## 4. Conflitos e divergências

- **`AC-09-VID-007` — divergência de catálogo (NC = 0), não de fonte.** O catálogo descreve "varredura de segurança de skills antes da instalação"; a inspeção (`94`) mostra busca em catálogo, sem varredura. O hash confere e V8 não disparou: o erro é da descrição, não do artefato. A síntese usa a inspeção (`AC-09-VID-007`, bloco Catálogo). É a terceira divergência `NC = 0` consecutiva da rodada, todas por descrição de conteúdo (fechamento da área 09, registro 1).
- **`AC-09-PRT-001` — erro de hierarquia na transcrição do print (NC = 2).** O catálogo **redistribui** a estrutura do original (Nessus sob Red Teaming em vez de Vulnerability Management) — primeiro caso do acervo em que o catálogo não apenas resume, mas rearranja (fechamento da área 09, registro 2). A parte confirmada (divisão Blue/Red e elementos principais) é a única usada.
- **Tensão interna de `AC-09-REP-001`**: o artefato é o mais controlado da área (`E06 = 4`), mas sua motivação numérica (26,1% / 5,2%) tem fonte genérica não identificável (`E15 = 1`). A ficha resolve a tensão declarando que a relevância não depende dos percentuais (`AC-09-REP-001`, portas de veto V7); a síntese registra as duas pontas, sem escolher silenciosamente.
- **Conflito de afirmação sobre o que conta como "auditoria de segurança"**: `AC-09-VID-006` sugere que pedir a uma IA para "revisar prompts contra injeção, listar o que está em produção e fazer varredura contínua" constitui auditoria; o relatório `94` registra o contra-argumento — isso "não substitui escopo, ferramentas, autorização, testes, revisão humana ou controles contínuos" (`AC-09-VID-006`, E15 = 1). A síntese fica com o contra-argumento, porque a alegação é forte e não verificada.
- **Sem divergência de hash e sem soma de notas incompatíveis**: os 10 itens reconferem (`V8 = 0` na área); nenhum RF foi calculado por média (fechamento da área 09).

## 5. Candidatos fortes, pilotos e referências

Registro por ID, nunca ordenado por prioridade. Nenhuma classificação equivale a adoção.

| ID | Classe provisória | Motivo de uma linha (citando a ficha) |
|---|---|---|
| `AC-09-REP-001` | **PILOTO** | RF = CANDIDATO A PILOTO: `LV = 4` · `E06 = 4` · `E07 = 4` · `RP = 4` · 1 ND ≤ 4 · nenhum eixo do Bloco C em 0; barrado de CANDIDATO FORTE por `E15 = 1` (ficha, §9) |
| `AC-09-PRT-001` | REFERENCIA | RF = REFERÊNCIA: `LV ≥ 3`, insumo de consulta; `NC = 2` por erro de hierarquia (ficha, §9 e Catálogo) |
| `AC-09-PRT-002` | REFERENCIA | RF = REFERÊNCIA: `LV ≥ 3`, mapa de cobertura de nove blocos confirmado em `109` (ficha, §9) |
| `AC-09-VID-001` | REFERENCIA | RF = REFERÊNCIA: regra de parada com limiar; `LV = 3`, 5 ND (ficha, §9) |
| `AC-09-VID-002` | REFERENCIA | RF = REFERÊNCIA: demonstração de observabilidade com porta de aprovação; `LV = 3` (ficha, §9) |
| `AC-09-VID-003` | REFERENCIA | RF = REFERÊNCIA com V2 disparada (`E06 = 1`): "nunca candidato"; risco declarado, não confirmado (ficha, portas de veto) |
| `AC-09-VID-004` | REFERENCIA | RF = REFERÊNCIA: prompt de revisão copiável com fonte protegida de escrita; `LV = 3` (ficha, §9) |
| `AC-09-VID-005` | REFERENCIA | RF = REFERÊNCIA: protocolo Grill → Review → Verdict → Build com teto de cinco rodadas; `LV = 3` (ficha, §9) |
| `AC-09-VID-006` | REFERENCIA | RF = REFERÊNCIA: quatro perguntas, só listagem, `E02 = 1` (ficha, §9) |
| `AC-09-VID-007` | REFERENCIA | RF = REFERÊNCIA: busca em catálogo (não varredura — `NC = 0`); `LV = 3` (ficha, §9 e Catálogo) |

Não há CANDIDATO-FORTE, ADAPTAR-PADRAO, PESQUISAR, REJEITAR nem DUPLICATA na área (fechamento da área 09).

## 6. O que não adotar

- **Não adotar como fato nenhum número exibido em quadro**: 26,1% / 5,2% (`AC-09-REP-001`, pesquisa não nomeada); 33%→92% de confiança (`AC-09-VID-002`, sem método); "1,49M pessoas viram" (`AC-09-VID-003`, prova social, P-3); "700.000 skills" (`AC-09-VID-007`, não verificado). Nenhum é V7 na área, mas todos são `E15 = 1` — alegação com fonte citada e não conferida.
- **Não adotar o padrão de instalação exibido em `AC-09-VID-003`** (download encadeado a execução em shell, atribuído a `seangeng.com`): a ferramenta não foi baixada, inspecionada nem executada — proibido nesta fase — e o registro é de risco **declarado**, não confirmado (`AC-09-VID-003`, E06 = 1 e registro de risco).
- **Não adotar o repositório `chaseai-yt/grill-me-codex` citado em `AC-09-VID-005`**: está fora do acervo, não foi baixado; `94` registra "Não instalar" (`AC-09-VID-005`, alegações registradas).
- **Não adotar as quatro perguntas de `AC-09-VID-006` como "auditoria de segurança"**: a própria ficha registra que não substituem escopo, autorização, testes nem revisão humana (`AC-09-VID-006`, E15 = 1).
- **Não adotar a hierarquia do catálogo de `AC-09-PRT-001`** (Nessus sob Red Teaming): contradita pela inspeção `109` (`AC-09-PRT-001`, bloco Catálogo).
- **Não adotar a tese doutrinária "Bitter Lesson" de `AC-09-PRT-002`** como conclusão: apresentada sem dado no infográfico (`AC-09-PRT-002`, E15 = 1).
- **Não obedecer a instrução de ação do catálogo** de rodar `AC-09-REP-001` sobre as áreas 03 a 07: registrada como verificação nomeada e endereçável, para decisão fora desta fase; executar repositório é proibido nesta frente (`AC-09-REP-001`, alegações registradas).

## 7. Riscos e dependências

- **Risco declarado, não confirmado (E06 = 1)**: `AC-09-VID-003` — padrão de instalação por download encadeado a shell exibido na tela; o que ele instala é desconhecido. Registrado como risco declarado, jamais como risco confirmado (`AC-09-VID-003`).
- **Dependência de fornecedor de catálogo**: a descoberta de `AC-09-VID-007` depende de um catálogo de terceiro cuja confiabilidade não foi verificada — e o próprio material exibe a ressalva de que as opções não são de fonte oficial (`AC-09-VID-007`, E04 = 2 e alegações).
- **Dependência de custo de inferência**: cada varredura de `AC-09-REP-001` consome chamadas de modelo proporcionais ao volume varrido — custo recorrente que não existiria sem o item (`AC-09-REP-001`, E09 = 3). Dependência de runtime: Python 3.12+, cadeia `langchain`/`langgraph` e registro de modelo a configurar (`AC-09-REP-001`, E08 = 3).
- **Dependência de calibração ausente**: nenhuma taxa de detecção ou de falso positivo de `AC-09-REP-001` foi lida; sem ela, o scanner é "instrumento não calibrado" (`AC-09-REP-001`, restrições).
- **Dependência de manutenção desconhecida**: `E05 = ND` em `AC-09-REP-001` — não há `CHANGELOG` na raiz efetiva; resolveria consultar releases e commits na origem pública (`AC-09-REP-001`, E05).
- **Dependência transversal registrada na Fase 3**: a verificação de `AC-05-VID-018` (área 05) se faz comparando quadros com o `README` de `AC-09-REP-001`, já no acervo — pendência classificada como RESOLVÍVEL NA PRÓPRIA FONTE, dentro do teto de leitura (`00_PRE-CORRECOES` §2.4).
- **Bloqueio B-01 atinge 70% da área**: 7 dos 10 itens são vídeo; em todos, a fala sem transcrição revisada permanece desconhecida, e só quadros sustentam afirmação (nota de aplicação aos sete vídeos, área 09).

## 8. Lacunas

- **Calibração do scanner**: taxa de detecção e de falso positivo de `AC-09-REP-001` — **desconhecida**; nenhum resultado publicado foi lido (`AC-09-REP-001`, E13 = 4).
- **Fonte dos percentuais-motivação**: o estudo por trás de 26,1% / 5,2% — **desconhecido**; não nomeado no trecho lido (`AC-09-REP-001`, E15 = 1).
- **Conferência interna adiada**: os 68 padrões em 17 categorias são conferíveis em `src/` de `AC-09-REP-001`, mas `src/`, `docs/`, `extensions/` e `contrib/` **não foram lidos** sob o teto (`AC-09-REP-001`, cobertura da leitura).
- **Manutenção do único repositório**: `E05 = ND` em `AC-09-REP-001` — desconhecida dentro da fonte.
- **Fala dos sete vídeos**: quatro sem fala lexical confiável (`AC-09-VID-003` a `AC-09-VID-006`); três com STT automático bruto não revisado (`AC-09-VID-001`, `AC-09-VID-002`, `AC-09-VID-007`) — o que a fala acrescenta é **desconhecido** em todos os sete.
- **Eficácia dos mecanismos de qualidade**: nenhum vídeo mede o efeito do que propõe — a regra de parada de `AC-09-VID-001` não tem medição; a correção da causa raiz de `AC-09-VID-002` não é demonstrada; o agendamento "diário" de `AC-09-VID-004` não é demonstrado; a sandbox "somente leitura" de `AC-09-VID-005` é afirmada, não demonstrada (`AC-09-VID-001`; `AC-09-VID-002`; `AC-09-VID-004`; `AC-09-VID-005`, todos `E15 = 1`).
- **Origem e autoria**: `E03 = ND` em 9 dos 10 itens — data e origem desconhecidas fora do único repositório (fechamento da área 09: 45 ND).

## 9. Decisão provisória

| ID | Classe | Motivo de uma linha |
|---|---|---|
| `AC-09-REP-001` | PILOTO | Único `LV = 4`, `NF = 4`, `E06 = 4`, `E07 = 4`, 1 ND; barrado de CANDIDATO FORTE por `E15 = 1` (percentuais sem fonte nomeada) |
| `AC-09-PRT-001` | REFERENCIA | `LV3-V`; mapa Blue/Red com estrutura confirmada e hierarquia do catálogo descartada (`NC = 2`) |
| `AC-09-PRT-002` | REFERENCIA | `LV3-V`; nove blocos confirmados em `109`; mapa de cobertura, sem implementação |
| `AC-09-VID-001` | REFERENCIA | Regra de parada com limiar numérico; atribuição à Anthropic e causalidade não verificadas |
| `AC-09-VID-002` | REFERENCIA | Demonstração mais concreta da área; número de confiança sem método; `NC = 5` |
| `AC-09-VID-003` | REFERENCIA | V2 disparada (`E06 = 1`) fecha classes de candidato; risco declarado, não confirmado |
| `AC-09-VID-004` | REFERENCIA | Único conteúdo copiável em vídeo: prompt com fonte protegida de escrita; `NC = 5` |
| `AC-09-VID-005` | REFERENCIA | Protocolo específico (veredito binário, teto de cinco rodadas); condições de segurança afirmadas, não demonstradas |
| `AC-09-VID-006` | REFERENCIA | Só listagem (`E02 = 1`); alegação de "auditoria por prompt" rebatida na própria ficha |
| `AC-09-VID-007` | REFERENCIA | Busca em catálogo, **não** varredura (`NC = 0`); ressalva de não-confiabilidade embutida no próprio material |

A decisão provisória da área é, portanto: **um piloto cercado de reservas nomeadas** (`AC-09-REP-001` — calibração, fonte dos percentuais, manutenção) **e nove referências de consulta**, nenhuma delas candidata a qualquer classe superior. Nada aqui é adoção.

## 10. Experimento que poderia validá-la

**Proposta — não plano aprovado.** Duas verificações endereçáveis, já nomeadas nas fichas:

1. **Calibração controlada de `AC-09-REP-001`** (depende do proprietário — executar repositório é proibido nesta frente): montar um conjunto pequeno de itens do próprio acervo com veredito conhecido por inspeção manual — incluindo um item com padrão observado na tela, como a instalação encadeada a shell de `AC-09-VID-003` — e medir taxa de detecção e de falso positivo do scanner contra esse veredito. Validaria ou derrubaria a decisão PILOTO, que hoje repousa em artefato controlado **sem medida de desempenho** (`AC-09-REP-001`, E13 = 4 e restrições). A instrução do catálogo de rodá-lo sobre as áreas 03 a 07 é a forma bruta desta mesma verificação; ficou registrada, não obedecida (`AC-09-REP-001`, alegações registradas).
2. **Verificação interna já classificada como resolvível na própria fonte**: comparar os quadros de `AC-05-VID-018` (área 05) com o `README` de `AC-09-REP-001` — cabe no teto de leitura vigente e fecharia a pendência da área 05 que usa esta área como referência (`00_PRE-CORRECOES` §2.4). Não foi executada nesta fase (`00_PRE-CORRECOES` §2.9).

## 11. Confiança da síntese

**Média-alta para o que está nas fichas; estruturalmente limitada pelo que as fichas não alcançam.**

- **A favor — alta rastreabilidade da base**: 1 item em `LV4` com leitura real de artefato (`AC-09-REP-001`); os 10 hashes reconferem (`V8 = 0` na área); zero disparos de V7 — nenhuma relevância depende de alegação sem prova; todas as divergências de catálogo (1 com `NC = 0`, 1 com `NC = 2`) estão nomeadas e foram aplicadas como regra, não como exceção; zero itens em EXIGE PESQUISA — nenhuma pendência formal na área (fechamento da área 09).
- **Contra — cobertura rasa em 70% da área**: 7 dos 10 itens são vídeo em `LV3`, 4 deles sem fala lexical confiável; o bloqueio B-01 é o mais severo do acervo nesta área. A taxa de ND é a maior da rodada — **30,0%** (45 de 150 células) — concentrada em origem (`E03`), manutenção (`E05`) e verificação (`E13`) dos itens de mídia.
- **Onde a confiança é menor**: qualquer afirmação sobre **eficácia** — os mecanismos de qualidade dos vídeos são descrições de quadros sem medição, e o único artefato real é um scanner sem calibração lida. A decisão PILOTO de `AC-09-REP-001` é a mais forte da área e ainda assim depende de três lacunas nomeadas (calibração, fonte dos percentuais, manutenção).

## 12. Cobertura

| ID | Tipo | LV | NC | RF da ficha | Decisão provisória |
|---|---|---|---|---|---|
| `AC-09-REP-001` | REPO | LV4 | 3 | CANDIDATO A PILOTO | PILOTO |
| `AC-09-PRT-001` | PRINT | LV3-V | 2 | REFERÊNCIA | REFERENCIA |
| `AC-09-PRT-002` | PRINT | LV3-V | 3 | REFERÊNCIA | REFERENCIA |
| `AC-09-VID-001` | VÍDEO | LV3-V + LV3-A | 1 | REFERÊNCIA | REFERENCIA |
| `AC-09-VID-002` | VÍDEO | LV3-V + LV3-A | 5 | REFERÊNCIA | REFERENCIA |
| `AC-09-VID-003` | VÍDEO | LV3-V | 5 | REFERÊNCIA | REFERENCIA |
| `AC-09-VID-004` | VÍDEO | LV3-V | 5 | REFERÊNCIA | REFERENCIA |
| `AC-09-VID-005` | VÍDEO | LV3-V | 5 | REFERÊNCIA | REFERENCIA |
| `AC-09-VID-006` | VÍDEO | LV3-V | 5 | REFERÊNCIA | REFERENCIA |
| `AC-09-VID-007` | VÍDEO | LV3-V + LV3-A | 0 | REFERÊNCIA | REFERENCIA |

**Itens com ficha: 10 de 10 · IDs faltando: 0 · IDs repetidos: 0** (fechamento da área 09).

> Este arquivo é evidência externa, provisória e não normativa. Não autoriza adoção de nada.
