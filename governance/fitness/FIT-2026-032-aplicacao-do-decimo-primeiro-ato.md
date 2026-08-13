---
id: FIT-2026-032-aplicacao-do-decimo-primeiro-ato
titulo: Verificacao de aptidao — a aplicacao do decimo primeiro ato (PS-2026-018, MSG-2026-0011)
tipo: fitness-check
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: DEP-QAR
proprietario: DEP-QAR
aprovador: DEP-EXE
criado_em: 2026-08-12
atualizado_em: 2026-08-12
revisao_prevista: null
decisoes_relacionadas: [ADR-0038, ADR-0039]
substitui: []
substituido_por: null
veredito: apto-com-ressalva
---

# FIT-2026-032 — A aplicacao do decimo primeiro ato

**Objeto avaliado:** [`MSG-2026-0011`](../../memory/operacional/MSG-2026-0011-ato-soberano-migracao-e-contrato.md),
[`RFC-0034`](../../rfcs/RFC-0034-contrato-fabrica-acervo-e-migracao.md),
[`ADR-0039`](../../decisions/ADR-0039-contrato-fabrica-acervo.md) e a aplicacao dos itens I–VIII
do [`PS-2026-018`](../pacote-soberano-2026-08-12-migracao-e-contrato.md).
**Portao:** `QG-6`, obrigatorio (`CV-07`, classe `C3`).

> `FT-02`/`LV-03`: papel avaliador `DEP-QAR`; os objetos tem autor `DEP-GOV`/`SOBERANO` —
> separacao por papel conforme. `FT-10`: parecer, nao decisao.

## Veredito

**`apto-com-ressalva`.** Tres ressalvas, nenhuma bloqueia.

## 1. Conformidade — com sinal observavel

| # | Criterio | Sinal medido | Veredito |
|---|---|---|---|
| `F1` | **Ato ancorado por conteudo** | `H-A` do pacote assinado `572d9431…` + commit `53483e4`; palavras da assinatura transcritas | ✅ |
| `F2` | **`H-P` do insumo conferido ANTES da admissao** | pacote da fabrica: **`11/11`** sha256 reproduzem do manifesto | ✅ |
| `F3` | **Baseline reproduzida antes da 1ª escrita** | `260 · 75.343 · 4ed13e99… · 7d3b7d3f…`, `EXIT=0`, zero deriva contra o token 43 | ✅ |
| `F4` | ⭐ **A parada `§5(a)` foi EXERCIDA, nao so escrita** | `gente` e `coo`: documento de origem (`F18`) cita `0` `CAP-`/`DEP-`; o par existia so na convocacao — **devolvidos ao Soberano em lista nominal**, sem esticar | ✅ |
| `F5` | **Mapa por custodia DECLARADA, resolucao MECANICA** | destinos `B3/B4·B10·B8` resolvidos pela anotacao de blocos do proprio `TPL-carta` *(§4→NAO_FAZ, §5→POLITICAS, §8→PADRAO, §11→QUALIDADE)* — nunca por juizo; a estranheza semantica de `PADRAO→§8` **declarada** em `PT-2026-026` | ✅ |
| `F6` | **Vetos respeitados** | `0` bytes de CARGOS/FERRAMENTAS; `0` bytes em Fundacionais; `FND-02 §10` intacta com leitura compativel gravada em `ADR-0039` | ✅ |
| `F7` | **Item VII integral: `§13.2` remedido nas NOVE** | 5 com conteudo novo remedidas; **4 divergencias latentes achadas e corrigidas pelo gate de `RD-49`** *(grw `443→444` · tls `424→425` · prd `445→446` · exe ja divergia antes do conteudo)*; `gov` confere | ✅ |
| `F8` | **Contadores exercidos e movidos na mesma mudanca** | `MSG 0011` · `ADR 0039` · `RFC 0034` · `FIT 032` — todos por `V1` contra copia datada; indices e catalogo na mesma emissao (`SF-32`, `CC-03`) | ✅ |
| `F9` | **Correcao V2 no gate certo** | carimbo `LV-04` no `FIT-2026-002` *(nota falsa por omissao)* + reavaliacao de `ADR-0005` por `DEP-GOV` em `PT-2026-026` — `DEP-QAR` impedido, como o laudo mandou | ✅ |

## 2. ⚠️ Ressalvas

- **`R1` — as Cartas crescem ~30–40%** *(kms `464→638`, eng `402→575`, exe `506→688`…)*: o custo
  de contexto sobe, e `MK-7` da propria Carta KMS ja nomeia o risco do crescimento monotonico.
  Perfis remedidos mitigam a mentira, nao o peso. **Dono: DEP-KMS medir; DEP-EXE decidir
  consolidacao. Gatilho: proxima revisao estrutural.**
- **`R2` — dois setores voltaram** *(`gente`, `coo`)*: o freio funcionando, mas a fila do
  Soberano cresce em `+2` decisoes *(criar/apontar custodia ou aceitar o par da convocacao)*.
- **`R3` — `PADRAO→§8` e resolucao mecanica com encaixe semantico fraco** *(padrao de trabalho
  dentro de "Quando escalo")*: seguiu-se a letra do mapa da M-01 resolvida pelo `TPL`; se a
  revisao estrutural achar sede melhor, muda-se **por sucessor**, nunca em silencio.
