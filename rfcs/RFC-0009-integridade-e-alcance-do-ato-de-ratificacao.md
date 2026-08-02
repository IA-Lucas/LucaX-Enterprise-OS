---
id: RFC-0009-integridade-e-alcance-do-ato-de-ratificacao
titulo: O que um ato de ratificacao vincula, e como provar que ele nao foi contornado
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
decisoes_relacionadas: [ADR-0006, ADR-0008, ADR-0009, ADR-0011]
substitui: []
substituido_por: null
classe_mudanca: C2
prazo_analise: 2026-07-28
resumo: Pergunta se o ato de ratificacao vincula o arquivo, o conteudo normativo ou a versao, e propoe fixar a resposta por ADR com tres hashes distintos, sem emendar a Constituicao.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# RFC-0009: Integridade e alcance do ato de ratificacao

## Proposito
Responder **o que exatamente** um ato de ratificacao do Soberano vincula — o arquivo, o
conteudo normativo ou a versao —, e como se prova, depois do ato, que o artefato em vigor e
o mesmo que foi ratificado.

## Escopo
| Item | Definicao |
|---|---|
| Inclui | O objeto do ato de ratificacao; a distincao entre hash de arquivo, hash de conteudo normativo e metadados mutaveis de ciclo de vida; a colisao terminologica do verbo *ratificar*; a exigencia de ratificacao sobre `FIT` |
| **Nao** inclui | **Quem** ratifica — indelegavel, PI-01, e nao esta em questao. **O que** exige ratificacao por classe — FND-04 §2.1, tambem nao esta em questao. O merito de qualquer artefato ja ratificado |
| Subordinado a | [FND-10 §5.4](../foundation/10-artifact-framework.md) e [FND-01 §7.3](../foundation/01-constituicao.md) |

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| Propoe | **DEP-GOV** | Guardiao normativo; dono dos achados IC-2 e G1/G2 |
| Revisa | **DEP-QAR** | Verificacao independente; **nao** produziu os artefatos em causa |
| Aprova | **DEP-EXE** | FND-04 §2.1, linha C2 |
| Decide o que for **C3** | **SOBERANO** | Indelegavel — §5, Opcao D |

---

## 1. Situacao atual

Tres institutos com o mesmo nome e um objeto nao definido convivem no acervo:

| # | Fato observado | Fonte |
|---|---|---|
| 1 | O ato de 2026-07-28 sobre `DEP-QAR` ratificou um texto cujo hash e `fa07f55f…f286`. **O arquivo em disco hoje hasheia `c591fd62…c311b`** | [MSG-2026-0001 §2 e §5.2](../memory/operacional/MSG-2026-0001-ato-soberano-ratificacao-cartas-piloto.md) |
| 2 | A diferenca sao **dois campos de frontmatter** — `status` e `ratificacao` — que a **propria ratificacao** obriga a mudar (operacao **O4**, FND-10 §5.2) | FND-10 §5.2 e §5.4 |
| 3 | `FND-01 §7.3` usa a coluna **Ratifica: DEP-EXE** em duas materias, enquanto **LM-02** e **DC-09** reservam *ratificacao* ao ato do Soberano que da vigencia. **Dois institutos, um nome** | Achado **IC-2**, REV-INTERCLASSES §7 |
| 4 | `FND-10 §2.2` exige o campo `ratificacao` apenas em *"artefato de decisao C3 ou Tipo 1"*, e `FND-10 §10.3` exige ratificacao do Soberano para `FIT` de objeto C3. **`FIT` nao e artefato de decisao** | Achado **G1/G2**, [INC-2026-002 §5](../governance/incidents/INC-2026-002-ratificacao-declarada-em-fitness-check.md) |
| 5 | O ato de 2026-07-28 sobre `DEP-EXE`/`DEP-KMS`/`MEM-EST-0001` condicionou a eficacia a *"comprovar que nenhuma alteracao ocorreu entre a revisao e a ratificacao"* — exigencia que **so e verificavel se o objeto do ato estiver definido** | [MSG-2026-0002 §1](../memory/operacional/MSG-2026-0002-ato-soberano-cartas-comando-plataforma-e-contexto.md) |

## 2. Problema

