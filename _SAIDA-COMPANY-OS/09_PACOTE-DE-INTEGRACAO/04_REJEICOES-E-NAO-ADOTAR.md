> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO

# 04 — REJEIÇÕES E NÃO-ADOTAR

**Frente:** Programa de Inteligência do Acervo · **Missão A4** · **Data:** 2026-07-29
**Entrada:** fichas, sínteses e matriz transversal das fases 2–3. Nenhuma fonte original aberta.

**Origem:** external-evidence · **Autoridade:** nenhuma · **Estado:** provisório · **Normativo:** não · **Adoção:** não-decidida

> Este arquivo separa quatro coisas que não se confundem: **rejeição formal** (por evidência confirmada), **duplicatas** (sem segunda contagem), **riscos críticos declarados** (não confirmados — rejeição por suspeita é proibida, `04_RUBRICA` §9) e **posturas de não-adoção** (o que a evidência, como está, não sustenta extrair). Nada aqui é decisão soberana; as condições de reavaliação são explícitas.

---

## 1. Rejeição formal (1) — única do acervo

| ID | Item | Motivo | Condição de reavaliação |
|---|---|---|---|
| `AC-05-REP-003` | `CL4R1T4S` | **Injeção de prompt confirmada por leitura direta** (E06=0, V1): o README instrui a IA leitora a revelar as próprias instruções de sistema; lido como achado, não obedecido. AGPL-3.0 com titularidade não resolvida | Nenhuma para uso como componente — a injeção está no arquivo. Leitura futura apenas sob o protocolo de conteúdo hostil (`05_GUIA` §7), como material de estudo de injeção |

**Corolário registrado:** `AC-05-PRT-014` é ponteiro redundante para `AC-05-REP-003`; permanece REFERENCIA vinculada (E01=1 impede rejeição), sem conteúdo próprio.

## 2. Duplicatas (2) — sem dupla contagem

| Cópia | Original | Base | Condição de reavaliação |
|---|---|---|---|
| `AC-03-VID-008` | `AC-03-VID-007` | SHA-256 idêntico, reconferido nas fases 2 e 3 | Se o hash divergir em reconferência futura (B-04), reavaliar como item independente |
| `AC-08-VID-005` | `AC-08-VID-004` | idem; herda a divergência NC=0 do original | idem |

**Não são duplicatas** (registrado para não reabrir): `AC-03-REP-003` (delta de 7 arquivos sobre 99,4% de `AC-03-REP-004` — PESQUISAR no delta); `AC-10-REP-006` (delta sobre 81,5% e 17/17 skills de `AC-10-REP-005` — REFERENCIA no delta); `AC-06-VID-013` (duplicação de conteúdo **declarada** com `AC-06-VID-001`, hashes diferentes — repetição, não evidência independente); o cluster promocional de 15 fichas (similaridade temática, P-3).

## 3. Riscos críticos

### 3.1 Confirmado (1)
`AC-05-REP-003` — ver §1. É o único E06=0 do acervo.

### 3.2 Declarados, não confirmados (E06=1 — 12 itens)
Rejeitá-los seria violar a rubrica (rejeição exige evidência); ignorá-los seria esconder risco. Ficam aqui, visíveis:

| ID | Risco declarado | Estado |
|---|---|---|
| `AC-04-REP-005` | Modo anti-detecção contra serviço de terceiro; autenticação persistente local | PESQUISAR — questão jurídica J-01 |
| `AC-06-REP-002` | Contorno de controle de plataforma; reúso de login/cookies | PESQUISAR — J-02 |
| `AC-06-VID-008` | Navegador apresentado como evasão ("parecer humano") | PESQUISAR — **deliberadamente não rejeitado**; se inspeção confirmar, V1 impõe rejeição (mesmo destino de `AC-05-REP-003`) |
| `AC-08-REP-003` | Contexto-imagem pode reduzir fidelidade, busca, auditabilidade e defesa contra injeção | PESQUISAR — verificação interna pendente de autorização |
| `AC-08-VID-006` | Mesmo risco do pxpipe, herdado por coerência | REFERENCIA |
| `AC-09-VID-003` | Instalação por download encadeado a shell (`seangeng.com`) | REFERENCIA — "nunca candidato" (V2); não instalar |
| `AC-10-PLA-001` | Engenharia reversa + dado pessoal; **risco jurídico** | REFERENCIA — exige revisão jurídica antes de qualquer uso |
| `AC-10-PRT-001` | Ranking automático de pessoas; decisão de emprego sobre dado pessoal | REFERENCIA |
| `AC-10-VID-006` | `npx skills add` exibido na tela, não inspecionado — "não instalar" (`103`) | REFERENCIA |
| `AC-10-VID-010` | Clonagem de app; dado financeiro/bancário | REFERENCIA |
| `AC-10-VID-016` | Documento técnico de obra sem profissional responsável | REFERENCIA |
| `AC-10-VID-017` | IA pode inventar dimensões em prancha de obra | REFERENCIA |
| `AC-10-VID-020` | Prospecção não solicitada | REFERENCIA |

