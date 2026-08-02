> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO

# SÍNTESE — ÁREA 10 — APLICAÇÕES DE NEGÓCIO

**Frente:** Programa de Inteligência do Acervo · **Fase 3 — Síntese** (missão **A3**) · **Data:** 2026-07-29 · **Avaliador:** Claude Opus 5 (Fase 3)

**Origem:** external-evidence · **Autoridade:** nenhuma · **Estado:** provisório · **Normativo:** não · **Adoção:** não-decidida

**Entrada:** as 46 fichas de `_SAIDA-COMPANY-OS/07_FICHAS-DE-EVIDENCIA/10_APLICACOES-DE-NEGOCIO.md` (6 REPO · 16 PRINT · 23 VÍDEO · 1 PLANILHA), lidas integralmente, mais as pré-correções de `00_PRE-CORRECOES-E-CORRESPONDENCIA.md`. Nenhuma fonte original foi aberta nesta fase.

---

## 1. O que sabemos

A área é a maior do acervo — 46 itens — e sua pergunta central é *que verticais provar primeiro, e como um sistema de agentes é empacotado por domínio* (cabeçalho do arquivo de fichas).

Sobre **empacotamento por domínio**, a evidência mais sólida são os seis repositórios, todos LV4:

- Existe um padrão repetido de **"uma fonte, dois destinos"** — mesmo prompt e mesmas skills, instaláveis como plugin ou como agente gerenciado — observado no texto lido de `AC-10-REP-001` e `AC-10-REP-003`, e declarado (não verificado) como "Same system prompt, same skills — you choose where it runs" em `AC-10-REP-003`.
- Existe um padrão de **skill-fundação lida antes de todas as outras**, confirmado por leitura em `AC-10-REP-004` (`product-marketing`) e `AC-10-REP-005` (`social-media-context-sms`), e apontado como delta de `AC-10-REP-006` (peça-fonte única `about-me.md` + `voice.md` — este último só como alegação do catálogo, não confirmada por leitura de `skills/`). O mesmo padrão de perfil escrito uma vez aparece como recomendação visual em `AC-10-PRT-005` e, fora da área, em `AC-07-REP-004` (registrado na ficha de `AC-10-PRT-005`).
- Existe um caso de **falseabilidade embutida na saída do agente** — cada recomendação carrega a checagem "como saberíamos que isto falhou?" — em `AC-10-REP-002`, descrito na ficha como o padrão mais raro do acervo.
- Existe um caso de **portão de revisão profissional escrito na própria fonte** em `AC-10-REP-003` (os agentes "redigem material para revisão por profissional qualificado" e não executam transação nem vinculam risco) — fato observado no README. Em `AC-10-REP-001` o mesmo portão é alegação do catálogo **não observada** no trecho lido.

Sobre **quais verticais**, a evidência é fraca por natureza: inventários de casos de uso (`AC-10-PRT-006` com 63, `AC-10-VID-012` com cem, `AC-10-VID-004` com 33 skills em sete departamentos) são listagens sem critério de priorização, e a ficha de `AC-10-PRT-006` registra que a contagem "não informa impacto, frequência, dados exigidos nem risco". A única vertical instrumentada com dado de mercado é construção civil, via `AC-10-PLA-001` — um dossiê cujos totais internos não reconciliam entre si (ver §4) e cujo risco é jurídico, não técnico. A única vertical fora do eixo de software é construção civil, com sete vídeos (`AC-10-VID-014` a `AC-10-VID-020`).

Sobre **desenho de fluxo de produção de conteúdo**, três slides da série `workkflow conteudo` foram identificados pelo catálogo e confirmados pela inspeção como arquitetura, não copy: ciclo fechado com realimentação (`AC-10-PRT-009`), fan-out de uma entrada canônica para N gerações (`AC-10-PRT-011`) e camada de adaptadores por plataforma (`AC-10-PRT-013`) — os três com `E14 = 3`. O mesmo padrão de fan-out reaparece como artefato em `AC-10-REP-004` e `AC-10-REP-005` (registrado em `AC-10-PRT-011`).

Sobre **painéis de gestão**, há uma família de itens visuais: fluxo dados → insights → visualização → decisão com cinco blocos nomeados (`AC-10-VID-005`), seis painéis com indicadores por domínio (`AC-10-VID-007`), dez indicadores por papel de direção (`AC-10-VID-013`) — todos NF = 1, sem nenhuma medida de validade.

Desconhecido: nenhum item da área demonstra resultado medido de negócio — toda alegação numérica de ganho é não verificada (`AC-10-VID-003`, `AC-10-VID-015`, `AC-10-VID-022`, entre outros) ou não verificável (`AC-10-PRT-016`, `AC-10-VID-019`).

