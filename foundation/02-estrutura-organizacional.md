---
id: FND-02
titulo: Estrutura Organizacional do LucaX Enterprise OS
tipo: fundacao
versao: 1.4.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-EXE
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-30
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0001, ADR-0002, ADR-0003, ADR-0004, ADR-0016, ADR-0024]
substitui: []
substituido_por: null
resumo: Define 9 departamentos em 4 classes, matriz de interacao e a escada de especializacao.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: ratificada
---

# Estrutura Organizacional

## Proposito

Definir a arquitetura organizacional do LucaX Enterprise OS em alto nivel: quais
departamentos existem, o que cada um possui, a quem responde, como se relacionam, onde
comeca e termina o escopo de cada um, e como conflitos entre areas sao resolvidos.

Este documento define **estrutura**, nao implementacao. Nao cria agentes, nao atribui
modelos, nao define prompts, nao descreve ferramentas.

## Escopo

| Item | Definicao |
|---|---|
| **Inclui** | Niveis hierarquicos, classes de departamento, carta resumida de cada departamento, matriz de interacao, regras de fronteira, resolucao de conflito, criacao e extincao de departamento. |
| **Nao inclui** | Agentes, subagentes, prompts, modelos, ferramentas, automacoes, infraestrutura, cronogramas. |
| **Subordinado a** | [FND-01 Constituicao](01-constituicao.md). |
| **Consumido por** | Todas as fases futuras. Nenhum agente pode ser criado fora de um departamento definido aqui. |

## Responsaveis

| Papel | Responsavel |
|---|---|
| Proprietario do documento | DEP-EXE (Gabinete Executivo) |
| Guardiao normativo | DEP-GOV |
| Aprovador de mudanca estrutural | SOBERANO |
| Obrigados | Todos os departamentos |

---

## 1. Principios da Estrutura

| # | Principio estrutural | Consequencia |
|---|---|---|
| ES-01 | **Escopo exclusivo.** Toda responsabilidade tem exatamente um dono. | Nao existe responsabilidade compartilhada sem dono nomeado. |
| ES-02 | **Independencia da guarda.** Quem verifica nao responde a quem produz. | DEP-GOV e DEP-QAR nao se subordinam a linha. |
| ES-03 | **Departamento e escopo, nao pessoa.** Departamento existe por dominio de responsabilidade. | Departamento nao e criado por volume de trabalho. |
| ES-04 | **Estrutura minima suficiente.** Nao se cria area sem responsabilidade orfa que a justifique. | Funcao nova nasce dentro de departamento existente ate provar que precisa sair. |
| ES-04b | **Especializacao por evidencia (PI-14).** Constatado ganho de organizacao, reuso ou reducao de contexto, dividir e obrigacao — nao opcao. | Estrutura e revista periodicamente; generalismo por inercia e defeito, nao neutralidade. |
| ES-05 | **Interface explicita.** Areas trocam contratos, nao suposicoes. | Toda interacao entre departamentos tem formato definido em FND-05. |
| ES-06 | **Sem hierarquia oculta.** Autoridade so existe se estiver escrita. | Nenhum departamento manda em outro por costume. |
| ES-07 | **Plataforma serve, nao decide pela linha.** | Areas de plataforma habilitam; nao definem produto. |

## 2. Niveis Hierarquicos

```
NIVEL 0 — SOBERANIA
   Soberano (Lucas, humano)
   Autoridade final, indelegavel. Define direcao, ratifica, arbitra, veta.
        |
NIVEL 1 — COMANDO
   DEP-EXE  Gabinete Executivo
   Traduz direcao em prioridade, aloca capacidade, orquestra, cobra resultado.
        |
        +----------------------------------------------------------+
        |                                                          |
NIVEL 2 — GUARDA (independente da linha)          NIVEL 2 — LINHA (entrega valor)
   DEP-GOV  Governanca e Conformidade                DEP-PRD  Produto e Estrategia
   DEP-QAR  Qualidade e Risco                        DEP-ENG  Engenharia
   Respondem ao Nivel 0/1. Poder de veto.            DEP-OPS  Operacoes
                                                     DEP-GRW  Crescimento e Receita
        |
NIVEL 2 — PLATAFORMA (serve todos os departamentos)
   DEP-KMS  Conhecimento e Memoria
   DEP-TLS  Ferramentas e Integracoes
        |
NIVEL 3 — EXECUCAO
   Agentes e subagentes, sempre vinculados a exatamente um departamento.
   (Criados em fase futura. Nao existem nesta fase.)
```

### 2.1 Classes de departamento

