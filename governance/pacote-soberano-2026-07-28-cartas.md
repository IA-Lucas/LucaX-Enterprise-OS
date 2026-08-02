---
id: PS-2026-002
titulo: Pacote de decisao soberana — cinco Cartas de Departamento e a emenda constitucional candidata
tipo: relatorio
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: null
decisoes_relacionadas: [ADR-0011, ADR-0012, ADR-0013, ADR-0014]
substitui: []
substituido_por: null
canal: REPORTE
emissor: DEP-GOV
destinatario: SOBERANO
ttl: ate decisao do Soberano
resumo: Reune, para decisao do Soberano, as cinco Cartas de Departamento em em-revisao e a emenda constitucional candidata, com ID, versao, hash, riscos e recomendacao por objeto.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# PS-2026-002 — Pacote de decisao soberana

> ## Este pacote **informa**. Nao decide, nao aprova e nao antecipa.
>
> Aprovar e ratificar Carta de Departamento e ato **exclusivo e indelegavel do SOBERANO**
> (DC-09, FND-09 §8.2, PI-01). Enquanto o ato nao ocorrer, as cinco Cartas permanecem em
> `em-revisao` · `ratificacao: pendente`, e **nao produzem nenhum efeito** (LM-02).
>
> **Caminho exato deste pacote:** `governance/pacote-soberano-2026-07-28-cartas.md`.
> *(Cumprimento do achado **RE-01**: o pedido de decisao anexa o caminho, alem do ID.)*

## Proposito
Reunir em **um unico lugar** tudo o que o Soberano precisa para decidir sobre os objetos que
esta missao produziu e **nao pode** colocar em vigor por si.

## Escopo
| Item | Definicao |
|---|---|
| Inclui | **5** Cartas de Departamento em `em-revisao` · **1** emenda **C3** candidata a FND-01 · **1** questao **C2 escalada** sobre `FIT` |
| **Nao** inclui | O que **ja** foi decidido pelo ato de 2026-07-28 *(`DEP-QAR` 1.1.0 e o criterio de consolidacao)* · o que **nao** depende do Soberano *(ADR-0013, C2/Tipo 2, ja vigente)* |
| Natureza | **Reporte**, tipo documental de [FND-10 §4.6](../foundation/10-artifact-framework.md), entidade `MSG`. Nenhum tipo, entidade ou camada novo |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| **Autor das Cartas** | **DEP-EXE** | FND-09 §8.2, linha `DEP` |
| **Revisor independente** | **DEP-GOV** *(quatro Cartas)* · **DEP-QAR** *(Carta de `DEP-GOV`)* | RM-06b — quem e objeto nao revisa |
| **Monta este pacote** | **DEP-GOV** | Guardiao normativo; nao produziu as Cartas |
| **Revisa este pacote** | **DEP-QAR** | AC-03 |
| **DECIDE** | **SOBERANO** | **Indelegavel.** Nao ocorreu |

---

## 1. O que se pede, em uma tabela

| # | Objeto | Tipo de ato pedido | Se **nao** houver ato |
|---|---|---|---|
| **1** | As **cinco** Cartas de Departamento | **Aprovacao e ratificacao**, por Carta ou em bloco | As cinco ficam em `em-revisao`. **A cobertura documental permanece 9/9; a cobertura vigente permanece 4/9** |
| **2** | **ADR-0014** — emenda **C3** a FND-01 §7.3 | **Ratificacao**, ou devolucao | **IC-2 permanece contido por `IR-11`**, quinto ciclo. Nada quebra |
| **3** | **Q2 de RFC-0009** — `FIT` exige ratificacao? | **Determinacao** de qual leitura prevalece | **G1/G2 permanece aberta.** `FIT-2026-001` continua com o registro incorreto **contido, nao corrigido** |

> **Os tres sao independentes.** Decidir um nao obriga a decidir os outros, e **nao decidir e
> resultado valido** — cada linha declara o que acontece nesse caso.

## 2. As cinco Cartas — ID, versao, hash, Capability, revisao, riscos e recomendacao