## 2. Fontes mais fortes e por quê

Critério declarado: LV, NF, volume de ND e vetos — nunca popularidade.

- **`AC-10-REP-002` (claude-seo)** — a fonte mais forte da área: LV4, **NF = 4 com 7/7 eixos determinados (0 ND)**, `E06 = 4` (SECURITY.md, PRIVACY.md e release de segurança datado que documenta falhas próprias com caso e correção), `E13 = 4` (suíte de testes nomeada por risco), `E05 = 4` (atividade datada seis semanas antes da avaliação). Nenhuma porta de veto disparou. O que o separa de CANDIDATO FORTE é um único eixo: `E15 = 2` (contagens do README conferíveis e não conferidas).
- **`AC-10-REP-004` (marketingskills)** — LV4, **NF = 4 com 0 ND**, versionamento por skill com data em `VERSIONS.md` (`E03 = 4`, `E05 = 4`) e dois validadores executáveis na raiz. Para em EXIGE PESQUISA por um único eixo, `E06 = 2`: 419 arquivos de instrução sem SECURITY.md, sem escopo de permissão e sem varredura registrada. É o caso mais nítido do acervo de eixo único fechando classificação (registro 9 do fechamento da área).
- **`AC-10-REP-003` (financial-services)** — LV4, NF = 3 com 2 ND, e o único item com controle de segurança **no texto lido** (`E06 = 3` sustentado pelo bloco de destaque do README, não por atribuição de catálogo). Restrições: `E03 = 2` (sem versionamento) e `E13 = ND`.
- **`AC-10-REP-001` (claude-for-legal)** — LV4, NF = 3 com 2 ND, o maior README do acervo (53 KB) e onze domínios jurídicos empacotados; fica atrás dos três acima por `E06 = 2` e pela ausência de teste localizado.

Os demais 42 itens são LV3-V ou LV3: prints e vídeos não permitem determinar autoria, licença nem superfície de segurança (V2 e V4 disparam em todos os não-REPO — contagem do fechamento da área: V2 = 40, V4 = 40), e a planilha `AC-10-PLA-001` é LV3 por decisão declarada da Fase 2 (divergência de escala, ver §4). Nenhum deles sustenta afirmação forte.

## 3. Padrões recorrentes

- **Empacotamento "uma fonte, dois destinos"** — `AC-10-REP-001`, `AC-10-REP-003`.
- **Skill-fundação / perfil escrito uma vez, lido por todas as skills** — `AC-10-REP-004`, `AC-10-REP-005`, delta de `AC-10-REP-006`, recomendado em `AC-10-PRT-005`, e apontado nas fichas como recorrente também em `AC-07-REP-004` (fora da área).
- **Entrada canônica disparando N saídas (fan-out) e adaptadores por plataforma** — `AC-10-PRT-011`, `AC-10-PRT-013`, com correspondente em artefato em `AC-10-REP-004`/`AC-10-REP-005` e no delta editorial de `AC-10-REP-006` (newsletter como origem canônica — fato observado no README).
- **Laço fechado com realimentação (análise realimentando pesquisa)** — `AC-10-PRT-009`.
- **Portão humano antes do irreversível** — observado na fonte em `AC-10-REP-003`; apenas alegado pelo catálogo em `AC-10-REP-001`; exigido como ressalva pelo catálogo e por `103` em `AC-10-PRT-001`, `AC-10-VID-016`, `AC-10-VID-017`.
- **Inventário de casos de uso sem critério de priorização** — `AC-10-PRT-002`, `AC-10-PRT-003`, `AC-10-PRT-004`, `AC-10-PRT-006`, `AC-10-VID-012`; sobreposições registradas entre `AC-10-PRT-006` e `AC-10-VID-012`, e entre `AC-10-VID-004` e a área 05.
- **Painéis e indicadores por papel** — `AC-10-VID-005`, `AC-10-VID-007`, `AC-10-VID-009`, `AC-10-VID-011`, `AC-10-VID-013`; sobreposições registradas (`AC-10-VID-009` sobrepõe `AC-10-VID-007`; `AC-10-VID-013` sobrepõe `AC-10-VID-007` e `AC-10-VID-011`).
- **Alegação numérica sem método** — padrão dominante dos prints e vídeos: `AC-10-PRT-004` (20/80), `AC-10-PRT-015` (80%/10+ horas), `AC-10-VID-003` (razão de retorno sem atribuição), `AC-10-VID-022` (meta e prazo no nome do arquivo), delta de `AC-10-REP-006` (prova social de audiência, `E15 = 1`, regra P-3).
- **Catálogo que estreita, arredonda ou completa** — dez descrições NC = 2 numa só área (fechamento da área, registro 2): `AC-10-PLA-001`, `AC-10-PRT-008`, `AC-10-PRT-016`, `AC-10-VID-008`, `AC-10-VID-009`, `AC-10-VID-010`, `AC-10-VID-013`, `AC-10-VID-016`, `AC-10-VID-017`, `AC-10-VID-020`.

