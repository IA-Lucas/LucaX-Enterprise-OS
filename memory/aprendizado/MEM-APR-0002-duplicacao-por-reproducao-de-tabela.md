---
id: MEM-APR-0002-duplicacao-por-reproducao-de-tabela
titulo: Detectar duplicacao nao previne duplicacao — quem escreve tem de perguntar antes
tipo: memoria
versao: 1.1.0
status: ativo
camada_memoria: aprendizado
autor: DEP-KMS
proprietario: DEP-KMS
aprovador: DEP-KMS
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0004, ADR-0006, ADR-0008, ADR-0011]
substitui: []
substituido_por: null
origem: FIT-2026-002-artifact-framework
evidencia: Cinco ocorrencias da mesma familia em quatro missoes consecutivas — R2 de FIT-2026-001, R2 de FIT-2026-002, C4 de REV-CONSOLIDACAO, D8 de REV-SOBERANO e D1 de REV-DEPARTAMENTO
confianca: alta
ocorrencias: 5
ttl: permanente
aplica_se_a: [global]
resumo: Registra por que a auditoria de coerencia detectou a segunda reproducao de tabela sem preveni-la, e o que muda no momento da escrita.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# Detectar duplicacao nao previne duplicacao

## Proposito
Registrar por que um instrumento de auditoria que funcionou como projetado ainda assim
permitiu que o mesmo defeito reaparecesse na missao seguinte.

## Escopo
Aplica-se a todo defeito de **redacao normativa** que so se manifesta no texto pronto:
reproducao de tabela, sinonimo, definicao repetida. **Nao** se aplica a defeitos de conduta,
que exigem separacao de papeis, nem a defeitos de dado, que exigem verificacao de fonte.

## Responsaveis
| Papel | Quem |
|---|---|
| Dono | DEP-KMS |
| Quem deve ler | Todo papel que redija artefato normativo com tabela |
| Verificacao da licao | DEP-QAR |

---

## Situacao
A revisao do Meta Model registrou que o grafo de transicao de estados estava reproduzido em
FND-03 §5.1 **e** em FND-09 §7.1 (R2 de FIT-2026-001). A correcao de causa entao adotada foi
criar uma **auditoria de coerencia interna de norma** (FND-04 §8), que verifica *"tabela ou
diagrama reproduzido de outro documento em vez de referenciado"*.

## Observado
Na missao seguinte, o mesmo padrao reapareceu: a coluna Local da matriz FND-10 §10.3 repete o
diretorio de cada tipo, definido em FND-03 §7 (R2 de FIT-2026-002).

A auditoria **funcionou**: encontrou o caso. E o encontrou **depois** de o documento estar
escrito, revisado e submetido — quando a unica saida barata ja era registrar ressalva com
dono e gatilho, em vez de corrigir.

Resultado observavel: **duas missoes, duas ressalvas da mesma familia, zero fechadas** ate
ADR-0008.

## Causa
O instrumento foi colocado no lugar errado da linha do tempo.

Auditoria age sobre **resultado**. Reproducao de tabela nasce de uma decisao de redacao
tomada muito antes: o autor precisa de uma informacao que vive noutro documento, e copia-la e
sempre mais rapido, mais legivel e — no instante em que ocorre — inteiramente correto. O
defeito nao e a divergencia; e a segunda fonte de verdade, que so se torna visivel quando a
fonte muda. Nada no momento da escrita sinaliza erro.

Um controle que so age depois disso nao pode prevenir nada. Pode apenas informar, com custo
maior, o que ja esta feito.

## Licao
**Defeito que nasce no momento da escrita so e prevenido por verificacao no momento da
escrita.** Auditoria posterior mede a taxa do defeito; nao a reduz.

Corolario operacional: ao corrigir a causa de um defeito de redacao, pergunte **quem** faz a
verificacao e **quando** — nao apenas se ela existe. Deslocar o verificador do revisor para o
autor e uma correcao de causa; acrescentar mais uma linha a auditoria e correcao de
ocorrencia com aparencia de correcao de causa.

## Condicoes
**Aplica-se quando:** o defeito e invisivel no instante em que e cometido e so se manifesta
por evolucao posterior de outro artefato.

**Nao se aplica quando:** o defeito e detectavel por regra objetiva no proprio artefato —
campo ausente, ID malformado, revisor igual ao autor. Nesses casos a auditoria previne de
fato, porque bloqueia o portao.

**Sinal de que se esta no caso errado:** a correcao proposta acrescenta uma verificacao a uma
lista executada por quem **nao** escreveu o texto.

