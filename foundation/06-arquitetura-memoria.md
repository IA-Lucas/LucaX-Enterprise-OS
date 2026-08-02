---
id: FND-06
titulo: Arquitetura da Memoria Organizacional
tipo: fundacao
versao: 1.3.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-KMS
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0001, ADR-0002, ADR-0003, ADR-0004, ADR-0010]
substitui: []
substituido_por: null
resumo: Define as cinco camadas da memoria organizacional, o criterio de alocacao, a promocao, a expiracao e a curadoria.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: ratificada
---

# Arquitetura da Memoria Organizacional

## Proposito

Definir como o LucaX Enterprise OS lembra. Estabelece as cinco camadas da memoria
organizacional, o que pertence a cada uma, quem e responsavel por cada camada, como um
registro nasce, e promovido, expira ou e revogado, e como conflitos entre registros sao
resolvidos.

Memoria e o ativo que faz a organizacao compor: cada trabalho concluido deve tornar o
proximo mais barato, mais rapido e mais correto (Visao V2).

## Escopo

| Item | Definicao |
|---|---|
| **Inclui** | As 5 camadas, criterio de alocacao, formato do registro, ciclo de vida, promocao e rebaixamento, expiracao, resolucao de conflito, recuperacao (recall), higiene e curadoria. |
| **Nao inclui** | Banco de dados, indexacao tecnica, embeddings, ferramenta de armazenamento, automacao — tudo isso e implementacao de fase futura. |
| **Subordinado a** | [FND-01 Constituicao](01-constituicao.md), [FND-03 Taxonomia](03-taxonomia.md). |
| **Consumido por** | Todos os departamentos. Nenhum trabalho fecha sem passar por QG-5. |

## Responsaveis

| Papel | Responsavel |
|---|---|
| Proprietario da arquitetura | DEP-KMS |
| Curador de todas as camadas | DEP-KMS |
| Dono do conteudo de cada camada | Ver §3 (varia por camada) |
| Guardiao normativo | DEP-GOV |
| Aprovador de mudanca | SOBERANO (via ADR) |

---

## 1. Principios da Memoria

| # | Principio | Consequencia |
|---|---|---|
| MM-01 | **Um fato, um lugar.** Cada fato vive em exatamente uma camada. | Duplicata e defeito de curadoria, nao redundancia util. |
| MM-02 | **Toda memoria tem proveniencia.** Origem, autor, data e evidencia sao obrigatorios. | Registro sem proveniencia e tratado como nao confiavel. |
| MM-03 | **Estabilidade cresce para cima.** Camadas superiores mudam menos e valem mais. | Conflito e resolvido pela camada mais alta. |
| MM-04 | **Promocao exige evidencia, nao repeticao.** Algo sobe de camada por ter se confirmado. | Opiniao repetida nao vira principio. |
| MM-05 | **Esquecer e funcao, nao falha.** O que nao serve mais expira. | Memoria sem higiene vira ruido e aumenta contexto (PI-14). |
| MM-06 | **Memoria e escrita para ser lida por outro.** | Registro que so o autor entende nao cumpriu sua funcao. |
| MM-07 | **Registro nao substitui decisao.** Decisao vive em ADR; memoria aponta para ele. | Memoria referencia, nao reescreve a norma. |
| MM-08 | **Contexto minimo na recuperacao (PI-14).** Devolve-se o que a tarefa usa. | Despejar memoria e falha de curadoria. |
| MM-09 | **Memoria e append-first.** Corrige-se acrescentando e superando, nao apagando. | Historia preservada; ver §7.3. |
| MM-10 | **Sem credencial, sem dado sensivel.** | PI-08 vale integralmente na memoria. |

## 2. Visao Geral das Camadas