## 4. Conflitos e divergências

- **NC = 0 em `AC-10-VID-002`**: o catálogo descreve "agente/chatbot de vendas"; a inspeção de quadros mostra **conversão documental** (biblioteca que converte PDF, DOCX, PPTX e HTML para formatos estruturados, com teste de arquivo real). Esta síntese usa conversão documental; a descrição do catálogo está descartada. Hash confere — a divergência é de catálogo, não de fonte.
- **NC = 2 com omissão que muda o sentido em `AC-10-PRT-016`**: o gráfico tem **17 linhas**; o catálogo transcreveu **9**, e as 9 são as de maior diferença — recorte que reforça a conclusão que o próprio catálogo extrai. `109` nomeou as oito omitidas. A síntese usa só a parte confirmada (os nove valores conferem como transcrição) e nomeia a omissão; como o item é V7, nenhum número dele entra aqui como fato (ver §6 e §8).
- **Divergência de escala em `AC-10-PLA-001`** (única do acervo): a trilha Codex (`111`) atribui LV4 por inspeção direta das dez abas; a Fase 2 adotou **LV3** (DEF-07, P-1). Esta síntese trata a planilha como LV3 e não credita leitura direta a esta frente. Não é divergência de conteúdo.
- **Totais não reconciliados dentro de `AC-10-PLA-001`**: existem duas inconsistências internas de contagem (rotas; integrações presentes/ausentes), medidas por `111` e não reconciliadas pela própria planilha. Por decisão de higiene desta fase, **nenhum dos totais é citado como número** — registra-se apenas a existência da inconsistência. Adicionalmente, a fonte usa "vulnerabilidades" para designar **brecha comercial**, não falha de segurança.
- **Série incompleta**: o carrossel `AC-10-PRT-008` a `AC-10-PRT-015` exibe contador de 1/9 a 8/9; **o slide 9 não está no acervo**. O catálogo chama a série de "carrossel de 8 slides" — há oito arquivos, mas nove slides; a lacuna é do acervo, não do catálogo.
- **Divergência de qualificação em `AC-10-VID-017`**: o catálogo diz "prancha arquitetônica executiva"; `103` diz o contrário — a saída **não é** documentação executiva sem verificação profissional. A transformação exibida confere; o adjetivo, não.
- **Contagens não confirmadas**: o catálogo declara onze casos em `AC-10-VID-010` e a inspeção observou oito (PARCIAL, não DIVERGENTE — pode ser amostragem de quadros); "kit financeiro" do catálogo não observado em `AC-10-VID-013`; "logística" do catálogo não observada em `AC-10-VID-009`; busca restrita a "lojas de construção" pelo catálogo não confirmada em `AC-10-VID-020`; descrição do catálogo mais estreita que o observado em `AC-10-VID-016`; organizador do conteúdo divergente em `AC-10-VID-008` (só "Chrome MCP" legível; a ficha não infere nomes pelos ícones).
- **Instrução do catálogo não obedecida**: `AC-10-VID-014` foi sinalizado como "candidato a descarte"; `05` §10 manda não descartar, e o item recebeu ficha. O próprio catálogo se retratou na remessa posterior (registro na ficha).

## 5. Candidatos fortes, pilotos e referências

Vocabulário provisório; **nenhuma classe equivale a adoção**. Registro por ID, sem ordenação de prioridade.

