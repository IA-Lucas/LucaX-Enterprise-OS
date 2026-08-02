---
id: PT-2026-013
titulo: Relatorio de transicao da Missao 1.13.4.2 — pacote soberano das tres emendas de instrumento
tipo: relatorio
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-07-31
atualizado_em: 2026-07-31
revisao_prevista: null
decisoes_relacionadas: [ADR-0005, ADR-0007, ADR-0012, ADR-0027, ADR-0028, ADR-0029]
substitui: []
substituido_por: null
resumo: Produz o pacote soberano das tres emendas de instrumento com rito completo, dependencia medida em zero e minuta de ato redigida e nao emitida.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# PT-2026-013 — Missao 1.13.4.2: as tres emendas de instrumento

> ### ✅ Decisao: **`READY-FOR-RATIFICATION`**
>
> **Nove objetos criados, tres unidades independentes, dependencia entre elas medida em `0`.**
> **Nada foi aplicado, ativado, ratificado ou emitido.** `Q1` e `RD-33` continuam bloqueantes e
> intactos; o pacote da 1.13.4 segue **suspenso e com `0` bytes alterados**.
>
> **`READY-FOR-RATIFICATION` significa aqui exatamente duas coisas: rito completo e minuta
> redigida.** Nada alem disso — a definicao e a mesma que `PT-2026-012 §11.2` fixou, e ela
> continua valendo.

## Proposito

Separar as tres emendas do `BLOCKED` da Missao 1.13.4.1 — que foi por **proveniencia do
medAlly**, defeito alheio a elas — e leva-las ao rito completo.

## Escopo

| Item | Definicao |
|---|---|
| Inclui | **3** `RFC` · **3** `ADR` · **3** `FIT` · **1** pacote soberano com **minuta de ato nao emitida** · o **mapa de dependencias medido** · a **regra de reclassificacao** do `REWRITE` · a propagacao `CV-04` nos indices |
| **Nao** inclui | Aplicacao · ativacao · ratificacao · emissao de ato · julgamento de candidato · admissao de Produto · criacao de `Spec` · alteracao do pacote da 1.13.4 · fechamento de `RD-33` · correcao de achado fora das tres emendas |
| Natureza | **Rito.** Nenhum tipo, entidade, camada ou diretorio novo |

## 0. Pre-condicoes — cumpridas antes da primeira escrita

| # | Pre-condicao | Estado |
|---|---|---|
| `PC-1` | **`BL-2026-07-31-02` reproduzida pelo comando corrigido de `RD-53`** | ✅ **195 · 57.769 · `74b62fe9fd750c736778b3c420d969661989bac7ae4ac78c8f3cd711e0858335`** — bate nos tres valores com o catalogo `§10.11` |
| `PC-2` | **Copia datada fora do acervo** | ✅ `_backups/LucaX-Enterprise-OS_2026-07-31_pre-missao-1-13-4-2/` — **573** arquivos, **com a baseline reconferida na copia** |
| `PC-3` | **Ponto de rollback por `H-A`, antes de tocar qualquer objeto** | ✅ **195** artefatos; `sha256` do proprio ponto `96dfe8ff6b5150721090fe713532b0931ec9baf3ef9b1b3de58769817924caab` |
| `PC-4` | **Lease e fencing antes da primeira escrita** | ✅ `fencing_token: 4`, fenceado a `BL-2026-07-31-02` |
| `PC-5` | **Escritor unico por JANELA DE TEMPO** | ✅ Ultima escrita anterior: **10:59:01,96**. **`0` escritas de qualquer extensao** entre `11:00:00` e a aquisicao do lease, **16:03** — janela de **5h04m** |
| `PC-6` | **As tres minutas localizadas e citadas por caminho e hash** | ✅ §1 |
| `PC-7` | **Instrumento de hash calibrado ANTES do uso** | ✅ **8 de 8** controles de `PS-2026-014 §3` reproduzem nos 64 digitos |

> **`PC-5` foi respondida como a determinacao pediu: por tempo, nunca por hash de arvore
> alheia.** Medir a arvore de outra sessao provaria o que ela contem, jamais que ela nao esta
> escrevendo.

### 0.1 O instrumento de hash foi ESTENDIDO, e a extensao esta declarada

`O4` de `FND-10 §5.2` e *`em-revisao` → `aprovado` → `ativo`*. O instrumento da 1.13.4.1 so
tratava *`em-revisao` → `ativo`*; este trata **tambem** *`aprovado` → `ativo`*, porque `LM-02`
poe o artefato `C3`/`Tipo 1` nao ratificado em **`aprovado`**.

