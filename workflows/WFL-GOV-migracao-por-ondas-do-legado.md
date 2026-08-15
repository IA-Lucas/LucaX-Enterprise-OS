---
id: WFL-GOV-migracao-por-ondas-do-legado
titulo: Migração por ondas de precedentes do Legado para o Corpo
tipo: workflow
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-08-13
atualizado_em: 2026-08-13
revisao_prevista: 2027-02-13
decisoes_relacionadas: [ADR-0040]
substitui: []
substituido_por: null
resumo: Confronta precedentes do Legado contra o Corpo real e migra so o que tem ADAPT com consumidor, spec e vermelho antes do codigo.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
capabilities: [CAP-governanca, CAP-engenharia]
gatilho: DEP-GOV abre um grupo de precedentes do manifesto de triagem (Onda 7, F52) que ainda não tem fase própria (F5x)
portoes: [QG-0, QG-1, QG-2, QG-3, QG-5, QG-6]
---

# Migração por ondas de precedentes do Legado para o Corpo

## Propósito
Fechar, por grupo de precedentes, o ciclo completo que separa `triado` de `migrado`
(regra do Fundador, Onda 7): confrontar cada precedente do Legado contra o estado real
do Corpo, decidir `ADAPT`/`REWRITE`/`REJECT` por fibra com motivo, e só então produzir
spec, teste vermelho, implementação, consumidor ativo, reversão provada e registro no
roadmap — nunca cópia, nunca peça decorativa.

## Escopo
| Item | Definição |
|---|---|
| Aplica-se a | Grupos de precedentes do Legado (`acervo/detalhes/A-*.md`) já classificados pelo horizonte integral da F52 (manifesto `.scratch/F52_triagem_precedentes_lote{1..7}.csv` na Oficina), ainda sem fase F5x própria |
| **Não** se aplica a | Precedentes isolados sem classificação prévia da F52; matéria que exige ato do Soberano antes de decidir (recebe `WF-28`, ponto de intervenção humana, e o Workflow **para**); admissão de Produto, Capability ou tipo de entidade novo (rito próprio, fora deste Workflow) |
| Dono do resultado final | `DEP-GOV` |

## Responsáveis
| Papel | Quem |
|---|---|
| Proprietário | `DEP-GOV` |
| Dono do resultado final | `DEP-GOV` |
| Verificação | `DEP-QAR` |

## 1. Gatilho
| O que dispara | Quem dispara | Pré-condições |
|---|---|---|
| Um grupo de precedentes do manifesto F52 fica sem fase F5x própria, ou o Fundador/DEP-GOV decide abrir a próxima onda | `DEP-GOV` | O manifesto F52 existe e cobre os precedentes do grupo (horizonte integral já lido, `sha256` por arquivo); o grupo não colide com um `ADR` já reservado por rito próprio (ex.: `ADR-112`) |

## 2. Entradas
| Entrada | Origem | Obrigatória? |
|---|---|---|
| Lista de precedentes do grupo (`A-XXX`) | Manifesto de triagem F52 (Oficina) | Sim |
| Estado real do Corpo (código, `PRD.json`, `CLAUDE.md`) na área tocada | Repositório Corpo (`lucax-enterprise`) | Sim |
| Lease vigente da Mente (token, `estado_fenceado`) | `infraestrutura/leases/LucaX-Enterprise-OS.lease` *(ate 2026-08-15: `_leases/`)* | Sim, antes de qualquer escrita na Mente |

