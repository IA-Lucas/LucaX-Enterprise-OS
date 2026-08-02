> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO

# SÍNTESE — ÁREA 06 — MCP E CONECTORES

**Frente:** Programa de Inteligência do Acervo · **Fase 3 — Síntese** (missão **A3**) · **Data:** 2026-07-29 · **Avaliador:** Claude Opus 5 (Fase 3)

**Origem:** external-evidence · **Autoridade:** nenhuma · **Estado:** provisório · **Normativo:** não · **Adoção:** não-decidida

**Base:** 40 fichas de `07_FICHAS-DE-EVIDENCIA/06_CONECTORES-MCP.md` (4 REPO · 13 PRINT · 23 VÍDEO · 0 PLANILHA), lidas integralmente, mais as pré-correções de `08_SINTESES-DAS-11-AREAS/00_PRE-CORRECOES-E-CORRESPONDENCIA.md`. Nenhuma fonte original foi aberta nesta fase.

---

## 1. O que sabemos

A pergunta central da área é **como o sistema alcança o mundo externo**, e a observação de método da própria fase 2 fixa o enquadramento: conector é fronteira de autoridade — identidade, credencial, dados alcançáveis, operações permitidas e efeitos externos (`AC-06-REP-001`, nota de método do arquivo de fichas).

O que a evidência sustenta, em blocos:

- **Quatro artefatos inspecionáveis (LV4), todos com licença permissiva lida e íntegra:** `AC-06-REP-001` (Apache-2.0), `AC-06-REP-002` (MIT), `AC-06-REP-003` (MIT), `AC-06-REP-004` (MIT). Os 36 itens restantes estão em LV3: 13 prints com inspeção visual pela trilha Codex (`107`) e 23 vídeos com ficha visual (`101`) e STT automático não revisado (`117`) — LV3-V + LV3-A não produz LV4 (cobertura padrão dos vídeos, declarada no arquivo de fichas).
- **Há mecanismos concretos de alcance externo descritos com artefato:** árvore de acessibilidade com referências para agentes (`AC-06-REP-001`); recuperação de documentação por versão via duas ferramentas MCP nomeadas (`AC-06-REP-003`); roteamento de canais com backend preferencial e alternativo por plataforma (`AC-06-REP-002`); busca em 16 fontes com pontuação por engajamento medido (`AC-06-REP-004`).
- **O material não-repositório é dominado por listas e mapas sem escopo:** dos 13 prints, vários são "só listagem" ou "só índice" (`AC-06-PRT-001`, `AC-06-PRT-003`, `AC-06-PRT-005`, `AC-06-PRT-012`, `AC-06-PRT-013`); dos 23 vídeos, a maioria é divulgação de repositórios/ferramentas sem demonstração (`AC-06-VID-003`, `AC-06-VID-004`, `AC-06-VID-005`, `AC-06-VID-007`, `AC-06-VID-008`, `AC-06-VID-011`, `AC-06-VID-015`, `AC-06-VID-016`, `AC-06-VID-018`, `AC-06-VID-019`, `AC-06-VID-021`, `AC-06-VID-022`).
- **Os únicos controles explícitos enunciados na área vêm de prints, não de implementações:** aprovação humana no envio (`AC-06-PRT-009`) e somente-leitura primeiro, com confirmação manual de toda escrita financeira (`AC-06-PRT-011`). O fechamento da área registra que **nenhum** dos 23 vídeos exibe implementação de controle equivalente (fechamento da área 06, achado 4).
- **A superfície de segurança é predominantemente ND:** `E06 = ND` em todos os 13 prints e 23 vídeos (V2 disparada em todos eles); entre os repositórios, `E06 = 3` (`AC-06-REP-003`), `E06 = 2` (`AC-06-REP-001`, `AC-06-REP-004`) e `E06 = 1` — risco **declarado** pela própria fonte e **não confirmado** por inspeção (`AC-06-REP-002`, V2 disparada).
- **Volume de desconhecido medido:** 183 de 600 eixos em ND (30,5 %), recontado por ferramenta (fechamento da área 06).
- **Repetição promocional medida, não confirmação:** seis vídeos formam o cluster promocional da área (`AC-06-VID-007`, `015`, `016`, `018`, `021`, `022`), sobreposto ao cluster da área 05; `AC-06-VID-001` e `AC-06-VID-013` repetem a mesma demonstração (cobertura padrão dos vídeos; `AC-06-VID-013`, E14 = 0). A Fase 2 tratou a repetição como redução de E14, nunca como verificação (P-3).