**A extensao nao move nenhum controle publicado**, e os **8 de 8** o provam: nenhum objeto de
`PS-2026-014 §3` esta em `aprovado` **com** `ratificacao: pendente`.

## 1. As tres minutas — evidencia, nunca norma

| Minuta | Linhas | `sha256` |
|---|---|---|
| `MINUTA-A-classe-de-admissao-de-existencia-em-G3.md` | 89 | `76eb131918c63e34228ceceb07b4bf8604a76c1fb418f2695e3c6dc7544552d5` |
| `MINUTA-B-independencia-de-fornecedor.md` | 77 | `c1a04768b35cef31bf6309295644533527b50d671fb6696f8a43d61665a9ff88` |
| `MINUTA-C-superacao-de-ato-por-evidencia-posterior.md` | 84 | `b5cd82aeb06ebf5845f9b8a1aafc457df91d639e5df0c2da23319934d08e678a` |

Vivem em `_missao-1-13-4-1-2026-07-31/minutas/`, **fora do acervo**.

### 1.1 Tres afirmacoes das minutas NAO sobreviveram a conferencia

> **Missao `BLOCKED` nao confere autoridade ao que produziu.** O conteudo e materia-prima
> legitima, e materia-prima se confere contra a fonte antes de virar norma (`PJ-03`).

| # | A minuta dizia | A fonte diz | Consequencia |
|---|---|---|---|
| **1** | `G3` tem `ADOPT · ADAPT · REWRITE · **REJECT**` | **`RETIRE`** — `ADR-0007 §5.3` e `§5.4`. **`rejected` e valor de PROVENIENCIA de `§5.5`**, nao nome de classe | Corrigido em `RFC-0022 §1.1` e `ADR-0027 §5.2` |
| **2** | Reverter a emenda 1 custa *"1 linha de `ADR-0007`"* | **Duas secoes** — `§5.3` e `§5.4` —, e **nenhuma e editada**: `AL-02` e `LV-04` mandam **superar por instrumento novo** | Custo remedido em `ADR-0027 §10`; metodo pelo precedente de `ADR-0022`, que declara `supera:` sem preencher `superado_por` no superado |
| **3** | A emenda 2 supera **`ADR-0005`** *"quanto ao criterio de afericao"* | **`ADR-0005` nao contem criterio de afericao algum.** Ele proibe o **par reflexivo** da relacao `verifica` (`RM-06`). O criterio e **`AC-03` de `FND-10 §2.5`** | **A classe subiu de `C2` para `C3`** — `ADR-0028 §1.1` e `§11.1` |

> **A terceira e a que mais importa, e ela e um achado sobre o metodo, nao sobre a minuta.**
> Herdar o objeto superado teria produzido **rito insuficiente**: emendar `ADR` e `C2`;
> emendar **fundacional** e `C3` com ratificacao do Soberano. **A classe do rito nao se herda
> da fonte — determina-se contra `FND-04 §2`.** Achado **`RD-65`**.

## 2. Classe do rito — determinada, hipotese a hipotese

**As cinco hipoteses de `C3` de `FND-04 §2` foram percorridas uma a uma em cada emenda.**

| Emenda | `PI` | `LV` | Hierarquia | Direitos de decisao | A propria Fundacao | **Classe** |
|---|---|---|---|---|---|---|
| **`E1`** `G0` + `RECOGNIZE` | nao | nao | nao | nao | **nao — medido** | **`C2` · `Tipo 2`** |
| **`E2`** independencia por fornecedor | nao | nao | nao | nao | **SIM** | **`C3` · `Tipo 1`** |
| **`E3`** superacao de ato | nao | nao | nao | **SIM** | nao — medido | **`C3` · `Tipo 1`** |

| Emenda | A hipotese que **decidiu** | Como se sabe |
|---|---|---|
| `E1` | Nenhuma de `C3` incide; incide a de `C2` — *"muda escopo, **fronteira** … ou **padrao**"* | **`0`** ocorrencias das quatro classificacoes em `FND` algum — **varredura das tres arvores** |
| `E2` | **`FND-10 §2.2` e `§2.5` sao emendadas** | Campo novo no contrato universal + `AC-03` redefinida |
| `E3` | **`SA-4` cria o direito de INSTAURAR**, que nao existe em norma vigente | **`0`** ocorrencias de caminho de superacao de ato; **7 de 7** atos `ativo` |

**`Tipo`, determinado por custo medido, nunca por analogia:**

