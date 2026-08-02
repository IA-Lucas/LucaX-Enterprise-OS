---
id: RFC-0005-fronteira-greenfield-legado
titulo: Declarar a fronteira entre o LucaX Enterprise OS e o sistema preexistente, antes de qualquer contato
tipo: rfc
versao: 1.0.0
status: aprovado
camada_memoria: nao-aplicavel
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: null
decisoes_relacionadas: [ADR-0007]
substitui: []
substituido_por: null
classe_mudanca: C2
prazo_analise: 2026-07-28
resumo: Propoe declarar identidade greenfield, ausencia de autoridade do sistema preexistente e o portao de admissao de qualquer conteudo externo.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
---

# RFC-0005: Fronteira greenfield / legado

## Proposito
Propor que o sistema declare, **antes** de qualquer contato com o LucaX preexistente, tres
identidades distintas e um portao unico de admissao — para que nada entre por habito,
proximidade ou precedente.

## Escopo
Abrange a **fronteira** e a **regra de entrada**. Nao abrange o conteudo do sistema
preexistente, que nao e consultado, inventariado nem copiado nesta proposta.

## Responsaveis
| Papel | Quem |
|---|---|
| Proponente | DEP-GOV |
| Areas que devem se manifestar | DEP-QAR (risco de autoridade implicita), DEP-EXE (custo de cadencia), DEP-KMS (proveniencia e curadoria) |
| Aprovador | DEP-EXE, com parecer de DEP-GOV |
| Prazo de manifestacao | 2026-07-28 |

---

## 1. Situacao atual

O acervo tem **85 artefatos e 18.916 linhas**, todos produzidos dentro deste sistema
(medicao `wc -l`, 2026-07-28). Nenhum foi importado, e nenhuma norma foi derivada de
observacao do sistema preexistente.

Existe, fora deste repositorio, um **LucaX anterior** — em operacao ou em algum estado de
existencia, cujo conteudo esta fora do escopo desta proposta. Ele nunca foi consultado por
este sistema. O que existe hoje sobre origem externa e uma unica linha:

| Onde | O que diz | O que nao diz |
|---|---|---|
| FND-03 §9 | *"Artefato importado de fora recebe ID novo do sistema e declara a origem em `origem`"* | **Se pode entrar**, quem decide, contra o que se valida, e com que autoridade passa a valer |

A regra vigente governa a **forma** da importacao e e silenciosa sobre a **admissao**. Isso e
suficiente enquanto nada entra, e insuficiente no dia em que algo entrar.

## 2. Problema

Tres riscos concretos, nenhum hipotetico quanto ao mecanismo:

| # | Risco | Por que e concreto |
|---|---|---|
| P1 | **Autoridade por proximidade.** Conteudo do sistema anterior ser tratado como decidido por ja existir e funcionar | O acervo ja produziu exatamente esse defeito: [INC-2026-001](../governance/incidents/INC-2026-001-ratificacao-inferida.md) registra quatro decisoes que trataram **precedente** como ato de autoridade |
| P2 | **Inventario antes de decisao.** Levantar o legado "so para saber" cria acervo paralelo, sem tipo, sem dono e sem catalogo | RG-02 e MT-01 tornam nao localizavel e nulo o que entra sem classificacao — mas so **depois** de ter entrado |
| P3 | **Identidade ambigua.** Dois sistemas com o mesmo nome, um normativo e outro nao, sem termo que os distinga | LX-07 proibe sinonimo em documento normativo; sem termos oficiais, cada documento inventara o seu |

**O que acontece se nada mudar:** o primeiro contato com o sistema anterior definira a regra
por precedente — e o precedente e exatamente o mecanismo que este acervo ja identificou como
causa raiz de incidente.

## 3. Pergunta de decisao

O sistema deve declarar agora a fronteira entre si e o LucaX preexistente, com portao de
admissao definido — ou deve tratar a questao quando o primeiro candidato aparecer?

## 4. Criterios de avaliacao