> Hashes conforme [ADR-0012 §5.2, IR-07](../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md):
> **H-A** = `sha256` do arquivo **tal como submetido**; **H-N** = conteudo normativo, invariante
> sob a transicao de estado. Reproduzir: `sha256sum departments/<dep>/carta.md`.

### 2.1 `DEP-GOV` — Governanca e Conformidade *(Guarda)*

| Campo | Conteudo |
|---|---|
| **ID · versao** | `DEP-GOV` · **1.0.0** |
| **H-A** | `508c4c56f18f8096fdfbe0c418018a83f8b65bd48cbfc2242d1fd32046d0227f` |
| **H-N** | `3523bd0966d5450851d04e74d97638911b985f930b6c2e61c24d7fb7fbc27784` |
| **Linhas** | **457** |
| **Capabilities** | **Custodia 1:** `CAP-governanca` *(DIR · `nucleo`)*. **Exerce 1.** Nenhuma exercida sem custodiar |
| **Revisao independente** | **DEP-QAR** — desvio declarado: DEP-GOV e **objeto** e nao pode revisar o instrumento que define a propria autoridade |
| **Conformidade ao contrato** | **12 de 12 blocos** · **11 de 11 testes** ✅ · `B4 × B9` conferida sob o checklist **1.2.0** · nenhum conteudo proibido de ADR-0011 §5.4 |
| **Riscos declarados** | **6** — RG-1 a RG-6. Dois **observados**: o ponto cego da auditoria *(4 ocorrencias)* e a concentracao de papeis criticos *(5 ocorrencias)* |
| **Ressalvas** | **Cinco gatilhos de especializacao dispararam** e a decisao foi **manter**, porque os movimentos corretivos exigem **criar agente** *(proibido)* ou alterar FND-09 §8.2 *(C3)*. Custo declarado em §12.1 |
| **O que esta Carta fecha** | **IC-4** *(dois papeis criticos sem Carta)* · **RE-03**, declarado em **I-2** — a condicao unica de saida do rollout de FIT-2026-007 |
| **O que ela abre** | **RC-04** — DEP-GOV tem **11** responsabilidades exclusivas, nao 7; a contagem de P7 estava para menos |
| **RECOMENDACAO** | **APROVAR** |
| **Por que** | E a **quinta Carta**, escrita sozinha, exatamente como a Condicao 1 de FIT-2026-006 determinou. **Declara em B9 o impedimento que RE-03 exigia** e o que RC-02 expos. Enquanto ela nao vigorar, DEP-GOV continua exercendo **cinco** papeis criticos sem instrumento que declare os proprios limites |

### 2.2 `DEP-TLS` — Ferramentas e Integracoes *(Plataforma)*

| Campo | Conteudo |
|---|---|
| **ID · versao** | `DEP-TLS` · **1.0.0** |
| **H-A** | `2ce3ea2493d06cf144fd88614d524d6ec479b3499ab62be6c0570d0e52794616` |
| **H-N** | `716f363a96a51d521ca9a2c589f22fa73f12d81eb90d772daf1801bed93e9858` |
| **Linhas** | **424** |
| **Capabilities** | **Custodia 1:** `CAP-integracao` *(SUS · `habilitadora`)*. **Exerce 1** |
| **Revisao independente** | **DEP-GOV** |
| **Conformidade ao contrato** | **12 de 12 blocos** · **11 de 11 testes** ✅ · nenhum conteudo proibido |
| **Riscos declarados** | **6** — RT-1 a RT-6. Um **observado**: **DEP-TLS nao registrou nenhum ato no acervo** (RT-5, KT-7 = 0) |
| **Ressalvas** | **Zero gatilhos de especializacao com sinal** — e o motivo e o proprio RT-5: nao ha exercicio de que extrair sinal |
| **O que esta Carta trata** | **P4** *(operar sob politica ≠ custodiar a politica)* · **IC-7** *(fusao KMS+TLS)*, reavaliada com **metade do motivo removido** |
| **RECOMENDACAO** | **APROVAR** |
| **Por que** | **Completa a classe Plataforma** e e a unica area com mandato sobre **acesso e segredo por referencia** — materia de PI-08 e LV-02. Sem Carta, o improviso de acesso que ela existe para impedir **nao tem instrumento que o proiba nominalmente**. E a Carta com **menos exercicio comprovado do sistema**, e isso esta declarado, nao maquiado |

