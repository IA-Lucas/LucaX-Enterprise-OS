---
id: MSG-2026-0016
titulo: Ato Soberano de ratificação do ADR-0045 — poda semestral e nível de autonomia vigentes
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
decisoes_relacionadas: [ADR-0045, ADR-0039]
substitui: []
substituido_por: null
canal: DIRETIVA
emissor: SOBERANO
destinatario: DEP-GOV
ttl: 1 ciclo — expira sem perda; o ato fica ancorado por hash e os efeitos duráveis são aplicados na mesma sessão
resumo: Registra o décimo sexto ato soberano — a frase literal "Ratifico o ADR-0045 em 2026-08-14" — que faz vigorar D3 (rito semestral de poda de instruções, salvaguardas fora) e D4 (nível de autonomia nas Cartas), com os defaults Q1/Q2 sem objeção.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# MSG-2026-0016 — Ato Soberano de 2026-08-14 *(décimo sexto ato)*

## Propósito

Registrar o ato que o Fundador emitiu em conversa direta — a frase literal **"Ratifico o
ADR-0045 em 2026-08-14"**, acompanhada de *"pode comitar e dar push"* —, com a âncora de
hash do texto que o ato alcança
([`ADR-0045`](../../decisions/ADR-0045-absorcao-da-triagem-antigravity.md), no estado em
que estava no momento do ato) e a aplicação na mesma sessão, pelo mesmo fundamento do
décimo quinto ato: escopo mínimo, reversão trivial, `0` código tocado.

> **Décimo sexto ato soberano registrado.** Os quinze anteriores vivem em
> `MSG-2026-0001` a `MSG-2026-0015` (`memory/operacional/`). **Nenhum dos quinze foi
> editado.** Dezesseis atos, dezesseis fontes.

## Escopo

| Item | Definição |
|---|---|
| Inclui | O ato, literal; a âncora de hash de `ADR-0045` no momento do ato; a vigência de D3 e D4 com os defaults de `Q1`/`Q2`; a autorização de push desta aplicação; a aplicação nesta mesma sessão |
| **Não** inclui | O mérito — vive em [`RFC-0040`](../../rfcs/RFC-0040-absorcao-da-triagem-antigravity.md) e [`ADR-0045`](../../decisions/ADR-0045-absorcao-da-triagem-antigravity.md) · a execução da 1ª poda (2027-02, sessão própria) · a redação material do campo nas Cartas (rito próprio de manutenção das Cartas) |
| Instrumento | **Diretiva**, tipo documental de `FND-10 §4.6`, entidade `MSG`. Nenhum tipo, entidade, camada ou diretório novo |

## Responsáveis

| Papel | Quem | Fundamento |
|---|---|---|
| **Emissor** | **SOBERANO** | Ratificação de `C2` com ato — indelegável |
| **Registra e aplica** | **DEP-GOV** | `LM-05`, `CV-09` |
| **Verifica a eficácia** | **DEP-QAR** | `FND-10 §10.5` |

---

## 1. Âncora do ato — o texto ratificado, por hash

| Campo | Valor |
|---|---|
| **Objeto ratificado** | [`ADR-0045`](../../decisions/ADR-0045-absorcao-da-triagem-antigravity.md), versão `1.0.0`, no estado `em-revisao` em que foi submetido |
| Caminho | `decisions/ADR-0045-absorcao-da-triagem-antigravity.md` |
| **`H-A` do ADR no momento do ato** | `752dcab2029d0546a325849993bd850217c9d0b865886870017b4eff056086ec` |
| Como reproduzir | `sha256sum decisions/ADR-0045-absorcao-da-triagem-antigravity.md` sobre o commit `f4b9b07` (o HEAD no instante do ato) |

## 2. Decisão soberana — literal

**ATO SOBERANO — RATIFICAÇÃO DO ADR-0045**

> Ratifico o ADR-0045 em 2026-08-14. pode comitar e dar push.
>
> **Soberano** · data: 2026-08-14

