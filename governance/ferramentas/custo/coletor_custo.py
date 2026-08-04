#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Coletor de custo em dinheiro — a multiplicacao que faltava.

POR QUE ESTE ARQUIVO EXISTE
---------------------------
`lucaX/scripts/hub_operacao.py` ja nomeia este coletor como o que FALTA:

    campo:            "custo por resultado em dinheiro"
    coletor_que_falta:"tabela de preco por modelo nao e lida em runtime"
    motivo:           "orcamento_subagente.jsonl mede TOKEN, que e medida honesta.
                       Converter em dolar exigiria preco vigente por modelo, que
                       muda sem aviso — precedente A-231 (o CFO contava 1,8 bilhao
                       de tokens como US$ 0,00)."

Os dois lados ja existiam e nunca se encontraram: a telemetria grava o numero do
FORNECEDOR, e o catalogo de preco ja e lido em runtime pelo `consult`. Este
arquivo faz a multiplicacao — e carrega junto, dentro de toda saida, o que ela
NAO cobre. A regra da casa e que proxy declarada vale e proxy silenciosa e a
familia do MAJOR #3: o artefato que AFIRMA a propriedade em vez de exerce-la.

ONDE ELE MORA, E POR QUE AQUI
-----------------------------
`governance/ferramentas/custo/`, subpasta de uma entrada JA declarada na lista
fechada do `IR-BL/5`. Nao na raiz: o portao de raiz e lista fechada positiva e
recusaria medir (`exit 2`, familia RD-53/RD-81).

NENHUM `.md` FOI CRIADO AQUI, E ISSO E DELIBERADO E DECLARADO. O medidor conta
`find $ALVOS -name "*.md"` sob ACERVO; um `.md` aqui viraria artefato medido
(253 -> 254) e isso seria PROMOVER AO ACERVO CANONICO, que o despacho G2 proibe.
A documentacao mora nesta docstring e em `LEIA-ME.txt`. Isto NAO e driblar o
contador: ferramenta nao e artefato, e o proprio `baseline.sh` — o instrumento
mais citado deste acervo — vive fora dele, em `_missao-*/ferramentas/`.
Dar a este coletor uma sede documentada em `.md` exige ato do Fundador.

O QUE ELE LE (tudo em SOMENTE LEITURA, e nada aqui e do lucaX)
--------------------------------------------------------------
  1. lucaX/nucleo/reforco/orcamento_subagente.jsonl  — ts, agente, tokens
  2. lucaX/nucleo/reforco/voo_subagente.jsonl        — ts, agente, session_id, modelo
  3. SuperCondutor/config/catalogo-llms.json         — preco por modelo

O `lucaX` NAO e escrito por este coletor em nenhuma circunstancia: a fronteira
da Missao G2 negou escrita naquele repositorio, e ler nao e escrever.

A ARITMETICA, E POR QUE ELA E UM TETO E NAO UM GASTO
----------------------------------------------------
`tokens_estimados` sai de `juiz.py:estimar_tokens_subagente()`, que devolve o
MAIOR valor de `input_tokens + cache_read_input_tokens + cache_creation_input_tokens`
visto no campo `message.usage` do transcript. Consequencias, todas medidas no
proprio codigo-fonte e nao supostas:

  - e o lado da ENTRADA. Token de saida nao entra, e saida custa 5x a entrada
    em todo modelo do catalogo. O numero puxa para BAIXO.
  - e PICO de uma mensagem, nunca a soma da sessao. Puxa para BAIXO.
  - soma cache lido, cache criado e entrada fresca num numero so. Cobrar os tres
    a preco cheio de entrada puxa para CIMA, porque cache lido custa uma fracao.