```
                       ESTABILIDADE ALTA · VOLUME BAIXO · AUTORIDADE ALTA
  ┌──────────────────────────────────────────────────────────────────────┐
  │  EST  ESTRATEGICA    por que existimos e para onde vamos             │  DEP-GOV
  ├──────────────────────────────────────────────────────────────────────┤
  │  PRD  PRODUTO        o que construimos, para quem e por que          │  DEP-PRD
  ├──────────────────────────────────────────────────────────────────────┤
  │  TEC  TECNICA        como esta construido e por que assim            │  DEP-ENG
  ├──────────────────────────────────────────────────────────────────────┤
  │  OPR  OPERACIONAL    o que esta acontecendo agora                    │  DEP-OPS
  ├──────────────────────────────────────────────────────────────────────┤
  │  APR  APRENDIZADO    o que descobrimos ao fazer                      │  DEP-KMS
  └──────────────────────────────────────────────────────────────────────┘
                       ESTABILIDADE BAIXA · VOLUME ALTO · AUTORIDADE BAIXA

  APR e a camada transversal: alimenta-se de todas e promove para todas.
```

### 2.1 Quadro comparativo

| Camada | Pergunta que responde | Dono | Volatilidade | TTL padrao | Autoridade |
|---|---|---|---|---|---|
| **EST** | Por que existimos? Para onde vamos? | DEP-GOV | Muito baixa | Permanente | 1 (maxima) |
| **PRD** | O que construimos e para quem? | DEP-PRD | Baixa | Vida do produto | 2 |
| **TEC** | Como esta feito e por que assim? | DEP-ENG | Media | Vida do componente | 3 |
| **OPR** | O que esta acontecendo agora? | DEP-OPS | Alta | 1 ciclo (renovavel) | 5 (minima) |
| **APR** | O que aprendemos ao fazer? | DEP-KMS | Media | Ate ser refutado | 4 |

**Autoridade** define quem vence em conflito: numero menor prevalece (MM-03).

## 3. As Cinco Camadas em Detalhe

---

### 3.1 EST — Memoria Estrategica

| Campo | Definicao |
|---|---|
| **Proposito** | Guardar a identidade e a direcao da organizacao: o que nao muda com o projeto da semana. |
| **Dono** | DEP-GOV |
| **Escreve** | DEP-GOV, mediante ADR aprovado. Nenhuma outra area escreve diretamente. |
| **Le** | Todos, obrigatoriamente antes de qualquer decisao C2 ou C3 |
| **Volatilidade** | Muito baixa — mudanca aqui e sempre evento formal |
| **TTL** | Permanente. Nao expira; e superada. |
| **Localizacao** | `memory/estrategica/` |

**Pertence a esta camada**
- Missao, visao, valores, principios imutaveis, linhas vermelhas
- Objetivos de longo prazo e criterios de sucesso organizacional
- **O catalogo de Capabilities: o que a organizacao sabe fazer** (FND-08)
- **O Meta Model: o universo de entidades que podem existir e como se ligam** (FND-09)
- Estrutura organizacional vigente e direitos de decisao
- Decisoes de portfolio: por que um produto existe ou foi encerrado
- Posicionamento estrategico e apostas de longo prazo
- Restricoes permanentes impostas pelo Soberano
- Padroes duraveis de preferencia do Soberano sobre como o trabalho e feito

**Nao pertence**
- Detalhe de produto (→ PRD) · decisao tecnica (→ TEC) · estado de execucao (→ OPR)
- Aprendizado ainda nao consolidado (→ APR) · qualquer coisa com prazo de validade curto

**Regra de escrita:** so entra em EST o que sobreviveu a um horizonte inteiro ou o que foi
determinado diretamente pelo Soberano. Escrita em EST **sempre** exige ADR (C2 ou C3).

> **Conhecimento sobre o Soberano.** As duas ultimas linhas de *"Pertence a esta camada"* —
> restricoes permanentes e padroes duraveis de preferencia do Soberano — sao governadas pelo
> **Contrato de Conhecimento sobre o Soberano**, instituido por
> [ADR-0010 §5](../decisions/ADR-0010-contrato-de-conhecimento-do-soberano.md), que e a
> **fonte** de suas regras e nao e reproduzido aqui (PJ-01). O contrato acrescenta, a esta
> camada e apenas a este conteudo: proveniencia **por afirmacao** com classe de evidencia
> (CT-06); lista fechada de conteudo proibido (CT-15); pacotes de carregamento com custo
> medido (CT-21 a CT-24). **Nada disso altera a natureza da camada:** memoria informa e nao
> obriga (MM-07), e o registro cede diante da norma (CT-01).

