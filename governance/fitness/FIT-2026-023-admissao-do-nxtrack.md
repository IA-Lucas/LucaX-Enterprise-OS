---
id: FIT-2026-023
titulo: Verificacao de aptidao da admissao do nXtrack pelo portao de origem externa
tipo: fitness-check
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: DEP-QAR
proprietario: DEP-QAR
aprovador: SOBERANO
criado_em: 2026-08-01
atualizado_em: 2026-08-01
revisao_prevista: null
decisoes_relacionadas: [ADR-0007, ADR-0015, ADR-0027, ADR-0030]
substitui: []
substituido_por: null
veredito: apto-com-ressalva
resumo: Verifica a aptidao da admissao do nXtrack com G0 IDENTIDADE e G3 RECOGNIZE, com conformidade em 14 de 14 controles e quatro ressalvas de dono e gatilho declarados.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-GOV
ratificacao: nao-exigida
---

# FIT-2026-023: admissao do nXtrack

> **Parecer, nao decisao** (`ADR-0015`, `FT-10`). **Nao aprova, nao ratifica, nao promulga.**
> `FND-09 §8.2`, linha `FIT`: **ratifica `—`**. O objeto avaliado — `ADR-0030` — esta
> **`em-revisao`** e **nao esta em vigor**.

## Proposito

Emitir a Verificacao de Aptidao Arquitetural exigida por `CV-07` de `FND-04 §4.1` sobre a
mudanca `C2`/`Tipo 1` registrada em
[ADR-0030](../../decisions/ADR-0030-admissao-do-nxtrack-como-primeiro-produto.md), e cumprir a
condicao **`G4`** do portao de [ADR-0007 §5.3](../../decisions/ADR-0007-fronteira-greenfield-legado.md):
*"Validacao independente — verificacao por papel distinto de quem propos, **contra a norma
vigente — nao contra a pratica do Legacy**"*.

## Escopo

| Item | Definicao |
|---|---|
| Avaliado | O **rito** `RFC-0025` → `ADR-0030` · a declaracao de **`G0`** · a determinacao de **`G3`** · o fechamento de **`G1`** · o **fit-gap** de `G2` · o custo de reversao · os **limites obrigatorios medidos** · a nao-contaminacao do acervo e do candidato |
| **Nao** avaliado | **O merito tecnico do nXtrack** — nenhum controle de qualidade de software foi aplicado · a arquitetura do candidato · o codigo · os dados · `Q1`, que esta **respondida** · `E2` · `ADR-0026`, que segue `em-revisao` |

## Responsaveis

| Papel | Quem | Fundamento |
|---|---|---|
| Emite | **DEP-QAR** | `FND-09 §8.2` linha `FIT`; `G4` de `ADR-0007 §5.3` |
| Revisa a forma | **DEP-GOV** | idem |
| Aprova | **SOBERANO** | `C2`/`Tipo 1` |
| Ratifica | **—** | `FT-10` |

> ### Independencia desta verificacao — declarada pelo criterio VIGENTE
>
> **Criterio aplicado: `AC-03` de `FND-10 §2.5`** — `revisor` ≠ `autor`. **Satisfeito:** autor
> **DEP-QAR**, revisor **DEP-GOV**; o objeto avaliado (`ADR-0030`) tem autor **DEP-PRD** e o
> instrumento de origem (`RFC-0025`) tambem. **Tres papeis distintos, e nenhum verifica a si
> proprio.**
>
> **`ADR-0028` NAO esta em vigor e NAO se aplica a este parecer.** Sob o criterio que ela
> propoe, esta verificacao seria **`fornecedor_verificacao: interno`** — mesmo executor. **A
> diferenca esta escrita para que ninguem leia este parecer como independente de fornecedor.**
> A fila de retidos e `2` — `ADR-0026` e `ADR-0028` —, e `E2` segue **adiada e intacta**.

## 1. Controles obrigatorios

> Cada resultado abaixo foi **remedido por metodo distinto** do usado na producao do objeto.
> Nenhum e leitura do que o proponente escreveu.

