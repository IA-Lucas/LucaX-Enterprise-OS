---
id: FIT-2026-018
titulo: Verificacao de aptidao da aplicacao do setimo ato soberano — os catorze objetos em vigor
tipo: fitness-check
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: DEP-QAR
proprietario: DEP-QAR
aprovador: DEP-EXE
criado_em: 2026-07-30
atualizado_em: 2026-07-30
revisao_prevista: null
decisoes_relacionadas: [ADR-0005, ADR-0012, ADR-0015, ADR-0020, ADR-0022, ADR-0023, ADR-0024, ADR-0025]
substitui: []
substituido_por: null
veredito: apto-com-ressalva
resumo: Verifica a aptidao evolutiva da aplicacao do setimo ato soberano — catorze objetos em vigor, dez transicoes O4 determinadas por reproducao de H-P — e conclui apto-com-ressalva, com uma ressalva nova nao corrigivel por edicao.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-GOV
ratificacao: nao-exigida
---

# FIT-2026-018: Vigencia do Framework de Specifications

> **Parecer, nao decisao** (`ADR-0015`, `FT-10`). Este documento **nao aprova, nao ratifica e nao
> promulga**. `FND-09 §8.2`, linha `FIT`: **ratifica `—`**.

## Proposito

Verificar a **aptidao evolutiva** da aplicacao do setimo ato soberano: se o acervo, **depois** de
receber catorze objetos de uma vez, continua **evoluivel, verificavel e coerente consigo mesmo**.

## Escopo

| Item | Definicao |
|---|---|
| Avaliado | A **aplicacao** — ordem, atomicidade, integridade, reconciliacao e os instrumentos usados. `FND-11` **como sede**; as **cinco** Cartas **como familia**; a nova baseline |
| **Nao** avaliado | O **merito** de `ADR-0022` a `ADR-0025`, **nao reaberto** — a decisao e do Soberano · o **conteudo normativo** de `SF-01` a `SF-32`, ja avaliado em `FIT-2026-015` e `FIT-2026-016` · `RD-33`, `S1`, `S2` · `RD-47`, `RD-48`, `RD-43`, `RD-13`, `RD-36` |
| Portao | **`QG-6`** — encerramento de mudanca `C3` |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| Autor do parecer | **DEP-QAR** | `FND-09 §8.2`, linha `FIT` |
| Revisor de forma | **DEP-GOV** | idem |
| Aprova | **DEP-EXE** | idem |

> **Impedimento declarado (`PI-10`, `ADR-0005`).** **`DEP-GOV` executou a aplicacao** e **nao**
> emite este parecer. **`DEP-EXE` e autor das Cartas de `ADR-0023` e `ADR-0025`** e **nao**
> participa da verificacao de integridade — aprova a **forma** do parecer, nao o seu conteudo
> tecnico. **`DEP-QAR` nao aplicou nada**, e e quem mede.

---

## 1. Conformidade — os controles obrigatorios

| # | Controle | Fonte | Medida | Veredito |
|---|---|---|---|---|
| **F1** | `H-P` reproduzido em todos os objetos | `IR-07` | **14 de 14** | ✅ |
| **F2** | `H-N` invariante sob `O4` | `IR-02`, `IR-06` | **10 de 10** | ✅ |
| **F3** | `IR-09` — reconstrucao reproduz `H-A` | `IR-09` | **10 de 10** com `O4`; **4 de 4** binariamente identicos sem `O4` | ✅ |
| **F4** | Nenhuma alteracao alem do diff autorizado | `IR-05` | **71 fontes normativas: 10 autorizadas mudaram, 61 byte a byte identicas · 0 intrusos · 0 removidos.** Reconciliacao *(8 `M3`)* e registros *(3)* sao **exigidos pelo ato** | ✅ |
| **F5** | Terminadores preservados | §III.7 do ato | `FND-10` **785/785 `CRLF`**, `0` convertidas | ✅ |
| **F6** | Ordem de aplicacao obrigatoria | §III.6 do ato | **(a) ADR → (b) `FND-11` → (c) `FND` → (d) Cartas**, cumprida | ✅ |
| **F7** | Atomicidade `FND-11` + `FND-01` + `FND-03` | §III.1 do ato | Os tres aplicados **no mesmo bloco**, `FND-11` **antes** — **`0` links quebrados entre escritas** | ✅ |
| **F8** | Backup datado anterior a escrita | `PI-07`, `AF-35` | **576 arquivos**, fora do acervo, **reconferidos contra a origem** | ✅ |
| **F9** | Baseline anterior reproduzida antes da escrita | `BL-03` | **185 · 54.190 · `3d8dbea0…84da` · 2.727 · 125** — **sete valores** | ✅ |
| **F10** | Autoverificacao | `ADR-0005` | **0** coincidencias em **131** pares; **quem aplicou nao verificou** | ✅ |
| **F11** | Credencial em texto | `PI-08`, `LV-02` | **0** ocorrencias | ✅ |
| **F12** | Links relativos | `DoD-7` | **2.834 verificados · 0 quebrados** | ✅ |
| **F13** | Catalogo sincronizado na mesma mudanca | `RG-03`, `CV-04` | Catalogo, **4** indices e **3** achados novos reconciliados | ✅ |
| **F14** | `ADR-0020` e `ADR-0021` intocados | §VI.2 do ato | **`0` bytes**; nenhum `superado_por` gravado | ✅ |
| **F15** | Nenhum tipo, entidade, camada ou diretorio novo | `MT-01`, §VII.1 do ato | **`FND-11` e instancia de entidade e tipo JA existentes** — `FND`, Framework | ✅ |

**15 de 15 controles conformes.**

## 2. Aptidao evolutiva — o que a aplicacao melhorou