| Classe | Funcao | Departamentos | Pode vetar? | Responde a |
|---|---|---|---|---|
| **Comando** | Priorizar, alocar, orquestrar, cobrar | DEP-EXE | Nao (decide, nao veta) | Nivel 0 |
| **Guarda** | Verificar conformidade e qualidade | DEP-GOV, DEP-QAR | **Sim** | Nivel 0 diretamente |
| **Linha** | Produzir e entregar valor | DEP-PRD, DEP-ENG, DEP-OPS, DEP-GRW | Nao | DEP-EXE |
| **Plataforma** | Habilitar as demais areas | DEP-KMS, DEP-TLS | Nao | DEP-EXE |

**Regra de independencia (ES-02):** um departamento de Guarda nunca e avaliado, priorizado
ou instruido por um departamento de Linha. Veto de Guarda so cai por decisao registrada do
Soberano (LV-09).

## 3. Cartas Resumidas dos Departamentos

Cada departamento tera Carta completa em fase futura, seguindo `TPL-carta-departamento`.
Abaixo, a definicao estrutural minima e vinculante desde ja.

---

### DEP-EXE — Gabinete Executivo
**Classe:** Comando · **Nivel:** 1 · **Autonomia:** A3 · **Responde a:** Soberano

| Campo | Definicao |
|---|---|
| **Missao** | Converter a direcao do Soberano em prioridade executavel e garantir que a organizacao entregue o que foi priorizado. |
| **Possui (dono unico de)** | Portfolio ativo, fila de prioridades, alocacao de capacidade, cadencia organizacional, arbitragem entre departamentos de Linha, orcamento de recursos e custos. |
| **Decide** | O que entra e sai da fila; quem executa o que; quando um ciclo abre e fecha; empate entre areas de Linha. |
| **Nao decide** | Conteudo tecnico (DEP-ENG), escopo de produto (DEP-PRD), padrao de qualidade (DEP-QAR), norma (DEP-GOV). |
| **Entrega** | Prioridade vigente, briefing de trabalho, relatorio consolidado ao Soberano, decisao de arbitragem. |
| **Escala ao Soberano quando** | Decisao Tipo 1; conflito com norma; mudanca de portfolio; veto de Guarda que se pretende reverter. |
| **Funcao interna: Recursos (FIN)** | Acompanha custo, consumo e limites. Promovivel a departamento proprio via ADR quando a carga justificar (ES-04). |

---

### DEP-GOV — Governanca e Conformidade
**Classe:** Guarda · **Nivel:** 2 · **Autonomia:** A2 · **Responde a:** Soberano

| Campo | Definicao |
|---|---|
| **Missao** | Manter a integridade normativa do sistema e garantir que nada exista sem rastreabilidade e responsavel. |
| **Possui (dono unico de)** | Constituicao e Fundacao, taxonomia, registro de ADRs e RFCs, cadastro de Cartas, registro de excecoes formais, incidentes de conformidade, auditoria documental. |
| **Decide** | Se um artefato esta em conformidade; qual instrumento uma mudanca exige; se uma proposta contraria norma vigente. |
| **Poder de veto** | **Sim** — bloqueia qualquer componente sem Carta, sem rastreabilidade ou em violacao de norma. |
| **Nao decide** | Merito tecnico, escopo de produto, prioridade. Julga forma e conformidade, nao conteudo. |
| **Entrega** | Parecer de conformidade, numeracao oficial de decisoes, registro de excecoes, auditoria periodica. |
| **Escala ao Soberano quando** | Violacao de Principio Imutavel ou Linha Vermelha; pedido de excecao formal; proposta de emenda. |

---

### DEP-QAR — Qualidade e Risco
**Classe:** Guarda · **Nivel:** 2 · **Autonomia:** A2 · **Responde a:** Soberano

| Campo | Definicao |
|---|---|
| **Missao** | Garantir que o que sai da organizacao esteja correto, seguro e defensavel — por verificacao independente, nao por confianca. |
| **Possui (dono unico de)** | Definicao de Pronto aplicada, portoes QG-3 e QG-4, revisao adversarial, analise de risco, seguranca e privacidade, verificacao de evidencia, criterio de aceite de entrega. |
| **Decide** | Se um artefato passa ou e devolvido; qual o nivel de risco de uma mudanca; o que exige aprovacao humana por risco. |
| **Poder de veto** | **Sim** — barra entrega que nao atende o DoD ou que apresenta risco nao mitigado. |
| **Nao decide** | O que construir, como priorizar, qual arquitetura adotar. Julga o resultado, nao a intencao. |
| **Entrega** | Parecer de revisao, laudo de risco, lista de defeitos, veto fundamentado, verificacao de backup e reversao. |
| **Escala ao Soberano quando** | Risco Tipo 1; exposicao de dado vivo; credencial comprometida; veto contestado pela Linha. |

