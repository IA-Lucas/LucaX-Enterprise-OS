---
id: ADR-0029-superacao-de-ato-por-evidencia-posterior
titulo: Instituir o caminho de superacao de ato por evidencia posterior, preservando o ato original byte a byte e reservando a decisao ao Soberano
tipo: adr
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-07-31
atualizado_em: 2026-07-31
revisao_prevista: 2027-01-31
decisoes_relacionadas: [ADR-0012, ADR-0015, ADR-0020]
substitui: []
substituido_por: null
classe_mudanca: C3
tipo_decisao: 1
supera: []
superado_por: null
resumo: Institui o caminho pelo qual um ato ja emitido pode ser superado por evidencia posterior e independente, sem que um unico byte do ato original seja tocado.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: ratificada
---

# ADR-0029: superacao de ato por evidencia posterior

> **NAO ESTA EM VIGOR.** `status: em-revisao` · `ratificacao: pendente`. `C3`/`Tipo 1` exige
> **ratificacao explicita e datada do Soberano sobre o texto final** (`LM-02`, `CV-09`). Esta
> missao **nao emite ato** — e um instrumento que alcanca atos **so pode nascer de um ato**.

## Proposito

Registrar a decisao de instituir o caminho pelo qual um **ato ja emitido** e **superado** por
evidencia posterior — nunca editado, nunca anulado retroativamente.

## Escopo

| Item | Definicao |
|---|---|
| **Inclui** | `SA-1` a `SA-6`: o que e superacao, quem instaura, quem decide, o que a superacao enumera, o efeito temporal e o registro |
| **Nao inclui** | Edicao ou anulacao de ato · recurso contra decisao **de merito** · poder de departamento sobre decisao soberana · alteracao de `ADR-0012` · alcance sobre o `SSC+`, que nao e acervo |
| **Subordinado a** | [FND-01 §7.3 e §9](../foundation/01-constituicao.md) · [FND-04 §2](../foundation/04-governanca.md) |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| Proponente | **DEP-GOV** | Guarda da conformidade e da rastreabilidade |
| Revisor independente | **DEP-QAR** | `AC-03` — criterio **vigente** |
| Aprovador · Ratificador | **SOBERANO**, e somente ele | `FND-04 §2`, `C3`; §11 |
| Executor | **DEP-GOV** | |

---

## 1. Contexto

`ADR-0012` fechou, com metodo reproduzivel, a porta que o proprio Soberano mandou vigiar:
*"comprovar que nenhuma alteracao ocorreu entre a revisao e a ratificacao"*. **Ele fez isso
tornando o ato integro e imutavel** — `IR-01` a `IR-12`.

**O que nao existe e o que fazer quando o FATO que fundamentou o ato se revela outro.** O
acervo sabe superar **artefato**: `O8` arquiva, `O9` retira, `superado_por` encadeia. **Nao
sabe superar ATO.**

**Medido nesta missao:** **7** atos soberanos, **7 de 7** em `status: ativo` com
`substituido_por: null`, **`0`** superados, e **`0`** ocorrencias de caminho de superacao de
ato em norma vigente — a varredura sobre `foundation/`, `decisions/` e `governance/` so
encontra o **diagnostico** da lacuna.

> **A imutabilidade que protege o ato contra adulteracao o protege tambem contra a verdade.**

## 2. Problema / Pergunta de decisao

Deve existir caminho para superar ato ja emitido quando prova posterior contradiz a condicao
tecnica que o fundamentou?

## 3. Criterios de decisao