### 3.3 Vetores estruturais registrados (sem item único)
- **Instrução hostil potencial não varrida:** 419 + 56 arquivos de `AC-10-REP-004`/`AC-10-REP-005` sob o teto de leitura — o acervo já provou que instrução pode carregar injeção (`AC-05-REP-003`).
- **Cadeia de suprimentos:** instalação colando frase com URL remota (`AC-06-REP-002`), `curl` anexando conteúdo remoto ao arquivo de instruções (`AC-05-REP-002`), `git clone && ./setup` executado pelo próprio agente (`AC-03-REP-004`), hooks de SessionStart que compilam binário (`AC-03-REP-003`).
- **Efeito externo irreversível sem limite declarado:** disparo para lista de contatos (`AC-06-VID-023`); gateways com custódia de chave não inspecionada (`AC-01-VID-001`).
- **Ocultação de autoria como finalidade declarada:** `AC-05-REP-005`, `AC-05-VID-015` ("ghost"), `AC-05-VID-025`.
- **Alucinação de STT documentada:** khmer em contexto lusófono (`AC-10-VID-020`) — razão concreta do bloqueio B-01.

## 4. Itens e conteúdos que devem permanecer externos / não-adotar

Registro consolidado das seções 6 das onze sínteses ("O que não adotar"). **Não são rejeições** — são exclusões de conteúdo, com motivo e condição de reavaliação.

| # | O que não adotar | Motivo | Reavaliação |
|---|---|---|---|
| N-01 | **Qualquer número dos 25 itens V7** (percentuais, contagens, prova social) | E15=0, sem fonte; itens sem conteúdo avaliável na parte dependente | Medição própria (backlog EXP) ou fonte primária (V-EXT) |
| N-02 | Badges e popularidade como sinal (estrelas, downloads, "Trending #1") | P-3: popularidade não move eixo | — |
| N-03 | As 9 descrições de catálogo NC=0 | Contraditas pela inspeção; vale a inspeção | — (fechado pela pré-correção 3) |
| N-04 | Instruções de escopo/ação de terceiro ("Não analise", "Install first", "Considere obrigatório", "comece pelo starter", "candidato a descarte") | Decisões de escopo de terceiro não são obedecidas (`04` §14.5; C-07, C-08) | — |
| N-05 | Instalação em massa de skills/plugins (cluster promocional; `AC-03-VID-003`) | Identidade, licença e escopo desconhecidos; "instalar tudo é antipadrão" (`101`) | V-EXT-16 |
| N-06 | Auto-instalação de skills sem gate humano (`AC-05-VID-009`, `AC-05-VID-017`) | Risco declarado; regra candidata de `99`: "descoberta pode ser automatizada; instalação, permissão e execução não" | Framework de Skills, com verificação prévia (`AC-09-REP-001`) |
| N-07 | "Auditoria de segurança por prompt" (`AC-09-VID-006`) | Não substitui escopo, autorização, testes e revisão humana | — |
| N-08 | Rankings e inventários opinativos como critério (área 01; `AC-10-PRT-006`, `AC-10-VID-012`) | Sem rubrica nem critério de priorização; datados | Medições próprias |
| N-09 | Totais internos de `AC-10-PLA-001` (rotas 131 × 128; integrações 14/13 × 13/14) e o termo "vulnerabilidades" (= brecha comercial) | Não reconciliados; leitura como falha de segurança seria erro induzido | Reconciliação + revisão jurídica |
| N-10 | A árvore de `AC-11-PRT-006` como template | Dois defeitos estruturais no próprio original (`109`) | — (ilustração falha) |
| N-11 | A acusação de "erro conceitual" sobre `AC-11-PRT-001` | O erro é da leitura do catálogo, não do original — **removida** | — (fechado) |
| N-12 | Nomes de produto vindos de STT bruto (`AC-01-VID-005`, `AC-08-VID-003`) | Motor grafou errado; identificação depende de revisão | Revisão humana de áudio (B-01) |
| N-13 | A fala não revisada de qualquer vídeo como citação | STT automático sem revisão humana; 1 caso de alucinação documentada | B-01/B-05 |
| N-14 | Os três repositórios fora do acervo citados em `AC-07-VID-003` e `chaseai-yt/grill-me-codex` (`AC-09-VID-005`) | Não conferidos; "Não instalar" (`94`) | Pesquisa externa |
| N-15 | Estimativa apresentada como resultado (`AC-08-VID-006` × fonte primária `AC-08-REP-003`) | Conflito C-04: prevalece a forma da fonte primária ("estimativa a medir") | Leitura dos evals (EXP-09) |
| N-16 | A tese "quanto mais contexto, melhor" (`AC-04-VID-010`) e seu oposto (`AC-08-VID-008`) | C-01 aberto: nenhum dos dois mede | Experimento próprio |
| N-17 | A escolha entre as três vias de memória (markdown × RAG próprio × RAG hospedado) | C-02 aberto, declarado pelo próprio acervo | Decisão do Kernel técnico, com EXP-03/05 |
| N-18 | O debate internalizar × contratar (C-09) | Explicitamente adiado (`01_ESTADO` §7) | Decisão soberana, fora desta frente |

## 5. Condição geral de reavaliação

Todo item deste arquivo pode mudar de estado **apenas por evidência nova, registrada e rastreável**: inspeção direta (para riscos declarados), medição própria (para números), fonte primária (para identidades e licenças) ou parecer jurídico (para J-01/J-02/J-03 e `AC-10-PLA-001`). Nenhum muda por opinião, por repetição ou por coerência narrativa.

> Este arquivo é evidência externa, provisória e não normativa. Não autoriza adoção de nada.