## 2. Fontes mais fortes e por quê

Critério declarado: força medida pelos dados da ficha (LV, NF, ND, vetos), nunca por popularidade — `AC-06-VID-018` registra literalmente que "estrelas e 'crescimento' não provam qualidade".

- **`AC-06-REP-003` (context7) — a ficha mais forte da área.** LV4 com hash reconferido; NF = 4 com apenas 2 ND; `E06 = 3` (o único repositório da área que alcança 3 em segurança, com `SECURITY.md`, OAuth e caminho de remoção documentados); `E12 = 5` (reversão documentada pelo próprio autor); nenhuma porta de veto disparada; `RF = CANDIDATO A PILOTO`. Ressalvas registradas na própria ficha: `E11 = 2` (valor depende de índice hospedado por terceiro), `E13 = ND` (suíte não localizada sob o teto de leitura), `E15 = 1` (a alegação central — eliminar API alucinada — não tem eval lido).
- **`AC-06-REP-001` (agent-browser) e `AC-06-REP-004` (last30days) — LV4, NF = 4, mas com `E06 = 2`.** O primeiro tem `evals/` e `benchmarks/` inspecionados (E13 = 4) e superfície ampla sem `SECURITY.md` (`eval <js>`, conexão por protocolo de depuração, streaming em porta). O segundo traz o **único portão de qualidade quantificado do acervo inteiro** — cobertura mínima de 84 % com baseline datado de 2026-07-03 e regra escrita de não rebaixamento — e, ainda assim, o diretório `tests/` declarado no manifesto não aparece na raiz efetiva (E13 = 2; fechamento da área 06, achado 5).
- **`AC-06-REP-002` (Agent-Reach) — LV4, NF = 3, `E06 = 1`.** Forte em engenharia de degradação de canal (E14 = 4) e em testes de contrato nomeados, mas com risco ativo **declarado** (contorno de controle de plataforma e reúso de login/cookies) e inconsistência interna de versão (`1.5.0` no manifesto × `1.3.1` no changelog — fato observado).
- **Entre os LV3, os mais informativos são os que enunciam regra, não lista:** `AC-06-PRT-009` e `AC-06-PRT-011` (controles declarados, RP = 3), `AC-06-PRT-008` (regra de contenção "menu, not a shopping spree", RP = 3), `AC-06-VID-017` (pipeline reunião → decisão com saída estruturada, RP = 3) e `AC-06-VID-023` (mecanismo declarado de gateway MCP local, RP = 3, `E15 = 2` — alegações conferíveis no repositório público, ainda não conferidas).

## 3. Padrões recorrentes

- **Assimetria leitura × escrita.** A distinção entre ler/relatar e otimizar/executar aparece em `AC-06-VID-010` (achado estrutural registrado por `101`), é elevada a regra com portão humano em `AC-06-PRT-009`, atinge a forma mais dura em `AC-06-PRT-011` (somente-leitura primeiro; confirmação manual de toda escrita, "sem exceção") e reaparece como advertência em `AC-06-VID-022` ("não confundir análise com autorização para operar"). O fechamento da área consolida: é a assimetria entre o que o material recomenda e o que ele controla (achado 4).
- **Contenção contra instalação por volume.** "This is a menu. Not a shopping spree." (`AC-06-PRT-008`) converge com "`instalar tudo` é antipadrão" (`AC-06-VID-021`, avaliação `101`) e com o conjunto mínimo de cinco fronteiras de `AC-06-PRT-007`.
- **Composição por função em vez de catálogo por nome.** Cadeias organizadas por saída (`AC-06-PRT-002`), encadeamento erro → correção → proposta de mudança (`AC-06-PRT-008`), mapa ferramenta → função com composição de pipeline (`AC-06-VID-014`), mapa de 16 capacidades por família (`AC-06-VID-021`), prompt operacional associado a cada conector (`AC-06-PRT-004`).
- **Auto-hospedagem como mudança de natureza da fronteira, não só de fornecedor** (`AC-06-VID-003`), com a ressalva registrada de que self-hosting transfere operação e segurança para a empresa sem eliminar risco (`AC-06-VID-003`, avaliação `101`); reaparece na camada de voz auto-hospedável (`AC-06-PRT-006`) e no gateway local de mensageria (`AC-06-VID-023`).
- **Degradação de canal tratada como problema de engenharia** — backend preferencial + alternativo por plataforma com troca declarada quando um quebra (`AC-06-REP-002`, E14 = 4, sem equivalente no acervo).
- **Documentação defasada como problema de conector** — recuperação por identificador de biblioteca e versão no momento da geração (`AC-06-REP-003`, E14 = 3, sem equivalente pronto no acervo).
- **Reúso de sessão autenticada como capacidade oferecida**, sem controle declarado: "bring your own keys **and browser sessions**" (`AC-06-REP-004`, fato declarado que sustenta `E06 = 2`) e agente operando navegador com login na conta do usuário (`AC-06-VID-020`, fala provável, achado de superfície registrado).

