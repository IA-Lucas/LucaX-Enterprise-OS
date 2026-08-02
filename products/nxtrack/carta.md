---
id: PRO-nxtrack
titulo: NxTrack
tipo: carta
versao: 1.0.0
status: ativo
camada_memoria: produto
autor: DEP-PRD
proprietario: DEP-PRD
aprovador: SOBERANO
criado_em: 2026-08-01
atualizado_em: 2026-08-01
revisao_prevista: 2027-02-01
decisoes_relacionadas: [ADR-0030]
substitui: []
substituido_por: null
capabilities: [CAP-produto, CAP-inteligencia-artificial, CAP-dados, CAP-engenharia, CAP-operacoes]
resumo: Camada de inteligencia sobre o Rekordbox que prepara sets, cuida da biblioteca do DJ e explica cada recomendacao, sem alterar o banco interno do software.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: ratificada
---

# NxTrack (PRO-nxtrack)

> **ARTEFATO DO ACERVO — admitido pelo NONO ATO SOBERANO, em 2026-08-01.**
> Criada em `products/nxtrack/carta.md` pelo item **III** de
> [MSG-2026-0009](../../memory/operacional/MSG-2026-0009-ato-soberano-admissao-do-nxtrack.md),
> a partir do candidato de `H-A` `4d4c12e0...75c5`, que vivia **fora** do acervo em
> `_missao-1-13-4-4-2026-08-01/candidatos/`. O `id: PRO-nxtrack` **deixa de ser forma do
> template e passa a ser identidade alocada**, e `products/` nasce como raiz do acervo na
> mesma mudanca. **O que a admissao NAO faz continua valendo integralmente:** `G0` e
> `IDENTIDADE` e **`0` bytes** do repositorio do candidato entraram — `LA-1` a `LA-7` de
> `PS-2026-016 §6.3`.

> **O que esta Carta descreve e o que ela NAO importa.** Todo fato aqui foi **medido por
> consulta** ao repositorio do candidato (`FR-04`: *"consultar nao e importar"*), a partir de
> **17 fontes congeladas por hash** e listadas no pacote soberano. **Nenhum byte do candidato
> e transcrito como norma.** O codigo permanece no repositorio operacional; o acervo canonico
> recebe **identidade, governanca, decisoes e referencias** — e nada mais. Isto e `G0 =
> IDENTIDADE`.

## Proposito

Dar existencia formal, neste acervo, ao **NxTrack**: uma camada de inteligencia externa ao
Rekordbox que transforma a biblioteca de um DJ numa rede de relacoes entre faixas, para
preparar sets, recomendar o que tocar antes e depois **com a razao declarada**, e aprender com
o uso real — preservando fluxo nao destrutivo. O produto existe e opera; o que falta e a
**identidade governada**.

## Escopo

| Item | Definicao |
|---|---|
| **Faz parte do produto** | Importacao da colecao Rekordbox por XML · biblioteca permanente por usuario · recomendacao antes/depois com explicacao · geracao de set em tres versoes *(segura, equilibrada, criativa)* por beam search · edicao, trava, substituicao e regeneracao de trecho · playlists persistidas · exportacao `.m3u` · saude da biblioteca e divergencia de metadado · energia manual · organizacao fisica **por copia** com previa e manifesto · contas, sessoes revogaveis e separacao de bibliotecas · feedback persistido e aprendizado coletivo deliberado |
| **Nao faz parte do produto** | Ver §4 — escopo negativo |
| **Estagio** | **`construcao`** — beta funcional e **validado localmente**; publicacao publica **nao concluida**. Fonte: `README.md` e `ESTADO-nxtrack.md` do candidato |

## Responsaveis

| Papel | Quem |
|---|---|
| Proprietario | DEP-PRD |
| Construcao | DEP-ENG |
| Operacao | DEP-OPS |
| Comunicacao | DEP-GRW |
| Aprovador | SOBERANO |

> **Custodia hoje e custodia depois — a diferenca esta medida, nao suposta.** Hoje o candidato
> **nao tem custodia neste acervo**: vive em `E:\LucasIA\Projetos\lucaX\My_WorkSpace\Meus_projetos\nxtrack`,
> **subpasta** de um repositorio de terceiro (`lucaX`) com **758** caminhos sem commit e
> **escritor concorrente ativo**. A tabela acima descreve a custodia **que o ato do Soberano
> institui**, nao a que existe. Achado `RD-71`.