| # | Dimensao | Antes | Depois |
|---|---|---|---|
| **E1** | **Sede da norma da `Spec`** | Dentro de `ADR-0021` — um `ADR` fazendo as vezes de fundacional | **`FND-11`**, nivel 2, com `ADR-0021` **vigente e intacto** |
| **E2** | **Titular de `QG-1`** | **Duas respostas** no acervo: `DEP-EXE` pela fonte, `DEP-PRD` por **4** Cartas | **Uma** resposta, por **cinco caminhos concordantes** |
| **E3** | **Conformidade de contrato** | **2** fundacionais sem os campos de `AC-08` | **`0`** |
| **E4** | **Objetos retidos por falta de ato** | **4** no acervo + **10** candidatos submetidos | **`0`** |
| **E5** | **Regime de `O4`** | **Costume nao escrito** — achado **70** | **Costume contornado por prova**: o `H-P` publicado **determina** a transicao |

> **`E5` e melhora de metodo, nao de norma.** **`RD-47` continua aberto**: a assimetria de regime
> de estado entre Carta e fundacional **nao foi resolvida**, foi **contornada**. O contorno so
> funciona **enquanto o ato publicar `H-P`**. Um ato futuro que **nao** publique `H-P` reabre o
> problema inteiro — e e por isso que a ressalva `R1` abaixo existe.

## 3. Ressalvas

| # | Ressalva | Severidade | Estado |
|---|---|---|---|
| **`R1`** | **`RD-49` — `DEP-OPS`, `DEP-GRW` e `DEP-TLS` 1.1.0 declaram em §13.2 um custo de Carta integral que o proprio arquivo desmente** *(`437 · 443 · 424` contra `438 · 444 · 425`)*. **Terceira ocorrencia da familia de `RC-01` e `RD-46`** | **Media** | ⚠️ **ABERTA — nao corrigivel por edicao.** As tres estao **ratificadas** (`LV-04`); exige **ato novo**. **Nao impede a vigencia**: nenhum hash, diff, dependencia ou terminador divergiu, e o defeito **estava no candidato revisado e ratificado**, nao na aplicacao |
| **`R2`** | **A prova de `QG-1` depende de um detector construido nesta missao.** Ele reproduz `PS-2026-012 §5` **celula a celula**, mas **e novo** — e a primeira versao dele tinha **8 falsos positivos**, achados na calibracao | Baixa | ⚠️ **ABERTA como declaracao de limite.** O proximo uso deve **recalibrar contra o estado conhecido antes de servir de prova**, e nao invocar este precedente |
| **`R3`** | **`RD-47` e `RD-48` seguem abertos**, e este ato **nao os alcanca** | Baixa | ⚠️ **ABERTA por escopo declarado** — §VII.4 do ato |

## 4. Riscos observados

| # | Risco | Prob. | Impacto | Mitigacao |
|---|---|---|---|---|
| **RA-1** | **A familia de `RC-01`/`RD-46`/`RD-49` volta a ocorrer** — numero que o artefato declara sobre si e que envelhece na escrita seguinte | **Alta** | Media | **Remedir §13.2 DEPOIS da linha de historico**, nunca antes. `PS-2026-010` fez e acertou; `PS-2026-012` nao fez e errou nas tres |
| **RA-2** | **Ato futuro sem `H-P` publicado** devolve o `O4` ao costume | Media | **Alto** | `R1` de `FIT-2026-016` e `RD-47` — **regra escrita de regime de estado** continua devida |
| **RA-3** | **`FND-11` nasce sem uma unica `Spec`** — `SF-01` a `SF-32` sao **determinados e nao observados** | **Alta** | Media | Ja registrado como achado **58** e como `RD-33`. A **primeira `Spec` real aciona revisao empirica** de `FND-11` — `PILOTO-DEFERIDO`, [PT-2026-008 §4](../relatorio-transicao-2026-07-29-canonizacao.md) |

## 5. Evidencia ausente, declarada — `PI-10`

| # | O que **nao** foi observado |
|---|---|
| **A1** | **Nenhum rollback foi exercido.** O procedimento de §VI.3 do ato — reversao **por bloco**, com o conjunto atomico indivisivel — e **previsto e nao testado**. Os `H-A` de partida estao publicados, mas **restaurar nao foi executado** |
| **A2** | **Nenhuma `Spec` existe**, e portanto **nenhuma regra de `FND-11` foi exercida contra um caso real**. O Framework entra em vigor **por construcao**, nao por uso |
| **A3** | **`IR-05` continua sem disparo real.** Nenhuma divergencia de `H-N` ocorreu em sete atos — a eficacia do controle segue **prevista, nao observada** |

## 6. Veredito

**`APTO-COM-RESSALVA`.**

A aplicacao e **conforme em 15 de 15 controles** e **melhora o acervo em cinco dimensoes
medidas**. As tres ressalvas **nao impedem a vigencia**: `R1` e defeito **do candidato
ratificado**, nao da aplicacao, e sua correcao **depende de ato**, nao de edicao; `R2` e
declaracao de limite de instrumento; `R3` e escopo expressamente excluido pelo proprio ato.

**Gatilho de revisao deste parecer:** a **primeira `Spec` real** — que aciona a revisao empirica
de `FND-11` — **ou** o proximo ato que alcance Carta de Departamento, o que ocorrer primeiro.

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-30 | DEP-QAR | Verificacao de aptidao da **Missao 1.13.3**. **15 de 15** controles conformes; **5** dimensoes de melhora medidas; **3** ressalvas, sendo `R1` *(`RD-49`)* **nao corrigivel por edicao**; **3** riscos e **3** ausencias de evidencia declaradas. Veredito **`APTO-COM-RESSALVA`**. |