---

### DEP-PRD — Produto e Estrategia
**Classe:** Linha · **Nivel:** 2 · **Autonomia:** A2 · **Responde a:** DEP-EXE

| Campo | Definicao |
|---|---|
| **Missao** | Definir o que deve existir e por que, transformando intencao em problema bem formulado e resultado verificavel. |
| **Possui (dono unico de)** | Descoberta, definicao de problema, personas e publico, specs e requisitos, criterios de aceite funcionais, roadmap de produto, priorizacao dentro do produto, portao QG-1. |
| **Decide** | Escopo do produto, o que fica fora, ordem de valor, quando um requisito esta suficientemente definido. |
| **Nao decide** | Como implementar (DEP-ENG), se a entrega passa (DEP-QAR), se o produto entra no portfolio (Soberano). |
| **Entrega** | Spec, criterio de aceite, roadmap, definicao de sucesso do produto, decisao de escopo registrada. |
| **Escala ao Soberano quando** | Criacao ou encerramento de produto; mudanca de posicionamento; conflito entre valor e principio. |

---

### DEP-ENG — Engenharia
**Classe:** Linha · **Nivel:** 2 · **Autonomia:** A2 · **Responde a:** DEP-EXE

| Campo | Definicao |
|---|---|
| **Missao** | Construir a solucao mais simples defensavel que satisfaz a spec, e sustenta-la tecnicamente ao longo do tempo. |
| **Possui (dono unico de)** | Arquitetura, padroes tecnicos, decisoes de implementacao, modelagem de dados, integracoes internas, divida tecnica, portao QG-2, viabilidade e estimativa. |
| **Decide** | Como construir; qual arquitetura e padrao adotar; o que e viavel; qual divida assumir conscientemente. |
| **Nao decide** | O que construir (DEP-PRD), se a entrega e aceita (DEP-QAR), qual ferramenta externa e adotada oficialmente (DEP-TLS). |
| **Entrega** | ADR tecnico, desenho de arquitetura, implementacao, estimativa, avaliacao de viabilidade, registro de divida. |
| **Escala ao Soberano quando** | Decisao arquitetural Tipo 1; migracao ou reescrita; risco de perda de dado. |

---

### DEP-OPS — Operacoes
**Classe:** Linha · **Nivel:** 2 · **Autonomia:** A2 · **Responde a:** DEP-EXE

| Campo | Definicao |
|---|---|
| **Missao** | Manter em funcionamento o que ja existe e executar o trabalho recorrente com previsibilidade. |
| **Possui (dono unico de)** | Estado corrente de execucao, runbooks, rotinas recorrentes, monitoramento, incidentes operacionais, backups e sua verificacao, suporte, continuidade. |
| **Decide** | Como executar a rotina; quando acionar incidente; ordem de atendimento operacional. |
| **Nao decide** | Mudanca estrutural do que opera; padrao de qualidade; prioridade de portfolio. |
| **Entrega** | Runbook, status operacional, registro e postmortem de incidente, confirmacao de backup, relatorio de continuidade. |
| **Escala ao Soberano quando** | Incidente com perda ou exposicao de dado; falha de backup; indisponibilidade material. |

---

### DEP-GRW — Crescimento e Receita
**Classe:** Linha · **Nivel:** 2 · **Autonomia:** A1 · **Responde a:** DEP-EXE

| Campo | Definicao |
|---|---|
| **Missao** | Levar o que foi construido ate quem tem o problema, e converter isso em resultado sustentavel. |
| **Possui (dono unico de)** | Posicionamento, mensagem e narrativa, canais, conteudo, aquisicao, modelo de monetizacao, metricas de receita e retencao, relacao com o publico. |
| **Decide** | Como comunicar, por qual canal, com qual mensagem, sob qual metrica. |
| **Nao decide** | O que o produto e (DEP-PRD), o que pode ser prometido tecnicamente (DEP-ENG), o que pode ser exposto (DEP-QAR + Soberano). |
| **Entrega** | Posicionamento, plano de canal, conteudo, relatorio de aquisicao e receita. |
| **Escala ao Soberano quando** | Qualquer comunicacao externa em nome do sistema; uso de dado de terceiros; compromisso publico. |
| **Nota de autonomia** | Opera em A1 por default: toda saida externa passa por aprovacao humana (PI-01, LV-08). |

---

### DEP-KMS — Conhecimento e Memoria
**Classe:** Plataforma · **Nivel:** 2 · **Autonomia:** A2 · **Responde a:** DEP-EXE

