---
id: RFC-0021-admissao-do-medally-como-primeiro-produto
titulo: O medAlly deve ser admitido como o primeiro Produto do acervo, ou a via S1 deve esperar pelo nXtrack que o Soberano nomeou?
tipo: rfc
versao: 1.0.0
status: aprovado
camada_memoria: estrategica
autor: DEP-PRD
proprietario: DEP-PRD
aprovador: DEP-GOV
criado_em: 2026-07-31
atualizado_em: 2026-07-31
revisao_prevista: 2027-01-31
decisoes_relacionadas: [ADR-0007, ADR-0021, ADR-0022]
substitui: []
substituido_por: null
classe_mudanca: C2
prazo_analise: 2026-08-31
resumo: Submete ao Soberano a escolha do primeiro Produto do acervo entre medAlly, nXtrack e adiar, com evidencia medida sobre um candidato e ausencia declarada sobre o outro.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# RFC-0021: Admissao do medAlly como primeiro Produto

> **Pergunta em uma frase.** `RD-33` e a **unica pendencia bloqueante do acervo** ha quatro
> missoes, e a via de desbloqueio `S1` exige **um Produto real**. Existe **um** candidato com
> evidencia medida — o **medAlly** — e o Soberano ja nomeou **outro** — o **nXtrack** — como
> a via futura, **sob condicao**. Esta RFC pergunta **qual deles nasce primeiro**, e submete a
> escolha com a assimetria de evidencia declarada em voz alta.

## Proposito

Submeter a analise a admissao do medAlly como `PRO-medally`, primeiro Produto do LucaX
Enterprise OS, pelo portao de [ADR-0007 §5.3](../decisions/ADR-0007-fronteira-greenfield-legado.md).
A proposta e de **onboarding de governanca**: admite-se **identidade e proposta** de um produto
que ja existe fora do acervo, **nunca o seu conteudo**.

## Escopo

| Item | Definicao |
|---|---|
| **Inclui** | A escolha do primeiro Produto; a aplicacao cumulativa de `G1`–`G5` ao candidato medAlly; a classificacao `G3`; a avaliacao de **se `G1`–`G5` bastam** no primeiro caso real *(§12 de `ADR-0007` manda reavalia-los aqui)*; e a colisao com a decisao **7** de [PT-2026-009 §1](../governance/relatorio-transicao-2026-07-30-convergencia.md) |
| **Nao** inclui | O **merito tecnico** do medAlly · qualquer conteudo do seu repositorio · a criacao de `Spec`, `Projeto`, `Skill`, `Tool`, `Command`, `Workflow`, `Agente`, codigo ou infraestrutura · **o inventario do nXtrack ou de qualquer outro produto**, proibido por `FR-07` · a resolucao de `RD-33`, que **so fecha apos vigencia** |
| **Subordinado a** | [FND-01 §7.3](../foundation/01-constituicao.md) *(portfolio: decide o Soberano)* · [FND-03 §3.1](../foundation/03-taxonomia.md) · [FND-04 §2 e §6](../foundation/04-governanca.md) · [FND-09 §5.6 e §8.2](../foundation/09-meta-model.md) · [FND-10 §5.4](../foundation/10-artifact-framework.md) · [FND-11 §13](../foundation/11-framework-specifications.md) |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| Proponente | **DEP-PRD** | `FND-09 §8.2`, linha `PRO` — *propoe/cria* |
| Areas que devem se manifestar | **DEP-EXE** e **DEP-PRD** | `FND-01 §7.3`, linha *Portfolio* — **consulta obrigatoria** |
| Revisor independente | **DEP-QAR** | `AC-03`; `G4` de `ADR-0007 §5.3` |
| Validacao de forma | **DEP-GOV** | `FND-09 §8.2`, linha `RFC` |
| Decide a materia | **SOBERANO** | `FND-01 §7.3` — *Portfolio: criar/encerrar produto* |
| Prazo de manifestacao | **2026-08-31** | — |

---

## 1. Situacao atual — fatos verificaveis

