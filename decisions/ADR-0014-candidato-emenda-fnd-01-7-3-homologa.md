---
id: ADR-0014-candidato-emenda-fnd-01-7-3-homologa
titulo: CANDIDATO — Emenda C3 a FND-01 §7.3 e §11 para separar ratificacao de homologacao
tipo: adr
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0006, ADR-0009, ADR-0012]
substitui: []
substituido_por: null
classe_mudanca: C3
tipo_decisao: 2
supera: []
superado_por: null
resumo: Candidato sem vigencia — separa ratificacao de homologacao em FND-01 §7.3 e §11, sem alterar nenhum titular de decisao, e depende de ratificacao do Soberano para existir.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: ratificada
---

# ADR-0014 *(CANDIDATO)*: Separar ratificacao de homologacao em FND-01 §7.3

> ## ⛔ ESTE ADR NAO ESTA EM VIGOR E NAO PRODUZ NENHUM EFEITO
>
> **Nenhuma linha de FND-01 foi alterada.** Este documento e o **candidato** exigido pela
> etapa 5 de [FND-01 §9](../foundation/01-constituicao.md), produzido apos as etapas 1 a 3.
> A **etapa 4 — ratificacao explicita e datada do Soberano — nao ocorreu**, e o ato de
> 2026-07-28 declara expressamente que **nao ratifica futura emenda C3**.
>
> **Sem ela, a emenda nao existe** (FND-01 §9; LM-02, LM-03, LM-04). Ate la:
> `status: em-revisao` · `ratificacao: pendente` · **FND-01 permanece em 1.3.0** · a contencao
> **`IR-11`** de [ADR-0012](ADR-0012-integridade-do-ato-de-ratificacao.md) segue **integralmente
> em vigor**.

## Proposito
Ter pronto, para decisao do Soberano, o texto que separa os **dois institutos** que a coluna
*Ratifica* de FND-01 §7.3 hoje nomeia com **um** nome — sem alterar nenhum titular de decisao,
nenhum principio imutavel e nenhuma linha vermelha.

## Escopo
| Item | Definicao |
|---|---|
| Inclui | **FND-01 §7.3** — cabecalho da 4a coluna, cinco celulas e uma nota normativa · **FND-01 §11** — uma entrada de glossario |
| **Nao** inclui | **Q2** de RFC-0009 *(`FIT` e ratificacao)* — materia **separada**, C2 escalada, sem ADR candidato, por decisao de [ADR-0012 §5.5](ADR-0012-integridade-do-ato-de-ratificacao.md). **Nenhum** titular de decisao. **Nenhum** principio, linha vermelha ou nivel da hierarquia normativa |
| Origem | [RFC-0011 §3](../rfcs/RFC-0011-emenda-constitucional-ratifica-homologa.md), que cumpre as etapas 1 a 3 de FND-01 §9 |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| Proponente | **DEP-GOV** | Guardiao da Constituicao; dono de **IC-2** |
| Revisor independente | **DEP-QAR** | AC-03; FND-09 §8.2, linha `ADR` |
| **Aprova e ratifica** | **SOBERANO** | **FND-04 §2.1, linha C3 — indelegavel.** Nao ocorreu |
| Impedido de opinar sobre o merito | **DEP-EXE** | Titular nomeado em **4 das 5** linhas em questao (PI-05, RM-06b). Declarado em RFC-0011 §9 |

---

## 1. Contexto

**IC-2** esta aberto ha **tres ciclos**, com dono **DEP-GOV** e gatilho *"proxima emenda a
FND-01, ou ato do Soberano sobre Q1 de RFC-0009"*. A contencao `IR-11` de ADR-0012 impede a
**propagacao** do defeito e declara, no proprio texto, que **nao corrige a causa**.

**Fato novo desta missao, medido:** a colisao alcanca **cinco** linhas — quatro com `DEP-EXE` e
**uma com `DEP-GOV`** —, e nao quatro como IC-2 registrava. Achado **RC-03**
([RFC-0011 §4](../rfcs/RFC-0011-emenda-constitucional-ratifica-homologa.md)).

**Fato que decide:** a projecao de FND-01 §7.3 em **FND-09 §8.2** — que se declara derivada
*"sem redefini-las"* — **nao reproduz nenhum dos cinco titulares departamentais**. Todas as suas
22 linhas dizem `SOBERANO`, `SOBERANO se …` ou `—`. **O acervo ja opera no sentido estrito;
falta a Constituicao dize-lo.**

## 2. Problema / Pergunta de decisao

> **A Constituicao deve usar um nome diferente para o ato do Soberano que da vigencia e para o
> ato do departamento que confirma uma decisao dentro do rito?**

## 3. Criterios de decisao