**Se o ato vincula o arquivo, a ratificacao e autodestrutiva.** Aplicar o efeito da
ratificacao — transicionar `status` e `ratificacao` — altera o arquivo e, portanto, quebra o
hash que o ato vinculou. Um auditor que compare o hash do arquivo com o hash do ato encontra
divergencia **em toda ratificacao bem executada**, e nao consegue distinguir isso de uma
adulteracao real.

**Se o ato vincula so a versao, a protecao desaparece.** Transicao de estado nao incrementa
versao (ADR-0009, AC-08). Logo, qualquer alteracao que tambem nao incremente versao — uma
correcao `C0`, um ajuste de redacao — passaria como ratificada sem nunca ter sido submetida.

**Hoje o acervo nao tem regra para nenhum dos dois casos.** `MSG-2026-0001 §2` registrou os
dois hashes e o diff exato — solucao correta, aplicada **por bom senso do redator**, nao por
norma. Nada obriga o proximo ato a fazer o mesmo.

**E o mesmo nome cobre coisas diferentes.** *"Ratificado por DEP-EXE"* (FND-01 §7.3) e
*"ratificado pelo Soberano"* (LM-02) sao institutos distintos com efeitos distintos, e
`LX-07` proibe sinonimo — mas aqui o defeito e o inverso: **um nome para dois institutos**.

## 3. Pergunta de decisao

**O ato de ratificacao vincula o arquivo, o conteudo normativo ou a versao — e como se prova,
apos o ato, que o artefato em vigor e o que foi ratificado?**

Subordinadas: **(a)** `FIT` exige ratificacao do Soberano? **(b)** O verbo *ratificar* pode
continuar nomeando dois institutos?

## 4. Criterios de avaliacao

| # | Criterio | Por que |
|---|---|---|
| K1 | **A regra nao pode tornar a ratificacao autodestrutiva** | Aplicar o efeito nao pode invalidar a prova |
| K2 | **Alteracao pos-ato nao pode parecer ratificada** | E a exigencia literal do ato de 2026-07-28 |
| K3 | **Verificavel por terceiro com os instrumentos existentes** | CE-02 — sem ferramenta nova |
| K4 | **Nao altera quem ratifica nem o que exige ratificacao por classe** | PI-01, FND-04 §2.1 — fora de escopo |
| K5 | **Preserva atos historicos sem edita-los** | LV-04, CC-01, M1 |
| K6 | **Nao cria entidade, tipo documental, camada nem framework** | FND-09 §5; determinacao da Missao 1.8 |

## 5. Opcoes

### Opcao A — Vincular o **arquivo** (hash integral, e so ele)

| Campo | Conteudo |
|---|---|
| Como funciona | O ato vincula `sha256(arquivo)`. Qualquer divergencia posterior e adulteracao |
| A favor | Simplicidade maxima; uma unica medida |
| Contra | **Falha K1 de forma terminal:** a operacao O4 quebra o hash em toda ratificacao valida. Obrigaria a nao aplicar o efeito, ou a manter o artefato eternamente `em-revisao` |
| Veredito | **Recusada** |

### Opcao B — Vincular a **versao**

| Campo | Conteudo |
|---|---|
| Como funciona | O ato vincula `id + versao`. O texto e o que estiver naquela versao |
| A favor | Alinha-se a ADR-0009; barato |
| Contra | **Falha K2:** correcao `C0` e ajuste de redacao nao incrementam versao e passariam por ratificados. Cria exatamente a porta que o Soberano mandou fechar |
| Veredito | **Recusada** |

### Opcao C — Vincular o **conteudo normativo**, com tres hashes declarados *(recomendada)*

| Campo | Conteudo |
|---|---|
| Como funciona | O ato vincula **H-N** = `sha256` do artefato **excluidos os metadados mutaveis de ciclo de vida**, sobre uma lista **fechada** desses campos. O registro canonico do ato anexa tambem **H-A** (arquivo submetido) e **H-P** (arquivo apos a transicao), com o **diff exato** entre eles |
| Por que resolve K1 | **H-N e invariante sob O4** — a transicao so toca campos excluidos do calculo. Aplicar a ratificacao nao quebra a prova |
| Por que resolve K2 | Qualquer alteracao fora da lista fechada **muda H-N**. Divergencia de H-N = alteracao nao ratificada, e abre incidente. `C0` deixa de ser porta de entrada |
| Por que resolve K3 | `sha256sum` e um filtro de linhas. Verificavel com `sed`/`grep`, ja em uso (CE-02) |
| **Prova adicional** | Com H-A e o diff registrados, o texto ratificado e **reconstruivel** e conferivel byte a byte — executado com sucesso sobre `DEP-QAR` e `DEP-ENG` em [MSG-2026-0002 §5.1](../memory/operacional/MSG-2026-0002-ato-soberano-cartas-comando-plataforma-e-contexto.md) |
| Contra | Exige manter uma lista fechada de campos mutaveis; se a lista crescer sem rito, a protecao afrouxa. **Mitigacao:** alterar a lista e mudanca **C2** com ADR |
| Veredito | **Recomendada** |