- **CANDIDATO-FORTE:** nenhum — contagem zero na área (fechamento das fichas).
- **PILOTO:** `AC-10-REP-002` (LV4, NF = 4, 0 ND, `E06 = 4`; restrições: `E09 = 3`, `E11 = 3`, três contagens do README não conferidas) · `AC-10-REP-003` (LV4, `E06 = 3` com controle no texto; restrições: `E03 = 2`, `E13 = ND`, `E11 = 2`, delegação a subagentes declarada prévia de pesquisa pelo próprio autor).
- **PESQUISAR:** `AC-10-REP-001` (superfície de segurança e teste — resolvível na própria fonte, cabe no teto) · `AC-10-REP-004` (eixo único `E06 = 2` — varredura de `skills/` e `tools/` estoura o teto, depende de autorização) · `AC-10-REP-005` (`E06` + `E05` — `VERSIONS.md` resolve `E05` na própria fonte; varredura estoura o teto) · `AC-10-PRT-016` (estudo de origem + transcrição das 17 linhas — pesquisa externa) · `AC-10-VID-019` (existência e desempenho do alegado — pesquisa externa; a própria ficha registra "Fora do acervo e fora desta fase", com verificação escrita e executável).
- **REFERENCIA:** os 39 restantes — `AC-10-REP-006` (ficha de delta), `AC-10-PLA-001`, `AC-10-PRT-001` a `AC-10-PRT-015`, `AC-10-VID-001` a `AC-10-VID-018` e `AC-10-VID-020` a `AC-10-VID-023`. Inclui `AC-10-VID-023`, cuja ficha registra explicitamente: classificar como REFERÊNCIA **não é endosso** — `E01 = 1` fecha qualquer candidatura e EXIGE PESQUISA não se aplica por falta de relevância aparente.
- **REJEITAR / DUPLICATA:** nenhum na área. `AC-10-REP-006` **não** é duplicata: sobreposição de 81,5 % dos arquivos e 17/17 skills não é identidade binária; `05` §10 manda ficha de delta, e a porta DUPLICADO não foi aplicada.

## 6. O que não adotar

Nada nesta seção é adoção negada oficialmente — é o que a evidência, como está, **não sustenta extrair**:

- **Nenhum número de `AC-10-PRT-016`** (V7, `E15 = 0`): o item não tem conteúdo avaliável além do próprio texto — sem estudo nomeado, amostra, método ou definição de tarefa. Também não se adota a inferência do catálogo sobre "os três maiores deltas", extraída de um recorte de 9 das 17 linhas (ver §4). O próprio catálogo desqualifica a fonte ("trate como indicativo, não como dado") e ainda assim extrai conclusão dela.
- **Nenhuma alegação de `AC-10-VID-019`** (V7, `E15 = 0`): validação contra código construtivo, fábrica robótica e faixa de custo são alegações sobre empresa de terceiro, não verificáveis com o material disponível; `103` é explícito de que todas exigem fonte primária e validação de engenharia. Sem as alegações, não sobra conteúdo.
- **A descrição de catálogo de `AC-10-VID-002`** (NC = 0): não há chatbot de vendas; há conversão documental.
- **Os totais de `AC-10-PLA-001`**: não reconciliam internamente (ver §4); também não se adota "IA embarcada ausente" — `111` registra que ausência no bundle não prova ausência no produto. E "vulnerabilidades", ali, é brecha comercial: ler como falha de segurança seria erro induzido pelo termo.
- **A fala de qualquer vídeo**: nenhum item tem transcrição revisada por humano. Oito têm fala ALTA AUTOMÁTICA e um (`AC-10-VID-023`) MÉDIA AUTOMÁTICA — insuficiente para citação. Em `AC-10-VID-021` e `AC-10-VID-022` o conteúdo exato depende da fala ("a lista exata depende da fala", `103`): a fala permanece **desconhecida**, e só os quadros foram usados. `AC-10-VID-020` demonstra o porquê: STT detectou khmer com confiança alta num vídeo de contexto lusófono — alucinação documentada; as 27 palavras não são conteúdo.
- **Ranking automático de pessoas a partir de `AC-10-PRT-001`**: o print propõe decisão de emprego sobre dado pessoal; o risco é **declarado** (por `103` e pelo próprio catálogo), não confirmado por inspeção — e nenhum mecanismo de revisão está no material.
- **A prova social do delta de `AC-10-REP-006`** (números de audiência no README): regra P-3 — audiência não é qualidade do artefato; sustenta `E15 = 1`.
- **Instalação pelo comando exibido em `AC-10-VID-006`** (`npx skills add` na tela): o que ele instala não foi inspecionado; `103` registra "não instalar" — risco declarado, não confirmado.
- **As sete linhas de `AC-10-PRT-002` como recomendação de ferramenta**: a escolha de marca é apresentada como parte da solução, e o próprio catálogo registra que é substituível.

## 7. Riscos e dependências

Todos os riscos abaixo são **declarados** (E06 = 1 ou E06 = 2), nunca confirmados por inspeção — separação literal de `04_RUBRICA` §9, mantida nesta fase.