---

### 3.2 PRD — Memoria de Produto

| Campo | Definicao |
|---|---|
| **Proposito** | Guardar o entendimento acumulado sobre o que se constroi, para quem e sob quais criterios. |
| **Dono** | DEP-PRD |
| **Escreve** | DEP-PRD; DEP-GRW contribui sinal de mercado; DEP-OPS contribui sinal de uso |
| **Le** | DEP-ENG (antes de construir), DEP-QAR (antes de aceitar), DEP-GRW (antes de comunicar) |
| **Volatilidade** | Baixa a media |
| **TTL** | Vida do produto. Encerrado o produto, a memoria e arquivada, nao apagada. |
| **Localizacao** | `memory/produto/` |

**Pertence a esta camada**
- Definicao de cada produto: problema, publico, proposta de valor
- Personas, contextos de uso, jornadas
- Requisitos duraveis e criterios de aceite recorrentes
- Escopo negativo do produto: o que ele deliberadamente nao faz, e por que
- Roadmap e sua justificativa; o que foi despriorizado e por que
- Feedback de uso, metricas de produto, hipoteses validadas e invalidadas
- Vocabulario do dominio do produto

**Nao pertence**
- Como foi implementado (→ TEC) · estado de uma tarefa (→ OPR)
- Estrategia da empresa (→ EST) · licao generalizavel alem do produto (→ APR)

**Regra de escrita:** hipotese entra marcada como hipotese, com o teste que a confirmaria.
Hipotese invalidada **nao e apagada** — e marcada, com o que se aprendeu (MM-09).

---

### 3.3 TEC — Memoria Tecnica

| Campo | Definicao |
|---|---|
| **Proposito** | Guardar como o sistema esta construido e, sobretudo, **por que assim** — para que a proxima mudanca nao repita analise ja feita. |
| **Dono** | DEP-ENG |
| **Escreve** | DEP-ENG; DEP-TLS (dependencias externas); DEP-QAR (achados estruturais) |
| **Le** | DEP-ENG (antes de qualquer mudanca), DEP-QAR, DEP-OPS |
| **Volatilidade** | Media |
| **TTL** | Vida do componente que descreve |
| **Localizacao** | `memory/tecnica/` |

**Pertence a esta camada**
- Arquitetura vigente, componentes e suas fronteiras
- Padroes tecnicos adotados e proibidos
- Justificativa das escolhas tecnicas (aponta para os ADRs, MM-07)
- Modelo de dados e contratos de integracao
- Divida tecnica conhecida: o que e, por que foi assumida, o que custa
- Restricoes tecnicas, limites conhecidos, armadilhas do stack
- Dependencias externas e seu risco
- Caminhos ja tentados e descartados, com o motivo

**Nao pertence**
- O que construir (→ PRD) · incidente ou estado corrente (→ OPR)
- Licao generalizavel para outros contextos (→ APR) · credencial (proibido, PI-08)

**Regra de escrita:** registro tecnico sem o **porque** e incompleto. "Usamos X" nao e
memoria tecnica; "usamos X porque Y, tendo descartado Z por W" e.

---

### 3.4 OPR — Memoria Operacional

| Campo | Definicao |
|---|---|
| **Proposito** | Guardar o estado corrente da execucao: o que esta em curso, o que esta bloqueado, o que acabou de acontecer. |
| **Dono** | DEP-OPS |
| **Escreve** | Todos os departamentos |
| **Le** | DEP-EXE (para priorizar), todos (para saber onde estao) |
| **Volatilidade** | **Alta** — e a unica camada projetada para ser efemera |
| **TTL** | **1 ciclo**, renovavel enquanto o item estiver ativo |
| **Localizacao** | `memory/operacional/` |

**Pertence a esta camada**
- Trabalho em curso, fila e alocacao vigente
- Estado de portoes, handoffs pendentes, bloqueios
- Runbooks e procedimentos operacionais correntes
- Incidentes operacionais abertos e recentes
- Registro de backups, verificacoes e execucoes de rotina
- Consumo, custo e limites do ciclo corrente
- Excecoes formais vigentes e seus prazos