### 2.3 `DEP-PRD` — Produto e Estrategia *(Linha)*

| Campo | Conteudo |
|---|---|
| **ID · versao** | `DEP-PRD` · **1.0.0** |
| **H-A** | `b3cd0f06b530e9aeeedd535472e8aec0ace03494633534acc6f1aed03cd2349b` |
| **H-N** | `1af73b7feaad38a162cc6960bb346caed1f554f6b39ce4c5b4d92ccae3128543` |
| **Linhas** | **429** |
| **Capabilities** | **Custodia 3:** `CAP-produto` *(`nucleo`)*, `CAP-pesquisa`, `CAP-design` — **o dominio `VAL` inteiro**. **Exerce 3** |
| **Revisao independente** | **DEP-GOV** |
| **Conformidade ao contrato** | **12 de 12 blocos** · **11 de 11 testes** — 10 ✅, **1 ⚠️** *(T8, observacao de uniformidade, fundamentada em REV-ROLLOUT §3.1)* |
| **Riscos declarados** | **7** — RP-1 a RP-7. **RP-1 e o mais serio do lote:** DEP-PRD e o **unico liberador de QG-1**, o unico portao do sistema **sem contraditorio previo** |
| **Ressalvas** | Custodia **3**, que **iguala** o limite de VC-03 sem ultrapassa-lo — nao dispara **P6** |
| **RECOMENDACAO** | **APROVAR** |
| **Por que** | Encabeca o fluxo de FND-02 §5 e e **dependencia de DEP-GRW**. **A mitigacao de RP-1 e assimetrica e esta declarada como tal**: o contraditorio chega **depois** do portao, nao antes — e isso e propriedade do desenho de FND-01 §6.2, nao defeito desta Carta |

### 2.4 `DEP-OPS` — Operacoes *(Linha)*

| Campo | Conteudo |
|---|---|
| **ID · versao** | `DEP-OPS` · **1.0.0** |
| **H-A** | `48f53238b55d62e8afc1480816e3cf83aa6613374ba0f6fd71361c3fecd23679` |
| **H-N** | `6bf590c7ad8bd2f0fc643dcf94f42d8abf6788c1dcef1ac9e56bd0f5c28a0a48` |
| **Linhas** | **437** |
| **Capabilities** | **Custodia 2:** `CAP-operacoes`, `CAP-infraestrutura`. **Exerce 2** |
| **Revisao independente** | **DEP-GOV** |
| **Conformidade ao contrato** | **12 de 12 blocos** · **11 de 11 testes** — 10 ✅, **1 ⚠️** *(T3: o impedimento **I-1** declara "ninguem" como substituto, e a excecao esta fundamentada)* |
| **Riscos declarados** | **7** — RO-1 a RO-7. **RO-1 e critico:** copia sem verificacao de restauracao tratada como backup |
| **Ressalvas** | Depende **integralmente** de DEP-ENG: as duas Capabilities custodiadas dependem das dele (RO-6) |
| **RECOMENDACAO** | **APROVAR** |
| **Por que** | E a **unica** Carta do acervo que declara um impedimento **sem substituto possivel** — *sem copia datada e verificada, a acao nao ocorre* (PI-07, LV-01). **Nao dar substituto e a resposta correta**: nomear um criaria via de contorno para uma linha vermelha. **DEP-OPS ja e o departamento com mais atividade real medida** — duas copias datadas verificadas e tres registros na camada OPR |

### 2.5 `DEP-GRW` — Crescimento e Receita *(Linha)*