## 3. Etapas
| # | Etapa | Responsável | Entrada | Saída | Portão |
|---|---|---|---|---|---|
| 1 | Delimitar o grupo a partir do manifesto F52 | `DEP-GOV` (Oficina) | Manifesto CSV classificado | Lista fechada de N precedentes do grupo | `QG-0` |
| 2 | Ler cada precedente por inteiro no Legado (somente leitura, firewall de migração nunca cruzado) e confrontar contra o Corpo real | `DEP-GOV` (Oficina) | Precedentes + estado medido do Corpo | Decisão `ADAPT`/`REWRITE`/`REJECT` por fibra, com motivo escrito | `QG-2` |
| 3 | Adquirir lease na Mente antes da primeira escrita, invocando [`SKL-custodia-criar-copia-datada`](../skills/SKL-custodia-criar-copia-datada.md) para o `copia_datada` | Quem vai escrever | `estado_fenceado` medido pelo instrumento vigente (`baseline.sh`, `IR-BL/6`) | Lease adquirido: titular, motivo, `estado_fenceado`, `ponto_de_rollback`, `copia_datada` | — *(interno; verificado por `QG-0` da escrita seguinte)* |
| 4 | Para cada `ADAPT`: escrever spec no `PRD.json` do Corpo | `DEP-ENG` | Precedente + decisão `ADAPT` | Spec com requisitos numerados (`R1`…`Rn`) | — |
| 5 | Escrever teste que falha ANTES do código (vermelho provado) | `DEP-ENG` | Spec | Suíte vermelha, rodada e confirmada | `QG-1` |
| 6 | Implementar o mínimo necessário e ligar consumidor ativo real | `DEP-ENG` | Teste vermelho | Código + consumidor real (nunca peça decorativa) | — |
| 7 | Provar reversão (remover o fio e confirmar vermelho) e rodar a suíte inteira verde; regenerar mapa do repositório | `DEP-ENG` + `DEP-QAR` | Implementação | Reversão provada + suíte verde + mapa `EM DIA` | `QG-3` |
| 8 | Registrar no checklist do Corpo (`CLAUDE.md`) e commitar no Corpo | `DEP-ENG` | Suíte verde | Commit no repositório Corpo | — |
| 9 | Registrar a conferência de fechamento no roadmap da Mente (`ADAPT` e `REJECT` motivados) | `DEP-GOV` | Resultado do Corpo + decisões da etapa 2 | `governance/roadmap-canonico.md` atualizado + commit na Mente | `QG-5` |
| 10 | Pós-verificar (baseline reproduz, diff/secret-scan limpos) e liberar o lease com o próximo token | `DEP-GOV` | Commit na Mente | Lease liberado, `proximo_fencing_token` declarado | — |
| 11 | Fechar o grupo quando todo precedente estiver decidido (migrado ou rejeitado motivado); conferir se a onda inteira fecha | `DEP-GOV` | Todas as etapas anteriores, para todos os precedentes do grupo | Grupo fechado N/N no roadmap | `QG-6` |

> **Achado declarado ao redigir esta ficha — a primeira aresta real da cadeia de `1.19`, e
> um gap junto com ela.** A etapa 3 é exatamente o `gatilho` que `SKL-custodia-criar-copia-datada`
> já lista (`SK-11`: *"adquirir lease de escrita"*) — isso é a **primeira dependência real
> entre um `WFL` e uma `SKL`** no acervo, onde antes existiam três Skills mutuamente
> independentes. **Mas a conexão é declarada, não ainda plenamente exercida:** as quatro
> cópias datadas produzidas nesta própria Onda 7 (tokens 71–74 do lease) usaram
> `robocopy` + **contagem de arquivos** (`694/694`), não o procedimento completo de `SK-15`
> — manifesto `sha256` por arquivo (passo 5) e conferência arquivo a arquivo (passo 6).
> Contagem igual **não** é a mesma prova que `n/n` de hashes conferindo — é exatamente a
> distinção que `SK-18` faz entre *"copiou"* e *"medido"*. **Não corrigido nesta ficha**
> (corrigir a prática do lease é mudança na Mente, fora do escopo de instanciar o primeiro
> Workflow); **declarado para que a próxima invocação da etapa 3 exerça `SK-15` por
> inteiro**, e não repita a lacuna.

