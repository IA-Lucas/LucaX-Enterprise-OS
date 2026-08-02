---
id: FND-04
titulo: Governanca do LucaX Enterprise OS
tipo: fundacao
versao: 1.3.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0001, ADR-0002, ADR-0003, ADR-0004, ADR-0006]
ratificacao: ratificada
substitui: []
substituido_por: null
---

# Governanca

## Proposito

Definir como qualquer componente do LucaX Enterprise OS e criado, alterado, aprovado,
depreciado e removido — com responsavel nomeado, instrumento adequado ao risco e
rastreabilidade completa. Governanca e o mecanismo que impede que o sistema mude sem que
alguem responda pela mudanca.

## Escopo

| Item | Definicao |
|---|---|
| **Inclui** | Classes de mudanca, instrumentos exigidos, papeis de governanca, ciclo de vida de mudanca, requisitos de rastreabilidade, auditoria, excecoes, incidentes de conformidade, gestao de dependencias. |
| **Nao inclui** | O conteudo das decisoes (FND-07 define o formato do registro), formato de mensagem (FND-05). |
| **Aplica-se a** | Todo componente: documento, departamento, agente, subagente, skill, spec, ADR, RFC, template, workflow, memoria, ferramenta, produto, projeto. |
| **Subordinado a** | [FND-01 Constituicao](01-constituicao.md). |

## Responsaveis

| Papel | Responsavel |
|---|---|
| Proprietario | DEP-GOV |
| Autoridade de aprovacao final | SOBERANO |
| Verificacao de qualidade nos portoes | DEP-QAR |
| Arbitragem de merito | DEP-EXE |
| Obrigados | Todos os departamentos, sem excecao |

---

## 1. Principio Fundamental da Governanca

> **Nada existe, muda ou desaparece no LucaX sem: (a) um responsavel nomeado, (b) um
> instrumento proporcional ao risco, e (c) um registro localizavel.**

Corolarios:

| # | Corolario |
|---|---|
| GV-01 | Mudanca sem responsavel e nula. Nao produz efeito. |
| GV-02 | Instrumento e escolhido pelo **risco**, nao pela pressa nem pelo tamanho aparente. |
| GV-03 | Na duvida sobre a classe, aplica-se a classe **mais alta**. |
| GV-04 | Quem propoe nao aprova (PI-05). Quem executa nao verifica. |
| GV-05 | Aprovacao e ato explicito e datado. Silencio nunca aprova. |
| GV-06 | Registro precede execucao para C2 e C3; acompanha execucao para C1. |
| GV-07 | Mudanca sem plano de reversao so e permitida se comprovadamente reversivel por natureza. |
| GV-08 | Governanca nao e opcional sob urgencia. Urgencia altera o instrumento, nunca o registro. |

## 2. Classes de Mudanca

Toda mudanca e classificada antes de comecar. A classificacao e feita pelo proponente e
**validada por DEP-GOV**.

### C0 — Editorial
Sem efeito normativo: redacao, tipografia, link quebrado, exemplo, formatacao.

| Campo | Regra |
|---|---|
| Instrumento | Nenhum |
| Aprovador | Proprietario do artefato |
| Registro | `atualizado_em` + incremento de CORRECAO |
| Reversao | Trivial |
| Exemplo | Corrigir erro de digitacao em uma Carta |

### C1 — Operacional
Muda **como** algo e feito, dentro de escopo e norma ja aprovados. Reversivel.

| Campo | Regra |
|---|---|
| Instrumento | Nota de Decisao (registro leve, ver FND-07 §5) |
| Aprovador | Proprietario do artefato; revisor de papel distinto |
| Registro | Nota de Decisao + memoria camada Operacional |
| Reversao | Barata e documentada |
| Exemplo | Ajustar a ordem de etapas de um runbook; refinar criterio de aceite dentro da mesma spec |

### C2 — Estrutural
Cria, altera ou remove **um componente** ou muda escopo, fronteira, interface ou padrao.