De [RFC-0024 §3](../rfcs/RFC-0024-superacao-de-ato-por-evidencia-posterior.md): `K1` *(ato
original byte a byte)*, `K2` *(so o Soberano supera)*, `K3` *(nao vira recurso permanente)*,
`K4` *(efeito prospectivo por padrao)*, `K5` *(`ADR-0012` integro)`*.

## 4. Alternativas consideradas

[RFC-0024 §4](../rfcs/RFC-0024-superacao-de-ato-por-evidencia-posterior.md): **A** *(instituir
o caminho)*, **B** *(tratar como `INC`)*, **C** *(anotacao no ato)*, **D** *(superacao
automatica)* e **Z**. `B`, `C` e `D` falham cada uma num bloqueante diferente.

## 5. Decisao

### 5.1 As seis regras

| Regra | Conteudo |
|---|---|
| **`SA-1`** | **Ato pode ser SUPERADO por evidencia posterior. Nunca editado, nunca anulado retroativamente.** O ato original permanece **byte a byte**, `ativo` no historico, com **`0` bytes tocados** (`BL-02`, `CC-01`, `LV-04`) |
| **`SA-2`** | **A superacao e ato novo do Soberano**, e enumera: *(a)* o ato superado, por `id` **e `H-A`**; *(b)* **qual condicao tecnica** foi contradita, **citada literalmente** do ato original; *(c)* **a prova** que a contradiz, por **caminho e `sha256`**; *(d)* **o que passa a valer** no lugar (`SU-04`) |
| **`SA-3`** | **Efeito por padrao: prospectivo.** O que o ato superado ja produziu **permanece valido**, salvo declaracao expressa em contrario **item a item**. **Efeito retroativo e sempre expresso, nunca presumido** |
| **`SA-4`** | **Quem pode INSTAURAR ≠ quem pode DECIDIR.** Qualquer departamento instaura, **com a prova**; **so o Soberano supera**. **Instauracao nao suspende**: ato superavel continua em vigor ate o ato de superacao |
| **`SA-5`** | **A prova tem de ser POSTERIOR e INDEPENDENTE do ato.** Releitura da mesma evidencia **nao** e evidencia posterior — e discordancia, e **discordancia nao supera ato**. Sem isto, `SA-1` vira recurso permanente contra qualquer decisao |
| **`SA-6`** | **Registro de atos superados**, com data, ato superado, ato superador e a condicao contradita. **Contar quantas vezes a prova venceu o ato e a unica forma de saber se o portao esta calibrado** |

### 5.2 `ADR-0012` e pre-condicao, nao obstaculo

**`SA-2` so e executavel porque `IR-07` existe.** Sem `H-A` registrado no ato, nao ha como
identificar **qual texto** foi superado — e a superacao viraria afirmacao sobre um objeto que
ninguem consegue fixar.

| Regra de `ADR-0012` | Papel neste caminho |
|---|---|
| `IR-07` *(tres hashes no registro canonico)* | **Identifica** o ato superado — `SA-2` *(a)* |
| `IR-09` *(teste de reconstrucao)* | **Prova** que o ato superado nao foi alterado antes da superacao |
| `IR-05` *(divergencia de `H-N` e alteracao nao ratificada)* | **Continua valendo:** superar **nao** e caminho para alterar. Divergencia de `H-N` segue abrindo incidente |
| `IR-10` *(ausencia de `H-A` declarada)* | Ato sem `H-A` registrado **e superavel**, mas a superacao **declara** que o vinculo e o primeiro |

> **`0` bytes em `ADR-0012`.** Nada nele e retirado, e nada e reinterpretado.

### 5.3 O que este caminho **nao** faz

| # | Nao faz |
|---|---|
| 1 | **Nao permite editar, apagar ou reescrever ato algum** |
| 2 | **Nao da a departamento nenhum o poder de desfazer decisao do Soberano** — `SA-4` |
| 3 | **Nao cria recurso contra decisao DE MERITO.** Alcanca **condicao tecnica contradita por prova**, jamais preferencia revista |
| 4 | **Nao alcanca o `SSC+`**, que **nao e acervo** |
| 5 | **Nao supera nenhum dos 7 atos vigentes**, e **nenhum deles e candidato conhecido** |
| 6 | **Nao entra em vigor por esta redacao** — `SA-1` a `SA-6` sao texto sem efeito ate ato do Soberano |

## 6. Justificativa

| # | Fundamento |
|---|---|
| 1 | **A regra vem antes do caso, e o precedente e do proprio acervo.** `ADR-0007 §6` recusou decidir a fronteira com o conteudo a vista; aqui **`0` atos sao superaveis hoje**, e essa e a unica janela em que a regra e escrita sem interesse concreto |
| 2 | **Acrescenta sem retirar.** `ADR-0012` permanece integro e vira pre-condicao. Nao ha norma revogada |
| 3 | **A assimetria e reconhecida e contida.** `SA-5` existe porque `SA-1`, sem ele, transformaria toda decisao em provisoria |
| 4 | **Tradeoff aceito:** o instrumento mais alto do acervo deixa de ser definitivo. **Aceita-se** porque a alternativa e um ato de pe contra prova — e porque `SA-4` mantem a decisao **inteiramente** com o Soberano |

## 7. Impacto

| Dimensao | Impacto |
|---|---|
| Norma revogada | **Nenhuma** — lacuna de omissao |
| **Fundacionais emendados** | **`0`.** Precedente literal: `ADR-0012` instituiu **12** regras `IR` com **`0`** fundacionais emendados *(seu §7)* |
| `ADR-0012` | **`0` bytes** |
| Atos alcancados hoje | **`0`** — os 7 estao consumidos e sem contradicao de prova conhecida |
| **Direito de decisao criado** | **`SA-4` cria o direito de INSTAURAR**, que hoje nao existe em norma alguma |
| Registro novo | `SA-6` exige um registro de atos superados — **criado pelo ato que aplicar esta decisao**, nao por ela |
| Quem passa a fazer algo novo | **Qualquer DEP** *(instaurar, com prova)*; **DEP-GOV** *(manter o registro de `SA-6`)*; **SOBERANO** *(superar)* |

## 8. Evidencias

| # | Evidencia | Origem | Confianca | O que discrimina |
|---|---|---|---|---|
| `E1` | **`0`** ocorrencias de caminho de superacao de ato em norma vigente | Varredura de `foundation/`, `decisions/`, `governance/`, 2026-07-31 | **Alta — medida** | A lacuna e **de omissao**, e nao de contradicao. Sustenta *"nenhuma norma revogada"* |
| `E2` | **7** atos, **7 de 7** `ativo`, **`0`** superados | Frontmatter de `MSG-2026-0001` a `0007` | **Alta — medida** | Sustenta *"`0` atos superaveis hoje"* — a janela barata de §6 |
| `E3` | `ADR-0012` instituiu 12 regras com `0` fundacionais emendados | [ADR-0012 §7](ADR-0012-integridade-do-ato-de-ratificacao.md) | **Alta — literal** | Sustenta que o caminho **cabe em `ADR`**, sem cascata fundacional |
| `E4` | `IR-07` fornece o `H-A` que `SA-2` *(a)* exige | [ADR-0012 §5.2](ADR-0012-integridade-do-ato-de-ratificacao.md) | **Alta — literal** | Sustenta `§5.2`: pre-condicao, nao obstaculo |
| `E5` | Caso vivo do `SSC+`: `READY` de pe apos dois `ADJUST` posteriores, prova da ancoragem contradita | `RFC-0024 §6` | **Media — declarada pela Missao 1.13.4.1 e NAO reconferida por esta** | Mostra **a forma** do defeito. **Nao e acervo, nao e precedente** |
| **`A1`** | **Evidencia ausente, declarada:** **nenhum caso real de superacao de ato ocorreu neste acervo.** A eficacia de `SA-1` a `SA-6` e **prevista, nao observada** — `SA-6` nascera com o contador em **`0`** | `PI-10` | — | Impede ler o caminho como validado |
| **`A2`** | **Segunda ausencia:** `SA-5` distingue *"prova posterior"* de *"releitura"*, e **essa fronteira nunca foi exercida**. O primeiro caso real e que dira se ela discrimina | `PI-10`, `LV-12` | — | Nomeia onde este ADR pode falhar |

## 9. Riscos e mitigacao

| # | Risco | Prob. | Impacto | Mitigacao |
|---|---|---|---|---|
| `RA-1` | `SA-1` virar recurso permanente: toda decisao desagradavel vira pedido de superacao | **Media** | **Alto** | **`SA-5`** — prova **posterior e independente**; releitura e discordancia. **`SA-4`** — instaurar **nao suspende** |
| `RA-2` | Instauracao ser usada para **paralisar** por acumulo de pedidos | Media | Medio | `SA-4`, texto expresso: **instauracao nao suspende o ato** |
| `RA-3` | `SA-3` ser invertido na pratica — efeito retroativo virar o padrao por conveniencia | Media | **Alto** | `SA-3` exige declaracao **expressa e item a item**. Silencio **nao** retroage |
| `RA-4` | **A superacao ser irreversivel** — desfazer uma superacao ja feita nao tem caminho | **Certa** | **Alto** | **É a razao de `Tipo 1`.** `SA-5` encarece a entrada; `SA-1` preserva o ato original **byte a byte**, de modo que **o texto superado nunca se perde** |
| `RA-5` | **Esta decisao estar errada** — a fronteira de `SA-5` nao discriminar no caso real | Media | Medio | Gatilho de revisao na **primeira** instauracao, §12; `SA-6` mede a frequencia |

## 10. Plano de reversao — **explicito, exigido por `C3`/`Tipo 1`**

| Campo | Conteudo |
|---|---|
| Reversivel? | **A EMENDA sim; a SUPERACAO ja feita, nao** |
| Como desfazer a emenda | `ADR` de retirada (`O9`) superando este; `SA-1`–`SA-6` deixam de valer; o registro de `SA-6` passa a historico |
| **Custo de reverter a EMENDA — medido** | **1** `ADR` novo · **os indices `M3`** · o registro de `SA-6` *(preservado, nunca apagado — `FND-04 §7.2` etapa 5)*. **`0`** fundacionais · **`0`** artefatos migrados |
| **Custo de reverter uma SUPERACAO ja feita** | **Impossivel.** Um ato superado nao volta a vigorar por retirada da norma que permitiu supera-lo. **É exatamente por isso que `SA-5` existe e que a classe e `Tipo 1`** |
| Mitigacao da irreversibilidade | **`SA-1`**: o ato original permanece **integro e localizavel**, com `0` bytes tocados. **O que se perde e a vigencia, nunca o texto** |
| Janela | **Trivial enquanto o registro de `SA-6` estiver em `0`.** Hoje: **`0`** |
| Backup (`PI-07`) | `_backups/LucaX-Enterprise-OS_2026-07-31_pre-missao-1-13-4-2/` |

## 11. Classificacao — **determinada, nao presumida por analogia**

| Campo | Valor |
|---|---|
| Classe de mudanca | **`C3` — Constitucional** |
| Tipo de reversibilidade | **`Tipo 1`** |
| Aprovador | **SOMENTE o SOBERANO**, indelegavel |
| Ratificacao | **Sempre exigida** — `pendente` |
| Instrumento | **`RFC` obrigatoria → analise de impacto → `ADR` → ratificacao** — [RFC-0024](../rfcs/RFC-0024-superacao-de-ato-por-evidencia-posterior.md) |
| Fitness Check | **Obrigatorio** (`CV-07`) — [FIT-2026-022](../governance/fitness/FIT-2026-022-superacao-de-ato-por-evidencia-posterior.md) |

### 11.1 A determinacao, hipotese a hipotese

> **A classe NAO foi herdada de `ADR-0012`.** `ADR-0012` e `C2`/`Tipo 2`, e trata **do mesmo
> objeto** — o ato. **Herdar a classe dele seria o erro exato que esta missao foi mandada
> evitar.** `AL-01`: classifica-se pelo **efeito**.

| Hipotese de `C3` (`FND-04 §2`) | Incide? | Como se sabe |
|---|---|---|
| Altera **principio imutavel** | **Nao** | `PI-01` e `PI-06` intactos; o caminho e **exclusivamente** soberano e **reforca** os dois |
| Altera **linha vermelha** | **Nao** | `LV-04` *(nao reescrever historico)* e **satisfeita** por `SA-1`, nao alterada |
| Altera **hierarquia normativa** | **Nao** | Nenhum nivel de `FND-01 §10` se move. Ato supera ato — **mesmo nivel** |
| **Altera direitos de decisao** | **SIM** ⟵ | **`SA-4` cria o direito de INSTAURAR**, que **nao existe hoje**: nenhum departamento pode, em norma vigente, abrir procedimento que alcance ato soberano. **Uma hipotese basta** |
| Altera **a propria Fundacao** | **Nao — medido** | **`0`** fundacionais emendados; precedente literal de `ADR-0012 §7`, que instituiu 12 regras sobre atos **sem** tocar `FND` algum |

**`Tipo 1`, determinado:** `FND-04 §2.2` opoe reversivel a irreversivel. **`RA-4` mede a
irreversibilidade e ela e CERTA, nao provavel:** uma superacao consumada **nao se desfaz**
retirando a norma que a permitiu. `Tipo 2` exige reversao trivial sem consumidores — e aqui o
consumidor e o proprio ato superado, que nao retorna.

> **`GV-03` foi considerado e nao precisou ser aplicado:** a hipotese *"direitos de decisao"*
> incide **literalmente**, e nao por duvida resolvida em favor da classe mais alta.

## 12. Revisao

| Campo | Conteudo |
|---|---|
| Gatilho por evento | **Primeira instauracao** — verificar se `SA-5` discriminou prova posterior de releitura |
| Gatilho por evento | **Primeira superacao consumada** — verificar se `SA-3` foi respeitado e se algum efeito retroativo foi presumido |
| Gatilho por evento | **Terceira instauracao sem superacao** — sinal de `RA-1`: o caminho virou recurso |
| Gatilho temporal | 2027-01-31 |
| Sinal de que esta decisao deu errado | *(a)* instauracoes crescendo sem superacoes; *(b)* uma superacao com efeito retroativo declarado *"por coerencia"* em vez de item a item |
| Dono | **DEP-QAR** |

## 13. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Origem | [RFC-0024](../rfcs/RFC-0024-superacao-de-ato-por-evidencia-posterior.md) |
| Evidencia de origem *(nao norma)* | `MINUTA-C-superacao-de-ato-por-evidencia-posterior.md`, `sha256` `b5cd82aeb06ebf5845f9b8a1aafc457df91d639e5df0c2da23319934d08e678a` |
| **Norma superada** | **Nenhuma.** Lacuna de **omissao** — medido em `§8 E1` |
| Decisoes relacionadas | [ADR-0012](ADR-0012-integridade-do-ato-de-ratificacao.md) — **pre-condicao**, `0` bytes; [ADR-0015](ADR-0015-fitness-check-e-parecer-nao-decisao.md) — `FT-11`, a ratificacao incide sobre a mudanca, nunca sobre o parecer |
| Evidencia externa | `SSC+` — **nao e acervo**, confianca **Media**, **nao reconferida** por esta missao |
| Verificacao de aptidao | [FIT-2026-022](../governance/fitness/FIT-2026-022-superacao-de-ato-por-evidencia-posterior.md) |
| Pacote soberano | [PS-2026-015](../governance/pacote-soberano-2026-07-31-emendas-de-instrumento.md) |

---

## Checklist de validade (FND-07 §4.1)

- [x] `VD-01` — **4** alternativas reais + *"nao fazer nada"* (`RFC-0024 §4`)
- [x] `VD-02` — criterios declarados antes da escolha
- [x] `VD-03` — nenhuma alternativa de palha: `B`, `C` e `D` sao as respostas naturais
- [x] `VD-04` — tradeoff aceito explicito (§6, item 4)
- [x] `VD-05` — **duas** ausencias declaradas (§8, `A1` e `A2`)
- [x] `VD-06` — reversao **explicita**, com a **irreversibilidade da superacao nomeada** (§10)
- [x] `VD-07` — impacto mapeado; **`0` fundacionais, medido** (§7)
- [x] `VD-08` — data e responsavel presentes
- [x] `VD-09` — gatilhos de revisao definidos (§12)

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-31 | DEP-GOV | Decisao inicial, **`em-revisao` · `ratificacao: pendente`, NAO vigente**. Institui `SA-1` a `SA-6`. **Norma superada: nenhuma** — lacuna de omissao, medida em **`0`** ocorrencias de caminho em norma vigente e **7 de 7** atos `ativo`. `ADR-0012` vira **pre-condicao**, com `0` bytes. Classe **`C3`/`Tipo 1`** determinada percorrendo as cinco hipoteses — incide *"direitos de decisao"*, porque **`SA-4` cria o direito de instaurar**; **nao** foi herdada de `ADR-0012`, que e `C2`/`Tipo 2` sobre o mesmo objeto. Irreversibilidade da superacao consumada declarada como **certa**, nao provavel. |