| Emenda | `Tipo` | O custo que decidiu |
|---|---|---|
| `E1` | **2** | 1 `ADR` + 1 entrada de catalogo + indices; **`0`** consumidores — `0` admissoes `RECOGNIZE` |
| `E2` | **1** | **Segundo ato soberano** *(emendar fundacional)* + alcance sobre artefatos ja criados + **residuo nao editavel em `BL-02`** |
| `E3` | **1** | **Reverter superacao consumada e impossivel** — `RA-4` de `ADR-0029`, probabilidade **certa** |

> **`ADR-0012` e `C2`/`Tipo 2` e trata do MESMO objeto — o ato.** Herdar a classe dele para
> `E3` teria sido o erro exato que esta missao foi mandada evitar. `AL-01`: classifica-se pelo
> **efeito**.

## 3. Mapa de dependencias — medido, e o resultado e **zero**

| # | Medicao | Resultado |
|---|---|---|
| `D1` | Referencias cruzadas entre `ADR-0027`, `ADR-0028`, `ADR-0029` | **`0` de 6 pares** |
| `D2` | Normas alcancadas | **Disjuntas** — `ADR-0007` · `FND-10` · **nenhuma** |
| `D3` | Arquivos alterados no ato | `{}` · `{foundation/10-artifact-framework.md}` · `{}` — **todas as intersecoes vazias** |
| `D4` | `AV-3` de `E2` alcanca os objetos de `E1` e `E3`? | **Nao** — `0` ocorrencias; `AV-6` e prospectiva |

**Consequencia: tres unidades atomicas, e `0` acoplamento.** O Soberano pode decidir uma, duas
ou as tres, em qualquer ordem. **Acoplar faria a falha de uma reverter as outras, e nao ha
dependencia que pague esse custo** — [PS-2026-015 §3](pacote-soberano-2026-07-31-emendas-de-instrumento.md).

## 4. Autoverificacao — os dois criterios, **medidos nesta missao**

| Criterio | Definicao | Autoverificacoes | Base |
|---|---|---|---|
| **`C-1`** — divergencia de campo *(vigente, `AC-03`)* | `autor` == `revisor` | **`0`** | **138** artefatos declaram os dois |
| **`C-2`** — independencia de fornecedor *(proposto, `AV-1`)* | papeis do **mesmo executor** | **`131`** | os mesmos **138** |
| **Diferenca** | | **`131`** | |

**Os `7` que sobrevivem a `C-2` sao os sete atos do Soberano**, `autor: SOBERANO`.

> **Numero remedido, nao herdado.** A 1.13.4.1 mediu **`0` / `130` sobre `137`**, com **194**
> artefatos. O acervo cresceu em **1** artefato que declara os dois campos — `PT-2026-012` —, e
> por isso a base foi a **138** e a diferenca a **131**. **Copiar o numero alheio seria publicar
> como medido o que foi lido** — a familia de `MEM-APR-0002`.

## 5. Revisao independente pelo criterio VIGENTE

**As tres verificacoes foram aferidas por `AC-03` — `revisor` ≠ `autor` —, e as tres o
satisfazem:** os `FIT` tem autor **DEP-QAR** e revisor **DEP-GOV**; os objetos avaliados tem
autor **DEP-GOV** e revisor **DEP-QAR**.

> **`ADR-0028` NAO esta em vigor e NAO se aplica a si mesma nem aos pareceres desta missao.**
> Uma norma que se aplicasse a propria verificacao antes de vigorar seria **retroatividade** —
> `FND-01 §9`, `EV-03`.
>
> **E o numero que ela produziria sobre estes pareceres esta escrito:** sob `C-2`, os tres
> seriam **`fornecedor_verificacao: interno`** — **uma das `131`**. `AV-4` declara que isso
> **nao e defeito e nao bloqueia**: e **conferencia**, nao **atestado**. **Os tres pareceres
> desta missao sao conferencias internas, e o dizem.**

## 6. Provas de fechamento