| Campo | Regra |
|---|---|
| Instrumento | **RFC → ADR** (RFC dispensavel se a alternativa unica for obvia e DEP-GOV concordar por escrito) |
| Aprovador | DEP-EXE, com parecer de DEP-GOV; ratificacao do Soberano se Tipo 1 |
| Registro | ADR obrigatorio + atualizacao dos documentos afetados na mesma decisao |
| Reversao | Plano de reversao obrigatorio |
| Exemplo | Criar departamento, criar agente, mudar taxonomia, adotar ferramenta, criar produto |

### C3 — Constitucional
Altera principio imutavel, linha vermelha, hierarquia normativa, direitos de decisao ou a
propria Fundacao.

| Campo | Regra |
|---|---|
| Instrumento | **RFC obrigatoria → analise de impacto → ADR → ratificacao do Soberano** |
| Aprovador | **Somente o SOBERANO.** Indelegavel. |
| Registro | ADR + nova versao MAIOR do documento + versao anterior preservada |
| Reversao | Emenda revogatoria, com mesmo rito |
| Exemplo | Remover um Principio Imutavel; mudar quem ratifica portfolio; alterar a hierarquia normativa |

### 2.1 Tabela-resumo

| Classe | Instrumento | Aprova | Precisa RFC? | Precisa ADR? | Ratificacao humana |
|---|---|---|---|---|---|
| C0 | — | Proprietario | Nao | Nao | Nao |
| C1 | Nota de Decisao | Proprietario + revisor | Nao | Nao | Nao |
| C2 | RFC → ADR | DEP-EXE + parecer DEP-GOV | Sim (regra) | **Sim** | Se Tipo 1 |
| C3 | RFC → ADR → Emenda | SOBERANO | **Sim** | **Sim** | **Sempre** |

### 2.2 Classificacao cruzada com reversibilidade

| | Tipo 2 (reversivel) | Tipo 1 (irreversivel / caro) |
|---|---|---|
| **C1** | Proprietario decide | Escala: vira C2 |
| **C2** | DEP-EXE aprova | **Soberano ratifica** |
| **C3** | Soberano ratifica | **Soberano ratifica + plano de reversao explicito** |

**Regra dura:** qualquer mudanca Tipo 1 exige aprovacao humana explicita, independentemente
da classe (PI-06). Nao ha delegacao que remova essa exigencia.

## 3. Papeis de Governanca

Papeis sao funcoes por mudanca, nao cargos. Um mesmo departamento pode ocupar papeis
diferentes em mudancas diferentes — **nunca dois papeis conflitantes na mesma mudanca**.

| Papel | Faz | Nao pode |
|---|---|---|
| **Proponente** | Formula a proposta, classifica, levanta alternativas e impacto | Aprovar a propria proposta |
| **Revisor** | Avalia merito tecnico e de conteudo, de forma independente | Ser o proponente |
| **Guardiao** (DEP-GOV) | Valida classe, forma, conformidade, rastreabilidade; atribui ID | Julgar merito de conteudo |
| **Verificador** (DEP-QAR) | Verifica qualidade, risco, evidencia e reversao | Ser produtor do artefato |
| **Aprovador** | Autoriza a mudanca conforme a classe | Ser o proponente ou o executor |
| **Ratificador** (SOBERANO) | Da eficacia a C3 e a Tipo 1 | Ser substituido ou presumido |
| **Executor** | Aplica a mudanca aprovada, no escopo aprovado | Alterar o escopo durante a execucao |
| **Curador** (DEP-KMS) | Grava o resultado na camada de memoria correta | Alterar o conteudo da decisao |

### 3.1 Incompatibilidades absolutas

```
Proponente  ≠  Aprovador          (PI-05)
Executor    ≠  Verificador        (PI-05)
Proponente  ≠  Revisor            (PI-05)
Guardiao    ≠  Proponente         (independencia da guarda, ES-02)
```

Acumulo indevido de papeis torna a aprovacao **nula** (LV-03).

## 4. Ciclo de Vida de uma Mudanca

