---
id: MEM-APR-0003-campo-de-estado-em-artefato-imutavel
titulo: Campo de estado em artefato imutavel so pode registrar o estado no ato
tipo: memoria
versao: 1.0.0
status: ativo
camada_memoria: aprendizado
autor: DEP-KMS
proprietario: DEP-KMS
aprovador: DEP-KMS
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0006, ADR-0008]
substitui: []
substituido_por: null
origem: INC-2026-001-ratificacao-inferida
evidencia: O campo `ratificacao`, obrigatorio em ADR (classe M1), tornou-se inatualizavel quando o ato soberano ocorreu — CC-01 proibe editar o ADR, e o campo passou a afirmar o contrario do fato
confianca: alta
ocorrencias: 1
ttl: permanente
aplica_se_a: [global]
resumo: Registra por que exigir campo de estado em artefato de conteudo imutavel produz afirmacao que envelhece, e como o contrato passou a resolver.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# Campo de estado em artefato imutavel so pode registrar o estado no ato

## Proposito
Registrar o conflito entre "todo ADR C3/Tipo 1 declara `ratificacao`" e "ADR nunca e editado"
— e por que a saida nao e escolher um dos dois.

## Escopo
Aplica-se a todo campo que descreva **estado que muda no tempo** — ratificacao, vigencia,
situacao, veredito, confianca — quando declarado em artefato de classe **M1** (ADR, RFC
decidida, EXC, INC fechado, FIT, REV). **Nao** se aplica a campos que descrevem o ato em si —
autor, data, classe, decisao —, que sao imutaveis por natureza.

## Responsaveis
| Papel | Quem |
|---|---|
| Dono | DEP-KMS |
| Quem deve ler | Todo papel que proponha campo novo de frontmatter |
| Verificacao da licao | DEP-QAR |

---

## Situacao
FND-10 §2.2 tornou `ratificacao` obrigatorio em todo artefato de decisao C3 ou Tipo 1 — na
pratica, em ADRs. FND-10 §6.2 classifica ADR como **M1**: conteudo imutavel apos eficacia. E
**CC-01** e explicito: *"ADR historico nunca e editado — nem para corrigir erro, nem para
completar campo, nem para registrar ratificacao posterior."*

As duas regras nasceram na mesma missao, no mesmo documento, e nunca haviam sido exercidas
juntas.

## Observado
Quando o ato soberano de ratificacao ocorreu, em 2026-07-28, as duas colidiram:

| Saida possivel | Consequencia |
|---|---|
| Atualizar `ratificacao` nos ADRs | Viola CC-01, LV-04 e a determinacao expressa do ato |
| Nao atualizar | O frontmatter de ADR-0006 continua declarando `pendente` depois de ratificado — afirmacao falsa por envelhecimento |

Nenhuma das duas e aceitavel: a primeira quebra a imutabilidade que da fe publica ao registro
historico; a segunda deixa no acervo um campo que **afirma um fato que deixou de ser
verdadeiro**, exatamente o defeito que INC-2026-001 tratou.

## Causa
**Um campo de estado foi declarado obrigatorio em uma classe de artefato cujo conteudo nao
muda.** O erro nao esta em nenhuma das duas regras isoladamente — esta na combinacao, que
nao foi verificada quando o campo foi criado.

A causa profunda e de contrato, nao de redacao: `ratificacao` responde *"qual o estado hoje?"*,
e um artefato M1 so consegue responder *"qual era o estado quando isto foi escrito?"*. Foi
pedido a um documento congelado que carregasse informacao viva.

## Licao
**Antes de tornar um campo obrigatorio, verifique a classe de mutabilidade do artefato que vai
carrega-lo.** Campo de estado em artefato imutavel registra o estado **no ato** — nunca o
estado corrente —, e a fonte corrente precisa estar declarada em outro lugar.

Corolario operacional: a pergunta a fazer diante de um campo novo nao e apenas *"qual o valor
padrao?"* (AC-07), mas tambem *"quem o atualiza quando o fato mudar, e esse artefato pode ser
atualizado?"*. Se a resposta for "ninguem, porque nao pode", o campo e historico e deve ser
declarado como tal.

## Condicoes
**Aplica-se quando:** o campo descreve algo que pode mudar depois da aprovacao do artefato, e
o artefato e M1.

**Nao se aplica quando:** o artefato e M2 (versionavel) ou M3 (derivado) — nesses, atualizar
o campo e a operacao normal. Foi o que se fez com `ratificacao` em FND-01, FND-03, FND-04,
FND-08, FND-09 e FND-10.

**Sinal de que se esta no caso errado:** a correcao proposta e "so editar o arquivo" para um
artefato cuja classe declara que o texto nunca muda.

## Acao
| # | O que muda | Dono | Instrumento |
|---|---|---|---|
| A1 | **PJ-04:** campo de estado em artefato M1 registra o estado **no ato**; o estado corrente vive na fonte declarada | DEP-GOV | FND-10 §2.6 |
| A2 | A fonte corrente do estado de ratificacao passa a ser [INC-2026-001 §11](../../governance/incidents/INC-2026-001-ratificacao-inferida.md); o indice de decisoes a **projeta** | DEP-KMS | `decisions/README.md` |
| A3 | Nenhum arquivo de ADR foi editado, em nenhuma hipotese | DEP-GOV | CC-01, LV-04 |

## Confianca
**Alta**, com ressalva de amostra: uma unica ocorrencia, mas de mecanica inteiramente
verificavel — as duas regras estao escritas, a colisao e deducao direta, e nao depende de
julgamento. A ressalva e sobre **frequencia**, nao sobre a validade da licao.

## Proveniencia
| Campo | Conteudo |
|---|---|
| Origem | [INC-2026-001 §11.4](../../governance/incidents/INC-2026-001-ratificacao-inferida.md) |
| Detectado por | DEP-KMS, ao registrar o ato soberano |
| Evidencia | FND-10 §2.2 (campo obrigatorio) × FND-10 §6.2 CC-01 (ADR nunca editado) |

## Relacionados
| Referencia | Relacao |
|---|---|
| [ADR-0008](../../decisions/ADR-0008-uma-fonte-multiplas-projecoes.md) | Decisao que institui PJ-04 |
| [INC-2026-001](../../governance/incidents/INC-2026-001-ratificacao-inferida.md) | Incidente em cujo encerramento o conflito apareceu |
| [MEM-APR-0001](MEM-APR-0001-ratificacao-por-precedente.md) | Mesma materia — ratificacao —, causa distinta |
| [MEM-APR-0002](MEM-APR-0002-duplicacao-por-reproducao-de-tabela.md) | Mesma familia — fonte unica de verdade |
