---
id: REV-CAP-2026-07-28
titulo: Revisao Arquitetural do Enterprise Capability Model
tipo: relatorio
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-QAR
proprietario: DEP-QAR
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0002]
substitui: []
substituido_por: null
---

# Revisao Arquitetural do Enterprise Capability Model

## Proposito
Submeter o catalogo de 23 Capabilities a exame critico e independente, respondendo as oito
perguntas obrigatorias da missao e registrando achados com recomendacao.

## Escopo
| Item | Definicao |
|---|---|
| Inclui | Duplicacao, sobreposicao, amplitude, especializacao, lacuna, cobertura, classe `nucleo`, maturidade `experimental` |
| Nao inclui | Merito de cada competencia isolada; criacao de componentes |
| Metodo | Confronto do catalogo com FND-01 a FND-08, com a missao declarada e com os testes TC-1 a TC-6 |

## Responsaveis
| Papel | Responsavel |
|---|---|
| Executa a revisao | DEP-QAR *(independente de DEP-EXE, que propos o catalogo — PI-05)* |
| Conformidade | DEP-GOV |
| Decide sobre os achados | SOBERANO |

---

## Sumario dos achados

| # | Achado | Severidade | Acao |
|---|---|---|---|
| A1 | Proporcao de `nucleo` elevada: 8 de 23 (35%) | **Media** | Reavaliar no primeiro horizonte |
| A2 | Fronteira `CAP-conhecimento` × `CAP-comunicacao` e a mais fina do catalogo | Media | Monitorar; fusao prevista se indistinguivel |
| A3 | `CAP-design` sem consumidor duro | Baixa | Aceito; gatilho RL-06 sob observacao |
| A4 | `CAP-inteligencia-artificial` × `CAP-engenharia-de-agentes` exigem disciplina de fronteira | Media | Limites explicitados; monitorar |
| A5 | Lacuna: nao ha Capability de **suporte e relacao com usuario** | Baixa | Deliberadamente ausente; gatilho definido |
| A6 | 21 de 23 em `experimental`; 88 de 111 indicadores sem valor medido | **Alta** *(esperada)* | Aceito para a fase; e o estado honesto |
| A7 | `CAP-juridico` declara limite de competencia que nao pode ser superado internamente | Baixa | Registrado como limite permanente |

---

## 1. Existe duplicacao?

**Nao — nenhuma duplicacao de definicao foi encontrada.** Tres verificacoes:

### 1.1 Duplicacao com a Fundacao (criterio bloqueante C4 de ADR-0002)
As Capabilities que tangenciam normas existentes **referenciam** o documento por ID em vez
de reescrever a regra:

| Capability | Norma tangenciada | Como evita duplicar |
|---|---|---|
| `CAP-governanca` | FND-01, FND-03, FND-04, FND-07 | §13 aponta para as normas; nao repete classes nem ritos |
| `CAP-comunicacao` | FND-05 | Descreve a **competencia de exercer**; o protocolo permanece em FND-05 |
| `CAP-conhecimento` | FND-06 | Descreve a **competencia de curar**; a arquitetura das camadas permanece em FND-06 |
| `CAP-qualidade` | FND-01 §6 | Descreve a **competencia de verificar**; o DoD e os portoes permanecem em FND-01 |

**Verificacao aplicada:** nenhuma Carta contem tabela de classes de mudanca, de estados, de
camadas de memoria ou de portoes. Todas remetem por link. MM-01 preservado.

### 1.2 Duplicacao entre Capabilities
Nenhum par produz o mesmo artefato para o mesmo consumidor com a mesma finalidade. Os
pares mais proximos foram examinados individualmente em §2.

### 1.3 Duplicacao com a estrutura (risco R1 de ADR-0002)
O risco de as Capabilities virarem espelho dos departamentos **nao se materializou**:

| Evidencia | Numero |
|---|---|
| Departamentos | 9 |
| Capabilities | 23 |
| Correspondencias 1:1 (um departamento ↔ exatamente uma Capability) | **1** — DEP-TLS ↔ `CAP-integracao` |
| Departamentos custodiando 2+ Capabilities | 7 de 9 |
| Capabilities exercidas por 2+ departamentos | 2 |

O unico caso 1:1 e DEP-TLS, cujo escopo estrutural ja era estreito. Aceitavel: nao indica
espelhamento sistematico. **DEP-ENG custodia 5 Capabilities distintas** — a prova mais forte
de que as camadas nao coincidem.

