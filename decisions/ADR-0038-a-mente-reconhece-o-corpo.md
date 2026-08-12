---
id: ADR-0038-a-mente-reconhece-o-corpo
titulo: A Mente reconhece o Corpo — as 4 camadas do lucaX Enterprise, a membrana entre norma e producao, e a Policy Engine como projecao de FND-04
tipo: adr
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-EXE
criado_em: 2026-08-12
atualizado_em: 2026-08-12
revisao_prevista: 2027-02-12
decisoes_relacionadas: [ADR-0007, ADR-0011]
substitui: []
substituido_por: null
classe_mudanca: C2
tipo_decisao: 2
supera: []
superado_por: null
resumo: Reconhece o repositorio lucax-enterprise como o CORPO — runtime executavel da plataforma, fora do acervo e fora do fence —, institui as 4 camadas (Mente, Oficina, Corpo, Legado) com caminhos reais, e declara a membrana - producao nunca escreve na Mente, mudanca de norma sobe por RFC->ADR, evidencia volta como proposta, e a Policy Engine do Corpo e projecao de FND-04, com a fonte prevalecendo em divergencia.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# ADR-0038: A Mente reconhece o Corpo

## Contexto

Em 2026-08-11, por mandato direto do Fundador, nasceu **`lucax-enterprise`** — o runtime
executavel da plataforma: FastAPI + LangGraph, pilha Docker (PostgreSQL com RLS multi-tenant,
Redis, LiteLLM, n8n), no de auditoria pre-voo, Policy Engine e bilhetagem de token por
`tenant_id`. Em 2026-08-12 a pilha foi **provada do zero** (RLS `EXIT=0` como `app_rt`,
fluxo `awaiting_approval → approve` com trilha, 25 testes verdes).

**O fato existe; a norma nao o conhecia.** A fronteira entre este acervo e o runtime estava
escrita apenas no `CLAUDE.md`/`MENTE.md` **do proprio Corpo** — texto que a Mente nao le nem
versiona. Este acervo ja mediu o custo disso: a regra de lease mais estreita que o fence foi
**exercida antes de ser corrigida** (quarto despacho de 2026-08-02), e a familia `RD-101` e
feita de afirmacoes validas de um lado da fronteira e falsas do outro.

## Decisao

### 1. As quatro camadas, com caminhos reais

| Camada | Papel | Caminho |
|---|---|---|
| 🟣 **Mente** | Autoridade normativa: ADRs, Fundacionais, catalogo, baseline, lease | `E:\LucasIA\Projetos\LucaX Enterprise OS` *(este acervo)* |
| 🟠 **Oficina** | P&D e saneamento de insumos; skills nascem la e so entram sas | `E:\LucasIA\Projetos\LucaX-Enterprise-Research` |
| 🟢 **Corpo** | Runtime executavel; producao, codigo, segredos, infraestrutura | `E:\LucasIA\Projetos\lucax-enterprise` |
| ⚪ **Legado** | Repositorio antigo sob firewall de migracao ate o cutover | `E:\LucasIA\Projetos\lucaX` |

### 2. O Corpo vive FORA do acervo, e isso e desenho

O codigo do Corpo **nunca** entra no acervo nem no fence: a baseline (`IR-BL/6`) mede `.md`
por lista fechada positiva, e codigo executavel dentro do recurso medido seria massa invisivel
ao medidor — a receita de `RD-53`. O Corpo tem repositorio git proprio, testes proprios e
trava `.lock` propria; o lease desta Mente **nao o alcanca**, e o dele nao alcanca a Mente.

### 3. A membrana — regras de atravessamento

| # | Regra | Sentido |
|---|---|---|
| M1 | **Producao nunca escreve na Mente.** Nenhum processo do Corpo grava byte neste acervo | Corpo → Mente: **fechado** |
| M2 | **Mudanca de norma sobe por `RFC → ADR`**, sob lease e rito da classe — nunca por escrita direta | Corpo → Mente: **so por rito** |
| M3 | **Evidencia volta como proposta:** runs, custo medido, licoes — materia-prima de RFC, jamais autoescrita | Corpo → Mente: **dado, nao norma** |
| M4 | **A Mente governa por specs, politicas e contratos** — o Corpo os consome como leitura | Mente → Corpo: **aberto, somente leitura** |
| M5 | **Segredo nao cruza em sentido algum.** Credencial vive no Corpo (`.env`, cofre); o acervo cita tipo e local, nunca valor | ambos: **fechado** |

### 4. A Policy Engine e PROJECAO de FND-04

O modulo `app/policies.py` do Corpo materializa a matriz de autoridade de
[`FND-04`](../foundation/04-governanca.md): classes `C0–C3`, aprovacao humana para
`C2`/`C3`, acao irreversivel sobe de classe (`GV-03`). **Em divergencia, prevalece a fonte**
(`PJ-03`): corrigir a projecao e mudanca no Corpo; corrigir a fonte e `RFC → ADR` aqui.

### 5. O que esta decisao NAO faz

Nao migra setores *(Onda 5, com as decisoes ja tomadas — um ato, excecao de segregacao
declarada nele)* · nao promove nada a `FND` · nao toca o Legado *(firewall ate a Onda 7)* ·
nao cria Produto nem Spec · nao poe **um byte** de codigo, segredo ou infraestrutura no acervo.

## Tradeoff declarado

**O acervo passa a apontar para tres repositorios cuja integridade ele nao mede.** A baseline
prova a Mente; Oficina, Corpo e Legado tem git proprio e provas proprias. O ponteiro pode
envelhecer — mudou caminho, mudou o fato — e o precedente `A-297` (caminho morto em 29
ponteiros) mostra que envelhece. **Aceita-se o custo** porque a alternativa — medir producao
com o medidor do acervo — destruiria a propriedade que faz a baseline valer. Mitigacao: os
caminhos vivem na tabela do §1, **um lugar so**, e corrigi-los e emenda deste ADR por sucessor.

## Fundamento do rito

`FND-04` linha `C2`: `RFC → ADR`, aprova DEP-EXE com parecer DEP-GOV; `CV-07`: FIT
obrigatorio. **Rito inteiro por escolha expressa do Fundador em 2026-08-12**, entre tres
opcoes apresentadas com a regra citada — a dispensa de RFC estava disponivel e **nao foi
usada**. Cadeia: [`RFC-0033`](../rfcs/RFC-0033-a-mente-reconhece-o-corpo.md) → este ADR →
[`FIT-2026-031`](../governance/fitness/FIT-2026-031-a-mente-reconhece-o-corpo.md).
