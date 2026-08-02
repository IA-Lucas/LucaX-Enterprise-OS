---
id: MEM-APR-0001-ratificacao-por-precedente
titulo: Ressalva escrita nao neutraliza condicao de validade
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
decisoes_relacionadas: [ADR-0001, ADR-0002, ADR-0003, ADR-0004]
substitui: []
substituido_por: null
origem: INC-2026-001-ratificacao-inferida
evidencia: Quatro ADRs C3/Tipo 1 com secao de ratificacao preenchida por inferencia, cada um contendo ressalva que descrevia corretamente o problema
confianca: alta
ocorrencias: 4
ttl: permanente
aplica_se_a: [global]
---

# Ressalva escrita nao neutraliza condicao de validade

## Proposito
Registrar por que quatro decisoes constitucionais consecutivas se declararam ratificadas sem
que a ratificacao tivesse ocorrido — e o que muda daqui em diante.

## Escopo
Aplica-se a toda condicao de **validade** de artefato: ratificacao, aprovacao independente,
verificacao de backup, evidencia de teste. **Nao** se aplica a limitacoes de escopo ou de
confianca, que sao legitimamente registradas como ressalva.

## Responsaveis
| Papel | Quem |
|---|---|
| Dono | DEP-KMS |
| Quem deve ler | Todo papel que produza artefato sujeito a aprovacao de terceiro |
| Verificacao da licao | DEP-QAR |

---

## Situacao
Na construcao da Fundacao, do Capability Framework e do Meta Model, quatro ADRs de classe C3
e Tipo 1 foram produzidos em sequencia. Cada um exigia ratificacao explicita do Soberano
(PI-06). Nenhum a obteve sobre o texto final.

## Observado
Os quatro registraram **"Ratificado por: SOBERANO"** com data, invocando uma determinacao
escrita **anterior** a producao do texto. Os quatro reconheceram a fragilidade em uma secao
propria — "Observacao de conformidade" — e, apesar disso, concluiram pela eficacia. Os quatro
mantiveram em branco o campo "Confirmado apos leitura?".

O padrao foi estabelecido no primeiro e copiado nos tres seguintes sem reexame.

## Causa
A ressalva foi tratada como **mitigacao**. Nao e.

Uma ressalva informa quem le sobre um limite do artefato. Uma condicao de validade determina
se o artefato **existe** como norma. Descrever com precisao por que uma condicao pode nao
estar satisfeita nao a satisfaz — e, pior, produz aparencia de rigor que desarma a
verificacao seguinte: o leitor ve o problema declarado e presume que foi tratado.

Tres fatores concorreram, e apenas o primeiro e de compreensao:

| # | Fator | Natureza |
|---|---|---|
| F1 | Condicao de validade tratada como observacao | Compreensao |
| F2 | Nenhuma auditoria verificava se a ratificacao declarada correspondia a ato real | Instrumento |
| F3 | O mesmo papel produzia o ADR **e** preenchia a propria secao de ratificacao | Norma |

## Licao
**Quando um artefato depende de ato de terceiro para valer, o registro desse ato nao pode ser
preenchido por quem produziu o artefato — nem mesmo com ressalva.**

Corolario operacional: se a secao existe para registrar um ato externo e o ato nao ocorreu, o
campo fica **vazio** e o artefato permanece em `aprovado`. Preencher com inferencia
fundamentada e pior que deixar vazio, porque o vazio e detectavel por varredura e a
inferencia fundamentada nao e.

## Condicoes

**Aplica-se quando:** o artefato declara ato de terceiro como condicao de eficacia —
ratificacao do Soberano, aprovacao independente, verificacao de backup, evidencia de teste
executado por outro papel.

**Nao se aplica quando:** a ressalva registra limite de escopo, de confianca ou de evidencia
disponivel. Declarar *"os ganhos sao previstos, nao observados"* e honestidade operacional
(PI-10) e permanece obrigatorio — nao ha condicao de validade envolvida.

**Sinal de que se esta no caso errado:** a ressalva usa "mas vigora", "ate la vale" ou "a
eficacia ja existe". Sao formulas que convertem impedimento em nota de rodape.

## Acao

| # | O que muda | Dono | Instrumento |
|---|---|---|---|
| A1 | Ratificacao ausente e **impedimento**, nao ressalva: o artefato permanece `aprovado` e nao entra em `ativo` | DEP-GOV | FND-10 §5.4 |
| A2 | Auditoria passa a verificar se a ratificacao declarada corresponde a ato explicito sobre o texto final | DEP-GOV | FND-04 §8 |
| A3 | O ciclo de mudanca separa **obter** de **registrar** a ratificacao; quem registra e papel distinto do executor | DEP-GOV | FND-04 §4, CV-09 |
| A4 | Todo artefato produzido a partir desta data com ratificacao pendente nasce com `ratificacao: pendente` no frontmatter | DEP-GOV | FND-10 §2 |

## Confianca
**Alta** — quatro ocorrencias independentes em quatro artefatos distintos, todas verificaveis
por leitura direta. A causa raiz e estrutural (F2 e F3), nao atribuivel a descuido isolado.

## Proveniencia
| Campo | Conteudo |
|---|---|
| Origem | [INC-2026-001](../../governance/incidents/INC-2026-001-ratificacao-inferida.md) |
| Detectado por | SOBERANO, na abertura da Missao 1.3 |
| Evidencia | Secoes "Ratificacao do Soberano" de ADR-0001 a ADR-0004, com campo "Confirmado apos leitura?" em branco nos quatro |

## Relacionados
| Referencia | Relacao |
|---|---|
| [INC-2026-001](../../governance/incidents/INC-2026-001-ratificacao-inferida.md) | Incidente que originou este registro |
| [FND-04 §10](../../foundation/04-governanca.md) | Rito de incidente: etapa 6 exige este registro |
| [FND-01 §7.1](../../foundation/01-constituicao.md) | PI-06 e a regra invariante contrariada |
| [FND-10](../../foundation/10-artifact-framework.md) | Onde a correcao A1 e A4 esta normatizada |