### Opcao D — Resolver tambem a colisao terminologica de `FND-01 §7.3`

| Campo | Conteudo |
|---|---|
| Como funciona | Renomear a coluna *Ratifica* de FND-01 §7.3 para **Homologa** nas materias cujo titular nao e o Soberano |
| Classe | **C3** — emenda a Constituicao (FND-01 §9; FND-04 §2, C3) |
| Situacao | **O ato de 2026-07-28 nao concede ratificacao a nenhum ADR novo.** Sem ela, a emenda **nao existe** (FND-01 §9, etapa 4) |
| Veredito | **Nao decidida aqui — escalada.** Adotar contencao de efeito imediato enquanto nao houver ato: nenhum artefato novo pode registrar *"ratificado por DEP-EXE"*; o termo oficial para o ato de DEP-EXE e **homologacao**. A contencao e regra de **redacao de artefato** (dominio de FND-10, C2), e **nao** emenda a FND-01 |

### Opcao E — Declarar que `FIT` **nao** exige ratificacao *(G1/G2)*

| Campo | Conteudo |
|---|---|
| Como funciona | Emendar FND-10 §10.3 para harmoniza-la com §2.2: `FIT` e parecer, nao artefato de decisao; nao exige ratificacao |
| A favor | Recomendacao registrada de DEP-GOV ([INC-2026-002 §7](../governance/incidents/INC-2026-002-ratificacao-declarada-em-fitness-check.md)); o ato de 2026-07-28 acolheu os dois `FIT` *"sem eleva-los a norma"*, coerente com a tese |
| **Contra** | A emenda **reduz o que chega ao Soberano**. Ainda que FND-10 seja emendavel por C2 (precedente ADR-0009), **retirar materia da mesa do ratificador nao e decisao que o rito C2 deva tomar sozinho** (PI-01) |
| Veredito | **Nao decidida aqui — escalada ao SOBERANO.** O ato de 2026-07-28 decidiu **dois casos concretos** e disse expressamente *"sem eleva-los a norma"*; ler nele uma emenda geral seria **promover ato em norma por analogia** (LM-03) |

### Opcao Z — Nao fazer nada

| Campo | Conteudo |
|---|---|
| Efeito | Cada ato futuro resolve o objeto do proprio jeito. O acervo ja tem **um** ato bem registrado e **nenhuma** regra que obrigue o proximo a se-lo |
| Custo | A exigencia literal do Soberano — *"comprovar que nenhuma alteracao ocorreu"* — fica sem metodo definido, e a proxima ratificacao pode nao ser verificavel |
| Veredito | **Recusada** — K2 |

## 6. Recomendacao do proponente

**Opcao C**, com a contencao da **Opcao D** e a escalada das partes **D** e **E**.

| # | Fundamento |
|---|---|
| 1 | E a unica opcao que satisfaz **K1 e K2 ao mesmo tempo**. A e B falham cada uma em um deles |
| 2 | **Nao inventa nada:** formaliza o que `MSG-2026-0001 §2` e §5.2 ja fizeram na pratica, e que funcionou. Regra escrita a partir de pratica observada, nao de antecipacao (FND-08 §7.1, SE-01) |
| 3 | **Ja foi testada antes de ser proposta.** A reconstrucao do texto ratificado de `DEP-QAR` e `DEP-ENG` reproduziu os hashes do ato **exatamente** (MSG-2026-0002 §5.1). A regra nasce com **dois membros verificados**, nao com zero (AQ-03) |
| 4 | **Separa o que e C2 do que e C3, em vez de misturar.** A integridade do objeto e materia de FND-10 (C2); a colisao de FND-01 §7.3 e a exigencia sobre `FIT` mexem em Constituicao e em direito de decisao, e ficam **escaladas** |

