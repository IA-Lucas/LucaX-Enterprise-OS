---
id: IDX-incidents
titulo: Incidentes de Conformidade
tipo: relatorio
versao: 1.1.0
status: ativo
camada_memoria: operacional
autor: DEP-GOV
proprietario: DEP-GOV
aprovador: DEP-QAR
criado_em: 2026-07-28
atualizado_em: 2026-07-28
revisao_prevista: null
decisoes_relacionadas: [ADR-0001, ADR-0006]
substitui: []
substituido_por: null
resumo: Conta a sequencia INC e registra a situacao corrente de cada incidente de conformidade.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# Incidentes de Conformidade (`INC`)

## Proposito
Abrigar o registro de violacoes de norma detectadas, sua causa, seu efeito e a correcao
aplicada, conforme [FND-04 §10](../../foundation/04-governanca.md).

## Escopo
Violacao de Principio Imutavel ou Linha Vermelha, mudanca sem instrumento, acumulo indevido
de papeis, artefato ativo sem rastreabilidade, excecao vencida, credencial exposta, portao
pulado sem excecao formal.

## Responsaveis
| Papel | Responsavel |
|---|---|
| Abre e conduz | DEP-GOV |
| Verifica fechamento | DEP-QAR |
| Grava aprendizado | DEP-KMS |

---

## Incidentes registrados

| ID | Norma violada | Severidade | Aberto | Situacao | Fecha quem |
|---|---|---|---|---|---|
| [INC-2026-001](INC-2026-001-ratificacao-inferida.md) | PI-01 · PI-06 · GV-05 · CM-07 · **LV-05** | **Alta** | 2026-07-28 | ✅ **`fechado`** | DEP-QAR, 2026-07-28 |
| [INC-2026-002](INC-2026-002-ratificacao-declarada-em-fitness-check.md) | **LV-05** · GV-05 · CV-09 | Media | 2026-07-28 | ✅ **`fechado`** | **DEP-EXE**, 2026-07-28 |

Proximo numero: **INC-2026-003**

### INC-2026-001 em uma linha
Quatro ADRs C3/Tipo 1 declararam ratificacao do Soberano por inferencia a partir de instrucao
generica anterior. Efeito **isolado** sem editar registro historico (LV-04); causa corrigida
em FND-04 (CV-09, etapa [6] do ciclo, auditoria de eficacia de ratificacao); aprendizado em
[MEM-APR-0001](../../memory/aprendizado/MEM-APR-0001-ratificacao-por-precedente.md).
**Encerrado em 2026-07-28** pelo ato soberano registrado em
[§11](INC-2026-001-ratificacao-inferida.md), com verificacao independente de DEP-QAR em §12.

### INC-2026-002 em uma linha
FIT-2026-001 afirma ratificacao do Soberano que nao ocorreu, e FIT-2026-002 declara
`nao-exigida` uma ratificacao que FND-10 §10.3 exige. Efeito contido ao registro — os dois
vereditos permanecem integros. Nenhum dos dois arquivos foi editado (M1, PJ-04). Causa
herdada ja corrigida; causa propria — ambiguidade FND-10 §2.2 × §10.3 — registrada com dono e
gatilho, **sem ser corrigida por hipotese**.
**Encerrado em 2026-07-28** pelo ato soberano que **acolheu os dois `FIT` como pareceres, sem
eleva-los a norma** — fonte canonica
[MSG-2026-0002](../../memory/operacional/MSG-2026-0002-ato-soberano-cartas-comando-plataforma-e-contexto.md);
comprovacao independente em [§11.3](INC-2026-002-ratificacao-declarada-em-fitness-check.md).

> **Fechado nao significa resolvido, e o incidente diz qual e qual.** *Acolher* nao e
> *ratificar*: FIT-2026-001 **continua afirmando no proprio texto** uma ratificacao que nunca
> ocorreu — e **M1**, e nao se edita. E a **causa propria** (G1/G2) **nao foi eliminada**:
> migrou para [RFC-0009 Q2](../../rfcs/RFC-0009-integridade-e-alcance-do-ato-de-ratificacao.md),
> **aberta**, com dono DEP-GOV. O fechamento foi **condicionado** a essa migracao ter ocorrido.

> **Por que DEP-EXE fecha o INC-2026-002, e nao DEP-QAR.** DEP-QAR **produziu** os dois
> artefatos afetados. Verificar o proprio produto e vedado (PI-05, ADR-0005). Desvio da linha
> "Verifica fechamento: DEP-QAR" da tabela acima, declarado no proprio incidente.

## Rito
```
1. PARAR  2. REGISTRAR  3. CONTER  4. ANALISAR CAUSA
5. CORRIGIR (efeito E causa)  6. APRENDER (APR)  7. FECHAR (DEP-QAR)
```

> **Incidente nao e punicao — e informacao.** Omitir incidente observado e, em si,
> violacao (LV-11). Fechado sem correcao de causa, nao esta fechado.

Template: [`TPL-incidente`](../../foundation/templates/TPL-incidente.md)