## 4. Portões
| Portão | Momento | Quem libera | Critério |
|---|---|---|---|
| `QG-0` | Antes de delimitar o grupo | `DEP-GOV` | O grupo está claro, cabe no manifesto F52 e não colide com precedente já reservado por rito próprio |
| `QG-1` | Após escrever a spec (etapa 5, antes do código) | `DEP-EXE` | A spec define resultado, critério de aceite verificável e o que fica fora; o teste vermelho existe e falha pelo motivo certo |
| `QG-2` | Após decidir a arquitetura de cada fibra (etapa 2) | `DEP-ENG` + `DEP-GOV` | As alternativas (`ADAPT`/`REWRITE`/`REJECT`) foram consideradas e a decisão está registrada com motivo, não por omissão |
| `QG-3` | Após produzir (etapa 7) | `DEP-QAR` | Atende o DoD da spec e passou por reversão provada + suíte verde — nunca só "suíte passou" |
| `QG-5` | Após operar (etapa 9) | `DEP-KMS`/`DEP-GOV` | O aprendizado (decisões, motivos, contagem da onda) foi extraído e gravado no roadmap; se aplicável, memória (`MEM-APR`) também |
| `QG-6` | Ao encerrar o grupo/fase (etapa 11) | `DEP-QAR` + `DEP-GOV` | A arquitetura do Corpo ficou mais apta a evoluir do que estava — medido pela contagem da suíte e pelo mapa, nunca por afirmação sem número |

## 5. Saídas
| Saída | Destinatário | Formato |
|---|---|---|
| Código, spec e testes migrados | Repositório Corpo | Commit git + `PRD.json` + suíte |
| Registro da fase (`ADAPT`/`REJECT` motivados, contagem N/N) | Roadmap canônico da Mente | Conferência em `governance/roadmap-canonico.md` + commit git |
| Lição, se aplicável | Memória da Mente | `MEM-APR-XXXX` |

## 6. Critério de conclusão
O grupo fecha quando todo precedente do manifesto tem decisão registrada: `ADAPT` migrado
(spec + vermelho + consumidor + reversão + suíte) ou `REJECT`/reserva com motivo escrito —
nunca por cópia, silêncio ou peça decorativa. A fase entra no roadmap como `N/N fechados`,
e a onda maior fecha quando todos os seus grupos fecharem.

## 7. Critério de falha
| Falha | Como reconhecer | Onde retorna | Quem é acionado |
|---|---|---|---|
| Precedente decidido `ADAPT` sem consumidor real | Revisão em `QG-3` acha spec/código sem ponto de uso ativo | Etapa 6 (ligar consumidor real) | `DEP-ENG` |
| Suíte não fica verde após a implementação | `QG-3` reprova | Etapa 6 | `DEP-ENG` |
| Grupo contém precedente já reservado por rito próprio (ex.: `ADR-112`) | Medido na etapa 1 | Etapa 1 (excluir do grupo, não decidir) | `DEP-GOV` |
| Lease indisponível ou `estado_fenceado` não reproduz | Etapa 3 | Etapa 3 (investigar divergência antes de escrever) | `DEP-GOV` |
| **O que já foi produzido e o que se faz com isso** *(`WF-19`)*: specs e decisões já registradas em commits anteriores do grupo **não são desfeitas** por uma falha posterior — cada precedente decidido é unidade própria; a falha de um não invalida os já fechados do mesmo grupo | — | — | — |

## 8. Handoffs internos
| De | Para | O que transfere | Critério de aceite |
|---|---|---|---|
| Oficina (etapa 2) | Corpo (etapa 4) | Decisão `ADAPT` por fibra + motivo + `sha256`/commit da fonte | `DEP-ENG` recusa se a decisão não citar motivo, ou se o precedente não tiver sido lido por inteiro |
| Corpo (etapa 8) | Mente (etapa 9) | Commit hash + contagem da suíte (antes → depois) + descrição do que foi `ADAPT`/`REJECT` | `DEP-GOV` recusa se a suíte não estiver verde ou se a reversão não tiver sido provada |