---

## 2. Existe sobreposicao?

**Sim, em quatro fronteiras finas — todas delimitadas explicitamente, nenhuma nao resolvida.**

O atributo Limites (A-05) obrigou cada Carta a nomear a Capability dona do que ela exclui.
As quatro fronteiras que exigiram maior cuidado:

### 2.1 `CAP-conhecimento` × `CAP-comunicacao` — **achado A2**
| Aspecto | Conhecimento | Comunicacao |
|---|---|---|
| Verbo | Persistir e devolver | Transferir |
| Pacote de Contexto | **monta e cura** | **transporta** |
| Falha tipica | Registro nao encontrado | Handoff sem contexto |

**Risco residual:** o Pacote de Contexto e produzido por uma e consumido pela outra; sob
pressao, a curadoria tende a migrar para quem transporta. **Recomendacao:** monitorar o
indicador I5 de `CAP-comunicacao` (tamanho do nucleo do pacote) contra I4 de
`CAP-conhecimento` (volume por consulta). Divergencia entre os dois sinaliza que a fronteira
esta sendo atravessada. Fusao ja esta prevista como criterio de evolucao em ambas.

### 2.2 `CAP-inteligencia-artificial` × `CAP-engenharia-de-agentes` — **achado A4**
| Aspecto | IA | Engenharia de Agentes |
|---|---|---|
| Objeto | O modelo como **ferramenta** | O agente como **trabalhador** |
| Pergunta | Que modelo, com que instrucao, avaliado como? | Que papel, com que escopo, que limite? |
| Artefato tipico | Skill de avaliacao de saida | Carta de agente |

**Por que a separacao se justifica:** um bom prompt nao produz um bom papel organizacional,
e uma boa Carta de agente nao compensa modelo mal escolhido. Sao competencias que falham de
formas diferentes. **Recomendacao:** reavaliar apos os primeiros cinco agentes criados — se
a mesma pessoa/papel sempre exercer as duas juntas, a fusao esta indicada.

### 2.3 `CAP-governanca` × `CAP-qualidade` × `CAP-juridico`
Tres competencias de verificacao, com objetos distintos e nao sobrepostos:

| Capability | Verifica | Contra o que |
|---|---|---|
| `CAP-governanca` | Forma, conformidade, rastreabilidade | Norma **interna** |
| `CAP-qualidade` | Conteudo, correcao, risco | Criterio de aceite e evidencia |
| `CAP-juridico` | Licitude | Norma **externa** |

Um ADR pode ser perfeitamente conforme (governanca aprova) e conter decisao errada
(qualidade reprova) e ainda assim licita (juridico nao objeta). Os tres eixos sao
independentes. **Sem sobreposicao.**

### 2.4 `CAP-operacoes` × `CAP-seguranca` no backup
Deliberadamente separadas por PI-05: operacoes **executa** o backup, seguranca **verifica**
que ele e integro e restauravel. Concentrar as duas violaria LV-03. **Sobreposicao aparente
que e, na verdade, separacao de poderes.**

---

## 3. Existe alguma Capability ampla demais?

**Duas merecem atencao; nenhuma exige divisao agora.**

### 3.1 `CAP-engenharia` — a mais ampla
Cobre implementacao, verificacao propria, legibilidade, estimativa e manutencao. Sinal de
amplitude: nivel 5 no mapa, com fan-in de toda a realizacao.

**Por que nao dividir agora:** nenhum dos gatilhos de FND-08 §7.2 foi observado — nao ha
codigo escrito, portanto nao ha escopo heterogeneo constatado. Dividir agora seria
especializacao **por antecipacao**, recusada por FND-08 §7.1.
**Gatilho a observar:** construcao de superficie versus nucleo exigindo metodos distintos.

### 3.2 `CAP-conhecimento` — a de maior fan-out
Unica de nivel 0; seis Capabilities dependem dela duramente. RL-07 alerta: *"Capability da
qual tudo depende e sinal de escopo amplo demais."*

**Analise:** o fan-out aqui e **estrutural, nao acidental** — memoria e a base de uma
organizacao que compoe (Visao V2). Dividi-la fragmentaria a fonte unica de verdade e
violaria MM-01.
**Recomendacao:** manter unida; se a divisao vier, deve ser **dentro** da camada (por
dominio de memoria), nunca em Capabilities irmas — coerente com MI-01 de FND-06.