| # | Fato | Medido em |
|---|---|---|
| 1 | **`0` Produtos existem.** `products/` **nao existe** na raiz do acervo | 2026-07-31, varredura |
| 2 | **`0` `Spec`s existem**, e **nenhuma e criavel**: `FND-04 §6` exige *"Produto existe"* | `FND-11 §13` |
| 3 | **`RD-33` e a unica pendencia bloqueante do acervo**, aberta desde a Missao 1.12 | `PT-2026-010 §7` |
| 4 | As duas vias sao **disjuntas e ambas do Soberano**: **`S1`** *(ato que crie o primeiro Produto)* e **`S2`** *(RFC `C3` → ADR `C3` → ato)* | `ADR-0021 §7.3`, `FND-11 §13` |
| 5 | **O Soberano ja fixou a via:** *"`S1` com Produto real — **`nXtrack`, se seguir sendo o primeiro produto comercial**"*; **`S2` deferida** | [PS-2026-013 §7](../governance/pacote-soberano-2026-07-30-consolidado.md), decisao **7** de [PT-2026-009 §1](../governance/relatorio-transicao-2026-07-30-convergencia.md) |
| 6 | O portao de admissao de origem externa existe desde 2026-07-28 e **nunca foi exercido**: `0` candidatos submetidos | `ADR-0007`; §8 do proprio ADR declara a ausencia |
| 7 | `ADR-0007 §12` fixa como **gatilho de revisao por evento** o *"primeiro candidato real submetido ao portao — reavaliar se `G1`–`G5` sao suficientes e conferiveis na pratica"* | `ADR-0007 §12` |
| 8 | `ADR-0007 §12` fixa como **sinal de que a decisao deu errado**: *"nenhum candidato submetido ate a segunda revisao estrutural, com o Legacy em uso"* — sinal de que **o portao esta sendo contornado** | idem |

## 2. Problema

**O acervo tem uma norma completa sobre Produto e nenhum Produto, e uma norma completa sobre
`Spec` e nenhuma `Spec`.** `FND-11` entrou em vigor em 2026-07-30 com `SF-01` a `SF-32`
**determinados e nao observados** — nenhuma das 32 regras foi exercida contra um caso real
(`A2` de `FIT-2026-018`). O mesmo vale para o portao de `ADR-0007`: cinco condicoes escritas
antes do primeiro candidato, **nunca aplicadas**.

**A consequencia de manter o estado:** duas camadas normativas inteiras continuam validadas
apenas por construcao. E o proprio `ADR-0007 §12` declara que **a ausencia prolongada de
candidato e sinal de que o portao esta sendo contornado**, nao de que ele funciona.

**Quem perde:** o acervo, que carrega norma ociosa; e o produto real que existe hoje fora dele,
sem existencia formal, sem dono declarado e sem criterio de encerramento registrado.

## 3. Pergunta de decisao

**Qual objeto exerce `S1`: o medAlly agora, o nXtrack primeiro, ou nenhum dos dois ainda?**

E, subordinada a ela: **`G1`–`G5` bastam no primeiro caso real, ou o portao precisa de emenda
antes da segunda admissao?**

## 4. Criterios de avaliacao

> Declarados antes do exame das opcoes (`CD-01`, `VD-02`).

| # | Criterio | Peso | Como se mede |
|---|---|---|---|
| `K1` | **O candidato passa no teste de existencia de `FND-03 §3.1`** — se descontinuado, alguem perde algo | **Bloqueante** | Resposta com quem, o que e de que natureza |
| `K2` | **Publico, problema e valor comprovados, nao alegados** | **Bloqueante** | Evidencia separada em observado / alegado / inferido / desconhecido |
| `K3` | **Criterio de sucesso e de encerramento declaraveis hoje** | **Bloqueante** | `FND-04 §6`, linha *Produto* |
| `K4` | **Nenhum conteudo externo entra no acervo** | **Bloqueante** | Bytes admitidos = `0`; `FR-03`, `FR-07` |
| `K5` | Custo e reversibilidade | Alto | Arquivos do acervo alterados; custo de desfazer |
| `K6` | **Coerencia com a decisao ja fixada pelo Soberano** | Alto | A decisao **7** e satisfeita, contrariada ou **condicionada** |
| `K7` | Desbloqueia `RD-33` | Medio | `SF-23` item (9) passa a ser satisfazivel |

## 5. Opcoes

### Opcao A — **medAlly agora** *(recomendada)*