## 1. Problema

DJs mantem bibliotecas de milhares de faixas e nao conseguem lembrar o que combina com o que,
achar rapido a proxima faixa, organizar por contexto, construir curva de energia, preparar set
em pouco tempo nem recuperar musica esquecida. **BPM e tonalidade, isolados, nao determinam se
duas musicas funcionam juntas** — e essa e a afirmacao central que o produto ataca.

**Evidencia.** A hipotese esta escrita e **declarada como nao validada** pelo proprio
candidato: *"DJs consideram mais uteis as recomendacoes baseadas na combinacao entre
caracteristicas musicais, contexto pessoal e transicoes observadas em sets reais do que
recomendacoes baseadas somente em BPM, key ou genero"* — `spec-tecnica-v1.md §33`. **Nao ha
entrevista, teste com DJ externo nem medicao de aceitacao registrada.** A ausencia esta
declarada, nao mascarada (`PI-10`, `VD-05`).

## 2. Publico

| Persona | Contexto de uso | Dor principal | Como resolve hoje |
|---|---|---|---|
| **DJ dono da biblioteca** *(unico usuario com uso observado)* | Prepara set em casa, no Rekordbox, antes de tocar | Nao lembra o que combina; preparar set consome horas | Memoria propria, playlists manuais, tentativa e erro no Rekordbox |
| **Segundo usuario / socio** *(existencia indiciada, uso NAO medido)* | Biblioteca separada no mesmo runtime | idem | idem |
| **DJ externo** | — | — | **Nenhum.** `0` usuarios externos: porta ligada ao **loopback** |

> **`PB-1` — limite do publico, declarado.** O unico indicio de segundo usuario e o nome de um
> arquivo de backup (`nxtrack.antes-do-socio.db`) e o desenho multiusuario de
> `prototipo/usuarios.py`. **Os bancos NAO foram abertos** — a missao proibe abrir PII —, e por
> isso **o numero de usuarios reais NAO foi contado e nao e afirmado aqui.** Ausencia de
> medicao, nao medicao de ausencia.

## 3. Proposta de valor

Recomendacao **explicavel**: o produto nao afirma que duas faixas combinam — ele diz **por
que**, com evidencia de transicao observada, BPM, compatibilidade harmonica, curva de energia e
historico do proprio DJ. A alternativa atual do publico e a memoria do DJ, que nao escala com a
biblioteca.

## 4. Escopo negativo

> O que este produto deliberadamente **nao** faz, e por que. Protege contra ampliacao
> silenciosa (`PI-09`). **Todas as linhas sao declaracoes literais do candidato**, nao inferencia.

| Nao faz | Por que |
|---|---|
| **Alterar o banco interno do Rekordbox** | Decisao fechada do candidato: integracao ocorre **por XML/M3U, nunca por alteracao do banco interno** (`ESTADO-nxtrack.md`) |
| **Mover, apagar ou sobrescrever arquivo de audio** | Organizacao fisica **copia**, com previa e manifesto (`README.md`) |
| Controlar o Rekordbox em tempo real | `spec-tecnica-v1.md §25` — MVP e assistente de preparacao, nao sistema de performance |
| Acessar catalogo de streaming sem autorizacao | idem |
| Exportar arquivo protegido | idem |
| Identificar perfeitamente todo edit e bootleg | idem — limite tecnico assumido |
| Gerar transicao de audio pronta | idem |
| **Substituir decisao artistica do DJ** | idem — o motor seleciona, o DJ decide |
| **Burlar login, assinatura ou licenca de fonte externa** | `RELATORIO-SUPER-NXTRACK-2026-07-22.md`: compra e descoberta acontecem **no site da fonte** |
| **Baixar dado por conector automatico sem conferir `robots.txt`** | Regra local do candidato em `prototipo/fontes.py`: *"link de busca manual nao e conector"* |

## 5. Criterio de sucesso

