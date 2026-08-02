# LucaX Enterprise OS — instrucoes permanentes de trabalho

> Este arquivo **nao e artefato do acervo**: nao tem `id`, nao tem versao de
> sequencia, nao entra no catalogo e nao carrega autoridade normativa. E
> instrucao operacional de quem trabalha no repositorio.

---

## ROADMAP — `governance/roadmap-canonico.md`

- Ao **FINALIZAR** qualquer Goal, missao ou sequencia, conferir o roadmap e
  assinalar o que foi concluido, **na MESMA sessao que fechou**. Nunca deixar
  para depois, nunca abrir missao para isso.
- Conferir tambem se algum item marcado ficou desatualizado pelo que a missao
  produziu, e corrigir.
- **Estados:** `[ ]` pendente · `[x]` feito · `[~]` em curso · `[!]` espera
  decisao do Fundador.
- **Registro de acompanhamento: autoridade nenhuma, nao normativo.** Atualizar
  **NAO** exige ADR, hash, baseline nem ato.
- Divergencia que afete a sequencia entra na **secao propria do roadmap**, sem
  gerar missao.
- **Fechar missao sem conferir o roadmap e entrega incompleta.**

---

## Nota de medicao — leia antes de rodar a baseline

`baseline.sh` mede por **lista fechada positiva** e **para com erro** diante de
entrada nao declarada na raiz (portao de raiz, achado `RD-53`). **Este arquivo
esta na raiz e NAO esta declarado** — nem como acervo, nem como nao-acervo.
Enquanto assim for, o instrumento **recusa medir**, e a recusa e o portao
funcionando, nao falha.

Declarar `CLAUDE.md` na lista — e de que lado — e decisao do Fundador,
registrada como achado **`RD-81`** em
[`governance/artifact-registry.md §7`](governance/artifact-registry.md).
