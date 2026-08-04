#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Controle positivo do coletor de custo.

A PERGUNTA QUE ELE RESPONDE
---------------------------
Um coletor que devolve um numero plausivel nao provou nada: ele pode estar
lendo o arquivo errado, ignorando o registro, ou devolvendo uma constante. A
unica prova barata e MEXER NO INSUMO e comprovar que a saida se move — e que
se move NA MEDIDA CERTA, nao apenas que se move.

Este e o mesmo desenho do `ponto_cego.py` do kernel-de-evidencia e da reversao
vermelha da regra de prova do SSC+: plantar a alteracao e exigir que o
instrumento a acuse.

COMO ELE NAO CONTAMINA NADA
---------------------------
Copia as tres fontes para um diretorio TEMPORARIO e descartavel, altera la, e
roda o coletor apontado para a copia com `--raiz`. O `lucaX` NAO e tocado em
nenhum momento — nem para leitura destrutiva, nem para escrita. A fronteira da
Missao G2 negou escrita naquele repositorio.

    python controle_positivo.py

Saida 0 se as tres provas passarem. Saida 1 se qualquer uma falhar — e falhar
aqui significa que o numero do coletor nao pode ser citado.
"""

import json
import os
import shutil
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

import coletor_custo as cc  # noqa: E402


def montar_sandbox(raiz_real, destino):
    """Copia so o que o coletor le. Devolve a raiz da copia."""
    for rel in (cc.REL_ORCAMENTO, cc.REL_VOO, cc.REL_CATALOGO):
        origem = os.path.join(raiz_real, rel)
        alvo = os.path.join(destino, rel)
        os.makedirs(os.path.dirname(alvo), exist_ok=True)
        shutil.copy2(origem, alvo)
    return destino


def _linhas(caminho):
    with open(caminho, encoding="utf-8") as f:
        return [l for l in f.read().splitlines() if l.strip()]


def _gravar(caminho, linhas):
    with open(caminho, "w", encoding="utf-8") as f:
        f.write("\n".join(linhas) + "\n")


def prova_1_o_total_se_move(raiz):
    """Dobrar os tokens de UM registro precificado dobra a parcela dele.

    Escolhe um registro que o coletor JA precificou — mexer num orfao nao
    provaria nada, porque orfao nao entra na conta por desenho.
    """
    caminho = os.path.join(raiz, cc.REL_ORCAMENTO)
    antes = cc.coletar(raiz)

    # Achar um registro precificado e o preco do modelo dele.
    orc, _ = cc.ler_jsonl(caminho)
    voo, _ = cc.ler_jsonl(os.path.join(raiz, cc.REL_VOO))
    tabela, _, _ = cc.carregar_precos(os.path.join(raiz, cc.REL_CATALOGO))
    juntos, _ = cc.juntar(orc, voo)
    regs, _, _ = cc.precificar(juntos, tabela)
    alvo = next((r for r in regs if r["custo_usd"]), None)
    if alvo is None:
        return False, "nenhum registro precificado no corpus — prova impossivel"

    preco_entrada = tabela[alvo["modelo_no_catalogo"]][0]
    delta_esperado = round(alvo["tokens"] / 1_000_000 * preco_entrada, 6)

    # Dobrar os tokens DAQUELE registro, casando por (ts, agente).
    linhas, mexidas = [], 0
    for linha in _linhas(caminho):
        d = json.loads(linha)
        if (d.get("ts") == alvo["ts"] and d.get("agente") == alvo["agente"]
                and mexidas == 0):
            d["tokens_estimados"] = int(d["tokens_estimados"]) * 2
            mexidas += 1
            linha = json.dumps(d, ensure_ascii=False)
        linhas.append(linha)
    _gravar(caminho, linhas)

    depois = cc.coletar(raiz)
    obtido = round(depois["custo_de_entrada_no_pico_usd"]
                   - antes["custo_de_entrada_no_pico_usd"], 6)

    ok = abs(obtido - delta_esperado) < 1e-6
    return ok, (
        "registro %s/%s: %d -> %d tokens @ US$%s/Mtok\n"
        "      total  US$ %.6f -> US$ %.6f\n"
        "      delta  esperado US$ %.6f | obtido US$ %.6f"
        % (alvo["agente"], alvo["ts"], alvo["tokens"], alvo["tokens"] * 2,
           preco_entrada, antes["custo_de_entrada_no_pico_usd"],
           depois["custo_de_entrada_no_pico_usd"], delta_esperado, obtido))


def prova_2_orfao_nao_vira_zero(raiz):
    """Registro sem modelo NAO some e NAO entra como zero: ele e contado."""
    caminho = os.path.join(raiz, cc.REL_ORCAMENTO)
    antes = cc.coletar(raiz)

    linhas = _linhas(caminho)
    novo = json.dumps({"ts": "2999-01-01T00:00:00+00:00",
                       "agente": "agente-que-nao-existe",
                       "tokens_estimados": 999_999, "limite": 60000},
                      ensure_ascii=False)
    _gravar(caminho, linhas + [novo])

    depois = cc.coletar(raiz)
    custo_igual = (depois["custo_de_entrada_no_pico_usd"]
                   == antes["custo_de_entrada_no_pico_usd"])
    contado = (depois["nao_precificados"] == antes["nao_precificados"] + 1)
    tokens = (depois["tokens_nao_precificados"]
              == antes["tokens_nao_precificados"] + 999_999)

    return (custo_igual and contado and tokens), (
        "orfao de 999.999 tokens acrescentado\n"
        "      custo inalterado: %s (US$ %.6f)\n"
        "      nao_precificados %d -> %d\n"
        "      tokens fora da conta %d -> %d"
        % (custo_igual, depois["custo_de_entrada_no_pico_usd"],
           antes["nao_precificados"], depois["nao_precificados"],
           antes["tokens_nao_precificados"], depois["tokens_nao_precificados"]))


def prova_3_preco_manda(raiz):
    """Mudar o CATALOGO muda o total. Prova que o preco e lido, nao embutido."""
    caminho = os.path.join(raiz, cc.REL_CATALOGO)
    antes = cc.coletar(raiz)

    with open(caminho, encoding="utf-8") as f:
        cat = json.load(f)
    for reg in cat["provedores"][cc.PROVEDOR_PADRAO]["modelos"]:
        if reg.get("input_usd_mtok") is not None:
            reg["input_usd_mtok"] = float(reg["input_usd_mtok"]) * 10
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(cat, f, ensure_ascii=False, indent=2)

    depois = cc.coletar(raiz)
    esperado = round(antes["custo_de_entrada_no_pico_usd"] * 10, 6)
    obtido = depois["custo_de_entrada_no_pico_usd"]
    ok = abs(obtido - esperado) < 1e-4
    return ok, (
        "preco de entrada x10 no catalogo\n"
        "      total  US$ %.6f -> US$ %.6f (esperado US$ %.6f)"
        % (antes["custo_de_entrada_no_pico_usd"], obtido, esperado))


def main():
    raiz_real = cc.RAIZ_PADRAO
    provas = [
        ("1. o total se move na medida certa", prova_1_o_total_se_move),
        ("2. orfao e contado, nunca somado como zero", prova_2_orfao_nao_vira_zero),
        ("3. o preco vem do catalogo, nao do codigo", prova_3_preco_manda),
    ]
    print("=" * 78)
    print("CONTROLE POSITIVO — coletor_custo.py")
    print("=" * 78)
    print("Cada prova roda num sandbox PROPRIO e descartavel.")
    print("O lucaX nao e escrito em momento nenhum.\n")

    falhas = 0
    for titulo, prova in provas:
        tmp = tempfile.mkdtemp(prefix="controle-custo-")
        try:
            montar_sandbox(raiz_real, tmp)
            ok, detalhe = prova(tmp)
        except Exception as erro:            # noqa: BLE001
            ok, detalhe = False, "excecao: %r" % (erro,)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
        print("  [%s] %s" % ("PASSOU" if ok else "FALHOU", titulo))
        for linha in detalhe.splitlines():
            print("      " + linha.strip() if not linha.startswith("      ")
                  else linha)
        print()
        if not ok:
            falhas += 1

    print("=" * 78)
    print("%d de %d provas passaram." % (len(provas) - falhas, len(provas)))
    if falhas:
        print("FALHOU — o numero do coletor NAO pode ser citado.")
    else:
        print("O coletor le o insumo, respeita o orfao e obedece ao catalogo.")
        print("Isto NAO prova que o numero corresponde a fatura: ver `nao_cobre`.")
    print("=" * 78)
    return 1 if falhas else 0


if __name__ == "__main__":
    raise SystemExit(main())