| Metrica | Definicao | Meta | Prazo |
|---|---|---|---|
| **Aceitacao de recomendacao** | % de sessoes em que o usuario aceita ao menos uma recomendacao **e a adiciona a uma playlist** — metrica principal declarada em `spec-tecnica-v1.md §23` | **A definir pelo Soberano** — o candidato declara a metrica e **nao declara meta** | 1o horizonte apos a admissao |
| **Set exportado e tocado** | Set gerado no produto, importado no Rekordbox e **executado em CDJ** | ≥ 1 ensaio registrado | 1o horizonte |
| **Nao destrutividade** | Arquivos de audio originais alterados pelo produto | **`0`, sempre** — bloqueante | permanente |

> **`CS-1` — a Carta NAO inventa meta.** O candidato define **o que medir** e **nao define
> quanto**. Escrever um numero aqui seria publicar como decidido o que nao foi. As metas ficam
> **abertas para o ato do Soberano** (`Q3` do pacote).

## 6. Criterio de encerramento

> Obrigatorio na criacao (`FND-09 E-17`; `TPL-carta-produto`, instrucao 3).

| Condicao | Sinal observavel |
|---|---|
| **A hipotese central e refutada** | Apos ≥ 3 ensaios em CDJ com set gerado, a taxa de aceitacao de recomendacao nao supera a de uma linha de base por BPM+tom |
| **O fluxo do Rekordbox deixa de admitir XML/M3U** | Versao do Rekordbox sem exportacao de colecao em XML nem importacao de playlist |
| **O dono deixa de discotecar** | Ausencia de set preparado por 2 horizontes consecutivos |
| **Custo de operacao supera o valor** | Custo mensal de infraestrutura acima do teto que o Soberano fixar, sem usuario pagante |
| **Substituicao por capacidade nativa do Rekordbox** | O proprio Rekordbox passa a oferecer recomendacao explicavel com grafo de transicoes |

## 7. Hipoteses

| # | Hipotese | Como sera testada | Status |
|---|---|---|---|
| `H1` | Recomendacao que combina caracteristica musical, contexto pessoal e transicao observada e mais util que BPM+tom+genero | Ensaio em CDJ com registro de transicoes, falhas e percepcao | **aberta** |
| `H2` | O DJ aceita preparar set no produto em vez do Rekordbox | % de sets exportados sobre sets iniciados | **aberta** |
| `H3` | O grafo coletivo de transicoes melhora a recomendacao mais que o historico individual | Comparacao de aceitacao com e sem peso de grafo | **aberta** |
| `H4` | SQLite basta para o beta | Contador de `SQLITE_BUSY` e latencia de escrita | **aberta — e HOJE NAO MENSURAVEL**: `monitor_beta.py` mede disponibilidade, nao contencao (`roadmap.md`) |
| `H5` | Energia estimada sem medicao de audio e util | Correcao manual do usuario sobre energia estimada | **aberta** |

## 8. Capabilities consumidas

> Obrigatorio. `FND-09 E-17` declara `capabilities` **atributo minimo** de `PRO`; `FND-04 §6`
> faz do vinculo **pre-condicao universal I**. Toda linha aqui aparece no frontmatter, e
> vice-versa. As cinco estao **vigentes** no [catalogo](../../capabilities/README.md).

| Capability | Estado no catalogo | Para que este produto a consome | Departamento custodiante |
|---|---|---|---|
| **`CAP-produto`** | `nucleo` · `experimental` · **vigente** | Definicao do problema, publico, hipoteses e criterio de encerramento | DEP-PRD |
| **`CAP-inteligencia-artificial`** | `nucleo` · `experimental` · **vigente** | Motor de recomendacao, beam search e assistente que converte intencao em restricao | DEP-ENG |
| **`CAP-dados`** | `habilitadora` · `experimental` · **vigente** | Biblioteca por usuario, grafo de transicoes, persistencia `SQLite` em WAL, migracoes versionadas | DEP-ENG |
| **`CAP-engenharia`** | `habilitadora` · `experimental` · **vigente** | Runtime React + FastAPI de mesma origem, empacotamento e suite de testes | DEP-ENG |
| **`CAP-operacoes`** | `habilitadora` · `experimental` · **vigente** | Deploy fail-fast, monitor, backup/restore com manifesto e integridade | DEP-OPS |