| Campo | Definicao |
|---|---|
| **Missao** | Fazer com que a organizacao lembre: capturar, organizar, curar e devolver o conhecimento certo no momento certo. |
| **Possui (dono unico de)** | Arquitetura da memoria, curadoria das cinco camadas, promocao e expiracao de registros, camada de Aprendizado, indice organizacional, deteccao de duplicidade e contradicao, portao QG-5. |
| **Decide** | Onde um registro pertence; o que e promovido, arquivado ou expirado; quando dois registros se contradizem. |
| **Nao decide** | O merito do conteudo registrado. Cura a memoria, nao a substitui pela sua opiniao. |
| **Entrega** | Registro curado, sintese de aprendizado, indice, alerta de contradicao, pacote de contexto para outra area. |
| **Escala ao Soberano quando** | Contradicao entre camada Estrategica e decisao vigente; perda de memoria; conflito irreconciliavel entre registros. |

---

### DEP-TLS — Ferramentas e Integracoes
**Classe:** Plataforma · **Nivel:** 2 · **Autonomia:** A1 · **Responde a:** DEP-EXE

| Campo | Definicao |
|---|---|
| **Missao** | Prover, avaliar e manter as capacidades externas que a organizacao usa, sem que ninguem improvise acesso. |
| **Possui (dono unico de)** | Catalogo de ferramentas e integracoes, criterio de adocao e descarte, limites de uso, gestao de acesso e segredo (por referencia), avaliacao de dependencia externa. |
| **Decide** | Qual ferramenta e oficial para qual finalidade; quando uma ferramenta e descartada; quais limites de uso se aplicam. |
| **Nao decide** | Como o produto usa a ferramenta no dominio; se o risco e aceitavel (DEP-QAR). |
| **Entrega** | Ficha de ferramenta, parecer de adocao, catalogo vigente, mapa de dependencia externa. |
| **Escala ao Soberano quando** | Adocao envolve custo recorrente, dado sensivel ou dependencia critica; credencial exposta. |
| **Nota de autonomia** | Opera em A1: adocao de ferramenta nova sempre precisa de aprovacao (PI-11 exige qualidade como criterio, mas a adocao e Tipo 1 por dependencia). |

---

## 4. Matriz de Interacao entre Departamentos

### 4.1 Legenda

Cada celula declara os atos que o departamento da **linha** (**De**) pratica sobre o
departamento da **coluna** (**Para**). A leitura e **sempre direcional**: a celula (X, Y)
**nada afirma** sobre a celula (Y, X).

| Codigo | Ato de X sobre Y | O que significa, exatamente |
|---|---|---|
| **E** | **entrega para** | X produz e transfere a Y artefato, resultado ou evidencia |
| **C** | **consulta obrigatoria** | X nao conclui o ato sem ouvir Y. O parecer de Y **nao vincula**; **nao ouvir Y invalida o ato** |
| **V** | **pode vetar** | X barra o ato de Y. Y **nao executa** enquanto o veto vigorar. So o SOBERANO o reverte (LV-09) |
| **A** | **aprova** | X **homologa** o ato de Y dentro do rito (FND-01 §7.3). **Nao e ratificacao** e nao da vigencia |
| **R** | **revisa de forma independente** | X e o revisor independente de FND-04 §3.1 sobre o produto de Y. **Nao e veto e nao e aprovacao** |
| **—** | **nenhum ato direto** | X **nao** pratica ato estrutural direto sobre Y. **Nada afirma** sobre o que Y pratica sobre X |

**Uma celula pode conter mais de um codigo**, separados por espaco, quando a relacao e
composta. A ordem dos codigos **nao** e significativa. `—` nunca aparece acompanhado.

### 4.2 A matriz

| De \ Para | EXE | GOV | QAR | PRD | ENG | OPS | GRW | KMS | TLS |
|---|---|---|---|---|---|---|---|---|---|
| **EXE** | — | C | C | A | A | A | A | A E | A |
| **GOV** | E V | — | C R | V | V | V | V | E V | V |
| **QAR** | E V | C R | — | V | V | V | V | E C V | V |
| **PRD** | E | C | C | — | E | C | E C | E | C |
| **ENG** | E | C | C | C | — | E | — | E | C |
| **OPS** | E | C | C | C | E C | — | — | E | C |
| **GRW** | E | C | C | C E | — | — | — | E | C |
| **KMS** | E | C | E C | E | E | E | E | — | C |
| **TLS** | E | C | C | — | E C | E | — | E | — |

### 4.3 Regras de leitura