### 3.3 Verificacao de amplitude nas demais
Aplicado o teste "e invocada por motivos que nao se parecem entre si?" a todas as 23:
**21 passaram sem ressalva.** As duas acima ficam sob observacao com gatilho declarado.

---

## 4. Alguma merece especializacao?

**Nenhuma agora. Cinco com gatilho armado.**

Aplicando FND-08 §7.2 e o Teste de Especializacao de FND-04 §6.2 — que exige **sinal
observado**, nao ganho previsto:

| Capability | Especializacao provavel | Gatilho declarado | Sinal ja observado? |
|---|---|---|---|
| `CAP-engenharia` | Superficie × nucleo | Metodos incompativeis | **Nao** |
| `CAP-inteligencia-artificial` | Engenharia de contexto propria | Contexto por tarefa crescer | **Nao** |
| `CAP-engenharia-de-agentes` | Projeto de papel × orquestracao | Metodos divergirem | **Nao** |
| `CAP-conhecimento` | Sub-particao por dominio | Camada com naturezas distintas | **Nao** |
| `CAP-qualidade` | Verificacao × analise de risco | Metodos divergirem | **Nao** |

**Conclusao:** especializar qualquer uma nesta data seria violacao direta de FND-08 §7.1
(antipadrao de antecipacao) e do Teste de Especializacao. **Nao especializar e, aqui, a
decisao correta** — e ela propria fica registrada, conforme PI-14 regra 2.

---

## 5. Existe lacuna arquitetural?

**Uma lacuna deliberada e tres ausencias justificadas.**

### 5.1 Lacuna reconhecida — **achado A5**
**Suporte e relacao com usuario.** Nenhuma Capability cobre "atender quem usa quando algo
da errado para essa pessoa". Hoje o assunto se dispersa entre `CAP-operacoes` (incidente
tecnico) e `CAP-comercial` (retencao).

| Campo | Conteudo |
|---|---|
| Por que nao foi criada | Nao ha produto, nao ha usuario, nao ha volume — criar seria antecipacao (FND-08 §7.1) |
| Risco de nao criar | Baixo agora; cresce a partir do primeiro produto em operacao |
| **Gatilho de criacao** | Primeiro produto com usuario externo ativo |
| Custo assumido pelo adiamento | Se o volume surgir antes do reconhecimento, o atendimento sera improvisado por duas Capabilities que nao o possuem |

> Registrado como **decisao de nao decidir** (FND-07 §9): o custo esta declarado, nao
> invisivel.

### 5.2 Ausencias justificadas

| Ausencia | Por que nao e lacuna |
|---|---|
| **Pessoas / RH** | A organizacao nao tem pessoas alem do Soberano. A competencia analoga — projetar a forca de trabalho — e `CAP-engenharia-de-agentes` |
| **Contabilidade formal** | Coberta parcialmente por `CAP-financeiro` e `CAP-juridico`; o restante exige profissional humano, limite ja declarado |
| **Inovacao / P&D** | Distribuida entre `CAP-pesquisa` (descobrir), `CAP-estrategia` (apostar) e `CAP-aprendizado` (consolidar). Criar uma quarta produziria sobreposicao tripla |

### 5.3 Verificacao contra os portoes da Constituicao
Cada portao de FND-01 §6.2 tem Capability correspondente:

| Portao | Capability |
|---|---|
| QG-0 iniciar | `CAP-coordenacao` |
| QG-1 especificar | `CAP-produto` |
| QG-2 arquitetar | `CAP-arquitetura` + `CAP-governanca` |
| QG-3 revisar | `CAP-qualidade` |
| QG-4 liberar | `CAP-qualidade` + `CAP-seguranca` |
| QG-5 aprender | `CAP-aprendizado-organizacional` |

**Nenhum portao orfao.**

---

## 6. O catalogo cobre toda a organizacao?

**Sim.** Tres verificacoes de cobertura, todas com resultado completo.

### 6.1 Cobertura da estrutura — 9 de 9 departamentos
| Departamento | Capabilities custodiadas |
|---|---|
| DEP-EXE | estrategia, coordenacao, comunicacao, financeiro |
| DEP-GOV | governanca |
| DEP-QAR | qualidade, seguranca, juridico |
| DEP-PRD | pesquisa, produto, design |
| DEP-ENG | arquitetura, engenharia, dados, IA, engenharia-de-agentes |
| DEP-OPS | operacoes, infraestrutura |
| DEP-GRW | marketing, comercial |
| DEP-KMS | conhecimento, aprendizado-organizacional |
| DEP-TLS | integracao |