> **`VC-03` DISPARA, e esta declarado.** Cinco vinculos e **mais de tres**:
> *"sinal de componente amplo demais — avaliar especializacao **do componente**, nao criacao de
> Capability"* (`FND-08`, `VC-03`). **Nao se cria Capability nenhuma.** O sinal fica registrado
> como **achado `RD-74`**, com dono DEP-PRD e gatilho na primeira `Spec`. **Reduzir a lista
> para tres seria falsear o vinculo** — as cinco sao exercidas, e `VC-01` proibe elo que nao
> corresponde.

> **`CAP-seguranca`, `CAP-juridico`, `CAP-design` e `CAP-infraestrutura` NAO estao listadas** —
> e a omissao e deliberada: o produto **opera sob** politica dessas competencias, e *operar sob
> uma competencia nao e consumi-la como Capability* — a mesma distincao que fechou `P3`, `P4` e
> `P5` da projecao do catalogo.

## 9. Interfaces

> Interface **nao declarada** e acoplamento que ninguem pode revisar. `Natureza` distingue o
> que foi **observado no repositorio** do que o candidato **alega** sem prova no acervo.

| Direcao | Interface | Contraparte | Natureza |
|---|---|---|---|
| expoe | **HTTP em `127.0.0.1:8501`** — 21 rotas (`/sessao/*`, `/biblioteca/*`, `/set/*`, `/recomendar`, `/playlists*`, `/kpis`, `/diagnostico`) | Navegador **na propria maquina** | **observado** — `compose.beta.yml`, `rotas.py` |
| expoe | **Arquivo `.m3u`** | Rekordbox, por importacao manual | **observado** — `rotas.py`, `/playlist/m3u` |
| expoe | Copia fisica de arquivos com manifesto e previa | Sistema de arquivos do host | **observado** |
| consome | **XML de colecao do Rekordbox** | Rekordbox | **observado** — `importar_xml.py` |
| consome | **MusicBrainz** *(metadado)* | `musicbrainz.org` | **observado** — `enriquecimento.py` |
| consome | **Beatport** *(parser de HTML publico)* | `beatport.com` | **observado** — `enriquecimento.py`; **fragil por natureza**, risco declarado pelo candidato |
| consome | **Spotify Web API** *(token + consulta)* | `accounts.spotify.com`, `api.spotify.com` | **observado** — `enriquecimento.py` |
| consome | **Links de busca deterministicos** — Beatport, Traxsource, Bandcamp, SoundCloud, Beatsource | Lojas | **observado** — `fontes.py`; **zero requisicao, zero raspagem** |
| consome | **Backblaze B2** *(backup externo via Restic)* | `s3.<region>.backblazeb2.com` | **alegado** — `.env.example` prevê; **B2 real NAO validado** |
| consome | **Hetzner** *(host de publicacao)* | Hetzner | **alegado** — destino planejado, **nao provisionado** |
| consome | **Cloudflare Tunnel** | Cloudflare | **alegado e DESATIVADO** — `deploy --edge` falha fechado por CVE HIGH |
| consome | **Bitwarden Secrets Manager** *(segredos)* | Bitwarden | **alegado** — `.env.example` aponta; `0` segredo no repositorio |

## 10. Restricoes

| Restricao | Origem |
|---|---|
| **O codigo NAO entra no acervo canonico** | Norma — `G0 = IDENTIDADE` de `ADR-0027 §5.1`: `0` bytes do externo |
| **Nao ha repositorio proprio**: o produto vive em subarvore de terceiro | Tecnica — medido; achado `RD-71` |
| Integracao com Rekordbox limitada a XML/M3U | Tecnica e decisao do candidato |
| **`SQLite` e a decisao do beta**; sucessor nomeado (`PostgreSQL` + `pgAdmin`) sem sensor de gatilho | Tecnica — `ADR-100` do candidato; `roadmap.md` |
| Publicacao publica depende de credenciais externas hoje inacessiveis | Custo e operacao |
| **Fonte `Anton` sob SIL Open Font License** redistribuida no produto | **Legal** — `OFL-Anton.txt` no repositorio |
| **Direito autoral de catalogo musical**: o produto le metadado e caminho, nao redistribui audio | **Legal** — ver §Limites obrigatorios do pacote |
| Aprendizado de feedback e **coletivo** entre usuarios; bibliotecas permanecem separadas | Decisao do candidato — com consequencia de privacidade, §11 |

## 11. Riscos