| Campo | Conteudo |
|---|---|
| Descricao | O Soberano cria `PRO-medally` por ato `C2 · Tipo 1`, sobre a Carta candidata e o `ADR-0026`. **Nada do repositorio entra**; a classificacao `G3` e **`REWRITE`**, e a Carta nasce **`native`** |
| A favor | **Unico candidato com evidencia medida.** Publico nomeado com entrevista real; problema formulado por quem o tem; **7** portoes fechados e **37 de 37** trilhas em `simulacao`, medidos nesta missao. Exerce o portao de `ADR-0007` pela primeira vez e **satisfaz o gatilho de §12**. Desbloqueia `RD-33` sem tocar `FND-04 §6` |
| Contra | **Contraria a leitura literal da decisao 7**, que nomeia o nXtrack. O publico primario tem **um** membro. **Zero** criterios de sucesso medidos. O produto **nao atende paciente real** e pode nunca atender, se um dos sete portoes receber negativa |
| Custo | **5** artefatos novos no acervo *(1 RFC, 1 ADR, 1 pacote, 1 `FIT`, 1 relatorio)*, **1** Carta candidata fora dele, **`0`** bytes no repositorio do medAlly, **`0`** fontes normativas emendadas |
| Risco | A Carta ser lida como autorizacao de operacao real *(`R2` da Carta)*; admissao por atacado do repositorio *(`R3`)* |
| Quem e afetado | DEP-PRD *(dono)*, DEP-QAR *(revisao e veto)*, DEP-ENG, DEP-OPS, DEP-GRW *(responsabilidade declarada, nao exercida)* |
| Avaliacao | `K1` ✔ · `K2` ✔ · `K3` ✔ · `K4` ✔ · `K5` ✔ · `K6` **condiciona** · `K7` ✔ |

### Opcao B — **nXtrack primeiro**

| Campo | Conteudo |
|---|---|
| Descricao | Adiar o medAlly e submeter o nXtrack ao portao, cumprindo a decisao **7** ao pe da letra |
| A favor | **Coerencia literal com a decisao ja fixada pelo Soberano** *(`K6` ✔ pleno)*. Se o nXtrack for o primeiro produto **comercial**, ele traz o que falta ao medAlly: publico pagante, receita e um criterio de sucesso mensuravel hoje |
| Contra | **`K1`, `K2` e `K3` sao `desconhecido`.** Esta missao **nao inventariou o nXtrack e nao podia**: `FR-07` opera sobre **um candidato por vez, nomeado**, e o candidato nomeado e o medAlly. **Nao ha uma unica evidencia medida** sobre publico, problema, valor, estagio ou sinal de uso do nXtrack neste documento — e produzi-la exige **outra missao**, com o nXtrack nomeado |
| Custo | **Uma missao inteira de evidencia**, mais o rito. `RD-33` permanece bloqueante nesse intervalo |
| Risco | **Alto e assimetrico:** adiar por um candidato sobre o qual nada se mediu e trocar evidencia por expectativa. Se o nXtrack nao passar no teste de existencia, o acervo perde duas missoes |
| Quem e afetado | O acervo *(`RD-33` segue bloqueante)*; o medAlly *(segue sem existencia formal)* |
| Avaliacao | `K1` **desconhecido** · `K2` **desconhecido** · `K3` **desconhecido** · `K4` ✔ · `K5` ✔ · `K6` ✔ · `K7` **adiado** |

> **Esta opcao nao e de palha, e e importante que nao seja lida como tal.** Ela e a **unica**
> que cumpre a decisao 7 literalmente, e o seu unico defeito e **a ausencia de evidencia — que
> e ausencia desta missao, nao do nXtrack**. Se o Soberano souber, do nXtrack, o que esta RFC
> nao pode saber, **B vence A**.

### Opcao C — **Admitir os dois na mesma decisao**

| Campo | Conteudo |
|---|---|
| Descricao | Um unico ato cria `PRO-medally` e `PRO-nxtrack` |
| A favor | Resolveria a colisao entre A e B sem escolher |
| Contra | **Falha `K2` e `K4`.** Exigiria evidencia do nXtrack que nao existe, e obteve-la agora seria **inventario previo**, expressamente proibido por `FR-07`: *"o portao opera sobre um candidato por vez, nomeado; levantamento amplo previo e proibido"*. Alem disso viola a restricao expressa desta missao |
| Custo | Duas Cartas, duas evidencias, uma delas inexistente |
| Risco | **Institui o precedente que `ADR-0007` existe para impedir:** admissao em bloco |
| Avaliacao | `K2` **falha** · `K4` **falha** — **recusada** |

### Opcao Z — **Nao fazer nada**

| Campo | Conteudo |
|---|---|
| Consequencia de manter o estado atual | `RD-33` segue bloqueante; `SF-01` a `SF-32` seguem determinados e nao observados; `G1`–`G5` seguem sem exercicio |
| Custo da inacao | **Ele ja esta escrito na propria norma que se quer preservar:** `ADR-0007 §12` declara que *"nenhum candidato submetido ate a segunda revisao estrutural, com o Legacy em uso"* e **sinal de que o portao esta sendo contornado, nao respeitado**. O Legacy **esta em uso** — **19** commits em cinco dias, medidos nesta missao |
| Por que nao venceu | Adiar sem candidato nomeado nao produz informacao nova. **A duvida entre A e B se resolve com evidencia; Z nao produz nenhuma** |