| Campo | Conteudo |
|---|---|
| **ID · versao** | `DEP-GRW` · **1.0.0** |
| **H-A** | `7b24602ab7416201a6ecddab230d9d331feeae5915013a7139e808b3c5e1c0ba` |
| **H-N** | `2e0e7d95b82e1fff963efd473b1389a55e33bfeee547d26ed18b2bb4c20062ea` |
| **Linhas** | **443** |
| **Capabilities** | **Custodia 2:** `CAP-marketing`, `CAP-comercial`. **Exerce 2** |
| **Revisao independente** | **DEP-GOV** |
| **Conformidade ao contrato** | **12 de 12 blocos** · **11 de 11 testes** ✅ · nenhum conteudo proibido |
| **Riscos declarados** | **7** — RW-1 a RW-7. **Dois criticos:** promessa sem lastro e exposicao de dado sem autorizacao |
| **Ressalvas** | **13 impedimentos e 6 gatilhos E4** — os maiores do sistema. **Nao e excesso de cautela**: e o unico departamento cujo produto **sai da organizacao** |
| **RECOMENDACAO** | **APROVAR** |
| **Por que** | **Completa a cobertura 9/9.** E a area que mais depende de aprovacao humana — opera em **A1**, e toda saida externa e **Tipo 1** por natureza (LV-08). Sem Carta, **os treze impedimentos que a contem nao estao escritos em lugar nenhum** |

## 3. Quadro consolidado — as cinco em uma leitura

| Carta | Classe | Custodia | Blocos | Testes | Impedimentos | Riscos | **Recomendacao** |
|---|---|---|---|---|---|---|---|
| `DEP-GOV` | Guarda | 1 | 12/12 | **11/11** ✅ | 12 | 6 | **APROVAR** |
| `DEP-TLS` | Plataforma | 1 | 12/12 | **11/11** ✅ | 11 | 6 | **APROVAR** |
| `DEP-PRD` | Linha | 3 | 12/12 | 10 ✅ · 1 ⚠️ | 11 | 7 | **APROVAR** |
| `DEP-OPS` | Linha | 2 | 12/12 | 10 ✅ · 1 ⚠️ | 11 | 7 | **APROVAR** |
| `DEP-GRW` | Linha | 2 | 12/12 | **11/11** ✅ | 13 | 7 | **APROVAR** |

**5 recomendacoes de APROVAR · 0 de DEVOLVER.**

> ### Por que **nenhuma** recomendacao de DEVOLVER — e por que isso e um dado a vigiar
> **Devolver e a recomendacao correta quando ha falha estrutural, e nao houve nenhuma:** 55
> testes, 53 ✅, 2 ⚠️ fundamentadas, **0 ❌**.
>
> **Mas cinco de cinco aprovadas e, em si, um numero a auditar** — a mesma vigilancia que
> **FT-04** impoe aos vereditos de aptidao. **A mitigacao esta declarada:** o instrumento de
> validacao foi **testado primeiro contra as quatro Cartas ja em vigor**, e **acusou falha nelas
> tambem** — o que obrigou a distinguir defeito do instrumento de defeito da Carta. Nessa
> distincao nasceram **RC-05** e **RC-07**, ambos em Cartas **ja ratificadas**, e **nenhum foi
> suprimido** por melhorar o relatorio.
>
> **O que sustenta a recomendacao nao e a ausencia de achados — sao oito.** E que **nenhum
> deles esta nas cinco Cartas submetidas**.

## 4. Emenda constitucional candidata — **separada, como exige o rito**

> **Materia C3.** Nao se mistura com as Cartas, que sao C2 quanto ao instrumento e dependem do
> Soberano quanto a vigencia (DC-09). **Decidir as Cartas nao decide a emenda, e vice-versa.**

