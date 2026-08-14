---
id: MSG-2026-0015
titulo: Ato Soberano de ratificação do ADR-0044 — primeira Ferramenta vigente do acervo
tipo: relatorio
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: SOBERANO
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-08-14
atualizado_em: 2026-08-14
revisao_prevista: null
decisoes_relacionadas: [ADR-0041, ADR-0044]
substitui: []
substituido_por: null
canal: DIRETIVA
emissor: SOBERANO
destinatario: DEP-GOV
ttl: 1 ciclo — expira sem perda; o ato fica ancorado por hash e os efeitos duráveis são aplicados na mesma sessão
resumo: Registra o décimo quinto ato soberano — a frase literal "Ratifico o ADR-0044 em 2026-08-14", ancorada no H-A do ADR no momento do ato — que ratifica ADR-0044 e adota TOL-local-baseline-do-acervo como primeira Ferramenta vigente do acervo.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# MSG-2026-0015 — Ato Soberano de 2026-08-14 *(décimo quinto ato)*

## Propósito

Registrar o ato que o Fundador emitiu em conversa direta — a frase literal **"Ratifico o
ADR-0044 em 2026-08-14"** —, com a âncora de hash do texto que o ato alcança
([`ADR-0044`](../../decisions/ADR-0044-adocao-da-baseline-como-ferramenta.md), no estado em
que estava no momento do ato) e a aplicação, que ocorre na mesma sessão por ser de baixo
risco e escopo mínimo — diferente dos atos anteriores, que separaram emissão de aplicação
por serem admissões de Produto com risco Tipo 1 de maior superfície.

> **Décimo quinto ato soberano registrado.** Os catorze anteriores vivem em
> `MSG-2026-0001` a `MSG-2026-0014` (`memory/operacional/`). **Nenhum dos catorze foi
> editado.** Quinze atos, quinze fontes.

## Escopo

| Item | Definição |
|---|---|
| Inclui | O ato, literal; a âncora de hash de `ADR-0044` no momento do ato; o objeto que alcança (`ADR-0044` e, por decorrência declarada no próprio ADR §5, `tools/TOL-local-baseline-do-acervo.md`); a aplicação nesta mesma sessão |
| **Não** inclui | O mérito da adoção — vive em [`RFC-0039`](../../rfcs/RFC-0039-adocao-da-baseline-como-ferramenta.md) e [`ADR-0044`](../../decisions/ADR-0044-adocao-da-baseline-como-ferramenta.md) · qualquer alteração ao script `baseline.sh` · adoção de qualquer outra Ferramenta |
| Instrumento | **Diretiva**, tipo documental de `FND-10 §4.6`, entidade `MSG`. Nenhum tipo, entidade, camada ou diretório novo |

## Responsáveis

| Papel | Quem | Fundamento |
|---|---|---|
| **Emissor** | **SOBERANO** | `TF-10` — Ratificação, indelegável |
| **Registra e aplica** | **DEP-GOV** | `LM-05`, `CV-09` |
| **Verifica a eficácia da aplicação** | **DEP-QAR** | `FND-10 §10.5` |

---

## 1. Âncora do ato — o texto ratificado, por hash

> **O ato foi emitido sobre um texto identificado, não sobre uma referência.** Se o arquivo
> mudar depois, o `H-A` abaixo deixa de reproduzir — e o ato não alcança o texto novo.

| Campo | Valor |
|---|---|
| **Objeto ratificado** | [`ADR-0044`](../../decisions/ADR-0044-adocao-da-baseline-como-ferramenta.md), versão `1.0.0`, no estado `em-revisao` em que foi submetido |
| Caminho | `decisions/ADR-0044-adocao-da-baseline-como-ferramenta.md` |
| **`H-A` do ADR no momento do ato** | `44449f9417ff2e2d21bd445b1a8507cd68a99f009bdedec4bc81c1f915421aaf` |
| Como reproduzir | `sha256sum decisions/ADR-0044-adocao-da-baseline-como-ferramenta.md` sobre o commit `fad2c65` (o HEAD no instante do ato) |

## 2. Decisão soberana — literal

**ATO SOBERANO — RATIFICAÇÃO DO ADR-0044**

