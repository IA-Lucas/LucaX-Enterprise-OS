---
id: FIT-2026-019
titulo: Verificacao de aptidao da admissao do medAlly — o primeiro exercicio do portao de ADR-0007 e o primeiro Produto candidato
tipo: fitness-check
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: DEP-QAR
proprietario: DEP-QAR
aprovador: DEP-EXE
criado_em: 2026-07-31
atualizado_em: 2026-07-31
revisao_prevista: null
decisoes_relacionadas: [ADR-0005, ADR-0007, ADR-0012, ADR-0015, ADR-0021, ADR-0026]
substitui: []
substituido_por: null
veredito: apto-com-ressalva
resumo: Verifica a aptidao evolutiva da admissao candidata do medAlly, com C11 conforme em 13 de 13, e conclui apto-com-ressalva com cinco ressalvas e uma questao bloqueante nao resolvivel por parecer.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-GOV
ratificacao: nao-exigida
---

# FIT-2026-019: Admissao do medAlly

> **Parecer, nao decisao** (`ADR-0015`, `FT-10`). Este documento **nao aprova, nao ratifica e
> nao promulga**. `FND-09 §8.2`, linha `FIT`: **ratifica `—`**. **`0` Produtos existem** quando
> este parecer e emitido, e ele **nao muda esse numero**.

## Proposito

Verificar a **aptidao evolutiva** da admissao candidata do medAlly: se o acervo, **depois** de
receber o seu primeiro Produto e de exercer pela primeira vez o portao de origem externa,
continua **evoluivel, verificavel e coerente consigo mesmo** — e se `G1`–`G5` **bastam**, como
[ADR-0007 §12](../../decisions/ADR-0007-fronteira-greenfield-legado.md) obriga avaliar no
primeiro caso real.

## Escopo

| Item | Definicao |
|---|---|
| Avaliado | O **rito** — `RFC-0021` → `ADR-0026` → `PS-2026-014` · a **Carta candidata** · o **exercicio do portao** `G1`–`G5` · a **conformidade `C11`** de `FND-10 §11` · a integridade dos hashes |
| **Nao** avaliado | O **merito tecnico** do medAlly · **qualquer conteudo** do seu repositorio, que **nao foi submetido** · a escolha entre medAlly e nXtrack, que e do **Soberano** *(`Q1`)* · `RD-49`, `RD-47`, `RD-48`, `RD-43`, `RD-13`, `RD-36`, todos **fora do escopo e mantidos abertos** |
| Portao | **`QG-6`** — encerramento de mudanca `C2` (`CV-07`) |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| Autor do parecer | **DEP-QAR** | `FND-09 §8.2`, linha `FIT` |
| Revisor de forma | **DEP-GOV** | idem |
| Aprova | **DEP-EXE** | idem |

> **Impedimentos declarados (`PI-10`, `ADR-0005`, `PI-05`).**
> **`DEP-PRD` e autor da Carta e de `ADR-0026`** e **nao** participa desta verificacao.
> **`DEP-GOV` e autor de `PS-2026-014`** e sera o **executor** da aplicacao futura: revisa a
> **forma** deste parecer e **nao** o seu conteudo tecnico quanto ao proprio pacote — recorte de
> precedente `FIT-2026-003` e `FIT-2026-017`, com a parte impedida aprovada por **DEP-EXE**.
> **`DEP-EXE` nao e autor de nenhum objeto avaliado** — e a unica das quatro areas sem
> impedimento. **`DEP-QAR` nao produziu nenhum dos tres artefatos**, e e quem mede.

---

## 1. Conformidade — os controles obrigatorios