### Pacote de Contexto do handoff (`WF-18`)
O que viaja: decisão + motivo + hash de commit + contagem de testes — **por referência**
(identificador, nunca cópia do diff inteiro nem da fonte integral do Legado). O que **não**
viaja: o texto integral do precedente do Legado (fica custodiado na Oficina, com `sha256`
citável); o diff completo do commit (fica no git, citável por hash). Transferir tudo o que
se tem não é handoff cuidadoso — é transferir o custo de curadoria para quem recebe
(`CE-01`).

## 9. Memória
| Etapa | Camada alimentada | O que grava |
|---|---|---|
| 2 | operacional | Decisão `ADAPT`/`REWRITE`/`REJECT` por precedente, com motivo |
| 7 | técnica | Contagem da suíte antes/depois, mapa do repositório regenerado |
| 9 | operacional | Conferência de fechamento no roadmap: N/N do grupo, precedentes citados |
| 9 (quando aplicável) | aprendizado | `MEM-APR-XXXX`, quando o grupo produzir lição transversal (como ocorreu na F53) |

## 10. Ganho `PI-14`
| Campo | Conteúdo |
|---|---|
| Ganho declarado | Organização e reuso: substitui a redação ad-hoc do mesmo procedimento em cada conferência do roadmap por uma sequência única, nomeada, com portões e critério de falha explícitos — reduz o custo de contexto de quem retoma uma onda no meio |
| Sinal que motivou a criação | **Já observado, não previsto**: o mesmo padrão foi exercido **cinco vezes** nesta Onda 7 antes deste Workflow existir — F53 (aprendizado, 20 precedentes), F54 (integridade, 7), F55 (custo/contexto, 6), F57 (orquestração, 10, commits `2b7ee3e`/`4279763`/`c1bb01b`), F58 (skills/agentes/Capabilities, 10, commit `b8eb0bd`) — cada uma reinventando a mesma prosa no roadmap sem entidade formal que a nomeasse |
| Data de reavaliação | `2027-02-13` (`revisao_prevista`), ou no primeiro `retry`/`timeout`/`compensação`/`retomada` reais, ou na primeira falha *plausível e errada* — o que ocorrer primeiro (mesmo gatilho de revisão do Framework, `ADR-0040 §17`) |

## 11. Estados e transições
Os seis estados de execução de `WF-10` (distintos dos oito estados de artefato de
`FND-03 §5` — estes descrevem uma *execução* do Workflow, não o documento):

| Estado | Quando ocorre neste Workflow | Quem observa |
|---|---|---|
| `não-iniciado` | Antes da etapa 1 | `DEP-GOV` |
| `em-curso` | Etapas 1 a 9 em andamento | `DEP-GOV`/`DEP-ENG` conforme a etapa |
| `bloqueado` | Precedente exige objeto externo ausente (ex.: padrão da F56 — documento/vídeo real indisponível) | `DEP-GOV`; impedimento declarado com dono e prazo (`WF-15`) |
| `em-espera-humana` | Precedente cai no ponto de intervenção da §14 (matéria reservada ao Fundador) | `DEP-GOV` |
| `concluído` | Etapa 11 fecha o grupo N/N | `DEP-QAR` confirma via `QG-6` |
| `abandonado` | Grupo inteiro decidido `REJECT` sem nenhum `ADAPT` — fecha por rejeição motivada, não é falha do Workflow | `DEP-GOV` |

**Transições:** `não-iniciado → em-curso` dispara no gatilho (§ acima). `em-curso →
bloqueado` dispara quando a etapa 2 encontra objeto externo ausente, declarando o
impedimento. `em-curso → em-espera-humana` dispara quando a etapa 2 encontra matéria
reservada ao Fundador (§14). `em-curso → concluído` só pela etapa 11 completa — nunca
silenciosa. `bloqueado`/`em-espera-humana → em-curso` retomam quando a pré-condição que
faltava passa a existir (objeto chega, ou o Fundador decide).