**Nenhum departamento sem Capability. Nenhuma Capability sem custodio (OW-03).**

### 6.2 Cobertura das responsabilidades exclusivas de FND-02
Cada item de "o que possuo" das nove cartas resumidas foi mapeado a ao menos uma
Capability. **Nenhuma responsabilidade orfa.**

### 6.3 Cobertura da missao e da visao
| Elemento | Capabilities que o sustentam |
|---|---|
| Missao — converter direcao em produto | estrategia → produto → arquitetura → engenharia → qualidade |
| V1 Direcao suficiente | estrategia, produto, coordenacao |
| V2 Memoria que compoe | conhecimento, aprendizado-organizacional |
| V3 Qualidade sem vigilancia | qualidade, seguranca, governanca |
| V4 Auditabilidade total | governanca, conhecimento |
| Custo marginal decrescente | financeiro, conhecimento, engenharia-de-agentes |

### 6.4 Conformidade estrutural verificada
| Regra | Resultado |
|---|---|
| OW-01 custodia unica | 23/23 ✓ |
| OW-03 sem Capability orfa | 23/23 ✓ |
| OW-05 dominio GAR na Guarda | 3/3 — todas em DEP-QAR ✓ |
| RL-01 sem ciclo em `depende-de` | Ordem topologica de 8 niveis ✓ |
| RL-03 relacoes bilaterais | ✓ apos correcao de **6** divergencias detectadas na revisao |
| RL-04 profundidade de especializacao ≤ 1 | Nenhuma especializacao ainda ✓ |
| RL-05 verificador nao depende do verificado | 3 verificadores ✓ |
| §3.5 combinacoes proibidas | Nenhuma `nucleo`+`proposta`, nenhuma `madura` sem indicador ✓ |

---

## 7. Alguma Capability deve ser Core? — **achado A1**

**Oito foram classificadas `nucleo`. A proporcao e alta e merece registro critico.**

### 7.1 As oito e sua justificativa
Ver [catalogo §3.1](README.md). Cada uma foi submetida ao teste: *"se a organizacao for
mediocre nisto, a proposta inteira falha?"*

### 7.2 Achado: 35% do catalogo em `nucleo`
| Problema | Consequencia |
|---|---|
| `nucleo` implica investimento prioritario | Prioridade que se aplica a 8 de 23 nao prioriza nada |
| `nucleo` implica aposentadoria por emenda C3 | Rigidez excessiva se aplicada amplamente |
| Classe seletiva perde funcao ao ser generosa | O eixo deixa de discriminar |

### 7.3 Analise das candidatas a rebaixamento
| Capability | Argumento para rebaixar | Por que foi mantida `nucleo` |
|---|---|---|
| `CAP-estrategia` | A direcao vem do Soberano, nao da organizacao | A competencia de **traduzir** direcao em algo operavel e da organizacao, e V1 depende dela |
| `CAP-produto` | Muitas empresas definem produto bem; nao diferencia | Sem ela constroi-se a coisa errada com eficiencia — falha catastrofica, nao incremental |
| `CAP-inteligencia-artificial` | Poderia ser habilitadora de `engenharia-de-agentes` | E o substrato: mediocridade aqui degrada todo o trabalho, nao um papel |
| `CAP-aprendizado-organizacional` | Poderia fundir-se a `conhecimento` | Falham de formas diferentes: uma nao encontra, a outra nao aprende |

### 7.4 Recomendacao
**Manter as oito nesta fase**, pelas justificativas acima, **e reavaliar a classe de todas
na primeira revisao estrutural**, com o criterio adicional: *uma classe `nucleo` saudavel
nao deveria passar de aproximadamente um quarto do catalogo.*

Se em H2 a proporcao permanecer em 35% sem que os indicadores comprovem criticidade,
rebaixar `CAP-estrategia` e `CAP-produto` a `habilitadora` e a correcao indicada.

> Registrado como achado de severidade **media**, com gatilho e correcao propostos —
> nao como observacao sem destino (FND-04 §8).

---

## 8. Alguma deve permanecer Experimental? — **achado A6**

**Vinte e uma das 23 permanecem `experimental`, e isso e o estado honesto.**

### 8.1 Distribuicao de maturidade

| Maturidade | Qtd | Quais |
|---|---|---|
| `emergente` | 2 | `CAP-governanca`, `CAP-estrategia` |
| `experimental` | 21 | todas as demais |