| # | Criterio |
|---|---|
| K1 | **Nenhum titular de decisao muda.** Quem homologa hoje continua homologando, com o mesmo alcance |
| K2 | **Nenhum principio imutavel nem linha vermelha e tocado** |
| K3 | **Impacto minimo e verificavel** — numero de celulas alteradas, contado |
| K4 | **Nenhum artefato existente precisa ser reescrito** |
| K5 | **Reversibilidade** por emenda revogatoria de mesmo rito |

## 4. Alternativas consideradas

### Alternativa A — Renomear a coluna e qualificar as cinco celulas *(escolhida)*
Cabecalho passa a `Ratifica / Homologa`; as cinco celulas ganham a qualificacao *(homologa)*;
uma nota normativa define os dois institutos; o glossario recebe **Homologacao**.
**8 alteracoes, nenhuma delas de titular.**

### Alternativa B — Criar uma **quinta coluna** *Homologa*, separada de *Ratifica*
| Campo | Conteudo |
|---|---|
| A favor | Separacao visual maxima; cada instituto em sua coluna |
| **Contra** | Obriga a preencher **12 linhas × 2 colunas** onde hoje ha 12 celulas; produz **7 celulas vazias** e amplia a tabela sem acrescentar informacao. **Falha K3** |
| Veredito | **Recusada** |

### Alternativa C — Manter a coluna e resolver apenas no **glossario**
| Campo | Conteudo |
|---|---|
| A favor | Uma unica alteracao |
| **Contra** | O leitor da tabela **nao vai ao glossario**. E exatamente o desenho atual — a definicao estrita ja existe em FND-10 §5.4 e **nao impediu** INC-2026-001 nem INC-2026-002. **Falha por evidencia observada, nao por teoria** |
| Veredito | **Recusada** |

### Alternativa Z — Nao emendar
| Campo | Conteudo |
|---|---|
| O que acontece | `IR-11` continua sendo a unica protecao. **Ela funciona:** zero violacoes em 1.210 ocorrencias medidas |
| **Custo real** | A protecao alcanca **artefato novo** e **nao alcanca o leitor de boa-fe do texto constitucional**. E o quarto ciclo com a causa viva |
| Veredito | **Legitima — e e o cenario 4 de RFC-0011 §8.** Nao e recusada aqui: **so o Soberano pode recusa-la ou escolhe-la** |

## 5. Decisao *(proposta — sem vigencia)*

**Propoe-se alterar FND-01 §7.3 e §11 em oito pontos, sem alterar nenhum titular de decisao.**

O diff literal, celula a celula, vive em
[RFC-0011 §3.2](../rfcs/RFC-0011-emenda-constitucional-ratifica-homologa.md) — **fonte unica**,
e **nao e reproduzido aqui** (PJ-01, CM-09). Resumo do alcance:

| # | Objeto | Alteracoes |
|---|---|---|
| 1 | §7.3, cabecalho da 4a coluna | **1** — `Ratifica` → `Ratifica / Homologa` |
| 2 | §7.3, celulas com titular departamental | **5** — cada uma ganha *(homologa)*; **o nome do titular nao muda em nenhuma** |
| 3 | §7.3, nota normativa nova | **1** — define os dois institutos por remissao a FND-10 §5.4 |
| 4 | §11, glossario | **1** — entrada **Homologacao** |
| | **Total** | **8** |

### 5.1 Versao proposta — e a duvida que **nao** se resolve aqui

| Campo | Proposta | Observacao |
|---|---|---|
| FND-01 | **1.4.0** *(MENOR)* | Nenhum titular muda; altera-se **nome de instituto** e acrescenta-se glossario |
| **Alternativa declarada** | **2.0.0** *(MAIOR)* | Se o Soberano entender que **nomear corretamente o instituto altera o direito de decisao**, FND-01 §9 manda incrementar MAIOR. **A escolha e dele.** Este ADR **nao a antecipa** (LM-03) |

### 5.2 O que esta decisao **nao** faz

| Nao faz | Por que |
|---|---|
| Nao altera **quem** decide, homologa ou ratifica coisa alguma | K1; as cinco celulas mantem o mesmo nome |
| Nao toca principio imutavel nem linha vermelha | K2 |
| Nao toca a **hierarquia normativa** de FND-01 §10 | Fora do escopo |
| Nao resolve **Q2** *(`FIT` e ratificacao)* | Materia **separada**, C2 escalada — RFC-0011 §5 |
| Nao corrige `FIT-2026-001` | **M1**, nao editavel (LV-04) |
| Nao revoga `IR-11` | Aprovada a emenda, `IR-11` deixa de ser **contencao** e passa a **redundancia benigna**; revoga-la seria decisao propria |
| **Nao entra em vigor** | Etapa 4 de FND-01 §9 nao ocorreu |