## 12. Retry
Nenhuma etapa deste Workflow tem retry **automático**. Toda etapa com efeito registrado
(escrita em disco, commit) **não é idempotente**: reexecutá-la não repete o mesmo
resultado, redecide. Re-execução é sempre **manual e integral da etapa**, nunca laço
automático — consistente com `WF-20`: "repetir operação não idempotente produz efeito
duplicado". A única forma de "repetição" real observada é reler um precedente quando o
estado do Corpo mudou entre a leitura (etapa 2) e a decisão — e mesmo essa é um novo
ciclo da etapa 2, não um retry da mesma execução.

## 13. Timeout
| Estado | Prazo | Consequência ao vencer |
|---|---|---|
| `em-curso` | Sem prazo rígido — trabalho de leitura/decisão varia por grupo | Nenhum automático; revisão periódica do roadmap é quem observa deriva |
| `bloqueado` | Reavaliado a cada nova sessão que tocar a onda (sem prazo fixo em dias) | Permanece `bloqueado`; **nunca vira `abandonado` automaticamente** — objeto externo ausente não é decisão do Workflow, é fato |
| `em-espera-humana` | Sem prazo fixo — depende do Fundador | Permanece em espera; escalonamento (`WF-26`) é o dono do resultado (`DEP-GOV`) sinalizar de novo, nunca decidir no lugar do Fundador |

## 14. Compensação
Toda etapa com efeito externo declara sua compensação, ou declara por escrito que não
tem:

| Etapa com efeito externo | Compensação |
|---|---|
| 4–8 (commit no Corpo) | `git revert` do commit; a suíte deve voltar ao estado anterior verde |
| 9 (registro no roadmap da Mente) | **Não tem compensação por apagamento.** O acervo desta organização já pratica a regra: emendar registro histórico é **correção declarada, nunca silenciosa** — uma nova conferência, no mesmo arquivo, que corrige o enunciado anterior citando o que estava errado e por quê (padrão já exercido nesta mesma Onda 7, ex.: correções declaradas de `IR-BL` no `CLAUDE.md` do Corpo). **"Não tem compensação por apagamento" é informação legítima**, não lacuna — o registro de que uma decisão ocorreu é, ele mesmo, o ponto sem volta |
| 10 (liberação de lease) | Não tem compensação: liberar um token é irreversível por desenho (monotônico crescente); o erro se corrige adquirindo um token novo e escrevendo a correção declarada |

## 15. Rollback
Rollback (voltar a um ponto anterior) é distinto de compensação (`WF-23`): aplica-se
enquanto o commit não foi empurrado para `origin` e nenhuma decisão dependente foi
registrada por cima. Declara até onde volta: o commit anterior no repositório tocado
(Corpo ou Mente), nunca além do `ponto_de_rollback` citado no lease da etapa 3. O que já
foi entregue a terceiros (commit já empurrado, roadmap já lido por outra sessão) **não
volta a rascunho** (`RB-02`) — a partir daí o caminho é sempre compensação por correção
declarada, nunca reescrita silenciosa do histórico.

## 16. Retomada
Ponto de retomada **declarado antes**, e **verificado**, nunca só declarado (`WF-25`,
lição de `RD-103` — declarar não preserva, verificar preserva):

| Campo | Conteúdo |
|---|---|
| De onde retoma | O último `estado_no_fechamento` registrado no lease da Mente (contagem de artefatos/linhas, manifesto, impressão digital, `HEAD` do commit) |
| O que precisa estar preservado | O arquivo de lease (`infraestrutura/leases/LucaX-Enterprise-OS.lease`, até 2026-08-15 `_leases/`) íntegro e o histórico git dos três repositórios (Oficina, Corpo, Mente) |
| Quem verifica | Quem retoma roda `baseline.sh` (instrumento `IR-BL` vigente) e confere que o resultado bate com o `estado_no_fechamento` do último token liberado **antes de prosseguir** — é o mesmo passo que abriu esta sessão ("verifique onde parou"), agora nomeado como parte formal do Workflow |