- **Sete itens com E06 = 1** — o maior número do acervo numa área, por naturezas distintas (contagem do fechamento): dado pessoal e decisão de emprego (`AC-10-PRT-001`); execução de pacote remoto exibida (`AC-10-VID-006`); propriedade intelectual e dado financeiro/bancário (`AC-10-VID-010`); documento técnico de obra sem profissional responsável (`AC-10-VID-016`, `AC-10-VID-017`); prospecção não solicitada (`AC-10-VID-020`); engenharia reversa de material de terceiro com dado pessoal (`AC-10-PLA-001` — risco **jurídico**, declarado por `111`, com exigência registrada de revisão jurídica e de termos antes de qualquer uso).
- **Superfície ampla sem controle documentado (E06 = 2)**: `AC-10-REP-001` (conectores de dados jurídicos sem SECURITY.md nem escopo de permissão), `AC-10-REP-004` (419 arquivos de instrução + dois scripts de shell, sem varredura registrada — e o acervo já provou em `AC-05-REP-003` que conteúdo de instrução pode carregar injeção), `AC-10-REP-005` (instrução + script + integração externa nomeada como primária, sem política de dados lida).
- **Dependência de fornecedor declarada**: `AC-10-REP-001` e `AC-10-REP-003` (`E11 = 2` — os dois destinos de instalação são produtos do mesmo fabricante); `AC-10-REP-005` (`E11 = 3` — ferramenta externa como integração primária); `AC-10-REP-002` (`E11 = 3` — harness específico + provedores externos de dados; `E09 = 3` — até 15 agentes simultâneos e serviços pagos). Contraponto: `AC-10-REP-004` declara funcionar com quatro harnesses e qualquer agente que siga a especificação aberta (`E11 = 4`, como declaração não verificada), e o delta de `AC-10-REP-006` remove a integração externa do original (`E11 = 4`).
- **Licença e autoria indeterminadas em 40 itens** (V4 em todos os não-REPO): prints e vídeos não têm titular nem termos determináveis por inspeção; `AC-10-PLA-001` não tem licença, autoria nem termos acompanhando o arquivo (`E07 = ND`).
- **Maturidade e manutenção desconhecidas**: `E03` e `E05` são ND em todos os prints e vídeos; nos repositórios, `E05 = ND` em `AC-10-REP-001`, `AC-10-REP-003`, `AC-10-REP-005` e `AC-10-REP-006` (este último resolvível abrindo `VERSIONS.md`).

## 8. Lacunas

- **Estudo de origem de `AC-10-PRT-016`** — quem mediu, amostra, método, definição de tarefa; mais a **transcrição completa das 17 linhas** do gráfico (a tabela em uso no acervo é um recorte de 9). A segunda parte é operação de minutos e corrige um erro que já circula dentro do acervo; a primeira exige pesquisa externa.
- **Fonte primária de `AC-10-VID-019`** — existência e desempenho do configurador, da validação normativa e da fábrica alegados; exige pesquisa externa e validação de engenharia.
- **Varredura de segurança dos pacotes de skills** — `AC-10-REP-004` e `AC-10-REP-005`: procurar instrução hostil, execução de shell e chamada de rede em `skills/` e `tools/`; estoura o teto de leitura vigente, depende de autorização do proprietário.
- **Superfície de segurança e testes de `AC-10-REP-001`** — ler `CONNECTORS.md` e um README de domínio, listar os onze diretórios procurando teste; resolvível na própria fonte, cabe no teto.
- **`E05` de `AC-10-REP-005` (e do delta `AC-10-REP-006`)** — resolvível abrindo `VERSIONS.md`, dentro da própria fonte.
- **Slide 9 da série `workkflow conteudo`** — ausente do acervo (`AC-10-PRT-008` a `AC-10-PRT-015` cobrem 1/9 a 8/9); lacuna do acervo, não suprida por inferência.
- **Reconciliação interna e titularidade de `AC-10-PLA-001`** — os dois totais inconsistentes (§4), a autoria e os termos do dossiê, e os termos de uso do material analisado; também a substituição de confiabilidade autoatribuída por vínculo alegação → fonte → data → trecho.
- **Fala dos vídeos** — resíduo de transcrição declarado em `AC-10-VID-021` e `AC-10-VID-022` ("a lista exata depende da fala"); só revisão humana de áudio fecha. Nenhum dos 23 vídeos tem fala citável.
- **Titularidade dos 40 itens não-REPO** — E07 = ND em todos; sem autoria e termos, permanecem insumo de consulta.

## 9. Decisão provisória

Mapeamento do RF da ficha para o vocabulário fechado desta fase. **Nenhuma classificação equivale a adoção oficial.** Registro por ID, sem ordenação.