### 8.2 Por que apenas duas subiram
CL-01 proibe pular estagio, e `experimental → emergente` exige **exercicio com resultado
registrado**. Apenas duas competencias foram de fato exercidas nesta fase:

| Capability | Evidencia do exercicio |
|---|---|
| `CAP-governanca` | 2 ADRs, 1 RFC, taxonomia aplicada a 40 artefatos, auditoria de conformidade com 100% de aprovacao |
| `CAP-estrategia` | Missao, visao, valores, 3 horizontes com criterio de conclusao e escopo negativo declarado (FND-01) |

### 8.3 Candidatas que foram recusadas
| Capability | Argumento para promover | Por que foi recusada |
|---|---|---|
| `CAP-arquitetura` | "A Fundacao e uma arquitetura" | E arquitetura **organizacional** — exercicio de `CAP-governanca`. Nenhum sistema tecnico foi arquitetado |
| `CAP-conhecimento` | "FND-06 foi projetado" | Projetar a arquitetura de memoria nao e exercer a curadoria. **Zero registros curados** |
| `CAP-seguranca` | "Varredura de credencial executada" | Uma varredura sem dado vivo nem exposicao externa nao e exercicio da competencia |
| `CAP-qualidade` | "Auditorias foram executadas" | Foram auditorias de **conformidade** — `CAP-governanca`. Nenhuma entrega de produto verificada |

### 8.4 Leitura do achado
Vinte e uma Capabilities `experimental` e **88 de 111 indicadores sem valor medido** fazem
deste um catalogo **declarado, nao comprovado**. Isso e legitimo — ADR-0002 §8 declara
explicitamente que os ganhos sao previstos e nao observados — mas exige que ninguem trate o
catalogo como descricao do que a organizacao ja sabe fazer.

Dos 23 indicadores com valor, praticamente todos registram **zero ocorrencia de violacao**
(credencial exposta, envio sem autorizacao, autoverificacao) — o que mede ausencia de dano,
nao presenca de competencia.

**Recomendacao:** que a primeira revisao estrutural avalie promocao **caso a caso, com
evidencia**, e que nenhuma promocao ocorra por decurso de prazo. Maturidade declarada sem
indicador medido e devolvida por CL-06.

> **Nenhuma Capability deve ser rebaixada nesta data** — nenhuma foi declarada acima do que
> a evidencia sustenta.

---

## 9. Conclusao da revisao

| Criterio de conclusao da missao | Resultado |
|---|---|
| Framework completo | ✓ FND-08 com 13 atributos, 3 eixos, ciclo de 9 estagios, 7 relacoes, propriedade e evolucao |
| Consistente | ✓ 8 regras estruturais verificadas por varredura automatizada; 6 divergencias encontradas e corrigidas |
| Reutilizavel | ✓ Nenhuma Capability cita produto especifico; teste TC-6 aplicado a todas |
| Sustenta evolucao futura | ✓ Gatilhos de especializacao, fusao e depreciacao declarados em 23/23 |
| Camada intermediaria | ✓ Situada entre FND-01 e a estrutura operacional; hierarquia normativa emendada |

**Parecer de DEP-QAR:** o catalogo esta apto a servir de base para a fase seguinte. Os sete
achados sao registrados com gatilho e correcao propostos; nenhum bloqueia a adocao.

**Ressalva registrada (PI-10):** este catalogo descreve o que a organizacao **se propoe a
saber fazer**. Com 21 de 23 competencias em `experimental` e 88 de 111 indicadores sem valor
medido, ele **nao** e evidencia de que a organizacao ja saiba faze-las.

---

## 10. Achados que geram acao futura

| # | Acao | Quando | Responsavel |
|---|---|---|---|
| A1 | Reavaliar proporcao de `nucleo`; rebaixar estrategia e produto se nao se confirmarem | 1a revisao estrutural | DEP-EXE + DEP-QAR |
| A2 | Monitorar fronteira conhecimento × comunicacao pelos indicadores I4/I5 | Continuo | DEP-KMS |
| A4 | Reavaliar fronteira IA × engenharia-de-agentes | Apos 5 agentes criados | DEP-ENG |
| A5 | Criar Capability de suporte ao usuario | Primeiro produto com usuario externo | DEP-EXE |
| A6 | Promover maturidade caso a caso, com evidencia | 1a revisao estrutural | DEP-QAR |
| A3 | Verificar gatilho RL-06 de `CAP-design` | Fim do 1o horizonte | DEP-PRD |