| # | Criterio | Peso | Como se mede |
|---|---|---|---|
| C1 | Nenhuma origem externa recebe autoridade automatica | **Bloqueante** | Nao existe caminho normativo que faca conteudo externo valer sem decisao formal |
| C2 | Nao cria entidade, tipo documental, departamento, programa nem inventario agora | **Bloqueante** | Universo permanece em 21 entidades; nenhum artefato descreve o legado |
| C3 | Custo zero para o acervo existente | Alto | Numero de arquivos reescritos = 0 |
| C4 | O portao e verificavel antes da entrada, nao depois | Alto | Existe lista fechada de condicoes que DEP-GOV pode conferir |
| C5 | Reversivel | Medio | Desfazer nao destroi nada nem exige migracao |

## 5. Opcoes

### Opcao A — Declarar as tres identidades e o portao de admissao, sem tocar no legado

| Campo | Conteudo |
|---|---|
| Descricao | ADR declara `LucaX Enterprise OS` (greenfield, unica fonte normativa), `LucaX Legacy` (externo, sem autoridade) e `Programa de Migracao` (futuro, nao iniciado); proibe importacao direta; fixa as condicoes de admissao futura; registra proveniencia como campo **curado no catalogo**, com valor padrao `native` |
| A favor | Satisfaz C1 a C5. A regra existe antes do primeiro caso, que e a unica ordem que impede o precedente |
| Contra | Escreve norma sobre algo que ainda nao ocorreu — risco de a regra nao caber no caso real |
| Custo | 1 ADR, 2 termos no vocabulario, 1 coluna no catalogo, 0 arquivos reescritos |
| Avaliacao | C1 ✔ · C2 ✔ · C3 ✔ · C4 ✔ · C5 ✔ |

### Opcao B — Estender apenas FND-03 §9 com a regra de `origem`

| Campo | Conteudo |
|---|---|
| Descricao | Acrescentar a §9 que artefato importado declara `origem` e passa pelo rito da classe |
| A favor | Custo minimo; usa instrumento existente |
| Contra | **Falha em C1.** Governa a forma da importacao, nao a admissao: continua nao existindo quem decide, contra o que se valida e com que autoridade o conteudo passa a valer. Tambem nao resolve P3 |
| Custo | 3 linhas |
| Avaliacao | C1 **falha** · C2 ✔ · C3 ✔ · C4 **falha** · C5 ✔ |

### Opcao C — Criar agora o Migration Framework e o Programa de Migracao

| Campo | Conteudo |
|---|---|
| Descricao | Documento fundacional de migracao, com inventario do legado, matriz de equivalencia e programa com fases |
| A favor | Resolveria tudo de uma vez, se o legado fosse conhecido |
| Contra | **Falha em C2.** Cria camada conceitual inteira sem lacuna observada e sem um unico candidato real — o oposto de FND-04 §6.1 e de SE-01. Exigiria inventariar o legado antes de decidir o que fazer com ele, que e P2 executado deliberadamente |
| Custo | 1 documento fundacional, 1 programa, inventario de tamanho desconhecido |
| Avaliacao | C1 ✔ · C2 **falha** · C3 ✔ · C4 ✔ · C5 **falha** |

### Opcao Z — Nao fazer nada

| Campo | Conteudo |
|---|---|
| O que acontece | A fronteira permanece implicita. Nada quebra hoje: nada foi importado |
| Custo real da inacao | O custo aparece inteiro no primeiro contato, e na pior forma — decisao tomada sob pressao de um caso concreto, com o conteudo ja a vista. Julgar a regra com o caso na frente e o mecanismo classico de captura por precedente (P1) |
| Por que nao venceu | O momento em que a regra e barata **e** o momento em que ela parece desnecessaria. Depois, ela e cara e parece tardia |

## 6. Recomendacao do proponente

**Opcao A.**

A proposta nao decide nada sobre o legado — decide sobre **este** sistema. Declarar que
nenhuma origem externa tem autoridade automatica e uma afirmacao sobre a propria natureza
normativa, verificavel hoje, independente do que exista do outro lado.