| ID | Classe | Motivo (uma linha, citando a ficha) |
|---|---|---|
| `AC-10-REP-001` | PESQUISAR | `E06 = 2` (conectores jurídicos sem controle na raiz) e teste não localizado; verificação cabe no teto |
| `AC-10-REP-002` | PILOTO | LV4, NF = 4, 0 ND, `E06 = 4`; só `E15 = 2` o separa de CANDIDATO FORTE |
| `AC-10-REP-003` | PILOTO | LV4, `E06 = 3` com portão de revisão no texto lido; restrições `E03 = 2`, `E13 = ND`, `E11 = 2` |
| `AC-10-REP-004` | PESQUISAR | NF = 4, RP = 4, 0 ND, parado pelo eixo único `E06 = 2` (419 arquivos de instrução sem varredura) |
| `AC-10-REP-005` | PESQUISAR | `E06 = 2` (instrução + script + integração externa) e `E05 = ND` resolvível na fonte (`VERSIONS.md`) |
| `AC-10-REP-006` | REFERENCIA | Ficha de delta de `AC-10-REP-005` (81,5 %, 17/17); o delta é padrão editorial; melhores notas vêm de ausências |
| `AC-10-PLA-001` | REFERENCIA | Planilha LV3 (divergência de escala declarada); V2 (`E06 = 1`) e V4 (`E07 = ND`) fecham candidatura |
| `AC-10-PRT-001` | REFERENCIA | `E06 = 1` declarado (dado pessoal/decisão de emprego); V2/V4; NF = 1 |
| `AC-10-PRT-002` | REFERENCIA | Só listagem tarefa→ferramenta; NF = 1, E14 = 1; V2/V4 |
| `AC-10-PRT-003` | REFERENCIA | Promete "prompt pronto" que não está no print; NF = 1; V2/V4 |
| `AC-10-PRT-004` | REFERENCIA | Moldura 20/80 sem medição; NF = 1; sobrepõe `AC-10-PRT-002`/`003`; V2/V4 |
| `AC-10-PRT-005` | REFERENCIA | Print mais acionável do lote (estrutura de pastas/perfil); NF = 1; V2/V4 |
| `AC-10-PRT-006` | REFERENCIA | Inventário de 63 usos sem critério de priorização; NF = 1; V2/V4 |
| `AC-10-PRT-007` | REFERENCIA | Pipeline de dez papéis de pesquisa; prompts fora do print; NF = 1; V2/V4 |
| `AC-10-PRT-008` | REFERENCIA | Capa, só promessa; NC = 2 (contador 1/9, série de nove slides); V2/V4 |
| `AC-10-PRT-009` | REFERENCIA | Ciclo fechado de oito etapas com realimentação (E14 = 3); NF = 1; V2/V4 |
| `AC-10-PRT-010` | REFERENCIA | Sete fontes de pesquisa nomeadas; NF = 1; V2/V4 |
| `AC-10-PRT-011` | REFERENCIA | Padrão fan-out, uma entrada → N saídas (E14 = 3); NF = 1; V2/V4 |
| `AC-10-PRT-012` | REFERENCIA | Cinco fórmulas de gancho com exemplos; E14 = 1; NF = 1; V2/V4 |
| `AC-10-PRT-013` | REFERENCIA | Camada de adaptadores por plataforma (E14 = 3); NF = 1; V2/V4 |
| `AC-10-PRT-014` | REFERENCIA | Contraste retórico/copy de venda; RP = 2; sobrepõe `AC-10-PRT-009`; V2/V4 |
| `AC-10-PRT-015` | REFERENCIA | Seis classes de automação, números sem fonte; fecha a série (slide 9 ausente); V2/V4 |
| `AC-10-PRT-016` | PESQUISAR | V7: `E15 = 0`, o item é a alegação; sem estudo nomeado; recorte de 9 das 17 linhas |
| `AC-10-VID-001` | REFERENCIA | Contraste de ícones sem fala confiável; RP = 1; V2/V4 |
| `AC-10-VID-002` | REFERENCIA | NC = 0: inspeção mostra conversão documental; repositório exibido fora do acervo; V2/V4 |
| `AC-10-VID-003` | REFERENCIA | Razão de retorno sem período nem atribuição causal; RP = 1; V2/V4 |
| `AC-10-VID-004` | REFERENCIA | Taxonomia de 33 skills por departamento; sobrepõe `AC-10-REP-004` e a área 05; V2/V4 |
| `AC-10-VID-005` | REFERENCIA | Fluxo dados→decisão com cinco blocos nomeados (E14 = 3); NF = 1; V2/V4 |
| `AC-10-VID-006` | REFERENCIA | `E06 = 1` declarado (`npx skills add` na tela, não inspecionado); NF = 1; V2/V4 |
| `AC-10-VID-007` | REFERENCIA | Seis painéis com indicadores por domínio (E14 = 3); NF = 1; V2/V4 |
| `AC-10-VID-008` | REFERENCIA | Ecossistema de conectores, só "Chrome MCP" legível; NC = 2; RP = 1; V2/V4 |
| `AC-10-VID-009` | REFERENCIA | Painéis, um não capturado; NC = 2 ("logística" não observada); sobrepõe `AC-10-VID-007`; V2/V4 |
| `AC-10-VID-010` | REFERENCIA | `E06 = 1` declarado (clonagem de app, dado bancário); contagem 8×11 não confirmada (NC = 2); V2/V4 |
| `AC-10-VID-011` | REFERENCIA | Matriz de seis papéis de direção; advertência `103`: papel ≠ agente autônomo; NF = 1; V2/V4 |
| `AC-10-VID-012` | REFERENCIA | Cem funções em quatro blocos, sem comprovação; sobrepõe `AC-10-PRT-006`; NF = 1; V2/V4 |
| `AC-10-VID-013` | REFERENCIA | Dez indicadores por papel ×3; "kit financeiro" não observado (NC = 2); NF = 1; V2/V4 |
| `AC-10-VID-014` | REFERENCIA | Planta → casa navegável; "candidato a descarte" registrado e não obedecido (`05` §10); NF = 1; V2/V4 |
| `AC-10-VID-015` | REFERENCIA | Sete efeitos de apresentação; render ≠ viabilidade (`103`); áudio não é fala; NF = 1; V2/V4 |
| `AC-10-VID-016` | REFERENCIA | Cinco usos de obra encadeados; `E06 = 1` declarado (documento controlado, responsável); NF = 1; V2/V4 |
| `AC-10-VID-017` | REFERENCIA | `E06 = 1` declarado (IA pode inventar dimensões); catálogo diz "executiva", `103` nega; NF = 1; V2/V4 |
| `AC-10-VID-018` | REFERENCIA | Levantamento sobre planta com exportação estruturada (E14 = 3); NF = 1; V2/V4 |
| `AC-10-VID-019` | PESQUISAR | V7: `E15 = 0`; cadeia projeto→fábrica toda alegada sobre empresa de terceiro, sem fonte primária |
| `AC-10-VID-020` | REFERENCIA | `E06 = 1` declarado (prospecção não solicitada); alucinação de STT (khmer) documentada; RP = 1; V2/V4 |
| `AC-10-VID-021` | REFERENCIA | Checklist de Instagram; "a lista exata depende da fala" — fala desconhecida; NF = 1; V2/V4 |
| `AC-10-VID-022` | REFERENCIA | Planejamento de conteúdo; meta 100k/300d sem evidência; "estratégia completa depende do áudio"; RP = 1; V2/V4 |
| `AC-10-VID-023` | REFERENCIA | Oferta promocional; único MÉDIA AUTOMÁTICA do acervo; `E01 = 1`; REFERÊNCIA não é endosso |