As tres nao se cancelam de forma conhecida. Por isso a saida se chama
`custo_de_entrada_no_pico_usd` e nunca `gasto`, e o rotulo e `estimado`.
Quem citar este numero como fatura esta citando outra coisa.
"""

import argparse
import json
import os
import sys
from collections import defaultdict

PROXY = "entrada-no-pico-a-preco-cheio"
ROTULO = "estimado"

# --- Onde as fontes vivem. Descobertas por leitura, nao por convencao. --------
RAIZ_PADRAO = r"E:\LucasIA\Projetos"
REL_ORCAMENTO = r"lucaX\nucleo\reforco\orcamento_subagente.jsonl"
REL_VOO = r"lucaX\nucleo\reforco\voo_subagente.jsonl"
REL_CATALOGO = (r"lucaX\My_WorkSpace\Meus_projetos\SuperCondutor"
                r"\config\catalogo-llms.json")
PROVEDOR_PADRAO = "anthropic_claude"

# O QUE ESTA PROXY NAO CAPTURA. Cada item existe por um fato medido deste
# acervo, nunca por precaucao generica. Viaja DENTRO de toda saida.
NAO_COBRE = (
    {"codigo": "sessao-sem-eventlog-nao-existe-aqui",
     "porque": "so grava quem passa pelo hook SubagentStop do lucaX. A sessao "
               "PRINCIPAL nao grava nada — nem esta. E os tres repositorios "
               "onde a fabrica trabalha (LucaX Enterprise OS, SSC-Plus, "
               "LucaX-Enterprise-Research) NAO TEM diretorio .claude/: todo "
               "trabalho feito neles e invisivel para este coletor. Esta e a "
               "lacuna maior, e nao ha numero que a estime."},
    {"codigo": "saida-nao-e-medida",
     "porque": "`tokens_estimados` e so o lado da entrada. Token de saida custa "
               "5x a entrada em todo modelo do catalogo e nao esta aqui. O total "
               "real e MAIOR do que este por uma margem que nao se conhece."},
    {"codigo": "pico-nao-e-soma",
     "porque": "o coletor de origem devolve o maior `message.usage` de UMA "
               "mensagem, nao a soma dos turnos. Subagente de 10 turnos conta "
               "como um. Puxa para baixo."},
    {"codigo": "cache-cobrado-a-preco-cheio",
     "porque": "entrada fresca, cache lido e cache criado vem somados num campo "
               "so e sao cobrados aqui ao preco de entrada. Cache lido custa uma "
               "fracao disso na fatura real. Puxa para cima — e e por isso que "
               "o numero e TETO de entrada, nao valor."},
    {"codigo": "modelo-desconhecido-nao-tem-preco",
     "porque": "o modelo vem do `voo_subagente.jsonl`, que so passou a grava-lo "
               "depois de o log ja existir. Registro sem modelo nao e precificado "
               "e sai contado a parte, nunca somado como zero. Zero silencioso "
               "mudaria o resultado sem mudar o relatorio."},
    {"codigo": "juncao-por-tempo-nao-por-identificador",
     "porque": "`orcamento_subagente.jsonl` NAO grava `session_id`. A sessao vem "
               "do `voo_subagente.jsonl` casando `(ts, agente)`. Dois subagentes "
               "do mesmo tipo terminando no mesmo segundo sao indistinguiveis."},
    {"codigo": "preco-tem-data-e-nao-se-atualiza-sozinho",
     "porque": "o catalogo declara `atualizado_em`. Preco mudado no fornecedor e "
               "nao refletido ali produz numero errado com a mesma confianca de "
               "quando estava certo. A data sai em toda execucao."},
    {"codigo": "nada-aqui-foi-conferido-contra-fatura",
     "porque": "nenhum numero deste coletor foi comparado com cobranca real. "
               "Ele mede o que a telemetria gravou, nao o que foi cobrado."},
)


class FonteAusente(Exception):
    """Insumo que o coletor precisa e o disco nao tem."""


def ler_jsonl(caminho):
    """Uma lista de dicts. Linha quebrada e PULADA e CONTADA, nunca silenciada."""
    if not os.path.isfile(caminho):
        raise FonteAusente(caminho)
    linhas, ruins = [], 0
    with open(caminho, encoding="utf-8", errors="replace") as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue
            try:
                linhas.append(json.loads(linha))
            except json.JSONDecodeError:
                ruins += 1
    return linhas, ruins


def carregar_precos(caminho, provedor=PROVEDOR_PADRAO):
    """id do modelo -> (usd por Mtok de entrada, usd por Mtok de saida)."""
    if not os.path.isfile(caminho):
        raise FonteAusente(caminho)
    with open(caminho, encoding="utf-8") as f:
        cat = json.load(f)
    tabela = {}
    for reg in cat.get("provedores", {}).get(provedor, {}).get("modelos", []):
        ent, sai = reg.get("input_usd_mtok"), reg.get("output_usd_mtok")
        if ent is None or sai is None:
            continue
        tabela[reg["id"]] = (float(ent), float(sai))
    return tabela, cat.get("versao"), cat.get("atualizado_em")


def normalizar_modelo(nome, tabela):
    """O voo grava `claude-haiku-4-5-20251001`; o catalogo, `claude-haiku-4.5`.

    Resolve pelo prefixo mais longo que casa, e devolve None quando nada casa.
    None NAO vira preco zero: vira registro nao precificado, contado a parte.
    """
    if not nome:
        return None
    if nome in tabela:
        return nome
    achatado = nome.replace(".", "-")
    for chave in sorted(tabela, key=len, reverse=True):
        if achatado.startswith(chave.replace(".", "-")):
            return chave
    return None


def juntar(orcamento, voo):
    """Cada medicao de token ganha sessao e modelo, casando `(ts, agente)`.

    Nao ha identificador comum: `orcamento_subagente.jsonl` grava `ts` e
    `agente` e nada mais que identifique a corrida. Os dois logs sao escritos
    no MESMO evento (SubagentStop), entao o `ts` bate no segundo.
    """
    indice = {}
    for v in voo:
        indice.setdefault((v.get("ts"), v.get("agente")), v)
    saida, sem_par = [], 0
    for o in orcamento:
        par = indice.get((o.get("ts"), o.get("agente")))
        if par is None:
            sem_par += 1
        saida.append({
            "ts": o.get("ts"),
            "agente": o.get("agente"),
            "tokens": int(o.get("tokens_estimados") or 0),
            "limite": o.get("limite"),
            "estourou": o.get("estourou"),
            "session_id": (par or {}).get("session_id"),
            "modelo": (par or {}).get("modelo"),
            "modelo_executor": (par or {}).get("modelo_executor"),
            "pareado": par is not None,
        })
    return saida, sem_par


def precificar(registros, tabela):
    """Multiplica. Sem modelo conhecido, NAO precifica — e diz quanto ficou fora."""
    precificados, orfaos, tokens_orfaos = [], 0, 0
    for r in registros:
        chave = normalizar_modelo(r.get("modelo"), tabela)
        if chave is None:
            orfaos += 1
            tokens_orfaos += r["tokens"]
            r = dict(r, modelo_no_catalogo=None, custo_usd=None)
        else:
            entrada_mtok = tabela[chave][0]
            r = dict(r, modelo_no_catalogo=chave,
                     custo_usd=round(r["tokens"] / 1_000_000 * entrada_mtok, 6))
        precificados.append(r)
    return precificados, orfaos, tokens_orfaos


def _agrupar(registros, chave):
    caixas = defaultdict(lambda: {"registros": 0, "tokens": 0, "custo_usd": 0.0,
                                  "nao_precificados": 0})
    for r in registros:
        c = caixas[chave(r)]
        c["registros"] += 1
        c["tokens"] += r["tokens"]
        if r["custo_usd"] is None:
            c["nao_precificados"] += 1
        else:
            c["custo_usd"] = round(c["custo_usd"] + r["custo_usd"], 6)
    return dict(caixas)


def coletar(raiz=RAIZ_PADRAO, provedor=PROVEDOR_PADRAO):
    """A coleta inteira. Devolve o relatorio e os limites colados nele."""
    orc, orc_ruins = ler_jsonl(os.path.join(raiz, REL_ORCAMENTO))
    voo, voo_ruins = ler_jsonl(os.path.join(raiz, REL_VOO))
    tabela, cat_versao, cat_data = carregar_precos(
        os.path.join(raiz, REL_CATALOGO), provedor)

    juntos, sem_par = juntar(orc, voo)
    regs, orfaos, tokens_orfaos = precificar(juntos, tabela)

    total = round(sum(r["custo_usd"] for r in regs
                      if r["custo_usd"] is not None), 6)

    return {
        "proxy": PROXY,
        "rotulo": ROTULO,
        "unidade": "USD",
        "provedor": provedor,
        "catalogo_versao": cat_versao,
        "catalogo_atualizado_em": cat_data,
        "modelos_com_preco": sorted(tabela),
        "registros_lidos": len(orc),
        "linhas_ilegiveis": {"orcamento": orc_ruins, "voo": voo_ruins},
        "sem_par_no_voo": sem_par,
        "nao_precificados": orfaos,
        "tokens_nao_precificados": tokens_orfaos,
        "custo_de_entrada_no_pico_usd": total,
        "por_dia": _agrupar(regs, lambda r: (r["ts"] or "")[:10]),
        "por_sessao": _agrupar(regs, lambda r: r["session_id"] or "(sem sessao)"),
        "por_modelo": _agrupar(regs, lambda r: r["modelo_no_catalogo"]
                               or "(modelo desconhecido)"),
        "por_agente": _agrupar(regs, lambda r: r["agente"]),
        "nao_cobre": [dict(x) for x in NAO_COBRE],
    }


def relatar(rel, largura=78):
    """O relatorio em texto. Os limites saem SEMPRE, nunca sob flag."""
    L = []
    L.append("=" * largura)
    L.append("CUSTO DE ENTRADA NO PICO — proxy `%s` · rotulo `%s`"
             % (rel["proxy"], rel["rotulo"]))
    L.append("=" * largura)
    L.append("catalogo de preco: versao %s, atualizado em %s (%s)"
             % (rel["catalogo_versao"], rel["catalogo_atualizado_em"],
                rel["provedor"]))
    L.append("registros lidos:   %d" % rel["registros_lidos"])
    L.append("  sem par no voo:  %d  (ficam sem sessao e sem modelo)"
             % rel["sem_par_no_voo"])
    L.append("  nao precificados:%d  (%d tokens fora da conta, NAO somados como zero)"
             % (rel["nao_precificados"], rel["tokens_nao_precificados"]))
    if any(rel["linhas_ilegiveis"].values()):
        L.append("  linhas ilegiveis:%s" % rel["linhas_ilegiveis"])
    L.append("")
    L.append(">>> CUSTO DE ENTRADA NO PICO: US$ %.6f  (%s, TETO — nao e gasto)"
             % (rel["custo_de_entrada_no_pico_usd"], rel["rotulo"]))
    L.append("")

    def bloco(titulo, caixas, limite=None, ordenar_por_custo=True):
        L.append("-" * largura)
        L.append(titulo)
        L.append("-" * largura)
        itens = sorted(caixas.items(),
                       key=(lambda kv: -kv[1]["custo_usd"]) if ordenar_por_custo
                       else (lambda kv: kv[0]))
        if limite:
            itens = itens[:limite]
        L.append("  %-38s %7s %12s %12s" % ("", "regs", "tokens", "US$"))
        for nome, c in itens:
            marca = " *" if c["nao_precificados"] else ""
            L.append("  %-38s %7d %12d %12.6f%s"
                     % (str(nome)[:38], c["registros"], c["tokens"],
                        c["custo_usd"], marca))
        if limite and len(caixas) > limite:
            L.append("  ... e mais %d" % (len(caixas) - limite))

    bloco("POR DIA", rel["por_dia"], ordenar_por_custo=False)
    bloco("POR MODELO (o fornecedor)", rel["por_modelo"])
    bloco("POR AGENTE", rel["por_agente"], limite=10)
    bloco("POR SESSAO (as 10 mais caras)", rel["por_sessao"], limite=10)
    L.append("")
    L.append("  * a linha contem registro sem preco; o custo dela e parcial.")
    L.append("")
    L.append("=" * largura)
    L.append("O QUE ESTE NUMERO NAO COBRE — sai sempre, e nao ha flag que suprima")
    L.append("=" * largura)
    for i, item in enumerate(rel["nao_cobre"], 1):
        L.append("%2d. %s" % (i, item["codigo"]))
        texto = item["porque"]
        while texto:
            corte = len(texto) if len(texto) <= largura - 6 else \
                texto.rfind(" ", 0, largura - 6)
            L.append("    " + texto[:corte])
            texto = texto[corte:].lstrip()
    L.append("=" * largura)
    return "\n".join(L)


def main(argv=None):
    p = argparse.ArgumentParser(
        description="Multiplica a telemetria de token pelo catalogo de preco. "
                    "Somente leitura. Nunca escreve no lucaX.")
    p.add_argument("--raiz", default=RAIZ_PADRAO,
                   help="raiz que contem lucaX/ (padrao: %s)" % RAIZ_PADRAO)
    p.add_argument("--json", dest="json_saida",
                   help="grava o relatorio completo neste caminho")
    p.add_argument("--provedor", default=PROVEDOR_PADRAO)
    args = p.parse_args(argv)

    try:
        rel = coletar(args.raiz, args.provedor)
    except FonteAusente as erro:
        print("ERRO — insumo ausente: %s" % erro, file=sys.stderr)
        print("Sem insumo nao ha medicao. Ausencia nao vira zero.", file=sys.stderr)
        return 2

    try:
        print(relatar(rel))
    except UnicodeEncodeError:
        print(relatar(rel).encode("ascii", "replace").decode("ascii"))

    if args.json_saida:
        with open(args.json_saida, "w", encoding="utf-8") as f:
            json.dump(rel, f, ensure_ascii=False, indent=2, sort_keys=True)
        print("\njson: %s" % args.json_saida)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