**Nao pertence**
- Nada que precise sobreviver ao ciclo sem ser promovido
- Decisao (→ ADR) · licao (→ APR) · fato duravel sobre o produto (→ PRD) ou o sistema (→ TEC)

**Regra de escrita:** OPR e a unica camada onde **expiracao e o comportamento padrao**.
Item que ainda importa ao fim do ciclo e **promovido** (§5) ou renovado com justificativa.
Item que expira sem promocao e presumidamente irrelevante — e essa presuncao e desejada.

> Sem TTL agressivo em OPR, a memoria vira log; log vira ruido; ruido aumenta contexto e
> derruba a qualidade de todo o resto (MM-05, PI-14).

---

### 3.5 APR — Memoria de Aprendizado

| Campo | Definicao |
|---|---|
| **Proposito** | Converter experiencia em capacidade: o que funcionou, o que falhou, e o que a proxima ocorrencia precisa saber. |
| **Dono** | DEP-KMS |
| **Escreve** | DEP-KMS, a partir de contribuicao obrigatoria de todos os departamentos |
| **Le** | Todos, obrigatoriamente antes de iniciar trabalho semelhante (QG-0) |
| **Volatilidade** | Media — um aprendizado vale ate ser refutado |
| **TTL** | Ate refutacao ou promocao |
| **Localizacao** | `memory/aprendizado/` |

**Pertence a esta camada**
- Postmortems de incidentes: causa, efeito, correcao de causa
- Padroes que funcionaram e em que condicoes
- Antipadroes: o que falhou, por que, e como reconhecer cedo
- Heuristicas de estimativa e de risco calibradas pela experiencia
- Retrospectivas de ciclo e de projeto
- Calibracao de execucao: que tipo de instrucao produz bom resultado
- Ganhos de especializacao constatados ou nao confirmados (PI-14)
- Erros de conformidade e sua causa raiz

**Nao pertence**
- Relato de evento sem licao extraida (isso e OPR)
- Opiniao sem evidencia · norma (→ EST) · decisao (→ ADR)

**Estrutura obrigatoria de um registro APR**

```markdown
## Situacao        o contexto em que aconteceu
## Observado       o que de fato ocorreu (fato, nao interpretacao)
## Causa           por que ocorreu — causa, nao sintoma
## Licao           o que se conclui, de forma generalizavel
## Condicoes       quando esta licao se aplica — e quando NAO se aplica
## Acao            o que muda daqui em diante, e quem e o dono da mudanca
## Confianca       alta | media | baixa — e com base em quantas ocorrencias
```

**Regra de escrita:** aprendizado sem a secao **Condicoes** e perigoso — vira regra
universal a partir de caso unico. Aprendizado sem **Acao** e observacao, nao aprendizado.

---

## 4. Criterio de Alocacao

Fluxograma de decisao para saber onde um registro pertence. **Primeira resposta afirmativa
define a camada** (garante MM-01).

```
1. Isso define quem somos, para onde vamos ou como decidimos?
      SIM -> EST
2. Isso descreve o que construimos, para quem, ou por que vale a pena?
      SIM -> PRD
3. Isso descreve como algo esta construido e por que assim?
      SIM -> TEC
4. Isso e uma licao generalizavel extraida de experiencia vivida?
      SIM -> APR
5. Isso descreve o estado corrente da execucao?
      SIM -> OPR
6. Nenhuma das anteriores
      -> NAO E MEMORIA. Descartar ou converter no instrumento adequado.
```

### 4.1 Casos ambiguos resolvidos

| Registro | Camada | Por que |
|---|---|---|
| "Escolhemos PostgreSQL porque X" | TEC | Descreve construcao e justificativa |
| "Migracao de banco falhou por falta de dry-run" | APR | Licao generalizavel |
| "Migracao esta agendada para amanha" | OPR | Estado corrente |
| "O produto nao fara gestao de estoque" | PRD | Escopo negativo do produto |
| "Nunca migramos sem backup verificado" | EST | Virou norma da organizacao |
| "Cliente pediu exportacao em Excel" | PRD | Sinal sobre o produto |
| "Backup de ontem verificado com sucesso" | OPR | Registro de rotina, expira |
| "Estimativas de ENG saem 40% otimistas" | APR | Heuristica calibrada |
| "Divisao de DEP-X em dois nao reduziu contexto" | APR | Ganho de PI-14 nao confirmado |