## 10. Experimento que poderia validá-la

**Proposta, não plano aprovado** — nada abaixo foi executado nem autorizado nesta fase.

1. **Verificação interna de baixo custo (cabe no teto vigente):** executar a leitura nomeada em `AC-10-REP-001` (`CONNECTORS.md` + um README de domínio + listagem dos onze diretórios procurando teste). Fecharia a única pendência da área que a pré-correção classifica como resolvível na própria fonte e dentro do teto, e testaria se o item sai de PESQUISAR para PILOTO.
2. **Correção do recorte de `AC-10-PRT-016`:** reler a imagem transcrevendo as 17 linhas (operação declarada pela ficha como "de minutos") e, em paralelo, pesquisa externa pela publicação de origem do gráfico. Validaria ou encerraria o único print da área fora de REFERÊNCIA.
3. **Conferência das contagens de `AC-10-REP-002`:** contar `skills/` e `agents/` na própria fonte para verificar "25 sub-skills", "18 specialist agents" e "até 15 simultâneos" — é o único eixo (`E15 = 2`) que separa o item de CANDIDATO-FORTE.
4. **Comparação de padrão (depende de autorização, estoura o teto):** a varredura de `skills/` e `tools/` de `AC-10-REP-004` e `AC-10-REP-005` procurando instrução hostil e chamada de rede — exatamente o uso que `AC-09-REP-001` propõe, segundo a ficha de `AC-10-REP-004`. Validaria se o eixo único `E06 = 2` é risco real ou ausência de registro.