## 4. Conflitos e divergências

- **Catálogo × fonte (NC = 2), quatro fichas com divergência material:**
  - `AC-06-PRT-008` — o print escreve `Neo`; o catálogo grafa "Neon" sem evidência na imagem. A síntese usa o texto visível ("Neo", identidade a verificar).
  - `AC-06-PRT-012` — o print diz apenas "Data tools first"; o catálogo acrescenta "execução depois", inferência prudente **não presente no print**. A síntese registra só a metade visível e nomeia a omissão: a regra de adiar execução, que mudaria o sentido, **não é texto da fonte**.
  - `AC-06-VID-002` — dois dos três produtos citados no título do catálogo não aparecem entre os oito conectores legíveis; a atribuição material não conferiu.
  - `AC-06-VID-007` — o catálogo afirma "três instalações para começar"; `101` observa 24 complementos divulgados. Contagem divergente; a síntese usa os 24 observados.
- **Grafia divergente sem confirmação na origem:** "Camofox" (catálogo) × "Camoflox" (`101`) em `AC-06-VID-008`; "NanoBanana 2" preservado como observado em `AC-06-PRT-001`; erros do original "Ontlook" e "Microsoft 366" preservados em `AC-06-PRT-013`.
- **Inconsistência interna da mesma fonte:** `version = "1.5.0"` no manifesto × `[1.3.1] - 2026-03-27` como entrada mais recente do changelog em `AC-06-REP-002` (fato observado, não reconciliado).
- **Declarado × presente:** `testpaths = ["tests"]` e portão de cobertura de 84 % no manifesto de `AC-06-REP-004`, mas o diretório `tests/` não consta da raiz efetiva.
- **Controles declarados × controles implementados:** os prints `AC-06-PRT-009` e `AC-06-PRT-011` enunciam portões humanos; nenhum dos 23 vídeos exibe implementação equivalente (fechamento da área 06, achado 4). Declarado não é implementado.
- **Anomalia de fechamento (registrada, não resolvida):** a tabela de fechamento da área 06 declara `RF = EXIGE PESQUISA` = 9 e `RF = REFERÊNCIA` = 30, mas a contagem ficha a ficha produz **11 EXIGE PESQUISA** (`AC-06-REP-001`, `REP-002`, `REP-004`, `PRT-006`, `VID-006`, `VID-008`, `VID-011`, `VID-012`, `VID-019`, `VID-020`, `VID-023`) e **28 REFERÊNCIA**. O arquivo de pré-correções, ao classificar pendências, lista exatamente esses 11 itens da área 06 (8 externos + 1 resolvível na própria fonte que estoura o teto + 2 dependentes do proprietário), o que corrobora o valor 11. Esta síntese adota o RF declarado em cada ficha e trata os totais do fechamento como não reconciliados.

## 5. Candidatos fortes, pilotos e referências

Nenhuma classificação abaixo equivale a adoção oficial; o registro é por ID, nunca ordenado por prioridade.