| # | Regra |
|---|---|
| **MI-01** | **A celula e a fonte; as leituras obrigatorias de §4.4 sao projecao dela** (ADR-0008, PJ-03). Em conflito entre celula e leitura, **prevalece a celula**, e o conflito se corrige **na leitura**, nunca na celula por conta propria. |
| **MI-02** | **A matriz nao concede autoridade: projeta a que FND-01 §7.3, FND-02 §2.1 e §3 e FND-09 §8.2 ja constituem.** Celula que divirja dessas fontes e **erro desta tabela**, e resolve-se a favor da fonte — mesmo desenho declarado em FND-09 §8.2. |
| **MI-03** | **O SOBERANO nao figura nesta matriz.** Autoridade que termina no Soberano le-se em FND-01 §7.3 e FND-09 §8.2, **nunca por ausencia aqui**. |
| **MI-04** | **Ausencia nao cria nem retira autoridade.** `—` significa ausencia de **ato direto de X sobre Y**, e nunca *"Y nao tem autoridade sobre X"*. |
| **MI-05** | **O veto da Guarda incide sobre o objeto, nao sobre a classe de quem o produziu** (§3, DEP-GOV e DEP-QAR). Por isso alcanca **as quatro classes**, o Comando inclusive. |
| **MI-06** | **`R` declara aqui apenas revisao independente estrutural e permanente entre dois departamentos.** O mapa completo de *quem revisa o que*, por entidade, vive em **FND-09 §8.2** e **nao** e reproduzido aqui (CM-09). |

### 4.4 Leituras obrigatorias

- **Todos entregam a KMS.** Nenhum trabalho termina sem registro na memoria (QG-5) — **o Comando inclusive**, contribuinte obrigatorio da camada APR.
- **Todos consultam GOV.** Conformidade e pre-requisito, nao revisao final.
- **GOV e QAR vetam qualquer departamento — Comando, Linha e Plataforma —, e nenhum departamento veta a Guarda.** So o SOBERANO reverte veto de Guarda (LV-09).
- **PRD entrega a ENG, nunca o inverso.** Direcao de produto flui em um sentido so.
- **GRW nao instrui ENG.** Promessa externa nao vira requisito sem passar por PRD.

### 4.5 Exemplos normativos

| # | Situacao | Celula | Efeito |
|---|---|---|---|
| **EX-1** | DEP-GOV detecta que uma priorizacao de DEP-EXE abre componente **sem Carta** | `GOV → EXE` = **`E V`** | DEP-GOV **veta**; DEP-EXE **nao executa** e escala ao SOBERANO (§6, LV-09) |
| **EX-2** | DEP-QAR encontra **credencial em texto** em pacote de contexto de DEP-KMS | `QAR → KMS` = **`E V`** | Veto imediato, escalonamento **E4**, execucao bloqueada (PI-08, LV-02) |
| **EX-3** | DEP-KMS entrega evidencia medida a DEP-QAR **e** o consulta sobre um defeito | `KMS → QAR` = **`E C`** | **Uma celula, dois atos.** Nenhuma ambiguidade e **nenhuma autoridade nova** |
| **EX-4** | DEP-PRD precisa de capacidade externa e consulta DEP-TLS | `PRD → TLS` = **`C`** · `TLS → PRD` = **`—`** | A consulta e **direta e valida**. A ausencia no sentido inverso **nao** a apaga (**MI-04**) |
| **EX-5** | DEP-QAR revisa de forma independente artefato produzido por DEP-GOV | `QAR → GOV` = **`C R`** | Nao e veto nem aprovacao: e o revisor independente de FND-04 §3.1 (RM-06b) |

## 5. Fluxo Organizacional Padrao

```
  SOBERANO
     | direcao / intencao
     v
  DEP-EXE  ── QG-0 ──> prioriza, aloca, abre trabalho
     |
     v
  DEP-PRD  ── QG-1 ──> problema definido + spec + criterio de aceite
     |
     v
  DEP-ENG  ── QG-2 ──> arquitetura decidida (ADR) + construcao
     |
     v
  DEP-QAR  ── QG-3 ──> revisao independente: passa ou devolve
     |
     v
  DEP-QAR + SOBERANO ── QG-4 ──> liberacao para o mundo
     |
     +--> DEP-GRW  leva ao publico
     +--> DEP-OPS  opera e sustenta
     |
     v
  DEP-KMS  ── QG-5 ──> aprendizado extraido e gravado
     |
     v
  DEP-EXE  reporta ao Soberano e realimenta a fila

  DEP-GOV acompanha todo o fluxo: verifica rastreabilidade em cada portao.
  DEP-TLS habilita qualquer etapa que precise de capacidade externa.
```