```
 [1] ORIGEM          Alguem identifica necessidade
        |
 [2] CLASSIFICACAO   Proponente classifica (C0-C3 + Tipo 1/2)
        |            DEP-GOV valida a classificacao        <-- ponto de veto
        |
 [3] PROPOSTA        Instrumento da classe e produzido
        |            (Nota de Decisao | RFC | RFC+ADR)
        |
 [4] IMPACTO         Levantamento obrigatorio para C2/C3:
        |            componentes afetados, camadas de memoria,
        |            decisoes superadas, dependencias
        |
 [5] REVISAO         Revisor independente avalia merito
        |            DEP-QAR avalia risco e reversao       <-- ponto de veto
        |            DEP-GOV avalia conformidade           <-- ponto de veto
        |
 [6] APROVACAO       Aprovador da classe autoriza, com data
        |            SOBERANO ratifica se C3 ou Tipo 1     <-- indelegavel
        |            OBTER a ratificacao e REGISTRA-LA sao atos distintos:
        |            quem registra e papel diverso do executor (CV-09)
        |
 [7] REGISTRO        DEP-GOV atribui ID definitivo,
        |            publica ADR, atualiza indices e contadores
        |
 [8] EXECUCAO        Executor aplica exatamente o aprovado
        |            Desvio durante execucao => volta a [2]
        |
 [9] VERIFICACAO     DEP-QAR confirma que o resultado corresponde
        |            ao aprovado; confirma backup e reversao
        |
[10] PROPAGACAO      Documentos dependentes atualizados
        |            Decisoes superadas marcadas
        |
[11] APTIDAO         DEP-QAR emite a Verificacao de Aptidao Arquitetural
        |            (QG-6, FND-09 §10) — obrigatoria em C2 e C3
        |            Veredito `inapto` devolve o ciclo a [2]      <-- ponto de veto
        |
[12] MEMORIA         DEP-KMS grava na camada correta (QG-5)
        |
[13] REVISAO FUTURA  Data de reavaliacao registrada, quando aplicavel
```

### 4.1 Regras do ciclo

| # | Regra |
|---|---|
| CV-01 | Etapa 2 nunca e pulada. Mudanca nao classificada nao entra no sistema. |
| CV-02 | Para C2 e C3, o registro (7) precede a execucao (8). Executar antes de registrar e violacao. |
| CV-03 | Desvio de escopo durante a execucao reabre o ciclo na etapa 2. Nao se "estende" um aprovado. |
| CV-04 | Etapa 10 e parte da mudanca, nao trabalho posterior. Mudanca que deixa documento dependente desatualizado esta **incompleta**. |
| CV-05 | Etapa 12 e obrigatoria. Mudanca nao registrada em memoria nao esta encerrada (QG-5). |
| CV-06 | Veto em 5 interrompe o ciclo. Segue-se para [6] apenas apos o veto ser sanado ou revertido pelo Soberano. |
| CV-07 | **Etapa 11 e obrigatoria em C2 e C3.** Mudanca estrutural sem Verificacao de Aptidao emitida nao encerra (QG-6, FT-05). Veredito `inapto` devolve o ciclo a [2]; prosseguir apesar dele exige excecao formal do Soberano. |
| CV-08 | A etapa 11 e executada por quem **nao** produziu o artefato avaliado (PI-05, FT-02). Acumulo torna o veredito nulo (LV-03). |
| CV-09 | **Obter a ratificacao e registra-la sao atos distintos.** O registro e feito por papel diverso do executor, e so apos ato explicito e datado do Soberano sobre o **texto final**. Instrucao generica anterior, determinacao originadora e silencio **nao ratificam** (PI-01, PI-06, GV-05). Enquanto o ato nao ocorrer, a decisao permanece `aprovado` — **nao entra em `ativo`** — e declara `ratificacao: pendente`. Preencher a secao de ratificacao com inferencia, ainda que fundamentada e com ressalva, e violacao de **LV-05** e torna o registro nulo. *(INC-2026-001, MEM-APR-0001)* |

## 5. Requisitos de Rastreabilidade

Toda mudanca relevante (C1 ou superior) deve responder, a qualquer momento no futuro, a
estas sete perguntas:

| # | Pergunta | Onde a resposta vive |
|---|---|---|
| RT-1 | **O que** mudou? | Instrumento (Nota / ADR), campo "Decisao" |
| RT-2 | **Quem** propos, aprovou e executou? | Frontmatter: `autor`, `aprovador`; corpo do ADR |
| RT-3 | **Quando**? | `criado_em`, `atualizado_em`, data de aprovacao |
| RT-4 | **Por que**? | Campo "Contexto" e "Justificativa" |
| RT-5 | **O que foi descartado** e por que? | Campo "Alternativas consideradas" |
| RT-6 | **O que foi afetado**? | Campo "Impacto" + `substitui` / `substituido_por` |
| RT-7 | **Com base em que evidencia**? | Campo "Evidencias" |

**Teste de rastreabilidade:** se qualquer uma das sete perguntas nao puder ser respondida
sem consultar uma pessoa, a rastreabilidade falhou e DEP-GOV registra nao conformidade.

### 5.1 Cadeia de referencia
Todo artefato aponta para o que o originou e para o que ele afeta:

```
RFC-0003  --gera-->  ADR-0009  --altera-->  FND-02 v1.1.0
                          |
                          +--supera-->  ADR-0004
                          +--registra-->  MEM-EST-0021
```

Elo quebrado (referencia a ID inexistente) e erro de conformidade e bloqueia aprovacao.

## 6. Regras Especificas de Criacao

Alem do rito da classe, cada tipo de componente tem pre-condicoes proprias. **Todas
precisam ser verdadeiras** para a criacao ser aprovada.

> **Pre-condicao universal I (ADR-0002, alcance estendido por ADR-0003).** Departamento,
> Agente, Subagente, Skill, Workflow, Produto, **Projeto e Ferramenta** so podem ser criados
> com **vinculo declarado a ao menos uma Capability ativa** (FND-08 §8). Vinculo ausente, a
> Capability inexistente, `proposta` ou `aposentada` bloqueia a aprovacao (VC-01). Se a
> competencia nao couber em nenhuma Capability do catalogo, abre-se **RFC de Capability
> antes** de criar o componente (VC-02).

> **Pre-condicao universal II (ADR-0003).** Nenhum componente pode ser criado se o seu
> **tipo** nao constar do Meta Model (FND-09 §5). Tipo nao declarado e entidade nula, e o uso
> e incidente de conformidade (MT-01). Criar tipo novo tem rito proprio — ver a linha
> **Entidade (tipo novo)** na tabela abaixo.

| Componente | Pre-condicoes obrigatorias | Classe |
|---|---|---|
| **Entidade (tipo novo)** | Passa nos 7 testes TE (FND-09 §11.1); estrato, arquetipos, atributos minimos, relacoes permitidas, perfil de ciclo de vida e autoridade declarados; template criado (§3.9); sinal PI-14 observado | **C3 (Tipo 1)** |
| **Capability** | Passa nos 6 testes TC; sem sobreposicao com o catalogo; custodio aceito e apto; ao menos um indicador de saude; ganho PI-14 com sinal observado | C2 (Tipo 1) |
| **Departamento** | Responsabilidade orfa comprovada; nao cabe em area existente; fronteira sem sobreposicao; criterio de sucesso definido; **Capabilities custodiadas declaradas** | C2 (Tipo 1) |
| **Agente** | Pertence a um departamento existente; escopo e o que **nao** lhe compete declarados; autonomia ≤ do departamento; **Capabilities exercidas declaradas**; Carta aprovada | C2 |
| **Subagente** | Agente pai existe e esta ativo; escopo estritamente menor; profundidade maxima 1 | C2 |
| **Skill** | Procedimento se repete; resultado verificavel; usavel por mais de um papel | C2 |
| **Spec** | Produto existe; problema definido; criterios de aceite verificaveis; escopo negativo explicito | C1 |
| **ADR** | Decisao ja tomada; ≥2 alternativas reais + "nao fazer"; impacto mapeado | conforme a decisao |
| **RFC** | Pergunta clara; alternativas analisadas; prazo de analise definido | C2/C3 |
| **Template** | Tipo de artefato existe e e recorrente; campos derivados da taxonomia | C2 |
| **Workflow** | Gatilho, entradas, saidas, responsavel por etapa, portoes e criterio de falha definidos | C2 |
| **Memoria** | Camada unica identificada; proveniencia; nao duplica registro existente | C1 |
| **Ferramenta** | Finalidade; dado que trafega; custo; dependencia; alternativa avaliada; criterio de descarte; **Capabilities habilitadas declaradas** | C2 (Tipo 1) |
| **Produto** | Decisao do Soberano; publico e problema definidos; criterio de sucesso e de encerramento | C2 (Tipo 1) |
| **Projeto** | Resultado definido; criterio de encerramento; departamento responsavel nomeado; **Capabilities consumidas declaradas** | C1/C2 |
| **Verificacao de aptidao** | Objeto avaliado nomeado; seis respostas com sinal observavel; executor distinto do produtor; ressalvas com dono e gatilho | acompanha a mudanca avaliada |

