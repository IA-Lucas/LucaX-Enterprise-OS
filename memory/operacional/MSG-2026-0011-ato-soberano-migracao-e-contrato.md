---
id: MSG-2026-0011
titulo: Ato Soberano que assina o PS-2026-018 — grava o contrato fabrica-acervo e migra os setores CONVOCADOS da F34
tipo: relatorio
versao: 1.0.0
status: ativo
camada_memoria: operacional
autor: SOBERANO
proprietario: DEP-GOV
aprovador: SOBERANO
criado_em: 2026-08-12
atualizado_em: 2026-08-12
revisao_prevista: null
decisoes_relacionadas: [ADR-0007, ADR-0011, ADR-0038]
substitui: []
substituido_por: null
canal: DIRETIVA
emissor: SOBERANO
destinatario: DEP-GOV
ttl: 1 ciclo — expira sem perda; o ato fica ancorado por hash e os efeitos duraveis sao promovidos na aplicacao
resumo: Registra, como fonte canonica unica, o DECIMO PRIMEIRO ato soberano — a assinatura do PS-2026-018 1.1.0, dada em 2026-08-12 com as palavras "assino o PS-2026-018", ancorada no H-A do pacote 572d9431 e no commit 53483e4 — que promulga os oito itens do §3 da minuta - contrato fabrica-acervo, migracao dos CONVOCADOS por custodia declarada, excecao de segregacao do lote, aresta CAP-estrategia, emenda PRO-nxtrack, correcoes do F44, remedicao dos perfis e plano de reversao. NADA foi aplicado por este registro - a aplicacao e da missao ministerial sob o fencing_token 44, com as paradas do §5 vigentes.
perfil_contexto: missao
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# MSG-2026-0011 — Ato Soberano de 2026-08-12 *(decimo primeiro ato)*

## Proposito

Gravar, como **fonte canonica unica**, o ato soberano que assina o
[`PS-2026-018`](../../governance/pacote-soberano-2026-08-12-migracao-e-contrato.md) —
o pacote unico da **migracao dos setores `CONVOCADO` da F34** e da **gravacao do contrato
fabrica↔acervo** com forca normativa.

> ## Este registro NAO APLICA o ato. Registra que ele foi emitido.
>
> No instante desta escrita, **`0` bytes** foram alterados em Carta, Capability, Fundacional
> ou `products/` por causa do ato. A aplicacao e da **missao ministerial sob o
> `fencing_token` 44**, com o §3 do pacote como letra e o **§5 como freio** — inclusive a
> devolucao nominal de setor **sem custodia declarada**.

## §1 — O ato, nas palavras do Soberano

| Campo | Valor |
|---|---|
| **Palavras da assinatura** | **"assino o PS-2026-018"** |
| Data | **2026-08-12** |
| Objeto | [`PS-2026-018`](../../governance/pacote-soberano-2026-08-12-migracao-e-contrato.md) **versao 1.1.0** — a reemissao da revisao *(a 1.0.0 fora inscrita no mesmo dia; a revisao acrescentou o carimbo `MIGRADO` na origem e nada removeu)* |
| **Ancora `H-A` do pacote assinado** | `572d94315832c98b187f4e5458053c0fc1b74753e5902813b69377c2cb2e5b0b` *(sha256 do arquivo, 162 linhas, medido no instante do registro)* |
| Ancora de commit | `53483e4` *(o commit que gravou a 1.1.0; identico ao conteudo assinado — arvore limpa no registro)* |
| Sequencia | **DECIMO PRIMEIRO ato** — contador exercido, nao lido: `MSG-2026-0010` ✅ existe *(vivo e copia datada)* · `MSG-2026-0011` ✅ NAO existia |

## §2 — O que o ato promulga *(remissao, nunca reproducao — `PJ-01`)*

Os **oito itens do §3 do pacote**, com a letra **la** e so la: **I** contrato gravado por
`RFC → ADR` *(copia literal de `F35 §2.2`)* · **II** migracao dos `CONVOCADO` por **custodia
declarada**, 4 partes, com carimbo `MIGRADO` na origem e devolucao nominal do que nao tiver
custodia · **III** excecao de segregacao **so deste lote** · **IV** aresta `CAP-estrategia` ·
**V** emenda `PRO-nxtrack` · **VI** correcoes do laudo `F44` nos gates dele · **VII** os nove
perfis remedidos · **VIII** reversao `RB-01`.

## §3 — Condicoes vigentes na aplicacao

As **paradas do §5 do pacote**: custodia nao declarada → **lista nominal volta ao Soberano**;
`H-P` que nao reproduz → para; baseline que nao reproduz antes da primeira escrita → para;
secret-scan com achado no candidato → para. **A missao de aplicacao nao decide merito novo:**
o que nao couber na letra volta, nunca se estica.