> Ratifico o ADR-0044 em 2026-08-14.
>
> **Soberano** · data: 2026-08-14

## 3. Objetos que o ato alcança

| # | Objeto | Efeito |
|---|---|---|
| 1 | `decisions/ADR-0044-adocao-da-baseline-como-ferramenta.md` | `status: em-revisao → ativo`; `ratificacao: pendente → ratificada`; §11 (Classificação) ganha data da decisão e de vigência: `2026-08-14` |
| 2 | `tools/TOL-local-baseline-do-acervo.md` | `status: rascunho → ativo`; `ratificacao: pendente → ratificada` — por decorrência direta e declarada no próprio `ADR-0044 §5`, item 1 |

**Nenhum outro objeto é tocado.** `0` bytes do script `baseline.sh` mudam (`ADR-0044 §5`,
item 4). `0` entidades, classes, tipos, templates, papéis ou portões são criados (`ADR-0044
§5`, item 5).

## 4. Condições de eficácia — respondidas no próprio ADR, conferidas aqui

| # | Condição (`ADR-0044`) | Estado |
|---|---|---|
| `Q1` | Confirmar `criticidade: média`, ou ajustar | **Não objetado — permanece `média`** |
| `Q2` | Dono distinto de `DEP-TLS`? | **Não objetado — permanece `DEP-TLS`** |
| Checklist `FND-07 §4.1` | `VD-01` a `VD-09` | **9 de 9**, já `[x]` no ADR antes do ato |

Nenhuma condição ficou pendente de resposta — as duas questões submetidas eram
declaradamente não-bloqueantes, e o ato não trouxe objeção a nenhuma.

## 5. O que este ato NÃO faz

| # | Não faz | Verificação |
|---|---|---|
| `N1` | Não altera o script `baseline.sh` | `0` bytes, medido pelo `sha256` do script antes/depois do ato |
| `N2` | Não adota outra Ferramenta | Só `TOL-local-baseline-do-acervo` é objeto deste ato |
| `N3` | Não corrige `TPL-ferramenta` (`AF-1`/`AF-2`) | Seguem abertos, rito próprio de `TPL`, `DEP-GOV + DEP-TLS` |
| `N4` | Não emenda Fundacional alguma | `0` `FND` tocados |
| `N5` | Não fecha `1.19` | Passa de `3/10` para `4/10` — ainda restam Agente e o restante da cadeia de execução |

## 6. Aplicação

Diferente dos atos de admissão de Produto (`MSG-2026-0009`, `MSG-2026-0010`), que separaram
emissão de aplicação por escopo e risco maiores, **este ato é aplicado na mesma sessão**:
o efeito é a troca de dois campos de frontmatter em dois arquivos, já declarada
integralmente em `ADR-0044 §5`, com plano de reversão trivial (`ADR-0044 §10`) e `0`
dependente criado pela adoção. `DEP-GOV` aplica imediatamente após este registro, sob o
mesmo `fencing_token` do lease vigente.

## 7. Rastreabilidade

| Campo | Conteúdo |
|---|---|
| Origem | [`RFC-0039`](../../rfcs/RFC-0039-adocao-da-baseline-como-ferramenta.md) → [`ADR-0044`](../../decisions/ADR-0044-adocao-da-baseline-como-ferramenta.md) |
| Artefatos alterados pela aplicação | `ADR-0044` (`status`, `ratificacao`, §11) · `TOL-local-baseline-do-acervo.md` (`status`, `ratificacao`, §16) · `governance/roadmap-canonico.md` (`1.19`) · `governance/artifact-registry.md` (histórico) |
| Achados fechados | `AF-3` de `ADR-0041`, quanto à vigência |
| Achados que permanecem abertos | `AF-1`/`AF-2` de `ADR-0041` — não tocados |

## Histórico de versões

| Versão | Data | Autor | Mudança |
|---|---|---|---|
| 1.0.0 | 2026-08-14 | DEP-GOV | Registro do décimo quinto ato soberano. Ratifica `ADR-0044`; aplicado na mesma sessão por escopo mínimo e risco quase nulo. `0` bytes de código alterados; `2` arquivos de governança mudam `status`/`ratificacao`. |