### 6.1 Regra de nao-proliferacao
Antes de criar qualquer componente, o proponente deve responder por escrito:

1. Isso ja existe em outra forma? *(se sim, reusar e obrigatorio)*
2. Isso cabe em um componente existente sem distorce-lo? *(se sim, nao se cria novo)*
3. Qual ganho de PI-14 este componente produz — organizacao, reuso ou reducao de contexto —
   e qual sinal ja observado o comprova? *(ganho previsto sem sinal observado nao conta)*
4. Como se vai saber que este componente deixou de ser necessario?

Proposta que nao responde as quatro perguntas e devolvida por DEP-GOV sem analise de merito.

### 6.2 Teste de Especializacao (PI-14)

Nao-proliferacao e especializacao continua nao se contradizem: **ambas exigem evidencia.**
A primeira barra o componente sem ganho; a segunda obriga o componente com ganho. O teste
abaixo decide qual das duas se aplica.

| Pergunta | Resposta | Consequencia |
|---|---|---|
| Ha sinal observado de um gatilho de FND-02 §9.2? | Nao | **Nao especializar.** Registrar que foi avaliado. |
| | Sim | Segue |
| Qual ganho de PI-14 e produzido, e como sera constatado depois? | Nao sabe dizer | **Devolvido.** Ganho nao declarado = especulacao. |
| | Declarado e verificavel | Segue |
| Qual o degrau minimo da escada (FND-02 §9.1) que captura esse ganho? | — | **So esse degrau e aprovado.** Pular degrau e recusado. |
| Toda responsabilidade da parte original tem destino explicito? | Nao | **Devolvido.** Especializacao nao cria orfaos. |
| Ha invariante de FND-02 §9.5 ameacada? | Sim | **Vetado por DEP-GOV.** |

**Registro obrigatorio do ganho:** todo ADR que especializa declara o ganho pretendido e a
data em que ele sera reavaliado. Na reavaliacao, ganho nao confirmado abre proposta de
consolidacao (FND-02, §9.3) — nao se mantem divisao por inercia.

**Adiamento tambem se registra.** Gatilho constatado e especializacao adiada exige Nota de
Decisao com o motivo e o custo assumido (PI-14, regra 2). Custo aceito conscientemente e
divida declarada; custo invisivel e defeito de governanca.

## 7. Alteracao e Depreciacao

### 7.1 Alteracao
| Regra | Detalhe |
|---|---|
| AL-01 | Alteracao segue a classe do **efeito**, nao do tamanho do texto alterado. |
| AL-02 | ADR aprovado nunca e alterado — e superado por novo ADR (LV-04). |
| AL-03 | Alteracao que muda escopo exclusivo de departamento e sempre C2. |
| AL-04 | Alteracao MAIOR preserva a versao anterior; o texto antigo nunca desaparece. |
| AL-05 | Alteracao em cascata e parte da mesma mudanca (CV-04). |

