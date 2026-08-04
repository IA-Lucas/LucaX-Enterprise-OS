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

## LEASE — nenhuma escrita sob o recurso fenceado sem token adquirido

> **Nenhuma escrita em qualquer caminho sob o recurso fenceado sem lease adquirido —
> inclusive `_SAIDA-COMPANY-OS/` e qualquer diretorio que nao seja acervo mas viva
> dentro do recurso. Vale para correcao, registro e faxina, nao apenas para missao. A
> folga foi medida: sessao alheia escreveu em `_SAIDA-COMPANY-OS/` as `13:04:47` e
> `13:07:32` sob lease vivo, porque a regra dizia acervo e o lease fenceia o
> diretorio.**

Regra permanente, gravada por **determinacao (c) do TERCEIRO DESPACHO do Soberano de
2026-08-02** e **CORRIGIDA no QUARTO DESPACHO do mesmo dia**, que trocou *acervo* pelo
**recurso inteiro**. O fundamento e medido nas duas vezes:

- **Por que a regra existe.** As tres escritas do acervo de `10:47`, `11:50` e `11:59`
  ocorreram com o lease **LIBERADO**, porque o token 15 havia sido devolvido e nenhuma
  regra escrita obrigava a readquirir. **Sem regra explicita, a sessao escreve sem lease.**
- **Por que ela precisou ser corrigida em seguida.** A primeira redacao dizia *"no
  acervo"*, e o lease declara como `recurso` o **diretorio inteiro** — de modo que
  `_SAIDA-COMPANY-OS/` ficava **dentro** do recurso fenceado e **fora** da regra. A folga
  nao foi hipotese: **foi exercida** por sessao alheia enquanto o token 16 estava vivo.
  **Regra mais estreita que o fence deixa porta aberta com aparencia de porta fechada.**

- **Instrumento:** `E:\LucasIA\Projetos\_leases\LucaX-Enterprise-OS.lease`. Vive **fora
  do acervo** e **nao e artefato**.
- **Token monotonico crescente.** Escrita com token menor que o vigente e invalida.
- **Adquirir ANTES da primeira escrita**, declarando: titular, motivo, `estado_fenceado`
  *(os tres valores da baseline, medidos pelo instrumento vigente)*, `ponto_de_rollback`
  e `copia_datada`.
- **Liberar depois da pos-verificacao**, declarando `proximo_fencing_token`.
- **Alcance: o `recurso` que o lease declara, e nao a lista do medidor.**
  `_SAIDA-COMPANY-OS/`, `.obsidian/`, `.git/`, `.gitattributes` e este arquivo sao
  `NAO_ACERVO` **para efeito de MEDIR** — nao contam artefato nem linha — e continuam
  **DENTRO** da regra **para efeito de ESCREVER**. **As duas listas nao sao a mesma
  lista, e confundi-las foi a folga.** ✅ **FECHADA no quarto despacho de 2026-08-02**,
  depois de exercida.

---

## Nota de medicao — leia antes de rodar a baseline

`baseline.sh` mede por **lista fechada positiva** e **para com erro** diante de
entrada nao declarada na raiz (portao de raiz, achado `RD-53`). A recusa e o
portao funcionando, nao falha.

**Instrumento vigente: `IR-BL/3`**, `sha256`
`0d4f1b3db309c88ef44e1c8ef6aa6588230648c44880f6b772601660082f4ad7`, em
`E:\LucasIA\Projetos\_missao-1-13-5-1-2026-08-02\ferramentas\baseline.sh`.
Lado `NAO_ACERVO`: `.obsidian`, `_SAIDA-COMPANY-OS`, `CLAUDE.md`, `.git`,
`.gitattributes`.

> ### ⚠️ Correcao declarada, nao silenciosa — 2026-08-02
>
> Ate esta data este paragrafo afirmava que **este arquivo nao estava declarado**
> na lista e que por isso o instrumento **recusava medir**. **As duas afirmacoes
> ficaram FALSAS e continuaram no texto:** `CLAUDE.md` entrou em `NAO_ACERVO`
> ainda em **`IR-BL/2`**, por decisao do Fundador no despacho de abertura da
> Missao 1.13.4.5, e o achado **`RD-81`** esta **✅ FECHADO** desde 2026-08-01 —
> fechado **pelo proprio dono**, o Soberano.
>
> Corrigido ao gravar a regra de lease acima, **na mesma passagem e sem rito**:
> este arquivo declara-se nao-artefato, e por isso a correcao **nao exige** `ADR`,
> hash, baseline nem ato. **Registrada aqui em vez de emendada em silencio** —
> deixa-la seria mais um membro da familia de **`RD-101`**, *artefato que afirma
> propriedade que ja nao vale*, dentro do arquivo que instrui quem mede.