## 6. Recomendacao do proponente

**Opcao A**, com a decisao **7** tratada como **condicao satisfeita por mudanca de fato**, e nao
como norma contrariada.

O texto da decisao 7 e literal: *"`nXtrack`, **se seguir sendo o primeiro produto comercial**"*.
**A condicao esta escrita no proprio registro**, e ela pergunta sobre **precedencia comercial**,
nao sobre precedencia de admissao. Duas leituras cabem, e **so o Soberano pode escolher entre
elas**:

| Leitura | Consequencia |
|---|---|
| **L1** — a condicao e sobre o nXtrack ser o primeiro produto **comercial** | Nada impede que o **primeiro Produto do acervo** seja outro. A decisao 7 fica **intacta**, e `PRO-nxtrack` nasce quando houver evidencia |
| **L2** — a decisao 7 fixou o nXtrack como o primeiro Produto **do acervo** | A Opcao A **contraria decisao vigente do Soberano**, e so um ato dele pode altera-la |

**DEP-PRD recomenda `L1` e a Opcao A**, e **declara que a escolha entre `L1` e `L2` nao lhe
pertence.** Esta e a questao `Q1` de §9 — a unica bloqueante desta RFC.

## 7. Impacto previsto

| Dimensao | Impacto |
|---|---|
| Departamentos | **DEP-PRD** passa a ter Produto sob custodia — **o primeiro**. **DEP-QAR**, **DEP-ENG**, **DEP-OPS** e **DEP-GRW** recebem responsabilidade **declarada e nao exercida** |
| Componentes | **+1 Produto.** `products/medally/` nasce. **Nenhum outro componente** |
| Normas afetadas | **`0` fundacionais emendadas.** Nenhum artigo de `FND-01` a `FND-11` muda uma linha |
| Entidades e tipos novos | **`0`** — `PRO` e entidade `E-17` e tipo documental **ja existentes**; a cardinalidade sai de `0..n` **sem instancia** para `1` |
| Camadas de memoria | **PRD** *(definicao, personas, hipoteses)*; **APR** *(a licao do primeiro exercicio do portao)* |
| Diretorios novos | **1** — `products/`, ja previsto por `FND-03 §3.1` e `FND-09 §5.6`. **Nao e diretorio novo na norma; e a primeira instancia do que a norma ja declarava** |
| `RD-33` | **Passa a ser fechavel** — e **so fecha apos vigencia**, nunca por esta RFC nem pelo ADR |
| Ganho `PI-14` pretendido e sinal que o comprova | **Organizacao.** Sinal ja observado: **`0` de 32 regras de `FND-11` exercidas** e **`0` de 5 condicoes de `ADR-0007 §5.3`** exercidas — duas camadas normativas sem um unico caso real |

## 8. Riscos

| # | Risco | Impacto | Mitigacao |
|---|---|---|---|
| `RR-1` | **A decisao 7 ser contrariada sem que o Soberano perceba** | **Alto** | `Q1` de §9 e **bloqueante**; a minuta do ato a enuncia expressamente |
| `RR-2` | **A admissao ser lida como porta aberta para o repositorio inteiro** | **Alto** | `G3` = **`REWRITE`**: **nada entra**. `FR-07`: cada admissao futura tem portao proprio |
| `RR-3` | **Um Produto com publico de um so nao ser Produto** | Medio | Teste de existencia aplicado e **passado pelo motivo mais fraco**, com a fragilidade declarada; `H1` da Carta a testa com prazo |
| `RR-4` | **`G1`–`G5` nao bastarem, e ninguem notar** | Medio | §12 de `ADR-0007` **obriga** reavalia-los neste caso; a avaliacao esta em §9, `Q2` |
| `RR-5` | **O ato criar Produto e alguem entender que criou `Spec`** | Medio | A minuta declara em item proprio que **nenhuma `Spec` nasce**, e que `RD-33` **so fecha apos vigencia** |

## 9. Perguntas em aberto