| # | Controle | Fonte | Resultado |
|---|---|---|---|
| `F1` | **`G0` declarado ANTES de `G1`**, e determinando a lista de `G3` | `GA-01`, `ADR-0027 §5.1` | ✅ `ADR-0030 §5.1` declara `IDENTIDADE`; `§5.2` deriva dele a lista |
| `F2` | **`G3` determinado, jamais por eliminacao** | `GA-03`; enunciado da missao | ✅ Lista de `IDENTIDADE` tem **dois** membros; `RETIRE` descartada por **fato citado** *(decisao 7 de `PT-2026-009`)*; `RECOGNIZE` sustentada elemento a elemento da definicao |
| `F3` | **`G1` fechado por medicao, nao por presuncao** | Item 0 da missao | ✅ **`0`** caminhos sem commit na subarvore de **183** rastreados; **17 de 17** fontes consumidas com autor e data; **`0`** nao atribuiveis |
| `F4` | **Congelamento que sobrevive a repositorio vivo** | idem | ✅ Objeto `tree` **`b9b36be9…fb4b`**, identico em `HEAD` *(`b9fbccd`, de hoje)* e em `a7fc0946` *(2026-07-27)*. **Reconferido apos toda a escrita: identico** |
| `F5` | **Escritor concorrente medido, nao presumido ausente** | idem | ✅ **Presenca detectada** no hospedeiro *(sessao `2bad2c98`, 08:25:47; commit `b9fbccd` as 07:37)* e **`0`** escritas na subarvore apos `T0`. Nao se afirmou ausencia: mediu-se presenca e alcance |
| `F6` | **`0` bytes do candidato no acervo** | `K1` de `RFC-0025 §3` | ✅ **Medido por colisao de hash:** **179** hashes distintos dos 183 rastreados do candidato confrontados com **todos** os arquivos do acervo — **`0` colisoes** |
| `F7` | **`0` fundacionais emendados** | `CV-04`, `VD-07` | ✅ **Medido contra o `H-A` do ponto de partida:** `FND-01`, `FND-04`, `FND-08`, `FND-09`, `FND-10`, `FND-11` — **identicos** |
| `F8` | **`ADR-0007` aplicado, nao emendado** | `AL-02`, `LV-04` | ✅ **`0` bytes.** `ADR-0007`, `ADR-0027` e `ADR-0026` byte a byte identicos ao ponto de partida |
| `F9` | **`RFC` produzida quando a classe exige** | `FND-04 §2` | ✅ [RFC-0025](../../rfcs/RFC-0025-admissao-do-nxtrack-como-primeiro-produto.md) — **dispensa nao disponivel**, tres alternativas defensaveis (`ADR-0030 §11.2`) |
| `F10` | **Classe determinada, nao presumida por analogia** | `AL-01`, `FND-04 §2` | ✅ **As cinco hipoteses de `C3` percorridas uma a uma** (`ADR-0030 §11.1`); a hipotese de `C2` **nomeia o ato** — *"criar produto"* |
| `F11` | **`Tipo 1` respeitado**, e nao rebaixado pelo custo medido | `FND-09 E-17`; `PI-06` | ✅ `§11.1` declara que **custo baixo nao converte `Tipo 1` em `Tipo 2`** quando a norma o atribui por natureza do componente |
| `F12` | **Vinculo a Capability valido** | `VC-01`, pre-condicao universal I | ✅ **5 de 5** existem, estao **`ativo`** e constam do catalogo. **`VC-03` dispara e esta declarado** — nao suprimido |
| `F13` | **Custo de reversao medido objeto a objeto** | `VD-06` | ✅ `ADR-0030 §10`: 1 `ADR` + 1 Carta + 1 entrada + 5 indices; **`0`** historicos, **`0`** fundacionais, **`0`** migrados, **`0`** consumidores |
| `F14` | **Ausencia de evidencia declarada** | `VD-05`, `PI-10` | ✅ **Duas** ausencias em `ADR-0030 §8`: `A1` *(bancos nao abertos — usuarios reais nao contados)* e `A2` *(nenhum ensaio, nenhuma taxa de aceitacao)* |

**Conformidade: 14 de 14.**

## 2. As seis respostas com sinal observavel (`FND-04 §6`, linha *Verificacao de aptidao*)

| # | Pergunta | Resposta | Sinal observavel |
|---|---|---|---|
| 1 | **O objeto avaliado esta nomeado?** | Sim | `ADR-0030`, `RFC-0025`, e a Carta candidata de `H-A` `4d4c12e0…75c5` |
| 2 | **A mudanca cabe na norma vigente?** | **Sim** | O portao existe (`ADR-0007 §5.3`), a classe existe (`ADR-0027 §5.2`), a entidade existe (`FND-09 E-17`, `Cardinalidade 0..n`), o template existe (`TPL-carta-produto` 1.1.0) e o rito existe (`FND-04 §6`). **Nada precisou ser criado para caber** |
| 3 | **A mudanca cria acervo paralelo?** | **Nao** | **`0`** entidades novas, **`0`** tipos documentais novos, **`0`** arquivos do candidato copiados |
| 4 | **A mudanca e reversivel?** | Sim, a custo medido | `ADR-0030 §10`, objeto a objeto; janela: **enquanto `RD-33` nao fechar** |
| 5 | **O executor e distinto do produtor?** | **Sim pelo criterio vigente** | `AC-03`: autor `DEP-QAR`, revisor `DEP-GOV`, objeto de `DEP-PRD`. **Ressalva `S1`** abaixo |
| 6 | **As ressalvas tem dono e gatilho?** | Sim | §3 — quatro ressalvas, cada uma com dono e gatilho |