| # | Controle | Fonte | Medida | Veredito |
|---|---|---|---|---|
| **`F1`** | Baseline anterior reproduzida **antes** da escrita | `BL-03` | **189 · 55.280 · `a3ca6ce3…ca5d`** — **tres valores** | ✅ |
| **`F2`** | Backup datado anterior a escrita | `PI-07`, `AF-35` | **567** arquivos, fora do acervo, **reconferidos contra a origem** | ✅ |
| **`F3`** | Instrumento validado **antes** de medir objeto novo | `CE-02`; licao de `FIT-2026-018 R2` | **10 de 10** controles publicados reproduzem — **apos** a calibracao **reprovar** a primeira versao do filtro | ✅ |
| **`F4`** | `H-N` invariante sob `O4` | `IR-02`, `IR-06` | **2 de 2** | ✅ |
| **`F5`** | `IR-09` — reconstrucao reproduz `H-A` | `IR-09` | **2 de 2** | ✅ |
| **`F6`** | `O4` alcanca **somente** `status` e `ratificacao` | §6.3 de `PS-2026-014` | **`-3` bytes** em cada objeto, aritmeticamente explicados. **`atualizado_em` intocado** | ✅ |
| **`F7`** | **`G1` a `G4` comprovados; `G5` preparado** | `ADR-0007 §5.3` | **4 comprovados · 1 preparado.** Nenhuma condicao ausente — `FR-06` nao foi acionado | ✅ |
| **`F8`** | Classificacao `G3` — **exatamente uma** | `ADR-0007 §5.4` | **`REWRITE`**, com as outras tres eliminadas por escrito | ✅ |
| **`F9`** | **`0` bytes admitidos** do repositorio de origem | `FR-03`, `AM-01` | **`0`** — nenhum arquivo proposto para entrada | ✅ |
| **`F10`** | **`0` bytes escritos** no repositorio de origem **atribuiveis a missao** | Determinacao da missao | **O manifesto NAO e identico:** **16** caminhos divergem — **1** novo e **15** alterados —, **todos** sob `docs/demonstracao/` e os **3** geradores de `ferramentas/`. **`0`** deles foi lido ou executado pela missao; as **5** fontes consumidas estao **byte a byte identicas**; e **todas** as contagens publicadas remedem igual, exceto o total de arquivos *(550 → 551)*. **Mudanca paralela alheia** — `RD-59` | ✅ **com ressalva `R5`** |
| **`F11`** | Nenhum outro produto inventariado | `FR-07` | **`0`.** O nXtrack e citado **como alternativa** e **nao foi examinado** — declarado em `A2` de `ADR-0026 §8` | ✅ |
| **`F12`** | Vinculo a `Capability` **ativa** | `VC-01`, `FND-08 §8` | **5 de 5** `ativo`, conferidas no catalogo | ✅ |
| **`F13`** | Pre-condicoes de Produto | `FND-04 §6`, linha *Produto* | **3 de 4** satisfeitas; a quarta — *"Decisao do Soberano"* — **e o proprio ato**, e por isso **`0` Produtos existem** | ✅ |
| **`F14`** | Teste de existencia aplicado | `FND-03 §3.1` | **Passa**, com a fragilidade **declarada** — ressalva `R1` | ✅ |
| **`F15`** | Autoverificacao | `ADR-0005`, `AC-03` | **`0`** coincidencias em **136** pares. **Quem escreveu a Carta nao a revisou; quem escreveu o pacote nao emite este parecer** | ✅ |
| **`F16`** | Credencial em texto | `PI-08`, `LV-02` | **`0`** ocorrencias em **194** artefatos | ✅ |
| **`F17`** | Links relativos | `DoD-7` | **2.936 verificados · `0` quebrados** no acervo. A Carta candidata **esta fora do acervo** — ressalva `R2` | ✅ |
| **`F18`** | Catalogo e indices reconciliados na **mesma** mudanca | `RG-03`, `CV-04`, `IX-02` | Catalogo, **5** indices e **7** achados novos | ✅ |
| **`F19`** | Nenhuma entidade, tipo, camada ou diretorio novo **no acervo** | `MT-01`, `CS-01` | **`0`.** `PRO` e entidade `E-17` e tipo documental **ja existentes**; `products/` **nao e criado nesta missao** | ✅ |
| **`F20`** | Nenhum artefato `M1`, `MSG`, `FIT` ou baseline historica editado | `LV-04`, `BL-02`, `CC-01` | **`0` bytes.** `ADR-0007` **exercido, nao emendado** — `0` bytes | ✅ |

