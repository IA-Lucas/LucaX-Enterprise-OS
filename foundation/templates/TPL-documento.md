---
id: TPL-documento
titulo: Template Base de Documento
tipo: template
versao: 1.2.0
status: ativo
camada_memoria: nao-aplicavel
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: 2027-01-28
decisoes_relacionadas: [ADR-0001, ADR-0006, ADR-0008]
substitui: []
substituido_por: null
resumo: Fornece a estrutura minima e o contrato universal de qualquer artefato do sistema.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# Template Base de Documento

## Proposito
Fornecer a estrutura minima obrigatoria de qualquer documento do LucaX Enterprise OS,
conforme [FND-03 §4](../03-taxonomia.md), e o **contrato universal de artefato** de
[FND-10 §2](../10-artifact-framework.md).

> **Este e o template universal.** ADR-0006 estendeu-o em vez de criar um segundo: um
> template universal novo seria duplicacao — exatamente o que o Artifact Framework proibe.

## Escopo
Todo documento em Markdown do sistema que nao tenha template especifico. Documentos com
template proprio (ADR, RFC, Carta, Spec, Memoria, Skill, Workflow, Ferramenta, Excecao,
Incidente, Handoff, Reporte) usam o seu.

## Responsaveis
Proprietario: DEP-GOV · Fiscalizacao: DEP-GOV (veto sobre documento fora do padrao) ·
Revisor independente: DEP-QAR.

## Historico de versoes deste template
| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-28 | DEP-GOV | Criacao. Ratificado por ADR-0001. |
| 1.1.0 | 2026-07-28 | DEP-GOV | Emenda por ADR-0006: contrato de artefato (5 campos), bloco de Linhagem, checklist estendido. |
| 1.2.0 | 2026-07-28 | DEP-GOV | Emenda por **ADR-0008**: **teste preventivo de projecao** no checklist (PJ-05) e campo opcional `projecao_de` no frontmatter. Move a verificacao de duplicacao da auditoria para o autor, antes da submissao. |

## Instrucoes de uso
1. Frontmatter completo e obrigatorio. Campo vazio = artefato nao conforme.
2. Os blocos **Proposito**, **Escopo** e **Responsaveis** sao obrigatorios e vem nesta
   ordem, logo apos o titulo. Documento sem os tres e **nulo como norma**.
3. Nome de arquivo: minusculas, kebab-case, ASCII puro, sem acento (LX-01).
4. Datas em ISO-8601 (LX-04).
5. **`revisor` e obrigatoriamente distinto de `autor`** (AC-03, LV-03). Igualdade torna a
   aprovacao nula.
6. **Nao declare o que e derivavel** (AC-01): consumidores, relacoes, autoridade e custo de
   contexto sao computados, nunca escritos no frontmatter.
7. `resumo` diz **o que o artefato faz**, nao o que ele e (AC-02).
8. `ratificacao` so vai a `ratificada` apos ato explicito e datado do Soberano sobre o texto
   final, registrado por papel distinto do executor (CV-09, LM-02 a LM-05).
9. Registre o artefato no [catalogo mestre](../../governance/artifact-registry.md) — sem
   entrada, o artefato e nao localizavel (RG-02, DoD-7).

---
---
id: <ID canonico — ver FND-03 §2>
titulo: <titulo legivel>
tipo: <fundacao|carta|spec|adr|rfc|template|workflow|memoria|ferramenta|skill|relatorio|fitness>
versao: 1.0.0
status: <rascunho|em-revisao|aprovado|ativo|depreciado|superado|revogado|arquivado>
camada_memoria: <estrategica|produto|tecnica|operacional|aprendizado|nao-aplicavel>
autor: <DEP-xxx | SOBERANO>
proprietario: <DEP-xxx>
aprovador: <DEP-xxx | SOBERANO>
criado_em: <AAAA-MM-DD>
atualizado_em: <AAAA-MM-DD>
revisao_prevista: <AAAA-MM-DD | null>
decisoes_relacionadas: []
substitui: []
substituido_por: null
# contrato de artefato (FND-10 §2.2)
resumo: <uma linha, ate 200 caracteres, em voz ativa — o que este artefato faz>
perfil_contexto: <nucleo|missao|sob-demanda|arquivo>
confidencialidade: <publico|interno|restrito|soberano>
revisor: <DEP-xxx — distinto de `autor`>
ratificacao: <nao-exigida|pendente|ratificada>
# so quando o artefato for projecao (FND-10 §2.6, PJ-02) — omitir se nao for
projecao_de: <ID §secao>
---

# <Titulo>

## Proposito
<Para que este documento existe. Ate 3 frases.>

## Escopo
| Item | Definicao |
|---|---|
| Inclui | |
| **Nao** inclui | |
| Subordinado a | |
| Consumido por | |

## Responsaveis
| Papel | Responsavel |
|---|---|
| Proprietario | |
| Aprovador | |
| Guardiao normativo | DEP-GOV |
| Obrigados | |

---

## 1. <Primeira secao de conteudo>

<...>

---

## Linhagem

| Campo | Conteudo |
|---|---|
| Origem *(RFC / ADR / INC que o autorizou)* | |
| Deriva de | |
| Implementa | |
| Substitui / substituido por | |
| Gatilho de ativacao *(quando este artefato precisa ser carregado)* | |
| Dependencias minimas *(o que vem junto — e so isso)* | |

---

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | <AAAA-MM-DD> | | Criacao. |

---

## Checklist de conformidade (FND-03 §10, FND-10 §11)
- [ ] Frontmatter completo e valido, **incluindo os cinco campos do contrato** (FND-10 §2.2)
- [ ] `revisor` presente e **distinto de `autor`** (AC-03)
- [ ] `ratificacao` coerente com a classe da mudanca (LM-02)
- [ ] `resumo` diz o que o artefato **faz**, em ate 200 caracteres (AC-02)
- [ ] Nenhum atributo derivavel declarado no frontmatter (AC-01)
- [ ] ID no formato canonico
- [ ] Tipo documental consta de FND-10 §4 (CS-01)
- [ ] Localizacao conforme a estrutura de diretorios (FND-03 §7)
- [ ] Blocos Proposito / Escopo / Responsaveis presentes e nesta ordem
- [ ] Estado valido e transicao legal
- [ ] Cadeia origem → estado → substituicao percorrivel (LN-07)
- [ ] **Teste preventivo de projecao (PJ-05, obrigatorio antes de submeter):** para **cada**
      tabela, matriz ou diagrama deste artefato — o conteudo ja existe em outro documento?
      - **Nao** → segue.
      - **Sim, e serve so para consulta** → substitua por **referencia** a fonte (ID + secao).
      - **Sim, e a exibicao e necessaria** → declare **projecao** com as quatro informacoes
        de PJ-02: fonte, campos, finalidade e metodo de atualizacao; considere `projecao_de`.
      - Marcar este item **sem** ter percorrido as tabelas e reportar como verificado algo que
        nao foi (LV-05).
- [ ] Nenhuma duplicata de conteudo existente (referencia por ID, nao copia)
- [ ] Nenhuma credencial em texto (PI-08)
- [ ] Nome de arquivo em ASCII, minusculas, kebab-case
- [ ] **Entrada criada no catalogo mestre** (RG-02)