- **CANDIDATO-FORTE:** nenhum — o fechamento da área registra zero, e a ficha de `AC-06-REP-003` explicita o motivo (`E15 = 1`, abaixo de 3 no Bloco A).
- **PILOTO:** `AC-06-REP-003` — único item da área com `RF = CANDIDATO A PILOTO`. A própria ficha registra que "CANDIDATO A PILOTO não significa pilotar", com três restrições nomeadas (`E11 = 2`, `E13 = ND`, `E15 = 1`).
- **PESQUISAR (11):** `AC-06-REP-001`, `AC-06-REP-002`, `AC-06-REP-004`, `AC-06-PRT-006`, `AC-06-VID-006`, `AC-06-VID-008`, `AC-06-VID-011`, `AC-06-VID-012`, `AC-06-VID-019`, `AC-06-VID-020`, `AC-06-VID-023` — cada um com lacuna nomeada e verificação escrita na ficha (detalhes na seção 12).
- **REFERENCIA (28):** os doze prints restantes e dezesseis vídeos, todos insumos de consulta com LV ≥ 3 e `E06`/`E07` em ND (V2/V4 disparadas) — lista completa na seção 12.
- **ADAPTAR-PADRAO / REJEITAR / DUPLICATA:** nenhum nesta área. `AC-06-VID-013` tem duplicação de conteúdo **declarada** com `AC-06-VID-001`, mas não é DUPLICATA: os hashes diferem e nenhuma medição de sobreposição foi feita — a ficha o mantém como REFERÊNCIA tratada como repetição da mesma família promocional, não evidência independente. `AC-06-VID-008` foi **deliberadamente não rejeitado**: a rejeição exigiria `E06 = 0` por inspeção direta (§9), e o risco de evasão é declarado por terceiro, não confirmado.

## 6. O que não adotar

Registro de posturas que a evidência desaconselha — não são decisões de rejeição formal (nenhuma ficha da área tem `RF = REJEITADO`):

- **Instalação por volume:** "instalar tudo" é antipadrão declarado (`AC-06-VID-021`, avaliação `101`), convergente com `AC-06-PRT-008`.
- **Obediência a instrução de terceiro:** "Install first" (`AC-06-PRT-007`, registrado por `107` como "recomendação do slide, não autorização"); "Considere obrigatório em qualquer sistema que escreva código" (`AC-06-REP-003`, alegação do catálogo — instrução não obedecida, `04` §14.5).
- **Números promocionais como fato:** estrelas, "crescimento", contagens de upvotes e "Trending #1" (`AC-06-VID-018`, `AC-06-REP-002`, `AC-06-REP-004`, `AC-06-VID-006` — P-3 aplicado em todos). Nenhum número vindo dos quatro itens V7 da área (`AC-06-PRT-006`, `AC-06-VID-006`, `AC-06-VID-012`, `AC-06-VID-020`) entra como fato: esses itens **não têm conteúdo avaliável além do próprio texto** na parte que depende da alegação sem fonte.
- **Links encurtados não resolvidos:** `AC-06-PRT-003` é índice cujos destinos a captura não valida — resolver dezenas de links é navegação, fora do escopo desta frente.
- **Aplicativos de consumo tratados como infraestrutura empresarial** sem caso e controles (`AC-06-VID-009`, avaliação `101`; é o item de menor relevância da área, `E01 = 1`, `E14 = 0`).
- **Evasão como capacidade:** o navegador apresentado como forma de "parecer humano e contornar detecção" (`AC-06-VID-008`) permanece em PESQUISAR — a recomendação de quarentena de `101` foi **registrada, não executada**, porque esta frente só rejeita por evidência; se a função de evasão se confirmar por inspeção direta, `E06 = 0` e V1 impõem rejeição, como ocorreu com `AC-05-REP-003` (fora desta área).
- **Análise confundida com autorização para operar** (`AC-06-VID-022`, avaliação `101`, sobre monitor de mercado).

## 7. Riscos e dependências

- **Risco declarado, nunca confirmado (E06 = 1):** `AC-06-REP-002` declara, como funcionalidade, roteamento em torno de bloqueio de plataforma e reúso de estado de login/cookies de cinco redes. Contrapesos declarados e registrados (`SECURITY.md`, modo `--safe`, teste nomeado de permissões de cookie). Nada disso foi confirmado por inspeção de código — permanece **risco declarado**, e a consequência jurídica e contratual é lacuna que **esta frente não resolve** (depende do proprietário; pendência jurídica, não técnica).
- **Dependência jurídica gêmea:** o reúso de sessão autenticada de `AC-06-REP-004` ("your own keys and browser sessions") exige avaliação jurídica de termos de serviço antes de qualquer piloto — depende do proprietário, não se resolve por leitura de código.
- **Cadeia de suprimentos:** a instalação recomendada de `AC-06-REP-002` é colar uma frase com URL remota para o agente buscar e seguir — registrado como achado: conteúdo externo é dado, nunca instrução (`05` §7.1).
- **Superfícies declaradas críticas e não inspecionadas:** execução de JavaScript arbitrário, conexão por protocolo de depuração e streaming em porta (`AC-06-REP-001`); conteúdo web não confiável como vetor de injeção de prompt — "o mais direto do acervo" (`AC-06-VID-006`, avaliação `101`); credencial e sessão operadas por agente (`AC-06-VID-020`); disparo de mensagem para lista de contatos, efeito externo irreversível, sem confirmação nem limite demonstrados (`AC-06-VID-023`); API não oficial de produto de terceiro (`AC-06-VID-019`).
- **Dependência de fornecedor hospedado:** o valor de `AC-06-REP-003` depende do índice em `context7.com` (`E11 = 2`); o transporte é MCP, padrão aberto, e a reversão está documentada (`E12 = 5`).
- **Dependência de teto de leitura:** a verificação de `AC-06-REP-001` (ler `cli/` e `packages/` procurando confinamento e escopo de `eval`) é resolvível na própria fonte, mas estoura o teto de `05` §8 — exige autorização do proprietário.