A objecao valida a A — "escrever regra antes do caso" — e respondida por construcao: o portao
lista **condicoes de admissao**, nao criterios de conteudo. Nao antecipa o que sera adotado
nem como sera adaptado; exige apenas que se saiba de onde veio, contra o que foi comparado,
que classificacao recebeu, quem validou e quem decidiu. Nenhuma dessas cinco exigencias
depende de conhecer o legado.

**Limite declarado (PI-10):** a proposta nao produz nenhum ganho observavel hoje. Seu valor e
inteiramente preventivo, e so sera medido no primeiro candidato real. Isso e declarado, nao
disfarcado de beneficio imediato.

## 7. Impacto previsto

| Dimensao | Impacto |
|---|---|
| Departamentos afetados | DEP-GOV (guarda da fronteira), DEP-KMS (proveniencia no catalogo), DEP-QAR (validacao no portao) |
| Componentes afetados | Nenhum — nao existe componente |
| Entidades novas | **Zero.** Universo permanece em 21 |
| Tipos documentais novos | **Zero** |
| Documentos a atualizar | FND-03 §8 (2 termos) · FND-10 §10.4 (1 linha) · catalogo mestre (1 coluna) |
| Arquivos reescritos | **Zero** — `native` e o valor padrao do acervo |
| Ganho PI-14 | **Organizacao** — a decisao de admissao passa a ter lugar unico e anterior ao caso |

## 8. Riscos

| # | Risco | Probabilidade | Impacto | Mitigacao |
|---|---|---|---|---|
| R1 | O portao nao caber no primeiro caso real | Media | Baixo | Portao e C2 reversivel; o primeiro caso e o gatilho de revisao declarado |
| R2 | A proibicao de importacao direta ser lida como proibicao de **olhar** o legado | Media | Medio | O ADR distingue explicitamente **consultar como evidencia** de **importar como norma** |
| R3 | `Programa de Migracao` nomeado hoje virar expectativa de que sera criado | Baixa | Baixo | Declarado como **nao iniciado**, sem dono, sem prazo e sem artefato |

## 9. Perguntas em aberto

| # | Pergunta | Quem responde | Quando |
|---|---|---|---|
| Q1 | O `Programa de Migracao` sera `PRJ` ou sequencia de mudancas C2? | SOBERANO + DEP-EXE | Quando for iniciado — nao agora |
| Q2 | A classificacao ADOPT/ADAPT/REWRITE/RETIRE precisa de artefato proprio? | DEP-GOV | No primeiro candidato: se um bastar, e secao do ADR de admissao |
| Q3 | Ha algo no legado que justifique adiantar o programa? | SOBERANO | Fora do escopo desta RFC — exige olhar o legado |

## 10. Manifestacoes

| Area | Posicao | Fundamento |
|---|---|---|
| DEP-QAR | **A favor da Opcao A** | P1 nao e hipotetico neste acervo: INC-2026-001 e a prova de que precedente foi tratado como autoridade. A mesma classe de defeito com origem externa seria mais grave, porque o conteudo viria pronto |
| DEP-EXE | **A favor da Opcao A** | Custo de cadencia nulo: nenhuma entrega depende disto, e nada e bloqueado por isto |
| DEP-KMS | **A favor da Opcao A, com observacao** | Proveniencia deve ser campo **curado (L2)**, nunca frontmatter — declarar em 85 arquivos violaria a promessa de migracao zero de FND-10 §2.3 |
| DEP-GOV | **A favor da Opcao A** | Classe C2 confirmada: FND-04 §2 define C2 como mudanca que *"muda escopo, **fronteira**, interface ou padrao"* |

## 11. Resultado

| Campo | Conteudo |
|---|---|
| Resultado | **Aceita** |
| Decisao | [ADR-0007](../decisions/ADR-0007-fronteira-greenfield-legado.md) |
| Data | 2026-07-28 |
| Observacao de DEP-KMS acolhida | Sim — proveniencia entra como campo curado no catalogo, com padrao `native`, sem tocar em nenhum frontmatter |