**20 de 20 controles conformes.**

## 2. `C11` — Conformidade de [FND-10 §11](../../foundation/10-artifact-framework.md)

| # | Verificacao | Resultado |
|---|---|---|
| `C11-1` | Contrato `L1` completo | ✅ **3 de 3** artefatos novos declaram os 15 campos universais **e** os 5 de `FND-10 §2.2`. A Carta declara ainda `capabilities`, atributo minimo de `E-17` |
| `C11-2` | `revisor` ≠ `autor` | ✅ **3 de 3** — DEP-PRD × DEP-QAR *(Carta, ADR)*, DEP-GOV × DEP-QAR *(pacote)*, DEP-QAR × DEP-GOV *(este parecer)* |
| `C11-3` | `ratificacao` coerente com a classe | ✅ `ADR-0026` e a Carta declaram **`pendente`** e **nao entram em `ativo`**; `RFC-0021` e este parecer declaram **`nao-exigida`**, corretos para as suas linhas |
| `C11-4` | Tipo documental consta de `FND-10 §4` | ✅ `carta`, `adr`, `rfc`, `relatorio` e `fitness-check` — **todos ja existentes**; **`0`** tipos novos |
| `C11-5` | Atributo derivavel no frontmatter | ✅ **`0`.** Consumidores, relacoes, autoridade e custo de contexto vivem **no corpo** ou sao **calculados** (`AC-01`) |
| `C11-6` | Cadeia origem → estado → substituicao percorrivel | ✅ `RFC-0021` → `ADR-0026` → `PRO-medally`, com `PS-2026-014` e este parecer nos dois sentidos. **`0`** elos quebrados |
| `C11-7` | Custo de contexto **medido**, nao estimado | ✅ **359 · 315 · 253 · 428 · 180 · 283** linhas, por `wc -l`, com data |
| `C11-8` | Entrada no catalogo mestre presente | ✅ **5** artefatos novos em §4 do catalogo; a Carta candidata em §9, **como candidato e nao como artefato** (`FR-10`) |
| `C11-9` | Divisao com menos de dois sinais observados | ✅ **nao se aplica** — nenhuma especializacao proposta |
| `C11-10` | Tabela reproduzida sem declaracao de projecao | ✅ **`0`.** `ADR-0026 §3` **remete** aos criterios de `RFC-0021 §4` em vez de reproduzi-los; `PS-2026-014 §4` **nao reproduz** as 674 linhas dos objetos |
| `C11-11` | Teste preventivo de projecao aplicado, com evidencia | ✅ **`PJ-06` respondido nas duas metades:** houve duplicacao? **Nao.** O teste foi aplicado? **Sim** — e produziu **duas** decisoes de remissao, nomeadas em `C11-10` |
| `C11-12` | **Conteudo de origem externa admitido fora do portao** | ✅ **`0`.** Esta e a **primeira vez** que este controle tem objeto real, e ele **discriminou**: o candidato passou pelas cinco condicoes, e a classificacao resultante faz **`0`** arquivos entrarem |
| `C11-13` | Alteracao de conteudo sem incremento de versao | ✅ **`0`.** Os artefatos novos nascem em **1.0.0**; **nenhum** artefato existente teve conteudo alterado — somente projecoes `M3`, que `AC-09` isenta |

**`C11` conforme em 13 de 13.**

## 3. Aptidao evolutiva — o que esta missao melhorou, e o que ela nao melhorou

| # | Dimensao | Antes | Depois |
|---|---|---|---|
| `E1` | **Portao de origem externa** | **Escrito e nunca exercido** — `ADR-0007 §8` declarava *"nao ha nenhum candidato real"* | **Exercido sobre um candidato nomeado**, com `G1`–`G4` comprovados e **duas lacunas medidas** |
| `E2` | **Primeiro Produto** | **`0`** Produtos, **`0`** `Spec`s, `products/` ausente | **`0` Produtos** — e **um candidato integro, medido e submetido**. **A melhora e de prontidao, nao de estado** |
| `E3` | **Instrumento `IR-02`/`IR-03`** | Reimplementado a cada missao | **Defeito real encontrado e corrigido antes do uso** — filtro por chave de **frontmatter**, nunca por linha de corpo |
| `E4` | **Evidencia sobre produto** | Nenhum produto do CEO tinha evidencia estruturada no acervo | **12** evidencias separadas por natureza e **5** ausencias declaradas, sobre um candidato |

