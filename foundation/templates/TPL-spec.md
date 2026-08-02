---
id: TPL-spec
titulo: Template de Especificacao (Spec)
tipo: template
versao: 1.1.0
status: ativo
camada_memoria: nao-aplicavel
autor: DEP-GOV
proprietario: DEP-PRD
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-29
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0001, ADR-0018, ADR-0019, ADR-0021]
substitui: []
substituido_por: null
resumo: Da a forma da Spec com o contrato completo de FND-10 §2.2 e com autoridade derivada da classe, nunca fixada no esqueleto.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# Template — Spec

## Proposito
Definir **o que** deve ser verdadeiro, **sob que condicao** e **por qual evidencia** isso sera
aceito, conforme [FND-03 §3.6](../03-taxonomia.md) e
[ADR-0021](../../decisions/ADR-0021-framework-de-specifications.md). Spec nunca define o **como**
construir.

## Escopo
Toda unidade de trabalho de produto que atravesse o portao QG-1.

> **Regra dura:** decisao de arquitetura, escolha de tecnologia e detalhe de implementacao
> **nao entram na spec** (`SF-02`). Se aparecerem, DEP-GOV devolve o documento.

> **Pre-condicao que nao se presume (`SF-23`, item 9).** [FND-04 §6](../04-governanca.md),
> linha *Spec*, exige **`Produto existe`**, e as **quatro** pre-condicoes precisam ser
> verdadeiras para a criacao ser aprovada. **Criar Produto e decisao do SOBERANO** — C2 · Tipo 1.
> Sem Produto, `O1` nao pode ocorrer, e uma Spec criada assim e nula (`MT-01`, `AC-06`).

## Responsaveis
| Papel | Quem | Fundamento |
|---|---|---|
| **Propoe e escreve** | **DEP-PRD** | [FND-09 §8.2](../09-meta-model.md), linha `SPC` |
| **Revisores independentes** | **DEP-ENG** + **DEP-QAR** | FND-09 §8.2, linha `SPC`; `AC-03` — revisor ≠ autor |
| **Aprova** | **derivado da classe do efeito** — [FND-04 §2](../04-governanca.md), com `C1` como piso (FND-04 §6) | `SF-10`; ADR-0019 |
| **Ratifica** | **SOBERANO**, e somente se **C3 ou Tipo 1** | FND-09 §8.2; `LM-02` |
| **Libera QG-1** | **DEP-EXE** | [FND-01 §6.2](../01-constituicao.md); ADR-0018 |
| **Custodiante e proprietario** | **DEP-PRD** | FND-09 §8.2, linha `SPC` — *aposenta* |

> **Liberar o portao nao e aprovar o artefato** (FND-01 §6.2, nota). `QG-1` confirma que
> resultado, criterio de aceite e escopo negativo estao presentes e verificaveis por terceiro;
> **aprovar o conteudo segue a classe da mudanca**.

## Instrucoes de uso
1. Grave em `products/<slug>/specs/SPC-<NNN>-<slug>.md` — o unico local canonico
   ([FND-03 §3.6](../03-taxonomia.md), [FND-10 §4.4](../10-artifact-framework.md)).
2. **Nao fixe aprovador nem ratificador no esqueleto.** Os dois sao **derivados** (`SF-10`);
   fixa-los foi o defeito corrigido em 1.1.0.
3. Classifique **classe** e **tipo** antes de escrever, e submeta a validacao de DEP-GOV
   (FND-04 §2). Na duvida, prevalece a classificacao **mais restritiva** (FND-01 §7.1.6).
4. Todo requisito leva os **seis** campos de `SF-12`: `ID`, motivo, fonte, criterio de aceite,
   metodo de verificacao e evidencia esperada.
5. Criterio de aceite tem de ser verificavel por terceiro **sem consultar o autor**, por um dos
   **cinco** metodos de `SF-14`: INSPECAO, DEMONSTRACAO, TESTE, ANALISE, MEDICAO.
6. A secao **Fora de escopo** e obrigatoria (`SF-08`).
7. Adjetivo sem definicao verificavel e proibido (`SF-16`). *"Rapido"* sai ou ganha numero,
   instrumento e data.
8. Ao criar, **incremente o contador oficial da sequencia na mesma mudanca** (`SF-32`,
   `CV-04`, `IX-02`), e registre a entrada no
   [catalogo mestre](../../governance/artifact-registry.md) com custo **medido** (`RG-02`,
   `CE-02`).
9. Confira o **DoR de 9 itens** antes de submeter a revisao e o **DoD de 10** antes de encerrar
   (`SF-23`, `SF-24`).