### 4.2 Regra do fato duplicado
Se o mesmo fato parece pertencer a duas camadas, ele esta mal formulado. DEP-KMS o
decompoe em fatos distintos, cada um em sua camada, ligados por referencia. **Copiar entre
camadas e proibido** (MM-01, FND-03 §7.1).

## 5. Promocao e Rebaixamento

Memoria nao e estatica: registros sobem de camada quando se confirmam e descem quando
perdem generalidade.

### 5.1 Caminhos de promocao

```
  OPR ──(o fato sobreviveu ao ciclo e importa)──> PRD | TEC
  OPR ──(a experiencia rendeu licao)───────────> APR
  APR ──(a licao se confirmou e passou a ser regra)──> EST
  APR ──(a licao e especifica de um produto)───> PRD
  APR ──(a licao e especifica do sistema)──────> TEC
  PRD | TEC ──(virou principio da organizacao)──> EST
```

### 5.2 Criterios de promocao

| Promocao | Criterio obrigatorio |
|---|---|
| **para OPR** | Nenhum. E a camada de entrada. |
| **OPR → PRD/TEC** | O fato continua verdadeiro fora do ciclo em que nasceu, e tem dono. |
| **OPR/qualquer → APR** | Ha licao com causa identificada e acao definida. |
| **APR → EST** | A licao se confirmou em **≥ 2 ocorrencias independentes**, ou foi determinada pelo Soberano. Exige ADR. |
| **qualquer → EST** | **Sempre** exige ADR aprovado. Nunca ha promocao automatica para EST. |

### 5.3 Rebaixamento e revogacao

| Situacao | Acao |
|---|---|
| Licao APR refutada por evidencia nova | Marcada como `superado`, com o registro que a refutou. Nunca apagada (MM-09). |
| Registro TEC descreve componente extinto | Vai a `arquivado`, preservando o porque da escolha original. |
| Registro PRD de produto encerrado | Arquivado junto com a memoria do produto. |
| Registro EST superado por emenda | `superado`, com o ADR da emenda e a versao anterior preservada. |
| Registro OPR nao promovido no fim do ciclo | **Expira.** Comportamento padrao e desejado. |

### 5.4 Regra de nao promocao apressada
Promover cedo demais e pior que nao promover: coloca em camada estavel algo que ainda muda,
e obriga a organizacao a tratar como regra o que ainda e hipotese. Na duvida, **mantem-se no
nivel mais baixo** — o simetrico exato de GV-03, que na duvida escolhe a classe mais alta.

## 6. Formato do Registro de Memoria

```yaml
---
id: MEM-<CAMADA>-<NNNN>-<slug>
titulo: <titulo legivel>
tipo: memoria
versao: <semver>
status: <rascunho|ativo|superado|arquivado|revogado>
camada_memoria: <estrategica|produto|tecnica|operacional|aprendizado>
autor: <DEP-xxx | SOBERANO>
proprietario: <DEP-xxx dono da camada>
aprovador: <DEP-KMS | DEP-GOV se EST>
criado_em: <AAAA-MM-DD>
atualizado_em: <AAAA-MM-DD>
revisao_prevista: <AAAA-MM-DD | null>
decisoes_relacionadas: [<ADR-id>, ...]
substitui: []
substituido_por: null
# campos proprios de memoria
origem: <MSG-id | INC-id | PRJ-id | ADR-id | observacao direta>
evidencia: <como se sabe que e verdade>
confianca: alta | media | baixa
ocorrencias: <quantas vezes observado>
ttl: <AAAA-MM-DD | permanente>
aplica_se_a: [<PRO-id>, <DEP-id>, global]
---
```

### 6.1 Corpo

```markdown
# <Titulo>

## Proposito     por que este registro existe
## Escopo        a que se aplica e a que nao se aplica
## Responsaveis  dono, curador, quem deve ler

## Conteudo      o registro em si (estrutura propria da camada)
## Proveniencia  de onde veio, com referencia por ID
## Relacionados  [[MEM-...]], ADRs e artefatos ligados
```