## 17. Handoffs internos — ponto de intervenção humana
Três casos exigem parar e não admitem automação (`WF-28`):

**(a)** Precedente cuja decisão exigiria expor dado a terceiro sem base — não observado
até hoje neste Workflow, mas declarado como gatilho de parada se ocorrer.
**(b)** Qualquer efeito cuja classe seja `Tipo 1` — por exemplo, admitir um tipo de
entidade novo ou promover um ADR a `FND` nunca acontece dentro deste Workflow; a etapa 2
para e escala para rito próprio.
**(c)** Precedente já reservado por decisão anterior do Fundador ou por rito taxonômico
próprio — como `A-267`/`ADR-112`, reservado desde a F51. **A etapa 1 exclui esses
precedentes do grupo antes de decidir**, e a etapa 2 nunca os reabre. Onde a norma exige
ato do Soberano, este Workflow **para e não prossegue** — ele não pode contê-lo,
executá-lo nem antecipá-lo (`WF-28`).

## 18. Critério de descontinuação
Este Workflow deixa de valer a pena quando o Legado for retirado (Cutover concluído por
ato do Fundador) e não houver mais precedentes do manifesto F52 a triar — nesse ponto ele
é consolidado como memória histórica (`FND-02 §9.3`), não apagado: registra o método que
produziu a migração inteira da Onda 7.

## Rastreabilidade e revisão
| Campo | Conteúdo |
|---|---|
| Origem | `FND-03 §3.10` · `FND-09 §8.2` linha `WFL` — entidade recebida, `0` criada aqui |
| Não-proliferação (`FND-04 §6.1`), respondida por escrito | **(1)** Já existe em outra forma? Não como artefato — existia como prosa repetida em cada conferência do roadmap (F53/F54/F55/F57/F58), nunca como entidade nomeada com portão e critério de falha. **(2)** Cabe em componente existente? Não: atravessa três papéis (Oficina, Corpo, Mente) e tem portão — por `WF-02`/`FND-10 §4.8`, isso é `WFL`, nunca `SKL`. **(3)** Qual ganho de `PI-14`, com sinal já observado? Ver §10 acima — cinco execuções reais, não hipóteses. **(4)** Como se vai saber que deixou de ser necessário? Ver §18 — quando o Legado for retirado |
| Primeiro Workflow real | Este é o **primeiro** Workflow instanciado no acervo (`ADR-0040 §17`: gatilho de revisão do Framework, `L1`, dispara com esta criação) |
| Achado que este Workflow fecha | `AW-1` (`ADR-0040`/`RD-113`): `workflows/` não existia no disco — fecha com a criação deste arquivo, o próprio documento é a Carta aprovada por `DEP-EXE` em `C2`, sem ato |
| Achados que este Workflow **não** fecha, declarado | `AW-2`/`RD-114` (`TPL-workflow` sem bloco de retry/timeout/compensação/retomada) e `AW-3`/`RD-115` (divergência de `aprovador` no frontmatter-documento do template) seguem **abertos** — este artefato segue o template vigente mais os 18 blocos exigidos por `WF-08`, mas corrigir o `TPL-workflow` em si é fora do escopo desta instância (dono declarado: `DEP-GOV + DEP-EXE`) |
| Consumidor real | O próprio Épico 1 (`1.19`, roadmap da Mente) — reduz de `0` para `1` os Workflows instanciados na cadeia de dez elos |

## Histórico de versões
| Versão | Data | Autor | Mudança |
|---|---|---|---|
| 1.0.0 | 2026-08-13 | DEP-GOV | Criação — primeiro Workflow real do acervo, documentando o procedimento de migração por ondas já exercido cinco vezes na Onda 7 (F53/F54/F55/F57/F58). |