## Acao
| # | O que muda | Dono | Instrumento |
|---|---|---|---|
| A1 | Tabela normativa vive em fonte unica; toda outra exibicao e **projecao declarada** com fonte, campos, finalidade e metodo de atualizacao | DEP-GOV | FND-10 §2.6, PJ-01 e PJ-02 |
| A2 | O **autor** percorre cada tabela antes de submeter | DEP-GOV | `TPL-documento` v1.2.0, checklist (PJ-05) |
| A3 | O Fitness Check pergunta pela **prevencao aplicada**, com evidencia, nao so pela ocorrencia | DEP-QAR | `TPL-fitness-check` v1.1.0, F2.b (PJ-06) |
| A4 | A auditoria de coerencia interna **permanece**, como segunda barreira | DEP-GOV | FND-04 §8 |

## Confianca
**Alta** — **cinco** ocorrencias independentes, em documentos e missoes distintos, todas
verificaveis por leitura direta. A segunda ocorreu **apos** o instrumento de deteccao existir,
o que isola a causa: o problema nao era ausencia de controle, era posicao do controle.

### Serie de ocorrencias

| # | Ocorrencia | Onde foi documentada | Objeto |
|---|---|---|---|
| 1 | Grafo de estados reproduzido em FND-03 e FND-09 | R2 de [FIT-2026-001](../../governance/fitness/FIT-2026-001-meta-model.md) | Tabela |
| 2 | Coluna Local da matriz FND-10 §10.3 repete FND-03 §7 | R2 de [FIT-2026-002](../../governance/fitness/FIT-2026-002-artifact-framework.md) | Tabela |
| 3 | FND-09 §7.3 reproduzia listas de valores de cinco fontes | C4 de [REV-CONSOLIDACAO §0](../../foundation/revisao-arquitetural-consolidacao-2026-07-28.md) | Tabela |
| 4 | Numero afirmado divergente da tabela que o sustenta | D8 de [REV-SOBERANO](../../foundation/revisao-arquitetural-conhecimento-do-soberano-2026-07-28.md) | **Afirmacao derivada** |
| 5 | Artefato declarando-se projecao **sem ser** majoritariamente projecao | D1 de [REV-DEPARTAMENTO §0](../../foundation/revisao-arquitetural-cartas-de-departamento-2026-07-28.md) | **Natureza do artefato** |

> **O alcance da licao cresceu tres vezes, e o mecanismo nunca mudou.** Comecou em *copiar
> tabela*; passou a *afirmar numero derivado que nao confere*; chegou a *classificar o proprio
> artefato como projecao sem ser*. O que se repete e a **segunda fonte de verdade**, nao o
> formato dela.

> **As ocorrencias 3, 4 e 5 foram documentadas em revisoes e nao chegavam a este registro.**
> C4 declarou-se expressamente *"terceira ocorrencia da familia, nunca registrada"* e o campo
> `ocorrencias` permaneceu em **2** por tres ciclos. Corrigido nesta versao; o defeito de
> propagacao esta registrado como achado **DR-8** de REV-DEPARTAMENTO.

## Proveniencia
| Campo | Conteudo |
|---|---|
| Origem | [FIT-2026-002](../../governance/fitness/FIT-2026-002-artifact-framework.md) §Aprendizado |
| Detectado por | DEP-QAR, em duas verificacoes de aptidao consecutivas |
| Evidencia | R2 de [FIT-2026-001](../../governance/fitness/FIT-2026-001-meta-model.md); R2 e §F2 de FIT-2026-002 |

## Relacionados
| Referencia | Relacao |
|---|---|
| [ADR-0008](../../decisions/ADR-0008-uma-fonte-multiplas-projecoes.md) | Decisao que executa A1 a A4 |
| [FND-10 §2.6](../../foundation/10-artifact-framework.md) | Onde a regra passa a viver |
| [MEM-APR-0003](MEM-APR-0003-campo-de-estado-em-artefato-imutavel.md) | Terceiro caso da mesma familia, de natureza distinta |
| [FND-04 §8](../../foundation/04-governanca.md) | Auditoria que detectou e nao preveniu |
| [MEM-APR-0004](MEM-APR-0004-projecao-revela-divergencia-antiga.md) | **Mesma familia, sentido inverso** — o ganho de exibir a mesma fonte por outro eixo |
| [ADR-0011](../../decisions/ADR-0011-contrato-de-carta-de-departamento.md) | Decisao em cuja validacao a quinta ocorrencia apareceu |

---

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-KMS | Registro inicial, com 2 ocorrencias. |
| 1.1.0 | 2026-07-28 | DEP-KMS | Emenda **MENOR**: `ocorrencias` **2 → 5**; serie de ocorrencias acrescentada a secao Confianca. As ocorrencias **3, 4 e 5** ja estavam documentadas em REV-CONSOLIDACAO, REV-SOBERANO e REV-DEPARTAMENTO e **nunca haviam chegado a este registro** — defeito de propagacao (CV-04), achado **DR-8**. |