## 11. Confiança da síntese

**Média**, com distribuição interna desigual — alta para os padrões sustentados por repositório, baixa para tudo o que depende de print ou vídeo:

- **Cobertura de LV:** apenas 6 dos 46 itens são LV4 (os REPO); 39 são LV3-V e 1 é LV3 por decisão de escala (`AC-10-PLA-001`, com a trilha Codex divergindo para LV4). 85 % da área repousa em inspeção de quadros/relatório de terceiro, sem leitura direta de artefato executável.
- **Volume de ND:** 196 de 690 células de eixo (28,4 %) — concentrado nos prints e vídeos, onde E03, E05, E07 e E13 são estruturalmente indetermináveis. Nenhum item atingiu o gatilho de V6, e todos os 196 ND nomeiam o que os resolveria.
- **Itens V7:** 2 (`AC-10-PRT-016`, `AC-10-VID-019`) — ambos tratados sem nenhum número como fato.
- **Itens NC = 0:** 1 (`AC-10-VID-002`) — tratado pela inspeção, não pelo catálogo.
- **EXIGE PESQUISA:** 5 itens, incluindo 3 dos 6 repositórios — ou seja, metade da evidência forte da área ainda tem lacuna aberta.
- **A favor da confiança:** 0 divergências de hash (V8 = 0 em 46 reconferências); o fechamento da área traz contagens por ferramenta que esta síntese reproduz sem alterar; as duas fichas com Bloco A integralmente determinado (`AC-10-REP-002`, `AC-10-REP-004`) dão âncora sólida aos padrões de empacotamento.

## 12. Cobertura

Todos os 46 IDs da área, com a decisão provisória de cada um (detalhe do motivo em §9). Contagem: **PILOTO 2 · PESQUISAR 5 · REFERENCIA 39 · CANDIDATO-FORTE 0 · ADAPTAR-PADRAO 0 · REJEITAR 0 · DUPLICATA 0**.

| ID | Decisão | ID | Decisão |
|---|---|---|---|
| `AC-10-REP-001` | PESQUISAR | `AC-10-PRT-012` | REFERENCIA |
| `AC-10-REP-002` | PILOTO | `AC-10-PRT-013` | REFERENCIA |
| `AC-10-REP-003` | PILOTO | `AC-10-PRT-014` | REFERENCIA |
| `AC-10-REP-004` | PESQUISAR | `AC-10-PRT-015` | REFERENCIA |
| `AC-10-REP-005` | PESQUISAR | `AC-10-PRT-016` | PESQUISAR |
| `AC-10-REP-006` | REFERENCIA (ficha de delta → `AC-10-REP-005`) | `AC-10-VID-001` | REFERENCIA |
| `AC-10-PLA-001` | REFERENCIA | `AC-10-VID-002` | REFERENCIA |
| `AC-10-PRT-001` | REFERENCIA | `AC-10-VID-003` | REFERENCIA |
| `AC-10-PRT-002` | REFERENCIA | `AC-10-VID-004` | REFERENCIA |
| `AC-10-PRT-003` | REFERENCIA | `AC-10-VID-005` | REFERENCIA |
| `AC-10-PRT-004` | REFERENCIA | `AC-10-VID-006` | REFERENCIA |
| `AC-10-PRT-005` | REFERENCIA | `AC-10-VID-007` | REFERENCIA |
| `AC-10-PRT-006` | REFERENCIA | `AC-10-VID-008` | REFERENCIA |
| `AC-10-PRT-007` | REFERENCIA | `AC-10-VID-009` | REFERENCIA |
| `AC-10-PRT-008` | REFERENCIA | `AC-10-VID-010` | REFERENCIA |
| `AC-10-PRT-009` | REFERENCIA | `AC-10-VID-011` | REFERENCIA |
| `AC-10-PRT-010` | REFERENCIA | `AC-10-VID-012` | REFERENCIA |
| `AC-10-PRT-011` | REFERENCIA | `AC-10-VID-013` | REFERENCIA |
| `AC-10-VID-014` | REFERENCIA | `AC-10-VID-019` | PESQUISAR |
| `AC-10-VID-015` | REFERENCIA | `AC-10-VID-020` | REFERENCIA |
| `AC-10-VID-016` | REFERENCIA | `AC-10-VID-021` | REFERENCIA |
| `AC-10-VID-017` | REFERENCIA | `AC-10-VID-022` | REFERENCIA |
| `AC-10-VID-018` | REFERENCIA | `AC-10-VID-023` | REFERENCIA |

> Este arquivo é evidência externa, provisória e não normativa. Não autoriza adoção de nada.