### 6.2 Regras de formato
| # | Regra |
|---|---|
| FM-01 | `evidencia` vazia ⇒ `confianca: baixa` obrigatoriamente. |
| FM-02 | `ttl` obrigatorio em OPR. Ausente ⇒ registro invalido. |
| FM-03 | `aplica_se_a: global` em camada nao-EST exige justificativa no corpo. |
| FM-04 | Registro sem `origem` e nao confiavel e nao pode ser usado como base de decisao (MM-02). |
| FM-05 | Relacionamento e feito por ID; conteudo de outro registro nunca e recolado (MM-01). |

## 7. Conflito, Contradicao e Correcao

### 7.1 Resolucao de conflito

| Situacao | Regra |
|---|---|
| Registros de camadas diferentes se contradizem | Vence a camada de **autoridade menor em numero** (§2.1): EST > PRD > TEC > APR > OPR. |
| Registros da mesma camada se contradizem | Vence o mais recente **se** tiver evidencia igual ou melhor. Senao, DEP-KMS escala ao dono da camada. |
| Memoria contradiz ADR vigente | **ADR vence** (MM-07). A memoria e corrigida e o erro vira registro APR. |
| Memoria contradiz a Fundacao | **Fundacao vence** (PI-02). Abre-se incidente de conformidade. |
| Conflito irreconciliavel | DEP-KMS escala: dono da camada → DEP-GOV → Soberano. |

**Regra dura:** contradicao detectada e **sempre** registrada, mesmo quando resolvida
trivialmente. Contradicao silenciosamente corrigida perde a informacao de por que existia.

### 7.2 Deteccao
DEP-KMS varre a memoria em busca de: duplicatas, contradicoes, registros sem proveniencia,
TTL vencido, referencias quebradas e registros nunca recuperados. Achado vira correcao,
promocao, expiracao ou proposta de mudanca — nunca observacao sem destino.

### 7.3 Correcao append-first (MM-09)
Memoria errada **nao e apagada**. Cria-se o registro correto, o antigo passa a `superado`
apontando para ele, e — quando o erro tiver causa relevante — abre-se registro APR sobre
por que a organizacao acreditou no que era falso.

Excecao unica: dado que **nao poderia ter sido gravado** (credencial, dado sensivel, PI-08)
e removido imediatamente, com incidente de conformidade registrado em seu lugar.

## 8. Recuperacao (Recall)

Memoria que nao e recuperada no momento certo nao existe na pratica.

### 8.1 Quando consultar e obrigatorio

| Momento | Camadas obrigatorias |
|---|---|
| QG-0 — antes de iniciar qualquer trabalho | APR + a camada do dominio |
| Antes de decidir (C2/C3) | EST + APR + camada do dominio |
| Antes de construir | PRD + TEC |
| Antes de aceitar entrega (QG-3) | PRD (criterios) + APR (falhas conhecidas) |
| Antes de comunicar externamente | EST + PRD |
| Antes de especializar (PI-14) | APR (ganhos ja constatados ou frustrados) |
| Antes de criar qualquer componente | EST — catalogo de Capabilities, para declarar o vinculo (VC-01), **e Meta Model, para confirmar que o tipo existe** (MT-01) |
| Antes de encerrar mudanca C2/C3 | APR — degradacoes ja constatadas; EST — Meta Model, para a verificacao de aptidao (QG-6) |

### 8.2 Regras de recuperacao
| # | Regra |
|---|---|
| RC-01 | Recuperacao devolve **contexto minimo suficiente** (MM-08, CM-04), no formato de Pacote de Contexto (FND-05 §5). |
| RC-02 | Item recuperado vem com `confianca` e `origem`. Consumir memoria sem olhar a confianca e erro do consumidor. |
| RC-03 | "Nao encontrei" e resposta valida e obrigatoria. Inventar memoria e LV-12. |
| RC-04 | Registro repetidamente recuperado para o mesmo fim e candidato a promocao ou a virar Skill (PI-14). |
| RC-05 | Registro nunca recuperado ao longo de um horizonte e candidato a expiracao. |

## 9. Higiene e Curadoria