## 3. Ressalvas — com dono e gatilho, e **sem missao** (congelamento em vigor)

| # | Ressalva | Severidade | Dono | Gatilho |
|---|---|---|---|---|
| **`S1`** | **Independencia e de PAPEL, nao de fornecedor.** Os tres papeis sao distintos por `AC-03`, e o executor material e o mesmo. Sob `ADR-0028` — **`em-revisao`, `E2` adiada** — este parecer seria `fornecedor_verificacao: interno` | **Media** | DEP-QAR | Vigencia de `ADR-0028` |
| **`S2`** | **Custodia do Produto fica fora do acervo.** O nXtrack e subarvore de `lucaX`, com **758** caminhos sem commit e escritor concorrente. A Carta descreve a custodia **que o ato institui**, nao a que existe | **Alta** | DEP-PRD | Primeira `Spec` do `PRO-nxtrack` — achado `RD-71` |
| **`S3`** | **A Carta descreve um produto vivo e nao tem mecanismo de sincronia.** Se o candidato evoluir e ninguem emendar, a Carta vira ficcao — e este e o sinal *(a)* de erro declarado em `ADR-0030 §12` | **Media** | DEP-PRD | Primeira `Spec`, ou primeiro commit no candidato apos a vigencia |
| **`S4`** | **`VC-03` disparado:** cinco Capabilities vinculadas onde a norma sinaliza em tres. Nao se cria Capability; avalia-se especializacao **do componente** | **Media** | DEP-PRD | Primeira `Spec` — achado `RD-74` |

## 4. Resultado negativo, declarado (`PI-10`)

A verificacao **procurou e nao encontrou**: arquivo do candidato dentro do acervo *(`0`
colisoes em 179 hashes)*; fundacional emendado *(`0` em 6)*; artefato historico editado
*(`0`)*; `ADR-0007` alterado *(`0` bytes)*; Capability inexistente, `proposta` ou `aposentada`
no vinculo *(`0` em 5)*; escrita da missao no repositorio do candidato *(`0`; `tree` e `HEAD`
identicos)*; `Spec` criada *(`0`)*; `products/` existente *(**nao existe**)*; ato emitido
*(`0` — seguem **8** `MSG`)*. **Nove verificacoes, nove negativos — e isso e o resultado bom.**

## 5. Veredito

> **`apto-com-ressalva`.**
>
> **A admissao esta apta pelo criterio vigente:** o rito e o competente, a classe e determinada
> com fundamento citado, `G1` fecha por medicao, `0` bytes do candidato entram e o custo de
> reversao esta medido. **As quatro ressalvas nao invalidam a admissao** — nenhuma delas atinge
> a validade do ato — **e nenhuma se resolve com esta missao**: `S2`, `S3` e `S4` sao trabalho
> da primeira `Spec`, e `S1` depende de norma que segue adiada.
>
> **O que este parecer NAO afirma:** que o nXtrack e tecnicamente bom, que a hipotese central
> foi validada, que ha usuarios reais medidos ou que a custodia esta resolvida. **Nenhum
> controle de merito foi aplicado — porque `RECOGNIZE` nao avalia conteudo, e admitir o
> contrario seria exatamente o defeito que `ADR-0027 §12` manda vigiar.**

## 6. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Objeto avaliado | [ADR-0030](../../decisions/ADR-0030-admissao-do-nxtrack-como-primeiro-produto.md) · [RFC-0025](../../rfcs/RFC-0025-admissao-do-nxtrack-como-primeiro-produto.md) |
| Condicao do portao cumprida | **`G4`** de [ADR-0007 §5.3](../../decisions/ADR-0007-fronteira-greenfield-legado.md) |
| Portao completo | [PT-2026-014 §3](../relatorio-transicao-2026-08-01-portao-nxtrack.md) |
| Evidencia de `G1` *(nao norma)* | `_missao-1-13-4-4-2026-08-01/evidencia/ITEM-0-proveniencia-nxtrack.md` |
| Pacote soberano | [PS-2026-016](../pacote-soberano-2026-08-01-nxtrack.md) |
| Ressalvas abertas | `S1` · `S2` · `S3` · `S4` |

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-08-01 | DEP-QAR | Parecer inicial. **14 de 14** controles conformes, remedidos por metodo distinto do da producao; **seis** respostas com sinal observavel; **quatro** ressalvas com dono e gatilho; **nove** resultados negativos declarados. Veredito **`apto-com-ressalva`**. Cumpre `G4` do portao e `CV-07` de `FND-04`. |