Devolucao em QG-3 retorna ao departamento produtor, nunca ao inicio do fluxo — salvo
quando a causa e defeito de spec, caso em que retorna a DEP-PRD com registro do motivo.

## 6. Regras de Fronteira

| Situacao | Regra |
|---|---|
| Responsabilidade sem dono claro | DEP-EXE atribui provisoriamente e DEP-GOV registra; a atribuicao definitiva vira ADR. |
| Dois departamentos reivindicam a mesma responsabilidade | DEP-EXE arbitra. Se envolver norma, DEP-GOV decide a forma e DEP-EXE o merito. |
| Trabalho atravessa areas | O departamento dono do resultado final e o responsavel unico perante DEP-EXE. |
| Departamento precisa de capacidade que nao possui | Solicita a area dona por Handoff formal (FND-05). Nunca executa por conta propria. |
| Departamento discorda de veto da Guarda | Registra discordancia fundamentada e escala ao Soberano. Nao executa enquanto isso (LV-09). |
| Urgencia real | Aplica-se excecao formal (Constituicao 8.3). Urgencia nao dispensa registro. |

## 7. Conflito entre Departamentos

| Nivel | Tipo de conflito | Resolve | Prazo de resolucao |
|---|---|---|---|
| N1 | Operacional entre areas de Linha | As proprias areas, por acordo registrado | Mesmo ciclo |
| N2 | Escopo, prioridade ou recurso | DEP-EXE | Mesmo ciclo |
| N3 | Conformidade ou qualidade | DEP-GOV / DEP-QAR — decisao vinculante | Imediato |
| N4 | Norma, principio, portfolio ou Tipo 1 | Soberano | Ate decisao explicita |

Todo conflito de nivel N2 ou superior gera registro. Conflito recorrente entre as mesmas
areas e sintoma de fronteira mal desenhada e obriga proposta de ajuste estrutural via RFC.

## 8. Criacao, Alteracao e Extincao de Departamento

### 8.1 Criar
Um departamento novo so nasce quando **todas** as condicoes forem verdadeiras:

1. Existe responsabilidade real hoje sem dono, ou com dono que gera conflito de interesse.
2. A responsabilidade nao cabe em nenhum departamento existente sem distorcer o escopo dele.
3. A fronteira com os departamentos vizinhos e descritivel sem sobreposicao.
4. Ha criterio objetivo para dizer que o departamento esta funcionando.

Instrumento: **RFC → ADR → ratificacao do Soberano**. Classe C2 (ver FND-04).

### 8.2 Alterar
Mudanca de missao, de escopo exclusivo, de classe, de subordinacao ou de nivel de autonomia
e mudanca estrutural: exige ADR e atualizacao deste documento na mesma decisao.

### 8.3 Extinguir
Departamento e extinto quando sua responsabilidade deixa de existir ou e absorvida. A
extincao obriga: destino explicito de cada responsabilidade, destino da memoria produzida,
e ADR de encerramento. **Responsabilidade nao pode ficar orfa na extincao.**

### 8.4 Funcao antes de departamento
Responsabilidade nova comeca como **funcao nomeada dentro de um departamento existente**
(ES-04). So e promovida a departamento quando a funcao provar carga e fronteira proprias.
Exemplo vigente: funcao Recursos (FIN) dentro de DEP-EXE.

## 9. Evolucao da Estrutura (PI-14)

A estrutura descrita neste documento e o estado **atual**, nao o estado **final**. Ela e
projetada para se especializar continuamente.

### 9.1 Escada de especializacao

Toda responsabilidade sobe apenas o degrau que o ganho constatado justifica, e nunca pula
degraus. Descer a escada (consolidar) usa o mesmo rito.

```
  degrau 6  CAPABILITY      competencia permanente, independente de quem a exerce
     ^                      (camada distinta — ver nota abaixo)
  degrau 5  DEPARTAMENTO    dominio proprio, fronteira propria, poder de decisao proprio
     ^
  degrau 4  AGENTE          papel executor com Carta e autonomia declarada
     ^
  degrau 3  SUBAGENTE       recorte estreito dentro de um papel
     ^
  degrau 2  SKILL           procedimento reutilizavel por mais de um papel
     ^
  degrau 1  FUNCAO NOMEADA  responsabilidade batizada dentro de area existente
     ^
  degrau 0  TRABALHO DIFUSO ainda sem nome proprio
```

**Regra da escada:** subir um degrau exige demonstrar pelo menos um dos tres ganhos de
PI-14. Subir sem ganho constatado e proliferacao (FND-04, §6.1) e e recusado por DEP-GOV.