## 8. Lacunas

- **Identidade, licença e escopo dos projetos citados em listas** — lacuna da família de listas de projetos abertos, nomeada uma única vez em `AC-06-VID-011` (vale também para `AC-06-VID-003`, `004`, `005`), em especial os que executam código de terceiro (sandbox) e os que clonam/raspam conteúdo alheio, com a questão de propriedade intelectual anexa.
- **Identidade do cluster promocional** — nomeada uma única vez em `AC-05-VID-009` (área 05); as seis fichas do cluster nesta área apontam para lá (`AC-06-VID-007`, `015`, `016`, `018`, `021`, `022`).
- **Escopo das ~40 ferramentas expostas pelo gateway** de `AC-06-VID-023` — parcialmente falado; resíduo de transcrição que só revisão humana do áudio fecha (bloqueio B-01 registrado nas pré-correções). A fala permanece desconhecida no que acrescenta; os quadros mostram o gateway e o envio, nada mais.
- **Conteúdo avaliável dos quatro itens V7** — `AC-06-PRT-006` (identidade, autoria, licença efetiva e desempenho medido do produto de voz retratado), `AC-06-VID-006` (ganho de "10×" sem medição nem definição), `AC-06-VID-012` (promessas de preço/velocidade/qualidade e enquadramento de "cinco IAs" que agrupa classes incomparáveis), `AC-06-VID-020` (desconto e alegação de preço, possivelmente com vínculo de afiliação não declarado; identidade da ferramenta de controle de navegador). Nos quatro, a proposta depende de alegação sem fonte: **não há conteúdo avaliável além do próprio texto** na parte dependente.
- **Manutenção (E05) desconhecida** em todos os 13 prints e 23 vídeos, e também em `AC-06-REP-001` e `AC-06-REP-003` (E05 = ND, sem data observada no material lido).
- **Consequência jurídica** de contorno de controle de plataforma e reúso de login/sessão (`AC-06-REP-002`, `AC-06-REP-004`) — fora da competência desta frente.
- Onde não há evidência, o estado é **desconhecido** — nenhuma lacuna acima foi preenchida por coerência narrativa.

## 9. Decisão provisória

Tabela ID → classe → motivo de uma linha citando a ficha. Vocabulário fechado; nenhuma classe equivale a adoção; registro por ID, sem ordenação por prioridade.