## 3. Objetos que o ato alcança

| # | Objeto | Efeito |
|---|---|---|
| 1 | `decisions/ADR-0045-absorcao-da-triagem-antigravity.md` | `status: em-revisao → ativo`; `ratificacao: pendente → ratificada`; §7 ganha data da decisão e de vigência de D3/D4: `2026-08-14` |
| 2 | **D3 vigente** | Rito semestral de poda de instruções comportamentais; matéria 🔒 fora por desenho; **1ª poda: 2027-02, piloto no Corpo** (`Q1` default, sem objeção) |
| 3 | **D4 vigente** | Toda missão de Carta **criada ou emendada a partir de 2026-08-14** declara `nivel_de_autonomia` (conduzido/assistido/autônomo); **por Carta, na primeira missão que a tocar** (`Q2` default, sem objeção); Cartas paradas não são reabertas para isso |

**D1 e D2 já vigoravam** como registro desde a emissão (competência `DEP-GOV`) — o ato
não os altera, confirma o conjunto.

## 4. Condições de eficácia

| # | Condição (`ADR-0045 §8`) | Estado |
|---|---|---|
| `Q1` | 1ª poda: piloto no Corpo ou fábrica inteira? | **Não objetado — piloto no Corpo** |
| `Q2` | Campo de autonomia: por Carta ou nas 8 de uma vez? | **Não objetado — por Carta, na primeira missão que a tocar** |
| Checklist `FND-07 §4.1` | `VD-01` a `VD-09` | **9 de 9**, já `[x]` no ADR antes do ato |

## 5. O que este ato NÃO faz

| # | Não faz | Verificação |
|---|---|---|
| `N1` | Não executa a 1ª poda | Agendada: 2027-02, sessão própria, piloto no Corpo |
| `N2` | Não emenda nenhuma Carta nem o template das Cartas | A redação material segue rito próprio; o princípio vale para missão nova/emendada |
| `N3` | Não toca código de repositório algum | `0` bytes fora de `governance/`, `decisions/`, `memory/` |
| `N4` | Não emenda Fundacional alguma | `0` `FND` tocados |
| `N5` | Não autoriza podar salvaguarda | Matéria 🔒 (segurança, backup, credencial, escopo/honestidade, bloqueios destrutivos) está fora da poda **por desenho do próprio D3** |

## 6. Aplicação

Aplicado na mesma sessão, sob o `fencing_token 80`, pelo mesmo fundamento do décimo
quinto ato: o efeito durável é troca de campos de frontmatter e registro — reversão
trivial (`ADR-0045 §6`), `0` dependente criado. O push desta aplicação foi autorizado
no próprio ato.

## 7. Rastreabilidade

| Campo | Conteúdo |
|---|---|
| Origem | [`RFC-0040`](../../rfcs/RFC-0040-absorcao-da-triagem-antigravity.md) → [`ADR-0045`](../../decisions/ADR-0045-absorcao-da-triagem-antigravity.md) → triagem de 2026-08-14 (Oficina, handoffs) |
| Artefatos alterados pela aplicação | `ADR-0045` (`status`, `ratificacao`, §7, histórico) · `governance/roadmap-canonico.md` (conferência + agenda da 1ª poda) · `governance/artifact-registry.md` (2.58.0) |
| Compromissos futuros criados | 1ª poda **2027-02** (piloto: Corpo) · campo `nivel_de_autonomia` obrigatório em missão de Carta criada/emendada |
| Pendências que permanecem na Oficina | Registro de entrada das 3 peças · reconciliação 175×207 vídeos |

## Histórico de versões

| Versão | Data | Autor | Mudança |
|---|---|---|---|
| 1.0.0 | 2026-08-14 | DEP-GOV | Registro do décimo sexto ato soberano. Ratifica `ADR-0045`; D3/D4 vigentes com os defaults `Q1`/`Q2` sem objeção; aplicado na mesma sessão; push autorizado no próprio ato. |