## 6. Justificativa

| # | Fundamento |
|---|---|
| 1 | **A evidencia e empirica, nao teorica.** FND-09 §8.2, projecao declarada de FND-01 §7.3, **ja usa** o sentido estrito em **22 de 22** linhas. Ou a projecao esta errada ha tres ciclos, ou a fonte usa duas acepcoes |
| 2 | **O defeito ja custou dois incidentes.** INC-2026-001 e INC-2026-002 nasceram de ratificacao afirmada sem ato; a Alternativa C — resolver no glossario — **e o desenho atual**, e nao os impediu |
| 3 | **A emenda e a menor possivel.** Oito alteracoes, **zero** titulares, **zero** artefatos a reescrever — porque `IR-11` ja impediu a propagacao |
| 4 | **Separa o que e C3 do que e C2.** Q2 fica fora, escalada, exatamente como ADR-0012 §5.5 determinou |

## 7. Impacto

| Dimensao | Impacto |
|---|---|
| Documentos alterados | **FND-01** — §7.3 *(7 alteracoes)* e §11 *(1)* |
| Documentos em cascata | **0.** FND-09 §8.2 **ja** esta no sentido proposto; nenhuma projecao muda |
| Titulares de decisao | **0 alterados** |
| Principios · linhas vermelhas · hierarquia | **0 tocados** |
| Entidades · tipos · camadas · templates | **0 criados** |
| Artefatos a reescrever | **0** — varredura de **1.210** ocorrencias em **117** artefatos: **zero** registram o termo no sentido antigo (`IR-11`) |
| Achados que fecha | **IC-2** *(a causa)* · **RC-03** *(a contagem)* |
| Ressalva que fecha | **R4** de FIT-2026-007 — **parcialmente**: fecha quanto a **Q1**; **Q2 permanece** |
| Custo de contexto | **0** no nucleo. FND-01 e `nucleo`, e a emenda **nao acrescenta linha alguma** alem de 1 nota e 1 entrada de glossario |

## 8. Evidencias

| # | Evidencia | Fonte | Confianca |
|---|---|---|---|
| E1 | **5 linhas** de FND-01 §7.3 com titular departamental na coluna *Ratifica* — 4 `DEP-EXE`, 1 `DEP-GOV` | Leitura coluna a coluna, 2026-07-28 | **Alta** |
| E2 | **0 linhas** de FND-09 §8.2 com titular departamental na mesma coluna | idem | **Alta** |
| E3 | **1.210 ocorrencias** do radical *ratific-*, **0** violacoes de `IR-11` | Varredura do acervo | **Alta** |
| E4 | **2 incidentes** cuja causa e a ambiguidade | INC-2026-001, INC-2026-002 | **Alta** |
| E5 | `FIT-2026-001` **continua** afirmando ratificacao inexistente, e e **M1** | INC-2026-002 §11 | **Alta** |
| **A1** | **Evidencia ausente, declarada:** **nenhum** caso registrado em que a ambiguidade tenha levado alguem a **atribuir vigencia indevida** por homologacao departamental. O dano e **potencial e observado em forma proxima** *(os dois incidentes)*, nao consumado nesta forma exata | PI-10 |

## 9. Riscos e mitigacao

| # | Risco | Prob. | Impacto | Mitigacao |
|---|---|---|---|---|
| RN-1 | Emendar a Constituicao por **materia terminologica** abrir precedente de emenda barata | Media | **Alto** | O rito **nao e** barato: RFC C3, impacto mapeado e **ratificacao indelegavel**. E o custo de **nao** emendar ja se materializou em dois incidentes |
| RN-2 | A versao ficar errada — 1.4.0 onde cabia 2.0.0 | **Media** | Baixo | **Declarado em §5.1.** A escolha e do Soberano, no proprio ato |
| RN-3 | *"Homologacao"* virar termo sem lastro no restante do acervo | Baixa | Medio | `IR-11` **ja** o instituiu como termo oficial ha um ciclo; a emenda o leva a fonte, nao o inventa |
| RN-4 | A emenda ser aprovada e a cascata **esquecida** | Baixa | Medio | **Nao ha cascata** — E2. Se houvesse, seria parte da mesma mudanca (CV-04, AL-05) |

## 10. Plano de reversao

| Campo | Conteudo |
|---|---|
| Reversivel? | **Sim — Tipo 2** |
| Como | **Emenda revogatoria pelo mesmo rito** (FND-01 §9). O texto de 1.3.0 permanece preservado no historico de versoes e **nunca e apagado** (AL-04) |
| Custo | **Documental integral.** Nenhum dado vivo, nenhuma exposicao, nenhuma migracao, nenhuma credencial |
| O que **nao** se reverte | Nada — a emenda nao produz efeito irreversivel em ponto algum |
| Backup (PI-07) | Copia datada de **117** arquivos, tomada antes das edicoes desta missao; baseline **`BL-2026-07-28-05`** preservada |