## 7. Impacto previsto

| Dimensao | Impacto |
|---|---|
| Documentos fundacionais | **Nenhum emendado.** ADR-0012 acrescenta regra sobre **como se registra** um ato — nao altera FND-10 §5.4, que continua valendo integralmente |
| Entidades / tipos / camadas | **0** criados |
| Artefatos alterados | Nenhum artefato historico. Atos futuros passam a registrar tres hashes |
| Atos historicos | **Preservados.** `MSG-2026-0001` **nao e editado**: ele ja registrou H-A e H-P; H-N e **calculavel a posteriori** a partir do arquivo, e foi calculado em MSG-2026-0002 §2 sem tocar a fonte |
| Custo de contexto | **+1 ADR** de perfil `sob-demanda`. Nenhum artefato entra no nucleo |
| Reversibilidade | **Tipo 2.** Revogar a regra nao invalida ato nenhum ja registrado |

## 8. Riscos

| # | Risco | Prob. | Impacto | Mitigacao |
|---|---|---|---|---|
| RR-1 | A lista fechada de campos mutaveis cresce sem rito e a protecao afrouxa | Media | **Alto** | A lista e **normativa**: altera-la e C2 com ADR (IR-04) |
| RR-2 | A regra vira burocracia em atos triviais | Baixa | Medio | So se aplica a artefato **que exija ratificacao** — hoje, `DEP` e `MEM-EST`. Nao alcanca C0/C1 |
| RR-3 | A contencao da Opcao D vira norma de fato e substitui a emenda C3 devida | **Media** | Medio | Declarada **como contencao**, com gatilho e dono; e componente aberto de **IC-2**, que **nao fecha** por causa dela |
| RR-4 | Escalar D e E deixa duas dividas sem prazo | **Media** | Medio | Ambas entram no **mapa unico de bloqueios** de REV-ESTRUTURAL-I §5, com dono, gatilho e custo |

## 9. Perguntas em aberto

| # | Pergunta | Quem decide | Estado |
|---|---|---|---|
| Q1 | A coluna *Ratifica* de FND-01 §7.3 passa a **Homologa**? | **SOBERANO** — C3 | **Aberta** — Opcao D |
| Q2 | `FIT` exige ratificacao do Soberano? | **SOBERANO** | **Aberta** — Opcao E; herda G1/G2 de INC-2026-002 |
| Q3 | A lista fechada deve incluir `revisao_prevista`? | DEP-GOV | **Resolvida — nao.** Alterar a data de revisao prevista e decisao de conteudo, e deve mudar H-N |

## 10. Manifestacoes

| Departamento | Posicao | Observacao |
|---|---|---|
| **DEP-GOV** *(proponente)* | Opcao **C** + contencao **D** | Dono de IC-2 e de G1/G2 |
| **DEP-QAR** *(revisor)* | **De acordo com C**; **insiste** em que D e E fiquem escaladas | Verificou a reconstrucao de §6, item 3. Registra que fechar Q2 por C2 aproximaria o ratificador do verificado (FT-02, PI-05) |
| **DEP-KMS** *(evidencia)* | Sem objecao | Forneceu as medicoes de hash |
| **DEP-EXE** *(aprovador)* | Aprova a Opcao C | Nao produziu nenhum dos artefatos avaliados por esta RFC |

## 11. Resultado

| Campo | Conteudo |
|---|---|
| Estado | **Aceita em parte** |
| Aceito | **Opcao C** integralmente e a **contencao** da Opcao D → [ADR-0012](../decisions/ADR-0012-integridade-do-ato-de-ratificacao.md) |
| **Nao decidido — escalado** | **Q1** *(emenda C3 a FND-01 §7.3)* e **Q2** *(exigencia de ratificacao sobre `FIT`)*. Ambas dependem de ato do Soberano; nenhuma e resolvida por este rito |
| Data | 2026-07-28 |
| Aprovado por | **DEP-EXE**, com parecer de **DEP-GOV** e revisao de **DEP-QAR** |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-GOV | Proposta inicial: cinco opcoes sobre o objeto do ato de ratificacao, a colisao terminologica de FND-01 §7.3 e a exigencia sobre `FIT`. Aceita em parte — Opcao C e a contencao de D geram ADR-0012; Q1 e Q2 escaladas ao Soberano. |