> **`E2` e a dimensao que mais importa e a que menos avancou, e isso esta escrito de proposito.**
> **`RD-33` continua bloqueante**, e continuara ate a **vigencia** — nao ate este parecer, nao
> ate o pacote, e nao ate o ato: **ate a aplicacao verificada**. Ler qualquer um dos tres como
> desbloqueio seria `LV-05`.

## 4. Ressalvas

| # | Ressalva | Severidade | Estado |
|---|---|---|---|
| **`R1`** | **O publico primario do Produto tem um membro.** O teste de existencia de `FND-03 §3.1` passa — a norma pergunta *"alguem"*, nao *"muitos"* — **pela margem minima**. A Carta declara o fato em §2, cria `H1` para testa-lo e escreve o encerramento correspondente em §6 | **Media** | ⚠️ **ABERTA como fato declarado.** **Nao impede a admissao**, e **nao deve ser lida como validada** |
| **`R2`** | **Os links relativos da Carta candidata apontam para o destino e nao resolvem onde ela esta.** E consequencia **necessaria** de submeter o byte exato que sera aplicado. **A Carta esta fora do acervo e fora da varredura de `F17`** | Baixa | ⚠️ **ABERTA como limite declarado.** Resolve-se sozinha **no instante da aplicacao**, e a aplicacao deve **reconferir os 9 links** |
| **`R3`** | **A evidencia central do publico e `alegada`, nao `observada`.** A entrevista foi **lida**; o entrevistado **nao foi consultado** por esta missao. Todo `K2` repousa sobre um documento de terceiro com proveniencia declarada | **Media** | ⚠️ **ABERTA.** Fecha com a primeira medicao de `M1`–`M5`, que exige o medico presente |
| **`R5`** | **A prova de *zero escrita* deixou de ser um manifesto identico e passou a ser um recorte.** O candidato mudou **no mesmo dia**, entre a abertura e o fechamento da missao. A prova permanece **suficiente** — os **16** caminhos estao enumerados, **nenhum** foi lido ou executado pela missao, e as **5** fontes consumidas estao intactas —, **mas e mais fraca do que um manifesto que reproduz**, e a diferenca esta escrita em vez de suavizada | **Media** | ⚠️ **ABERTA.** **`RD-59`: `G1` exige *data*, e data nao basta para repositorio vivo.** **Terceira lacuna medida do portao**, ao lado de `RD-54` e `RD-55` |
| **`R4`** | **`Q1` nao e resolvivel por parecer.** A colisao com a decisao **7** e materia de **portfolio**, e `FND-01 §7.3` a atribui ao **Soberano**. Este parecer **nao a resolve e nao pode** | **Alta quanto ao efeito** | ⚠️ **ABERTA — e e por isso que o veredito nao e `apto`** |

## 5. Riscos observados

| # | Risco | Prob. | Impacto | Mitigacao |
|---|---|---|---|---|
| `RA-1` | **A admissao virar precedente de entrada por atacado** | Media | **Alto** | `G3` = `REWRITE` com **`0`** entradas; `AM-01` e `AM-05`; `FR-07` — **cada admissao futura tem portao proprio**. O precedente que este caso institui e o **oposto**: o portao pode terminar sem nada entrar |
| `RA-2` | **`RD-33` ser dado por fechado antes da vigencia** | **Alta** | Medio | `AM-02`, item `IV.5` da minuta e §3 `E2` deste parecer. **Tres declaracoes independentes, de proposito** |
| `RA-3` | **O ato ser lido como autorizacao clinica** | Media | **Alto** | `AM-04`, item `IV.3` da minuta e §4 da Carta. As **sete** linhas vermelhas aparecem nos tres documentos |
| `RA-4` | **`RD-54`/`RD-55` virarem contorno permanente** do portao | Media | Medio | Nascem com **dono** *(DEP-GOV)* e **gatilho** *(segunda admissao)*. `Q2` pergunta ao Soberano se devem ser emendados agora |
| `RA-5` | **A familia de `MEM-APR-0002` reincidir** — projecao nao remedida pela mudanca que altera a fonte | **Alta** | Baixo | Reconciliacao executada **artefato a artefato por ferramenta**, na mesma mudanca. **`RD-53` desta missao e mais uma ocorrencia da familia**, encontrada exatamente por remedir em vez de ler |

