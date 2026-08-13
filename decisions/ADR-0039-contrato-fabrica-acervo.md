---
id: ADR-0039-contrato-fabrica-acervo
titulo: O contrato fabrica-acervo vira norma — as cinco linhas de F35 §2.2 em copia literal, com o exercicio da F34 como portao de migracao
tipo: adr
versao: 1.0.0
status: ativo
camada_memoria: estrategica
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-08-12
atualizado_em: 2026-08-12
revisao_prevista: 2027-02-12
decisoes_relacionadas: [ADR-0007, ADR-0011, ADR-0038]
substitui: []
substituido_por: null
classe_mudanca: C3
tipo_decisao: 1
supera: []
superado_por: null
resumo: Grava como norma do acervo, por ratificacao do decimo primeiro ato (MSG-2026-0011), o contrato fabrica-acervo de 2026-08-08 - as cinco linhas de F35 §2.2 em copia literal, sem reacentuar - com o contexto fora do bloco - o "dezenove" da linha 5 superado pela decisao 2 do Fundador (vinte), e a leitura compativel da linha 3 - executor e o Departamento que ampara, nunca agente novo, preservando FND-02 §10 intacta. O portao de migracao e o exercicio da F34, ja exercido em 20/20.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: ratificada
---

# ADR-0039: O contrato fabrica↔acervo

## Contexto

A fabrica (Oficina) escreve setores **barato, sem rito**; o acervo (Mente) e a **autoridade**.
A fronteira entre os dois foi decidida pelo Fundador em **2026-08-08** *(F35/F36 da Oficina)*
e viveu, desde entao, **fora do acervo** — `CLAUDE.md §10.2` e `MAPA §5.2` da fabrica. Fronteira
escrita so de um lado e a folga que este acervo ja pagou *(a regra de lease exercida em
2026-08-02; a familia `RD-101`)*. O **decimo primeiro ato**
([`MSG-2026-0011`](../memory/operacional/MSG-2026-0011-ato-soberano-migracao-e-contrato.md))
assinou o [`PS-2026-018`](../governance/pacote-soberano-2026-08-12-migracao-e-contrato.md), cujo
item **I** manda gravar o contrato aqui, por este `ADR`.

## Decisao — o TEXTO, copia literal de `F35 §2.2`

**Regra da fonte (`F35 §2.1`): nao reacentuar, nao reescrever, nao renumerar.** Divergencia de
caractere seria parafrase:

```
CONTRATO ENTRE FABRICA E ACERVO
Decisao do Fundador, 2026-08-08. Texto identico nos dois lados.

1. A fabrica escreve o setor barato, sem ato, sem rito, sem baseline.
2. O setor e EXERCIDO antes de migrar. Setor nunca acionado nao tem o que
   migrar — migraria a descricao de um papel que ninguem exerceu.
3. O Enterprise recebe o setor como executor do Departamento que ja o ampara,
   quando ele passar no exercicio.
4. Enquanto nao migra, o setor vive na fabrica e a autoridade continua no
   acervo. A fabrica obedece a norma sem morar nela — a F21 citou
   CAP-engenharia §3 linha 77 literal, a F22 descobriu que a CAP-financeiro
   recusa duas das tres areas por escrito.
5. O gatilho de migracao e a F34, o exercicio de convocacao, que roda no fim
   da esteira com os dezenove escritos.
```

## O contexto FORA do bloco *(quem o colar dentro introduz a divergencia)*

1. **Linha 5, "dezenove":** numero vigente no dia da gravacao, **superado pela decisao `2` do
   Fundador do mesmo dia** *("a F34 roda com 20", F36 BLOCO 0)*. **O gatilho DISPAROU e foi
   exercido em 2026-08-12: F34 fechou `20/20`** — `10 CONVOCADO · 10 NAO CONVOCADO`.
2. **Linha 3, "executor" — leitura compativel, fixada por esta decisao:** o setor migrado entra
   como materia da **Carta do Departamento que o ampara** *(por custodia declarada da
   Capability)* — **nunca como agente novo**. `FND-02 §10` *("nesta fase nao existem agentes")*
   permanece **intacta e prevalece**; quando a fase mudar, mudara por emenda propria, nunca por
   arrasto deste contrato.
3. **Linha 2 e o veto:** setor `NAO CONVOCADO` **nao migra**. Os dez da F34 nesta condicao tem
   missao-teste definida a espera do **objeto externo** — a porta que so o Soberano abre.
4. **Sede dupla vetada:** o documento de origem, na fabrica, recebe carimbo **`MIGRADO`**
   apontando a Carta-sede *(item II do pacote, reemissao 1.1.0)*.

## Tradeoff declarado

O contrato cita instrumentos que vivem **fora** do acervo *(`F34`, `F35`, o `MAPA` da fabrica)* —
o mesmo tradeoff de ponteiro do `ADR-0038 §1`, aceito pelo mesmo fundamento: medir a fabrica com
o medidor do acervo destruiria a linha 1 do proprio contrato. Mitigacao identica: sede unica de
caminhos *(`ADR-0038 §1`)* e correcao por sucessor.

## Fundamento do rito

`C3` pelas tres incidencias de `FND-04 §2` medidas em `PS-2026-018 §3.I`. Cadeia completa:
[`RFC-0034`](../rfcs/RFC-0034-contrato-fabrica-acervo-e-migracao.md) → este `ADR` →
**ratificado por `MSG-2026-0011`** *(a assinatura do pacote e a ratificacao — o ato levou a
minuta com este conteudo)* → aptidao em
[`FIT-2026-032`](../governance/fitness/FIT-2026-032-aplicacao-do-decimo-primeiro-ato.md) →
revisao/transicao em [`PT-2026-026`](../governance/relatorio-transicao-2026-08-12-aplicacao-ps018.md).