### 7.2 Depreciacao e remocao
| Etapa | Regra |
|---|---|
| 1. Marcar | Estado passa a `depreciado`, com substituto indicado quando houver |
| 2. Periodo de convivencia | Componente depreciado continua valido ate a substituicao entrar em vigor |
| 3. Migrar dependentes | Toda referencia ao depreciado e redirecionada — **obrigatorio antes de superar** |
| 4. Superar ou revogar | `superado` (com substituto) ou `revogado` (sem substituto) |
| 5. Preservar | Artefato nunca e apagado. Historia nao e removida do sistema. |

**Remocao fisica de arquivo e proibida** para artefatos que ja estiveram em estado `ativo`.
Aplica-se PI-07 e LV-01: sem copia datada, nao se remove nada.

## 8. Auditoria

| Auditoria | Frequencia | Executada por | Verifica |
|---|---|---|---|
| **Conformidade de artefato** | A cada portao QG | DEP-GOV | Frontmatter, ID, localizacao, estado, blocos obrigatorios |
| **Integridade referencial** | A cada fechamento de ciclo | DEP-GOV | Elos quebrados, IDs inexistentes, duplicatas, **vinculos a Capability invalidos (VC-01)**, **relacoes fora dos pares permitidos (RM-02)**, **ciclo em `depende-de`**, **dependencia ascendente (PD-11)** |
| **Aptidao arquitetural** | Ao encerrar toda mudanca C2/C3 | DEP-QAR | As seis perguntas de FND-09 §10.3, com sinal observavel; veredito; ressalvas com dono e gatilho |
| **Eficacia de ratificacao** | A cada C3 e a cada Tipo 1 | DEP-QAR | Se a ratificacao **declarada** corresponde a ato explicito e datado do Soberano **sobre o texto final** — e nao a instrucao generica anterior, precedente ou silencio (CV-09) |
| **Coerencia interna de norma** | A cada mudanca C2/C3 em documento fundacional | DEP-GOV | Tabela ou diagrama **reproduzido** de outro documento em vez de referenciado (MM-01); vocabulario usado fora do declarado |
| **Cobertura de Capabilities** | Por horizonte | DEP-QAR + DEP-EXE | Sobreposicao, lacuna, amplitude, classe, maturidade declarada vs. indicador medido |
| **Excecoes vigentes** | A cada fechamento de ciclo | DEP-GOV | Excecoes vencidas nao regularizadas |
| **Coerencia normativa** | A cada mudanca C2/C3 | DEP-GOV | Contradicao entre norma nova e vigente |
| **Sanidade da memoria** | Periodica | DEP-KMS | Duplicidade, contradicao, registro sem proveniencia, TTL vencido |
| **Risco e seguranca** | A cada QG-4 | DEP-QAR | Credencial exposta, dado vivo, backup, plano de reversao |
| **Revisao estrutural (PI-14)** | Por horizonte, minimo semestral | DEP-GOV + DEP-EXE + DEP-KMS | Gatilhos de especializacao e de consolidacao; ganhos declarados que nao se confirmaram |
| **Revisao da Fundacao** | Semestral | DEP-GOV + SOBERANO | Aderencia dos 7 documentos a realidade operacional |

Achado de auditoria vira: correcao imediata (C0/C1), proposta de mudanca (C2/C3) ou
incidente de conformidade — nunca observacao sem destino.

## 9. Excecoes Formais

Instrumento: `EXC-<AAAA>-<NNN>`. Ver Constituicao §8.3.

| Requisito | Regra |
|---|---|
| Quem autoriza | **Somente o Soberano** |
| Forma | Escrita, com motivo, escopo exato, componente afetado e prazo |
| Prazo | Obrigatorio e finito. **Excecao sem prazo e invalida.** |
| Expiracao | Automatica ao fim do prazo. Nao ha renovacao tacita. |
| Registro | `governance/exceptions/EXC-<id>.md`, criado por DEP-GOV |
| Regularizacao | Ao expirar: estado regular restaurado, ou nova excecao explicita, ou mudanca de norma via RFC |
| Nao admitem excecao | Principios Imutaveis (PI-01 a PI-13) e Linhas Vermelhas LV-02, LV-05, LV-12 |