---
---
id: SPC-<NNN>-<slug>
titulo: <o que deve ser verdadeiro, em uma linha>
tipo: spec
versao: 1.0.0
status: rascunho
camada_memoria: produto
autor: DEP-PRD
proprietario: DEP-PRD
aprovador: <derivado da classe — FND-04 §2; nunca fixado aqui>
criado_em: <AAAA-MM-DD>
atualizado_em: <AAAA-MM-DD>
revisao_prevista: null
decisoes_relacionadas: []
substitui: []
substituido_por: null
resumo: <uma linha, ate 200 caracteres, voz ativa: o que esta spec faz — nao o que ela e>
perfil_contexto: sob-demanda
confidencialidade: <publico | interno | restrito | soberano>
revisor: DEP-QAR
ratificacao: <nao-exigida | pendente | ratificada — "nao-exigida" salvo se C3 ou Tipo 1>
classe_mudanca: <C0 | C1 | C2 | C3 — a classe do EFEITO, com C1 como piso>
tipo_decisao: <1 | 2>
capabilities: [<CAP-slug — ao menos uma, ativa>]
produto: <PRO-id>
criterios_aceite_count: <N>
---

# SPC-<NNN>: <Titulo>

## Proposito
<O que esta spec define. Ate 3 frases.>

## Escopo
| Item | Definicao |
|---|---|
| Produto | <PRO-id> |
| Capability | <CAP-slug> |
| Departamento custodiante | <DEP-xxx> |
| Inclui | |
| Nao inclui | *(ver §4 — obrigatorio)* |

## Responsaveis
| Papel | Quem |
|---|---|
| Autor | DEP-PRD |
| Revisores | DEP-ENG + DEP-QAR |
| Aprovador | *(derivado da classe — FND-04 §2)* |
| Ratificador | *(SOBERANO, se C3 ou Tipo 1; senao `—`)* |
| Libera QG-1 | DEP-EXE |
| Executor previsto | DEP-ENG |
| Consumidores | <quem le esta spec para agir> |

## 1. Problema
<Qual necessidade isto atende, para quem, com que consequencia se nao existir.>

## 2. Resultado esperado
<Descricao do estado final. Observavel, nao abstrato.>

## 3. Requisitos
> Cada requisito leva os **seis** campos de `SF-12`. Requisito com menos e devolvido.
> Declare a natureza de cada linha (`SF-13`): FATO · REQUISITO · HIPOTESE · RECOMENDACAO · NOTA.
> Decisao **nao entra** — remeta ao ADR.

| ID | Natureza | Verbo | Requisito | Motivo | Fonte | Criterio de aceite | Metodo | Evidencia esperada | Perfil |
|---|---|---|---|---|---|---|---|---|---|
| RQ-1 | REQUISITO | MUST | | | | | TESTE | | FUNCIONAL |
| RQ-2 | | | | | | | | | |

> **Verbos** (`SF-11`): `MUST` = deve · `SHOULD` = deveria · `MAY` = pode · `MUST NOT` = nao deve.
> **Perfis** (`SF-17`): FUNCIONAL · INTERFACE · DADOS · QUALIDADE · SEGURANCA · OPERACAO · AVALIACAO.
> **Metodos** (`SF-14`): INSPECAO · DEMONSTRACAO · TESTE · ANALISE · MEDICAO.

### 3.1 Cobertura das quatro categorias (`SF-25`)
| Categoria | Requisitos | Se ausente, o motivo |
|---|---|---|
| Funcional | | |
| Nao funcional *(com numero, instrumento e data)* | | |
| **Negativo** — o que **nao** deve ocorrer | | |
| **De falha** — o que ocorre quando o caminho feliz falha | | |

## 4. Fora de escopo
> Obrigatorio. Protege contra ampliacao silenciosa (PI-09, `SF-08`).

| Item | Por que fica de fora | Quando poderia entrar |
|---|---|---|

## 5. Limites declarados (`SF-26`)
| Natureza | Conteudo |
|---|---|
| **Suposicao** — o que se assume sem verificar, e o que muda se for falso | |
| **Limite** — o que esta fora da capacidade declarada, com o numero | |
| **Rollback** — como se desfaz, com responsavel e custo | |
| **Abandono** — como se sabe que esta spec deixou de ser necessaria | |

## 6. Restricoes
| Restricao | Origem |
|---|---|

## 7. Interfaces e dependencias
| Tipo | Contraparte | Relacao (`SF-21`) | Dono | Estado |
|---|---|---|---|---|

> Relacoes: `refina` · `restringe` · `implementa` · `verifica` · `substitui`.
> **`conflita` nao e relacao — e achado** (`SF-22`), com severidade, dono e gatilho.

## 8. Riscos
| # | Risco | Prob. | Impacto | Mitigacao | Sinal observado |
|---|---|---|---|---|---|

## 9. Verificacao e evidencia
| RQ | Metodo | Quem verifica | Quando | Evidencia registrada onde |
|---|---|---|---|---|