| # | Prova | Resultado |
|---|---|---|
| `F1` | Baseline anterior reproduzida **antes** da primeira escrita | ✅ **195 · 57.769 · `74b62fe9…8335`**, reconferida na copia datada |
| `F2` | Instrumento de hash calibrado antes do uso | ✅ **8 de 8** controles de `PS-2026-014 §3` |
| `F3` | **`P1` — `H-N` invariante sob `O4`** | ✅ **3 de 3** |
| `F4` | **`P2` — `IR-09` reconstroi `H-A`** | ✅ **3 de 3** |
| `F5` | **`P3` — `O4` alcanca exatamente os campos declarados** | ✅ `ADR-0027` **`−5` bytes / 1 campo**; `ADR-0028` e `ADR-0029` **`−3` bytes / 2 campos**. **`atualizado_em` nao tocado em nenhum: `0` ocorrencias no diff** |
| `F6` | `H-P` publicado **so** onde ha `O4` | ✅ **3 de 9** — `RFC` e `FIT` **nao transicionam**, e publicar `H-P` deles seria publicar transicao que nunca ocorre |
| `F7` | Dependencia entre as emendas | ✅ **`0`**, por **quatro** medicoes independentes |
| `F8` | Autoverificacao pelos dois criterios | ✅ **`0`** e **`131`**, diferenca **`131`**, base **138** |
| `F9` | Contador **exercido, nao lido** (`V1` de `MEM-APR-0006`) | ✅ **9 de 9** testados contra a copia datada: **nenhum existia**. `ADR` **26 → 29** · `RFC` **21 → 24** · `FIT` **19 → 22** |
| `F10` | **Historicos, `ADR`, `MSG`, `FIT`, `PT` e baselines editados** | ✅ **`0`** — §7 |
| `F11` | **Pacote da 1.13.4 alterado** | ✅ **`0` bytes** — `PS-2026-014`, `PT-2026-011`, `FIT-2026-019`, `ADR-0026`, `RFC-0021` |
| `F12` | **`ADR-0005`, `ADR-0007` e `ADR-0012` alterados** | ✅ **`0` bytes** nos tres — **superados por instrumento novo** |
| `F13` | **Fundacionais alterados** | ✅ **`0`** — o diff de `FND-10` esta **escrito e nao aplicado** |
| `F14` | Ato emitido · candidato julgado · Produto admitido · `Spec` criada | ✅ **`0`** em cada |
| `F15` | Links relativos resolvidos | §8 |
| `F16` | Nova baseline reproduzivel | §8 |
| `F17` | Lease vivo do inicio ao fim | ✅ `fencing_token: 4` |

## 7. O conjunto de mudanca — enumerado, nao afirmado

**Criados — 11:**

| # | Artefato | Natureza |
|---|---|---|
| 1–3 | `RFC-0022` · `RFC-0023` · `RFC-0024` | Propostas |
| 4–6 | `ADR-0027` · `ADR-0028` · `ADR-0029` | Decisoes **nao vigentes** |
| 7–9 | `FIT-2026-020` · `FIT-2026-021` · `FIT-2026-022` | Pareceres |
| 10 | `PS-2026-015` | Pacote soberano com **minuta nao emitida** |
| 11 | **Este relatorio** | O registro que `CV-04` exige da propria mudanca |

**Alterados — 6, todos projecao `M3` ou indice:**

`rfcs/README.md` · `decisions/README.md` · `governance/fitness/README.md` ·
`governance/artifact-registry.md` · `governance/README.md` · `README.md`.

**Removidos: `0`.** **Nenhuma fonte normativa foi alterada** — a unica que as emendas
alcancariam, `FND-10`, tem **`0` bytes**.

## 8. Fechamento

| Item | Valor |
|---|---|
| **Nova baseline** | **`BL-2026-07-31-03`** — **206 · 60.151 · `17a5ea411b4fb0871ff632e330cf18c5d42755971a4206fb9b4feba97356986d`**, catalogo `§10.12`. **Remedida apos a ultima escrita e reproduz** |
| Links | **3.095 verificados · `0` quebrados** |

## 9. O que esta missao NAO fez

| # | Nao feito | Por que |
|---|---|---|
| 1 | **Nenhum ato emitido, nada ratificado, nada aplicado ou ativado** | Limite expresso. As tres emendas estao **`em-revisao`** |
| 2 | **Nenhum candidato julgado, Produto admitido ou `Spec` criada** | Limite expresso. **`RD-33` bloqueante** e **`Q1` precede o ato** |
| 3 | **Pacote da 1.13.4 nao alterado** | Limite expresso — **`0` bytes**, suspenso e nao descartado |
| 4 | **`ADR-0005`, `ADR-0007`, `ADR-0012` e `FND-10` nao editados** | `AL-02`, `LV-04`: **supera-se por instrumento novo** |
| 5 | **`RD-62` nao corrigido, e agravado** | **Fora da lista.** `ADR-0028` leva a tabela de `FND-10 §2.2` a **sete** linhas sob titulo que diz *"cinco"*. **Declarado, nunca corrigido em silencio** |
| 6 | **`RD-63`, `RD-60`, `RD-61`, `RD-64` mantidos abertos** | Fora da lista |
| 7 | **`FIT-2026-020` nao recomenda aprovar `E1` antes de `Q2`** | Aprovar `C2` por DEP-EXE **antes** da resposta do Soberano seria decidir por ele materia ja submetida |
| 8 | **Registro de `SA-6` nao criado; cascata de templates de `AV-3` nao executada** | Sao **efeito do ato**, nao da redacao |