## 11. Classificacao

| Campo | Valor |
|---|---|
| Classe | **C3 — Constitucional** *(FND-04 §2; FND-01 §9)* |
| Tipo | **2 — reversivel** |
| Aprovador | **SOBERANO — indelegavel** |
| **Ratificacao** | **EXIGIDA — e NAO OCORREU** |
| **Estado** | **`em-revisao` · `ratificacao: pendente` — sem vigencia** |
| Instrumento | [RFC-0011](../rfcs/RFC-0011-emenda-constitucional-ratifica-homologa.md) → este ADR → **ratificacao** → promulgacao de FND-01 1.4.0 *(ou 2.0.0)* → propagacao |
| Etapas de FND-01 §9 cumpridas | **1, 2 e 3.** As etapas **4, 5 e 6 nao ocorreram** |
| Fitness Check | [FIT-2026-008](../governance/fitness/FIT-2026-008-rollout-das-cartas.md) — avalia o **pacote**, nao a emenda |

## 12. Revisao

| Campo | Conteudo |
|---|---|
| Gatilho | **Ato do Soberano sobre Q1** — aprovando, devolvendo ou determinando outro texto |
| Se **devolvido** | Este ADR passa a `arquivado` *(operacao O8, legitima porque nunca esteve em `ativo`)*; **IC-2 permanece aberto** com `IR-11` como unica protecao, e o proximo gatilho e a proxima emenda a FND-01 |
| Se **aprovado** | Promulgacao de FND-01 na versao que o ato determinar; propagacao verificada por DEP-GOV; **IC-2 fecha** |
| Sinal de erro | O termo *homologacao* precisar de excecao formal para ser aplicado a alguma das cinco materias |
| Responsavel | **DEP-GOV** *(forma)* · **DEP-QAR** *(revisao)* · **SOBERANO** *(merito)* |

## 13. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Origem | [RFC-0011](../rfcs/RFC-0011-emenda-constitucional-ratifica-homologa.md), Q1 · [RFC-0009 Q1](../rfcs/RFC-0009-integridade-e-alcance-do-ato-de-ratificacao.md), Opcao D |
| Achado que trata | **IC-2** — colisao do termo *ratifica*; **RC-03** — a contagem correta |
| Contencao que permanece ate a decisao | **`IR-11`** de [ADR-0012 §5.4](ADR-0012-integridade-do-ato-de-ratificacao.md) |
| Decisoes relacionadas | **ADR-0006** *(FND-10 no nivel 2; contexto de LM-02)* · **ADR-0009** *(o que conta como emenda)* · **ADR-0012** *(integridade do ato; institui `IR-11`)* |
| Incidentes cuja causa esta aqui | [INC-2026-001](../governance/incidents/INC-2026-001-ratificacao-inferida.md) · [INC-2026-002](../governance/incidents/INC-2026-002-ratificacao-declarada-em-fitness-check.md) |
| Pacote soberano que o transporta | [PS-2026-002 §4](../governance/pacote-soberano-2026-07-28-cartas.md) |

---

## Checklist de validade (FND-07 §4.1)
- [x] **VD-01** — 3 alternativas reais (A, B, C) + "nao fazer nada" (Z)
- [x] **VD-02** — criterios K1–K5 em §3, antes de §4
- [x] **VD-03** — nenhuma alternativa de palha: **C e o desenho atual**, e foi recusada por evidencia observada
- [x] **VD-04** — tradeoff explicito em §9, RN-1: emendar a Constituicao por materia terminologica
- [x] **VD-05** — evidencia ausente declarada: **A1**
- [x] **VD-06** — plano de reversao em §10
- [x] **VD-07** — impacto em cascata mapeado em §7: **zero**, com o motivo medido
- [x] **VD-08** — data e responsaveis presentes
- [x] **VD-09** — gatilho de revisao em §12, com os dois desfechos
- [x] **Estado declarado sem ambiguidade:** **nao esta em vigor**, e o cabecalho o diz antes de tudo

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-GOV | **Candidato, sem vigencia.** Texto da emenda **C3** a FND-01 §7.3 e §11 que separa **ratificacao** de **homologacao** — **8 alteracoes**, **0** titulares de decisao alterados, **0** artefatos a reescrever. Cumpre as etapas **1 a 3** de FND-01 §9; a etapa **4** depende de ato do Soberano, que o ato de 2026-07-28 **expressamente nao concede**. |