| ID | Classe | Motivo (uma linha) |
|---|---|---|
| AC-06-REP-001 | PESQUISAR | `RF = EXIGE PESQUISA`: LV4/NF = 4, mas `E06 = 2` — superfície ampla sem `SECURITY.md`; verificação interna estoura o teto (§9 da ficha). |
| AC-06-REP-002 | PESQUISAR | `RF = EXIGE PESQUISA` por V2: `E06 = 1`, contorno de plataforma e reúso de login **declarados**; lacuna jurídica que esta frente não resolve. |
| AC-06-REP-003 | PILOTO | `RF = CANDIDATO A PILOTO`: LV4, `E06 = 3`, `E12 = 5`, sem veto; ressalvas `E11 = 2`, `E13 = ND`, `E15 = 1` na própria ficha. |
| AC-06-REP-004 | PESQUISAR | `RF = EXIGE PESQUISA`: `E06 = 2` (reúso de sessão autenticada declarado) e `tests/` declarado ausente da raiz efetiva. |
| AC-06-PRT-001 | REFERENCIA | `RF = REFERÊNCIA`: matriz dez tarefas × três candidatos, só listagem, sem critério (NF = 1, V2/V4). |
| AC-06-PRT-002 | REFERENCIA | `RF = REFERÊNCIA`: seis cadeias de produção por saída; o padrão transfere, as cadeias são do autor (E04 = 2). |
| AC-06-PRT-003 | REFERENCIA | `RF = REFERÊNCIA`: índice de links encurtados não validados; resolver destinos é navegação, fora do escopo. |
| AC-06-PRT-004 | REFERENCIA | `RF = REFERÊNCIA`: oito conectores com prompt operacional por conector (RP = 3), sem escopo inspecionado. |
| AC-06-PRT-005 | REFERENCIA | `RF = REFERÊNCIA`: onze combinações ferramenta × promessa, conferidas só "como texto visível". |
| AC-06-PRT-006 | PESQUISAR | `RF = EXIGE PESQUISA` por V7 (`E15 = 0`): alegação de substituição vem de legenda de post; sem conteúdo avaliável além do próprio texto. |
| AC-06-PRT-007 | REFERENCIA | `RF = REFERÊNCIA`: conjunto mínimo de cinco fronteiras; "Install first" não obedecido; um dos cinco tem ficha própria (`AC-06-REP-003`). |
| AC-06-PRT-008 | REFERENCIA | `RF = REFERÊNCIA` (NC = 2): regra "menu, not a shopping spree" e encadeamento concreto; grafia "Neo" preservada, "Neon" descartada. |
| AC-06-PRT-009 | REFERENCIA | `RF = REFERÊNCIA`: único controle declarado para escrita externa (aprovação humana no envio), sem implementação inspecionada. |
| AC-06-PRT-010 | REFERENCIA | `RF = REFERÊNCIA`: cinco conectores criativos; números promocionais conferem só como texto visível (NF = 1). |
| AC-06-PRT-011 | REFERENCIA | `RF = REFERÊNCIA`: regra mais explícita da área — somente-leitura primeiro, confirmação manual de toda escrita; declarada, não verificada. |
| AC-06-PRT-012 | REFERENCIA | `RF = REFERÊNCIA` (NC = 2): só "Data tools first" é texto da fonte; "execução depois" é inferência do catálogo, nomeada como tal. |
| AC-06-PRT-013 | REFERENCIA | `RF = REFERÊNCIA`: 20 conectores por categoria com erros do original preservados ("Ontlook", "Microsoft 366"); não é fonte de nomes exatos. |
| AC-06-VID-001 | REFERENCIA | `RF = REFERÊNCIA`: demonstração audiovisual isolada, sem prompt nem parâmetro; repetição da família com `AC-06-VID-013`. |
| AC-06-VID-002 | REFERENCIA | `RF = REFERÊNCIA` (NC = 2): oito de quinze conectores legíveis; dois produtos do título do catálogo não aparecem nos quadros. |
| AC-06-VID-003 | REFERENCIA | `RF = REFERÊNCIA`: auto-hospedagem como mudança de fronteira (E01 = 3); lacuna de identidade é da família, nomeada em `AC-06-VID-011`. |
| AC-06-VID-004 | REFERENCIA | `RF = REFERÊNCIA`: oito projetos legíveis de dez por domínio; lacuna da família em `AC-06-VID-011`. |
| AC-06-VID-005 | REFERENCIA | `RF = REFERÊNCIA`: nove ferramentas legíveis de dez; social proof e economia são alegações (P-3). |
| AC-06-VID-006 | PESQUISAR | `RF = EXIGE PESQUISA` por V7 (`E15 = 0`): "10×" sem medição; injeção de prompt via conteúdo web não inspecionada; sem conteúdo avaliável além do próprio texto. |
| AC-06-VID-007 | REFERENCIA | `RF = REFERÊNCIA` (NC = 2): cluster promocional; catálogo diz 3 instalações, `101` observa 24 — repetição não é validação. |
| AC-06-VID-008 | PESQUISAR | `RF = EXIGE PESQUISA`: navegador apresentado como evasão; **deliberadamente não rejeitado** — §9 exige `E06 = 0` por inspeção direta. |
| AC-06-VID-009 | REFERENCIA | `RF = REFERÊNCIA`: menor relevância da área (`E01 = 1`, `E14 = 0`); `E01 ≠ 0`, logo não cabe rejeição. |
| AC-06-VID-010 | REFERENCIA | `RF = REFERÊNCIA`: distinção leitura/relatório × otimização/execução (RP = 3), mais desenvolvida em `AC-06-PRT-009`/`011`. |
| AC-06-VID-011 | PESQUISAR | `RF = EXIGE PESQUISA`: carrega a lacuna da família — identidade, licença e superfície de execução dos projetos abertos (sandbox, scraping). |
| AC-06-VID-012 | PESQUISAR | `RF = EXIGE PESQUISA` por V7 (`E15 = 0`): promessas sem fonte e enquadramento de classes incomparáveis; sem conteúdo avaliável além do próprio texto. |
| AC-06-VID-013 | REFERENCIA | `RF = REFERÊNCIA`: duplicação de conteúdo declarada com `AC-06-VID-001`, mas hashes diferem e não há medição — não é DUPLICATA; conta como repetição, não evidência independente. |
| AC-06-VID-014 | REFERENCIA | `RF = REFERÊNCIA`: separação por função e composição de pipeline (RP = 3); marcas são candidatas, não arquitetura. |
| AC-06-VID-015 | REFERENCIA | `RF = REFERÊNCIA`: cluster; três dos seis repositórios já têm ficha própria mais forte no acervo. |
| AC-06-VID-016 | REFERENCIA | `RF = REFERÊNCIA`: cluster; cinco dos oito itens já têm ficha própria; combinação amplia a superfície (avaliação `101`). |
| AC-06-VID-017 | REFERENCIA | `RF = REFERÊNCIA`: pipeline reunião → decisão rastreável (RP = 3); gate de consentimento/retenção declarado por `101`, não verificado. |
| AC-06-VID-018 | REFERENCIA | `RF = REFERÊNCIA`: cluster; estrelas e "crescimento" não provam qualidade (P-3). |
| AC-06-VID-019 | PESQUISAR | `RF = EXIGE PESQUISA`: item apresentado como **API não oficial** de produto de terceiro — identidade, licença e termos do produto original. |
| AC-06-VID-020 | PESQUISAR | `RF = EXIGE PESQUISA` por V7 (`E15 = 0`): alegações comerciais sem fonte; sessão autenticada operada por agente sem controle declarado. |
| AC-06-VID-021 | REFERENCIA | `RF = REFERÊNCIA`: mapa de 16 capacidades; "instalar tudo" é antipadrão declarado por `101`. |
| AC-06-VID-022 | REFERENCIA | `RF = REFERÊNCIA`: cluster; quatro dos cinco são repetição no mesmo lote (`E14 = 0`); análise ≠ autorização para operar. |
| AC-06-VID-023 | PESQUISAR | `RF = EXIGE PESQUISA`: efeito externo irreversível (disparo em lista); escopo das ~40 ferramentas parcialmente falado — resíduo de transcrição; `E15 = 2`, conferível na origem. |