## 10. Achado novo

| # | Achado | Severidade | Estado |
|---|---|---|---|
| **`RD-65`** | **A classe do rito nao se herda da fonte que descreveu o defeito.** A minuta B declarava superar `ADR-0005` *"quanto ao criterio de afericao"*, e **`ADR-0005` nao contem criterio algum** — ele mora em `AC-03` de `FND-10 §2.5`. Herdar o objeto superado teria produzido **`C2` onde a norma exige `C3`**, isto e, **aprovacao por DEP-EXE onde a Constituicao exige ratificacao do Soberano**. **O erro nao estava na classe declarada — estava no OBJETO, e a classe era consequencia** | **Media** | ✅ **CORRIGIDO nesta missao**, nos tres instrumentos. Registrado como achado porque **o metodo e reutilizavel**: antes de aceitar a classe de uma fonte, **localizar a norma superada no documento que a contem** — nunca no que a cita. Familia de `MEM-APR-0002` *(afirmar o nao medido)*, aplicada a **norma** em vez de a **numero** |

## 11. Decisao

**`READY-FOR-RATIFICATION`.**

| # | Criterio de validacao | Estado |
|---|---|---|
| 1 | Tres emendas com rito completo e **classe determinada, nao presumida** | ✅ `RFC` → `ADR` → `FIT` nas tres; cinco hipoteses de `C3` percorridas em cada |
| 2 | **Dependencias medidas**, com acoplamento atomico **so onde provado** | ✅ **`0`** por quatro medicoes → **`0`** acoplamento, **3** unidades |
| 3 | Rastreabilidade defeito → minuta → `ADR` → minuta de ato | ✅ `PS-2026-015 §7` |
| 4 | **Autoverificacao pelos dois criterios, com a diferenca em numero** | ✅ **`0`** e **`131`**, diferenca **`131`** |
| 5 | Zero link quebrado | ✅ §8 |
| 6 | Nova baseline reproduzivel | ✅ `BL-2026-07-31-03` |

> **O que este `READY-FOR-RATIFICATION` NAO significa.** **Minuta redigida nao e norma.**
> Enquanto nao houver ato: `G3` **segue sem `RECOGNIZE`**; a independencia **segue aferida por
> campo**, e a linha *Autoverificacao* segue podendo publicar `0` onde a medicao por fornecedor
> da **`131`**; e **ato emitido segue sem caminho de superacao**. **Os tres instrumentos
> continuam defeituosos, e o que mudou e que agora existe rito completo para consertar cada um
> — separadamente.**

## 12. Rastreabilidade

| Campo | Conteudo |
|---|---|
| Missao anterior | [PT-2026-012](relatorio-transicao-2026-07-31-manutencao-instrumentos.md) — **`BLOCKED` por proveniencia do medAlly**, defeito alheio a estas emendas |
| Pacote submetido | [PS-2026-015](pacote-soberano-2026-07-31-emendas-de-instrumento.md) |
| Achados que as emendas fecham **na vigencia** | `RD-54` · `RD-55` *(`E1`)* |
| Achado novo | **`RD-65`** |
| Achado agravado e declarado | **`RD-62`** |
| Baseline de abertura | `BL-2026-07-31-02` — **reproduzida** |
| Baseline de fechamento | **`BL-2026-07-31-03`** |
| Instrumentos | `_missao-1-13-4-2-2026-07-31/ferramentas/` — `baseline.sh` · `hashes.sh` *(estendido)* · `manifesto.sh` · `autoverificacao.sh` *(novo)* |

## Historico de versoes

| Versao | Data | Autor | Mudanca |
|---|---|---|---|
| 1.0.0 | 2026-07-31 | DEP-GOV | Relatorio da **Missao 1.13.4.2**. **Nove objetos** em **tres unidades independentes**, com dependencia **medida em `0`** por quatro criterios. Classes **determinadas percorrendo as cinco hipoteses de `C3`**: `E1` **`C2`/`Tipo 2`**, `E2` e `E3` **`C3`/`Tipo 1`**. **Tres afirmacoes das minutas nao sobreviveram a conferencia**, e a terceira **elevou o rito de `E2` de `C2` para `C3`** — achado **`RD-65`**. Autoverificacao **remedida**: `0` e `131`, base `138`. Provas `P1`, `P2` e `P3` **3 de 3**. **`0` bytes** em `ADR-0005`, `ADR-0007`, `ADR-0012`, `FND-10` e no pacote da 1.13.4. Decisao **`READY-FOR-RATIFICATION`**. |