| Rotina | Frequencia | Executa | Verifica |
|---|---|---|---|
| Expiracao de OPR | Fim de cada ciclo | DEP-KMS | TTL vencido; promove o que sobrevive |
| Colheita de aprendizado | Fim de cada ciclo | DEP-KMS | Todo trabalho encerrado gerou registro APR (QG-5) |
| Deteccao de duplicata | Periodica | DEP-KMS | Mesmo fato em dois lugares |
| Deteccao de contradicao | Periodica | DEP-KMS | Registros incompativeis |
| Revisao de confianca | Por horizonte | DEP-KMS | Confianca ainda corresponde as evidencias |
| Candidatos a promocao | Por horizonte | DEP-KMS + dono da camada | O que se confirmou e deve subir |
| Poda de nao recuperados | Por horizonte | DEP-KMS | O que nunca foi util (RC-05) |
| Auditoria de proveniencia | Por horizonte | DEP-GOV | Registros sem origem ou evidencia |

### 9.1 Sinal de saude
| Metrica | Direcao |
|---|---|
| % de registros com proveniencia completa | → 100% |
| % de trabalhos encerrados com registro APR | → 100% |
| Registros OPR vencidos e nao tratados | → 0 |
| Contradicoes abertas | → 0 |
| Taxa de recuperacao (registros usados / existentes) | ↑ |
| Volume de contexto por consulta | ↓ (PI-14) |

> Memoria que so cresce e sintoma de curadoria ausente. Uma memoria saudavel **encolhe em
> volume e cresce em densidade**.

## 10. Evolucao da Arquitetura de Memoria (PI-14)

Esta arquitetura tambem se especializa. Gatilhos e limites:

| Gatilho | Movimento | Instrumento |
|---|---|---|
| Uma camada acumula registros de naturezas nitidamente distintas | Sub-particionar a camada por dominio (`memory/tecnica/<dominio>/`) | C2 |
| Uma consulta recorrente exige montar sempre o mesmo recorte | Criar Pacote de Contexto nomeado; se recorrer, vira Skill | C2 |
| O mesmo tipo de registro e produzido repetidamente | Criar template proprio para o tipo | C2 |
| Volume de contexto por consulta sobe ciclo apos ciclo | Endurecer TTL e poda antes de criar estrutura nova | C1 |

### 10.1 Invariantes que a evolucao nao pode quebrar

| # | Invariante |
|---|---|
| MI-01 | Continuam existindo **exatamente cinco camadas**. Sub-particao ocorre **dentro** de uma camada, nunca criando uma sexta. |
| MI-02 | A ordem de autoridade (§2.1) e imutavel salvo emenda C3. |
| MI-03 | MM-01 (um fato, um lugar) sobrevive a qualquer particionamento. |
| MI-04 | Promocao para EST continua exigindo ADR, sempre. |
| MI-05 | Proveniencia continua obrigatoria em qualquer estrutura nova. |

Criar uma sexta camada e mudanca **C3** e exige emenda constitucional — a divisao em cinco
camadas e parte da identidade da arquitetura, nao detalhe de organizacao.

---

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-GOV | Arquitetura inicial: 5 camadas, criterio de alocacao, promocao, curadoria. Ratificada por ADR-0001. |
| 1.1.0 | 2026-07-28 | DEP-GOV | Emenda por ADR-0002: catalogo de Capabilities passa a integrar a camada EST; consulta obrigatoria antes de criar componente. |
| 1.2.0 | 2026-07-28 | DEP-GOV | Emenda por ADR-0003 e ADR-0004: o Meta Model passa a integrar a camada EST; consulta obrigatoria ao tipo antes de criar componente e antes de encerrar mudanca C2/C3. |
| 1.3.0 | 2026-07-28 | DEP-GOV | Emenda C2 por **ADR-0010**: §3.1 remete ao Contrato de Conhecimento sobre o Soberano, que governa as restricoes permanentes e os padroes duraveis de preferencia do Soberano ja alocados a esta camada. Nenhuma camada, regra de alocacao ou invariante e alterada. Frontmatter passa a declarar os cinco campos do contrato de artefato (AC-08, ADR-0009). |