> Indicador **sem valor medido** declara-se `definido, sem valor` (`LM-01`, `SF-15`).
> Fabricar evidencia, fonte, metrica ou resultado e **LV-12**.

## 10. Rastreabilidade (`SF-20`)
```
objetivo -> Capability -> Departamento -> decisao -> Spec -> requisito -> aceite -> evidencia -> resultado
```
| Elo | Valor |
|---|---|
| Objetivo | |
| Capability | |
| Departamento | |
| Decisao de origem | |
| Requisitos | RQ-1 … RQ-N |
| Resultado esperado | |

## 11. Memoria consultada
| Registro (MEM-id) | O que informou esta spec |
|---|---|

## 12. Perguntas em aberto
| Pergunta | Dono da resposta | Bloqueia? |
|---|---|---|

## 13. Vigencia e evolucao
| Campo | Conteudo |
|---|---|
| Classe · Tipo | |
| Aprovacao — quem e quando | |
| Ratificacao — exigida? ato? data? | |
| Vigencia | |
| Gatilho de revisao | |
| Sucessao prevista | |

## 14. Economia de contexto (`SF-31`)
| Campo | Valor |
|---|---|
| Resumo operacional | *(o `resumo` do frontmatter)* |
| Gatilho de ativacao | |
| Pacote minimo | |
| Custo medido — linhas, por `wc -l`, com data | |
| Requisito enderecavel | `<SPC-id> RQ-nn` carrega o bloco, nao o documento |

## 15. DoR — antes de submeter a revisao (`SF-23`)
| # | Item | OK |
|---|---|---|
| 1 | Problema definido **antes** da solucao | [ ] |
| 2 | Consumidor nomeado e necessidade demonstrada | [ ] |
| 3 | As quatro perguntas de nao-proliferacao respondidas (FND-04 §6.1) | [ ] |
| 4 | Capability **ativa** vinculada (VC-01) | [ ] |
| 5 | Classe e tipo classificados, e validados por DEP-GOV | [ ] |
| 6 | Exclusoes declaradas (§4) | [ ] |
| 7 | Todo requisito com os seis campos | [ ] |
| 8 | Revisores designados, **≠ autor** | [ ] |
| 9 | Pre-condicoes de FND-04 §6 satisfeitas — inclusive **`Produto existe`** | [ ] |

## 16. Portao QG-1 e DoD (`SF-24`)
| Verificacao | OK |
|---|---|
| Problema definido | [ ] |
| Resultado observavel | [ ] |
| Criterios verificaveis por terceiro | [ ] |
| Fora de escopo declarado | [ ] |
| Nenhuma decisao de implementacao embutida | [ ] |
| Cobertura das quatro categorias, ou ausencia justificada | [ ] |
| Limites, rollback e abandono declarados | [ ] |
| Cadeia de nove elos percorrivel | [ ] |
| Entrada no catalogo mestre, com custo medido | [ ] |
| Contador oficial da sequencia incrementado na mesma mudanca | [ ] |
| **Liberado por** | **<DEP-EXE, data>** |
| Aprovado por | *(derivado da classe — quem, e em que data)* |
| Ratificado por | *(SOBERANO, se C3 ou Tipo 1 — ato explicito e datado)* |

---

## Historico de versoes
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-GOV | Criacao. |
| 1.1.0 | 2026-07-29 | DEP-PRD | Emenda **C2** por [ADR-0021](../../decisions/ADR-0021-framework-de-specifications.md), que **fecha `RD-23`**. **Cinco defeitos medidos e corrigidos**, onde o achado declarava dois: o esqueleto fixava **`aprovador: DEP-PRD`** — agora **derivado da classe** (`SF-10`, ADR-0019); **nao tinha `ratificacao`** — agora presente, `nao-exigida` salvo **C3 ou Tipo 1**; **nao tinha `resumo`, `perfil_contexto`, `confidencialidade` nem `revisor`** — os quatro acrescentados, por `FND-10 §2.2` e `AC-06`; **§11 declarava *"Liberado por DEP-PRD"*** — agora **DEP-EXE**, por `FND-01 §6.2` pos-ADR-0018; e **§Responsaveis nao tinha revisor** — agora **DEP-ENG + DEP-QAR**, por `AC-03`. Acrescenta o corpo exigido por `SF-05` a `SF-31`: requisitos com **seis** campos e natureza declarada, **quatro** categorias de cobertura, **quatro** limites, **cinco** metodos de verificacao, rastreabilidade de **nove** elos, economia de contexto e os checklists **DoR de 9** e **DoD de 10**. **Nenhum campo novo foi criado** (`AC-07`); **nenhuma fonte foi emendada**; o vinculo a `products/<slug>/specs/` **foi preservado e explicitado como pre-condicao que nao se presume** — achado `RD-33`. |