> **Nota sobre o degrau 6.** Capability **nao e um departamento maior** — e outra camada.
> Enquanto os degraus 1 a 5 respondem *"quem responde por isso?"*, o degrau 6 responde
> *"o que a organizacao sabe fazer?"*. A promocao a Capability nao ocorre por acumulo de
> carga, e sim quando a competencia se revela **independente da estrutura que a hospeda**:
> continua verdadeira ainda que todos os departamentos sejam reorganizados (FND-08 §1.1).
>
> Consequencia pratica: **toda Capability tem custodio em algum degrau 5**, e todo
> componente dos degraus 1 a 5 declara vinculo a ao menos uma Capability (FND-08 §8).
> As duas camadas se cruzam; nao se substituem.

> **Nota sobre a escada e o Meta Model (ADR-0003).** Esta escada trata de **instancias**:
> uma responsabilidade concreta sobe de funcao a agente, de agente a departamento. O Meta
> Model (FND-09) trata de **tipos**: se `AGENTE` pode existir como categoria, com que
> atributos e ligado a que. Subir um degrau desta escada nao cria tipo novo — usa um tipo ja
> declarado. Criar tipo novo tem escada propria, em FND-09 §11.2, e classe C3.

### 9.2 Gatilhos de especializacao

Quando um destes sinais aparece, a proposta de especializacao passa a ser **obrigatoria** —
seja para executa-la, seja para registrar por escrito a decisao de adia-la (PI-14, regra 2).

| Gatilho | Sinal observavel | Ganho correspondente | Movimento tipico |
|---|---|---|---|
| **Escopo heterogeneo** | A area e acionada por motivos que nao se parecem entre si | Organizacao | Dividir dominio |
| **Fronteira em disputa** | Conflito recorrente entre as mesmas duas areas (§7) | Organizacao | Redesenhar fronteira |
| **Duplicacao** | O mesmo procedimento e refeito em lugares diferentes | Reuso | Extrair Skill (degrau 2) |
| **Contexto excessivo** | Executar a tarefa exige carregar material que a tarefa nao usa | Reducao de contexto | Recortar Subagente (degrau 3) |
| **Gargalo de decisao** | Uma area vira fila para decisoes que nao sao dela | Organizacao | Devolver direito de decisao |
| **Carga concentrada** | Uma funcao consome a maior parte da capacidade da area hospedeira | Organizacao | Promover funcao a agente ou departamento |
| **Conhecimento ilhado** | Um resultado so sai bem quando um papel especifico atua | Reuso | Converter pratica em Skill ou registro |

### 9.3 Gatilhos de consolidacao (movimento simetrico)

Especializar sem reverter gera fragmentacao. Estes sinais obrigam proposta de reunificacao:

| Sinal | Interpretacao |
|---|---|
| Componente sem acionamento ao longo de um horizonte inteiro | A divisao nao correspondeu a demanda real |
| Duas areas que sempre atuam juntas e nunca isoladas | A fronteira entre elas nao existe de fato |
| Handoff que so transporta, sem transformar o trabalho | Etapa intermediaria sem valor proprio |
| Custo de coordenacao maior que o ganho declarado na criacao | O ganho previsto nao se confirmou |

### 9.4 Revisao estrutural periodica

| Item | Regra |
|---|---|
| Frequencia | A cada fechamento de horizonte e, no minimo, semestralmente |
| Executada por | DEP-GOV (forma) com DEP-EXE (merito) e DEP-KMS (evidencia da memoria) |
| Verifica | Gatilhos de §9.2 e §9.3; fronteiras em disputa; ganhos declarados que nao se confirmaram |
| Produz | Proposta de especializacao, proposta de consolidacao, ou registro fundamentado de "manter" |
| **Encerramento** | **Verificacao de Aptidao Arquitetural obrigatoria** (QG-6, FND-09 §10): a revisao estrutural so fecha com `FIT` emitido |
| Regra | Revisao que conclui "manter tudo" tres vezes seguidas e ela propria sinal de analise complacente e escala ao Soberano |

### 9.5 Invariantes que a evolucao nao pode quebrar

Por mais que a estrutura se especialize, estas propriedades permanecem verdadeiras:

| # | Invariante |
|---|---|
| IV-01 | A independencia da Guarda (ES-02) nunca e diluida por especializacao. |
| IV-02 | Toda responsabilidade continua tendo exatamente um dono (ES-01). |
| IV-03 | Nenhum componente novo nasce sem Carta (PI-12). |
| IV-04 | Profundidade maxima de subagente permanece 1 (FND-03, §3.4). |
| IV-05 | A cadeia de autoridade continua terminando no Soberano (PI-01). |
| IV-06 | Especializacao nunca elimina rastreabilidade: a divisao e registrada com origem e destino. |
| IV-07 | **Nenhuma competencia se perde na reorganizacao.** Extinguir ou dividir departamento transfere a custodia das Capabilities envolvidas; nunca as aposenta (FND-08 §1.3, OW-06). |
| IV-08 | Todo componente permanece vinculado a ao menos uma Capability, antes e depois da mudanca (FND-08 §8). |
| IV-09 | **Nenhum componente existe fora do Meta Model.** Especializar ou consolidar usa tipos ja declarados em FND-09 §5; criar tipo novo e mudanca C3 com rito proprio (FND-09 §11.1). |
| IV-10 | Toda mudanca estrutural encerra com Architecture Review **e** Verificacao de Aptidao Arquitetural (QG-6). |

## 10. Restricoes Explicitas desta Fase

Nesta fase de fundacao, **nao existem agentes**. A estrutura acima descreve dominios de
responsabilidade, nao executores.

> **Atualizacao por ADR-0002:** a extincao de departamento agora exige tambem destino
> explicito da **custodia** de cada Capability que ele detinha (IV-07). Competencia orfa e
> tao proibida quanto responsabilidade orfa.

| Proibido nesta fase | Permitido nesta fase |
|---|---|
| Criar agente ou subagente | Definir departamento e escopo |
| Atribuir modelo, prompt ou ferramenta | Definir a quem uma responsabilidade pertence |
| Criar workflow ou automacao | Definir portoes e fluxo organizacional |
| Criar codigo, infra ou banco | Definir interface entre areas |

Quando agentes forem criados (fase futura), cada um devera declarar em sua Carta:
departamento de origem, nivel de autonomia herdado ou restringido, escopo, o que **nao**
lhe compete, e **as Capabilities que exerce** (FND-08 §8.2).

---

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-GOV | Estrutura inicial: 9 departamentos em 4 classes. Ratificada por ADR-0001. |
| 1.1.0 | 2026-07-28 | DEP-GOV | Emenda por ADR-0002: degrau 6 (Capability) na escada de especializacao; invariantes IV-07 e IV-08; custodia obrigatoria no destino de extincao. |
| 1.2.0 | 2026-07-28 | DEP-GOV | Emenda por ADR-0003 e ADR-0004: nota distinguindo a escada de instancias da escada de tipos (FND-09 §11.2); revisao estrutural passa a encerrar com QG-6; invariantes IV-09 e IV-10. |
| 1.3.0 | 2026-07-29 | DEP-GOV | Emenda **C3** por **ADR-0016**, que fecha o achado **RD-02**: §4 passa a ter legenda **direcional e inequivoca** com o codigo **`R`** *(revisao independente)*, celulas **multivaloradas**, as regras de leitura **MI-01 a MI-06** e **cinco exemplos normativos**; **doze celulas** passam a declarar a relacao completa — quatro delas registram o **veto da Guarda sobre Comando e sobre DEP-KMS**, que a tabela nao representava; duas leituras obrigatorias sao corrigidas. **Nenhuma autoridade e criada:** MI-02 declara que a matriz **projeta** FND-01 §7.3, FND-02 §2.1 e §3 e FND-09 §8.2, e o veto da Guarda ja estava constituido em §3 e declarado em **14 afirmacoes** das nove Cartas. Nenhum principio imutavel, linha vermelha, hierarquia normativa, classe, portao ou departamento foi alterado. |
| 1.4.0 | 2026-07-30 | DEP-GOV | Emenda **C3** por **ADR-0024**: o **frontmatter** recebe os **cinco** campos que `AC-08` (FND-10 §2.5) exige de todo artefato emendado apos a vigencia de FND-10 — `resumo`, `perfil_contexto`, `confidencialidade`, `revisor` e `ratificacao` —, fechando **RD-27 quanto a `FND-02`**, o unico artefato do acervo que nao declarava **nenhum** dos cinco. **Nenhum valor foi inventado:** `resumo` e o texto **ja curado** no catalogo mestre §4.1 pela via de migracao de FND-10 §2.3; `perfil_contexto` e o **padrao por tipo** de FND-10 §10.3 *(Doc. Fundacional → `missao`)*; `confidencialidade` e o padrao unico declarado do acervo; `revisor` e **DEP-QAR** por FND-09 §8.2, linha `FND`; e `ratificacao` registra o ato de 2026-07-29 que promulgou a 1.3.0. **Cinco alteracoes de frontmatter e nenhuma de corpo:** `0` bytes em §1 a §10, medido por `diff`. **Nenhum departamento, classe, invariante, celula da matriz de interacao ou degrau da escada de especializacao foi criado, removido ou alterado.** |