| Campo | Conteudo |
|---|---|
| **Objeto** | Separar **ratificacao** *(ato do Soberano que da vigencia)* de **homologacao** *(ato do titular que confirma decisao dentro do rito)* em **FND-01 §7.3** e **§11** |
| **Instrumento** | [RFC-0011](../rfcs/RFC-0011-emenda-constitucional-ratifica-homologa.md) → [ADR-0014](../decisions/ADR-0014-candidato-emenda-fnd-01-7-3-homologa.md) — **candidato, `em-revisao`, sem vigencia** |
| **Etapas de FND-01 §9 cumpridas** | **1, 2 e 3** — proposta com texto atual e proposto, analise de consistencia e impacto. **A etapa 4 — ratificacao — nao ocorreu** |
| **Diff** | **8 alteracoes**: 1 cabecalho de coluna · **5 celulas** · 1 nota normativa · 1 entrada de glossario. Literal em [RFC-0011 §3.2](../rfcs/RFC-0011-emenda-constitucional-ratifica-homologa.md) |
| **Titulares de decisao alterados** | **ZERO.** Quem homologa hoje continua homologando, com o mesmo alcance |
| **Principios, linhas vermelhas, hierarquia alterados** | **ZERO** |
| **Artefatos a reescrever** | **ZERO** — varredura de **1.210** ocorrencias em **117** artefatos: **nenhum** registra o termo no sentido antigo, porque `IR-11` ja impediu a propagacao |
| **Versao proposta** | **FND-01 1.4.0** *(MENOR)*. **Duvida declarada:** se o Soberano entender que nomear o instituto altera **direito de decisao**, a versao correta e **2.0.0**. **A escolha e dele**, e o ADR nao a antecipa |
| **Evidencia central** | **FND-09 §8.2 — projecao declarada de FND-01 §7.3 — nao reproduz nenhum dos cinco titulares departamentais.** Suas **22** linhas dizem `SOBERANO`, `SOBERANO se …` ou `—`. **O acervo ja opera no sentido estrito** |
| **Custo de nao emendar** | A causa de **dois incidentes** permanece viva; a protecao continua dependendo de uma regra de **redacao**, que alcanca artefato **novo** e nao alcanca o leitor do texto constitucional |
| **RECOMENDACAO** | **APROVAR** — com a ressalva de que **nao aprovar e legitimo**: `IR-11` funciona, com **0** violacoes medidas |

### 4.1 Questao **Q2** — escalada, sem ADR candidato

| Campo | Conteudo |
|---|---|
| **Pergunta** | **`Fitness Check` exige ratificacao do Soberano?** FND-10 **§2.2** exige `ratificacao` de *"todo artefato de **decisao** C3 ou Tipo 1"*; **§10.3** atribui a `FIT` *"Ratifica: SOBERANO se C3"*, tratando a classe do **objeto avaliado** como se fosse a do parecer |
| **Classe formal** | **C2** — FND-10 e FND-09 ja foram emendadas por C2 |
| **Por que nao se decide por C2** | **A emenda reduz o que chega ao Soberano.** [ADR-0012 §5.5](../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md) ja decidiu que *"retirar materia da mesa do ratificador nao e decisao que o rito C2 deva tomar sozinho"* (PI-01), e DEP-QAR **insistiu** nesse ponto em RFC-0009 §10. **Esta missao nao reabre decisao vigente** |
| **Texto proposto** | **3 alteracoes**, em [RFC-0011 §5.2](../rfcs/RFC-0011-emenda-constitucional-ratifica-homologa.md): FND-10 §10.3 linha `Fitness Check` → `—`; nota nova; **cascata obrigatoria** em FND-09 §8.2 |
| **Por que sem ADR candidato** | Um ADR C2 candidato sugeriria que **DEP-EXE** poderia aprova-lo — precisamente o que ADR-0012 §5.5 vedou |
| **RECOMENDACAO** | **DETERMINAR a leitura que prevalece.** Nao ha recomendacao de merito: a materia e do Soberano por decisao ja vigente |

## 5. O que **nao** esta neste pacote, e por que