Excecao vencida e nao regularizada e automaticamente um incidente de conformidade.

## 10. Incidentes de Conformidade

Instrumento: `INC-<AAAA>-<NNN>`, em `governance/incidents/`.

### 10.1 Quando abrir
- Violacao de Principio Imutavel ou Linha Vermelha
- Mudanca executada sem o instrumento da classe
- Aprovacao com acumulo indevido de papeis
- Artefato ativo sem rastreabilidade
- Excecao vencida sem regularizacao
- Credencial exposta
- Portao pulado sem excecao formal

### 10.2 Rito
| Etapa | Acao |
|---|---|
| 1 | **Parar.** A execucao em curso e interrompida. |
| 2 | **Registrar.** DEP-GOV abre o INC com fato, norma violada, autor e data. |
| 3 | **Conter.** Reverter o efeito quando possivel; isolar quando nao for. |
| 4 | **Analisar causa.** Falha de norma, de instrumento, de compreensao ou de execucao? |
| 5 | **Corrigir.** Correcao do efeito **e** correcao da causa. |
| 6 | **Aprender.** Registro obrigatorio na camada de memoria de Aprendizado. |
| 7 | **Fechar.** DEP-QAR verifica que causa e efeito foram tratados. |

**Incidente nao e punicao — e informacao.** Deixar de registrar incidente observado e, em
si, violacao (LV-11). Incidente fechado sem correcao de causa nao esta fechado.

## 11. Gestao de Dependencias entre Componentes

| Regra | Detalhe |
|---|---|
| DP-01 | Todo componente declara de quem depende (`decisoes_relacionadas`, `substitui`, referencias). |
| DP-02 | Antes de alterar um componente, DEP-GOV levanta quem depende dele. Alteracao sem esse levantamento e incompleta. |
| DP-03 | Dependencia circular entre normas e proibida. Detectada, exige RFC para desfazer. |
| DP-04 | Componente depreciado nao pode receber dependencia nova. |
| DP-05 | Dependencia externa (ferramenta de terceiro) exige alternativa avaliada e criterio de descarte registrados. |

## 12. O Que Governanca Nao Faz

Delimitacao explicita, para evitar que a governanca vire gargalo ou capture o merito:

| Governanca **nao** | Porque |
|---|---|
| Decide o merito tecnico | Isso e de DEP-ENG |
| Define escopo de produto | Isso e de DEP-PRD |
| Define prioridade | Isso e de DEP-EXE |
| Substitui a revisao de qualidade | Isso e de DEP-QAR |
| Exige instrumento acima da classe real | GV-02: proporcionalidade ao risco |
| Impede execucao de C0/C1 por formalidade | Essas classes existem justamente para fluir |

Governanca julga **forma, conformidade e rastreabilidade**. Merito e de quem tem o dominio.

---

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-GOV | Governanca inicial: 4 classes de mudanca, 8 papeis, ciclo de 12 etapas. Ratificada por ADR-0001. |
| 1.1.0 | 2026-07-28 | DEP-GOV | Emenda por ADR-0002: pre-condicao universal de vinculo a Capability; pre-condicoes de criacao de Capability; auditoria de cobertura do catalogo. |
| 1.2.0 | 2026-07-28 | DEP-GOV | Emenda por ADR-0003 e ADR-0004: ciclo de mudanca passa a 13 etapas, com **[11] Aptidao** (QG-6) e regras CV-07 e CV-08; pre-condicao universal II (tipo declarado no Meta Model); pre-condicoes de criacao de **Entidade** e de **Verificacao de aptidao**; vinculo a Capability estendido a Projeto e Ferramenta; auditorias de aptidao arquitetural e de coerencia interna de norma. |
| 1.3.0 | 2026-07-28 | DEP-GOV | Correcao de causa de **INC-2026-001**: etapa [6] separa **obter** de **registrar** a ratificacao; regra **CV-09** (ratificacao inferida e nula, artefato permanece `aprovado`); auditoria de **eficacia de ratificacao**. |