| # | Risco | Impacto | Mitigacao |
|---|---|---|---|
| `R1` | **Custodia difusa**: o produto e subpasta de repositorio de terceiro, com 758 caminhos sem commit e escritor concorrente | **Alto** | Admissao por `IDENTIDADE` **nao** move o codigo; a fronteira de custodia e requisito da primeira `Spec`. `RD-71` |
| `R2` | **Aprendizado coletivo entre usuarios** com bibliotecas separadas: feedback de um informa a recomendacao do outro | **Alto** | Declarado deliberado pelo candidato. **Nao ha politica de privacidade, termo de uso nem base legal escrita** — §Limites |
| `R3` | Parser publico do Beatport depende do HTML do site | Medio | Risco declarado pelo proprio candidato; degradacao e de enriquecimento, nao de nucleo |
| `R4` | **`H4` nao e mensuravel**: o gatilho de migracao de banco nao tem sensor | Medio | `roadmap.md` declara a lacuna. Criar o sensor e trabalho de `Spec`, nao de Carta |
| `R5` | **Energia sem medicao real** e explicitamente estimada | Baixo | Declarado no produto; correcao manual do usuario prevalece |
| `R6` | `0` evidencia de comportamento sob trafego publico | Medio | O produto **nao esta publicado**; o risco so se realiza na publicacao |
| `R7` | **Esta Carta estar errada** — descrever um produto que o Soberano nao quis | Medio | `Q1` esta **respondida** por `PT-2026-009 §1` decisao 7, em texto literal. A ressalva *"se seguir sendo o primeiro produto comercial"* mora em **documento distinto** (`PS-2026-013 §7`) e e tratada como `Q2` do pacote |

## 12. Decisoes fundadoras

| ADR | O que decidiu |
|---|---|
| **`ADR-0030`** | Admite o **nXtrack** pelo portao de origem externa com `G0 = IDENTIDADE` e `G3 = RECOGNIZE`, e cria `PRO-nxtrack` — **sujeito a ato do Soberano**, `C2`/`Tipo 1` |
| `ADR-0007` | Instituiu o portao unico de origem externa e a proibicao de importacao direta |
| `ADR-0027` | Acrescentou `G0` e `RECOGNIZE` — **a classe que descreve esta admissao** |
| `ADR-0002` | Vinculo obrigatorio a Capability |
| `ADR-0021` | Framework de `Spec` — o caminho pelo qual o conteudo do produto podera, um dia, ser normatizado |

## 13. Memoria

| Camada | O que este produto alimenta |
|---|---|
| **PRD** | Definicao, personas, as cinco hipoteses `H1`–`H5`, feedback de recomendacao e motivo de aceitacao/rejeicao |
| **TEC** | Arquitetura propria (via DEP-ENG): motor de recomendacao, grafo de transicoes, decisao de banco e seu gatilho |
| **OPR** | Operacao do beta: deploy, monitor, backup/restore, incidente de disponibilidade |
| **APR** | Licoes generalizaveis: **a primeira delas ja existe** — *portao escrito antes do caso so revela onde nao cabe quando o caso chega* (`ADR-0027 §1`) |

## 14. Rastreabilidade

| Campo | Conteudo |
|---|---|
| ADR de criacao | **`ADR-0030`** — `ativo` · `ratificacao: ratificada`, **vigente** |
| Decisao do Soberano (data) | **EMITIDA em 2026-08-01** — nono ato soberano, [`MSG-2026-0009`](../../memory/operacional/MSG-2026-0009-ato-soberano-admissao-do-nxtrack.md), item **III**. `Q1` decidida em `PT-2026-009 §1` decisao 7 *(via `S1` com Produto real — `nXtrack`)* |
| Specs derivadas | **`0`.** `RD-33` segue bloqueante e **so fecha apos a vigencia** |
| Portao de origem externa | `PT-2026-014 §3` — `G0` a `G5`, com `G1` fechado por medicao |
| Pacote soberano | `PS-2026-016` |
| Verificacao de aptidao | `FIT-2026-023` |
| Proveniencia do candidato | `tree` `b9b36be9324ae2d36ddc4149049ebbff9f40fb4b`; 17 fontes congeladas em `_missao-1-13-4-4-2026-08-01/evidencia/ITEM-0-proveniencia-nxtrack.md` |