| Objeto | Por que nao esta |
|---|---|
| **`DEP-QAR` 1.1.0** | **Ja decidida.** Ratificada pelo ato de 2026-07-28; em vigor. Registro em [MSG-2026-0003](../memory/operacional/MSG-2026-0003-ato-soberano-emenda-qar-e-criterio-de-consolidacao.md) |
| **O criterio de consolidacao (PS-1)** | **Ja decidido** pelo mesmo ato, e **ja formalizado** em [ADR-0013](../decisions/ADR-0013-criterio-de-horizonte-e-consolidacao.md) — C2/Tipo 2, **nao exige ratificacao** |
| **ADR-0013, RFC-0010, RFC-0011** | **Nao exigem ato.** C2/Tipo 2 e RFCs alcancam vigencia sem ratificacao (FND-04 §2.1) |
| **`REV-ROLLOUT` e `FIT-2026-008`** | **Pareceres**, nao decisoes. Se exigem ratificacao e **exatamente a questao Q2** — §4.1 |
| **Correcao de RC-01, RC-05 e RC-07** | Estao em Cartas **ja ratificadas**. Corrigi-las altera `H-N` e exige **ato novo** sobre **cada uma** (IR-01, IR-05). **Nao se pede aqui**, para nao inflar o ato com materia que nao urge — as tres tem efeito **nulo ou local** |
| **Qualquer agente, skill, workflow, produto ou ferramenta** | **Nenhum foi criado**, por determinacao |

## 6. Se o Soberano aprovar — o que muda, exatamente

| # | Efeito | Operacao |
|---|---|---|
| E1 | As cinco Cartas: `em-revisao` → **`ativo`**; `pendente` → **`ratificada`** | **O4** (FND-10 §5.2) |
| E2 | **Cobertura vigente passa de 4/9 para 9/9** | Projecao em `departments/README §1` |
| E3 | Registro canonico do ato, com **H-A, H-N e H-P** por Carta e o diff exato | Novo `MSG`, conforme IR-07 e IR-08 |
| E4 | **R2 de FIT-2026-006** encerra tambem quanto a vigencia | Reconciliacao |
| E5 | `IR-09` executado sobre as cinco, por **DEP-QAR**, com conferencia de DEP-GOV | IR-09 |
| E6 | Catalogo, baseline e indices atualizados na mesma mudanca | CV-04, IX-02 |

**Nenhum efeito e irreversivel.** As cinco Cartas sao **Tipo 2**: reverter e superar por nova
versao, sem dado vivo, sem exposicao externa e sem migracao.

## 7. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Contrato das Cartas | [ADR-0011](../decisions/ADR-0011-contrato-de-carta-de-departamento.md), **DC-01 a DC-10** |
| Validacao independente | [REV-ROLLOUT](../foundation/revisao-arquitetural-rollout-cartas-2026-07-28.md) — **55 testes, 0 falhas estruturais** |
| Projecao comparativa | [`departments/README.md`](../departments/README.md) |
| Verificacao de aptidao | [FIT-2026-008](fitness/FIT-2026-008-rollout-das-cartas.md) |
| Decisao de rollout que autorizou a producao | [FIT-2026-007 §Rollout](fitness/FIT-2026-007-revisao-estrutural-i.md) — **GO-CONDITIONAL** |
| Condicao unica de saida daquele rollout | *"A quinta Carta e a de DEP-GOV, escrita sozinha, e deve declarar em B9 o impedimento exposto por RE-03"* — ✅ **cumprida**, `DEP-GOV I-2` |
| Ato soberano anterior | [MSG-2026-0003](../memory/operacional/MSG-2026-0003-ato-soberano-emenda-qar-e-criterio-de-consolidacao.md) |
| Precedente de forma | [REV-INTERCLASSES §6](../foundation/revisao-arquitetural-validacao-interclasses-2026-07-28.md) — o primeiro pacote do sistema |
| Baseline vigente na submissao | **`BL-2026-07-28-06`** — [catalogo mestre §10](artifact-registry.md) |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-GOV | Pacote unico da **Missao 1.9**: **cinco** Cartas de Departamento com ID, versao, **H-A e H-N**, Capabilities, revisao independente, riscos, ressalvas e recomendacao **APROVAR** para as cinco; **uma** emenda **C3** candidata, separada, com **8 alteracoes** e **zero** titulares alterados; e **uma** questao **C2 escalada** sem ADR candidato, por decisao vigente de ADR-0012 §5.5. **Segundo pacote soberano do sistema, e o primeiro com o caminho exato anexado** — cumprimento de **RE-01**. |