| # | Questao | Quem responde | Bloqueia? |
|---|---|---|---|
| **`Q1`** | **A decisao 7 fixou o nXtrack como primeiro produto *comercial* (`L1`) ou como primeiro Produto *do acervo* (`L2`)?** | **SOBERANO** | ✅ **SIM** — sob `L2`, a Opcao A e inadmissivel sem ato que altere a decisao 7 |
| **`Q2`** | **`G1`–`G5` bastam?** A resposta medida desta missao e **quase**: os cinco foram conferiveis, e **duas lacunas apareceram** — (a) o portao **nao distingue admitir *identidade* de admitir *conteudo***, e foi preciso inventar a distincao para nao admitir 550 arquivos por atacado; (b) `G3` oferece **quatro** classificacoes pensadas para **conteudo**, e nenhuma delas descreve com precisao *"admitir a existencia de um produto sem admitir nada dele"* — **`REWRITE` foi a mais proxima, por eliminacao** | **SOBERANO**, sobre emendar ou nao `ADR-0007` | ❌ Nao — a admissao e possivel com `REWRITE` declarado |
| **`Q3`** | O `aprovador` do ADR de criacao e **DEP-EXE** *(regra de classe, `FND-07 §2.4`)* ou **SOBERANO** *(materia de portfolio, `FND-01 §7.3`; linha `PRO` de `FND-09 §8.2`)*? | **SOBERANO** | ❌ Nao — o candidato declara **SOBERANO**, a autoridade **mais alta**, por `GV-03` |
| **`Q4`** | O estagio `construcao` e o correto para um produto que roda, mas com **`0`** usuarios reais? | **SOBERANO**, com parecer de DEP-PRD | ❌ Nao |

## 10. Manifestacoes

| Area | Posicao | Fundamento | Data |
|---|---|---|---|
| **DEP-PRD** | **apoia** a Opcao A sob `L1` | Proponente; §6 | 2026-07-31 |
| **DEP-QAR** | **apoia com ressalva** | Revisao independente em [PS-2026-014 §5](../governance/pacote-soberano-2026-07-31-medally.md): a evidencia do candidato reproduz, e a ressalva e `RR-3` — publico de um so | 2026-07-31 |
| **DEP-GOV** | **apoia quanto a forma; nao se manifesta sobre o merito** | `FND-04 §3` — o Guardiao **nao julga merito de conteudo**. Forma conferida: classe, rito, instrumento, contrato e rastreabilidade | 2026-07-31 |
| **DEP-EXE** | **consulta obrigatoria — nao registrada** | `FND-01 §7.3` exige consulta a DEP-PRD **e** DEP-EXE. **DEP-EXE nao se manifestou**, e a ausencia e **declarada, nao suprida** *(`PI-10`, `LM-03`)* | — |
| **SOBERANO** | *(nao ocorrido)* | — | — |

## 11. Resultado

| Campo | Conteudo |
|---|---|
| Decisao | **aceita, quanto a forma** — gera `ADR-0026`, que **nao entra em vigor** sem ato |
| ADR gerado | [`ADR-0026`](../decisions/ADR-0026-admissao-do-medally-como-primeiro-produto.md) — `em-revisao`, `ratificacao: pendente` |
| Se rejeitada, por que | *(nao rejeitada)* |
| Se adiada, ate quando e sob qual condicao | **A materia esta adiada de fato ate o ato soberano.** `Q1` e bloqueante |
| Data | 2026-07-31 |
| Responsavel | DEP-PRD, com validacao de forma por DEP-GOV |

---

## Checklist de validade

| # | Item | Estado |
|---|---|---|
| 1 | Pergunta clara | ✅ §3 |
| 2 | Alternativas analisadas — **3 reais + "nao fazer nada"** | ✅ A, B, C, Z |
| 3 | Nenhuma alternativa de palha | ✅ B e a decisao **ja fixada pelo Soberano**, e §5 declara em que hipotese ela vence |
| 4 | Criterios antes das opcoes | ✅ §4 antes de §5 |
| 5 | Recomendacao obrigatoria presente | ✅ §6 *(`EC-03`)* |
| 6 | Prazo de analise definido | ✅ 2026-08-31 |
| 7 | Evidencia ausente declarada | ✅ §5 Opcao B; §10 linha DEP-EXE |
| 8 | Impacto mapeado | ✅ §7 |
| 9 | `revisor` ≠ `autor` | ✅ DEP-PRD × DEP-QAR |
| 10 | Nenhuma entidade, tipo, camada ou norma criada | ✅ §7 |

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-31 | DEP-PRD | Proposta inicial. **Tres opcoes reais** — medAlly agora, nXtrack primeiro, ambos — mais *"nao fazer nada"*. Recomenda a **Opcao A** sob a leitura `L1` da decisao 7, e **declara que a escolha entre `L1` e `L2` e do Soberano** (`Q1`, bloqueante). Registra as **duas lacunas medidas** de `G1`–`G5` (`Q2`) e a **ausencia de manifestacao de DEP-EXE**. |