## 10. Experimento que poderia validá-la

**Proposta — não é plano aprovado.** A decisão provisória mais forte da área é PILOTO para `AC-06-REP-003`, e ela repousa em uma alegação não verificada: que injetar documentação por versão elimina API alucinada (`E15 = 1`). O experimento que poderia validá-la:

1. Montar um conjunto fechado de tarefas de geração de código desta casa, contra bibliotecas com versões conhecidas, e registrar a taxa de referências a API inexistente ou desatualizada **sem** o conector.
2. Repetir as mesmas tarefas com a recuperação por versão ativada, medindo a mesma taxa com a mesma rubrica.
3. Registrar também o que é enviado ao serviço remoto (a ficha declara chave de API por cabeçalho e nenhum escopo de retenção lido — `E06 = 3`, teto declarado) e confirmar a reversão documentada (`npx ctx7 remove`, `E12 = 5`).

Custos e limites declarados: exige autorização do proprietário (experimento próprio), não envia conversa ou dado desta casa a terceiro sem decisão prévia, e não resolve `E13 = ND` (suíte não localizada sob o teto) nem `E05 = ND`. Um segundo experimento independente, também proposta: para `AC-06-VID-023`, enumerar na origem pública as ~40 ferramentas do gateway e classificar quais produzem efeito irreversível — **sem instalar nem conectar conta** —, fechando ao mesmo tempo o resíduo de transcrição por leitura da lista publicada, se ela existir.

## 11. Confiança da síntese

**Média**, com justificativa rastreável:

- **Cobertura de LV:** apenas 4 dos 40 itens em LV4 (os repositórios `AC-06-REP-001` a `004`); os 36 restantes são LV3-V (± LV3-A não revisado) — a área sabe muito sobre listas e pouco sobre artefatos.
- **Volume de ND:** 183 de 600 eixos (30,5 %), recontado por ferramenta (fechamento da área 06) — incluindo `E06` e `E07` em ND em **todos** os prints e vídeos.
- **Itens V7:** 4 (`AC-06-PRT-006`, `AC-06-VID-006`, `AC-06-VID-012`, `AC-06-VID-020`) — em nenhum deles número entrou como fato.
- **EXIGE PESQUISA:** 11 de 40 itens (27,5 %), dos quais 2 com pendência jurídica (`AC-06-REP-002`, `AC-06-REP-004`) e 1 com verificação interna que estoura o teto (`AC-06-REP-001`).
- **NC = 0:** nenhum nesta área. **NC = 2:** 4 fichas com divergência material (`AC-06-PRT-008`, `AC-06-PRT-012`, `AC-06-VID-002`, `AC-06-VID-007`), mais duas divergências de grafia/versão (`AC-06-VID-008`, `AC-06-REP-002`) — todas nomeadas, nenhuma normalizada em silêncio.
- **Anomalia não resolvida:** totais de fechamento da área (9 EXIGE PESQUISA / 30 REFERÊNCIA) divergem da contagem ficha a ficha (11 / 28); esta síntese adota o RF de cada ficha, corroborado pela classificação de pendências das pré-correções (seção 4).
- **Cluster promocional:** 6 fichas, tratadas como redução de diferencial, nunca como confirmação (P-3).

A confiança é média e não alta porque a decisão mais forte (PILOTO) depende de uma alegação central sem eval (`AC-06-REP-003`, `E15 = 1`), e é média e não baixa porque os quatro artefatos centrais têm LV4 com hash reconferido, licença lida e divergências explicitamente registradas.

## 12. Cobertura

Todos os 40 IDs da área, com a decisão provisória de cada um (espelha a seção 9; motivos completos lá):

| ID | Decisão provisória | ID | Decisão provisória |
|---|---|---|---|
| AC-06-REP-001 | PESQUISAR | AC-06-VID-005 | REFERENCIA |
| AC-06-REP-002 | PESQUISAR | AC-06-VID-006 | PESQUISAR |
| AC-06-REP-003 | PILOTO | AC-06-VID-007 | REFERENCIA |
| AC-06-REP-004 | PESQUISAR | AC-06-VID-008 | PESQUISAR |
| AC-06-PRT-001 | REFERENCIA | AC-06-VID-009 | REFERENCIA |
| AC-06-PRT-002 | REFERENCIA | AC-06-VID-010 | REFERENCIA |
| AC-06-PRT-003 | REFERENCIA | AC-06-VID-011 | PESQUISAR |
| AC-06-PRT-004 | REFERENCIA | AC-06-VID-012 | PESQUISAR |
| AC-06-PRT-005 | REFERENCIA | AC-06-VID-013 | REFERENCIA |
| AC-06-PRT-006 | PESQUISAR | AC-06-VID-014 | REFERENCIA |
| AC-06-PRT-007 | REFERENCIA | AC-06-VID-015 | REFERENCIA |
| AC-06-PRT-008 | REFERENCIA | AC-06-VID-016 | REFERENCIA |
| AC-06-PRT-009 | REFERENCIA | AC-06-VID-017 | REFERENCIA |
| AC-06-PRT-010 | REFERENCIA | AC-06-VID-018 | REFERENCIA |
| AC-06-PRT-011 | REFERENCIA | AC-06-VID-019 | PESQUISAR |
| AC-06-PRT-012 | REFERENCIA | AC-06-VID-020 | PESQUISAR |
| AC-06-PRT-013 | REFERENCIA | AC-06-VID-021 | REFERENCIA |
| AC-06-VID-001 | REFERENCIA | AC-06-VID-022 | REFERENCIA |
| AC-06-VID-002 | REFERENCIA | AC-06-VID-023 | PESQUISAR |
| AC-06-VID-003 | REFERENCIA | | |
| AC-06-VID-004 | REFERENCIA | | |

**Totais:** 40 IDs · PILOTO 1 · PESQUISAR 11 · REFERENCIA 28 · CANDIDATO-FORTE 0 · ADAPTAR-PADRAO 0 · REJEITAR 0 · DUPLICATA 0.

> Este arquivo é evidência externa, provisória e não normativa. Não autoriza adoção de nada.