## 6. Evidencia ausente, declarada — `PI-10`

| # | O que **nao** foi observado |
|---|---|
| `A1` | **Nenhum criterio de sucesso do Produto foi medido.** As 10 teleconsultas simuladas **nao ocorreram**, e `M1`–`M5` sao **metas, nunca resultados** |
| `A2` | **Nada foi medido sobre o nXtrack.** `FR-07` proibe inventariar candidato nao nomeado. A Opcao B de `RFC-0021` foi recusada **por ausencia de evidencia**, jamais por demerito — e **o Soberano pode ter a evidencia que esta missao nao pode ter** |
| `A3` | **DEP-EXE nao se manifestou**, e `FND-01 §7.3` o exige como consulta obrigatoria em materia de portfolio. **Silencio nao aprova** (`LM-03`, `GV-05`) |
| `A4` | **A suite de testes do candidato nao foi reexecutada.** O que se mediu foi estrutura — **50** arquivos, **1.298** funcoes `test_` —, nunca resultado |
| `A5` | **Nenhum rollback foi exercido.** O procedimento de `PS-2026-014 §6.4` e **previsto e nao testado** |
| `A6` | **`IR-05` continua sem disparo real** em oito ritos. A eficacia do controle segue **prevista, nao observada** |

## 7. Veredito

**`APTO-COM-RESSALVA`.**

O rito e **conforme em 20 de 20** controles e em **`C11` 13 de 13**, e melhora o acervo em
**quatro** dimensoes medidas. **`0` fontes normativas foram alteradas**, **`0` bytes entraram do
repositorio de origem** e **`0` bytes foram escritos nele por esta missao** — este ultimo **com a
ressalva `R5`**, porque a arvore do candidato **mudou em paralelo** e a prova deixou de ser um
manifesto identico para ser um **recorte enumerado**.

| Campo | Conteudo |
|---|---|
| **Por que nao `apto`** | **`R4`.** A questao `Q1` e uma **escolha real que so o Soberano pode fazer**, e ela nao e cosmetica: sob a leitura `L2`, o pacote inteiro e inadmissivel. **Declarar nao e resolver** |
| **Por que nao `inapto`** | **`0`** regras normativas criadas; **`0`** fontes alteradas; **`C11` 13 de 13**; **20 de 20** controles; **10 de 10** validacoes de instrumento; **`IR-09` 2 de 2**. **Nada aqui aumenta o custo de evoluir sem ganho declarado** |
| **`0` Produtos entraram em vigor** | Confirmado: `products/` **nao existe** na raiz do acervo, e **`0`** artefatos de tipo `PRO` estao no catalogo como vigentes |

**Gatilho de revisao deste parecer:** o **ato soberano sobre `PS-2026-014`** — ou a **segunda
admissao pelo portao de `ADR-0007`**, o que ocorrer primeiro.

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-31 | DEP-QAR | Verificacao de aptidao da **Missao 1.13.4**. **20 de 20** controles conformes e **`C11` 13 de 13** — a **primeira vez** que `C11-12` *(conteudo externo admitido fora do portao)* tem objeto real. **4** dimensoes de melhora; **5** ressalvas, sendo **`R4`** *(`Q1`)* **nao resolvivel por parecer** e **`R5`** *(`RD-59`)* nova; **5** riscos e **6** ausencias de evidencia declaradas. Veredito **`APTO-COM-RESSALVA`**. **`0` Produtos em vigor.** |
