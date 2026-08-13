---
id: MEM-APR-0022-configuracao-de-processo-fica-na-borda
titulo: Configuracao de processo fica na borda — import nao toma posse de recurso global compartilhado
tipo: memoria
versao: 1.0.0
status: ativo
camada_memoria: aprendizado
autor: DEP-KMS
proprietario: DEP-KMS
aprovador: DEP-KMS
criado_em: 2026-08-13
atualizado_em: 2026-08-13
revisao_prevista: 2027-02-13
decisoes_relacionadas: []
substitui: []
substituido_por: null
origem: Onda 7 — dedupe F53 da Oficina; precedente A-130 do lucaX, fonte lida integral em somente-leitura
evidencia: modulo importado reembrulhou sys.stdout no nivel global; o coletor do wrapper anterior fechou o buffer compartilhado e qualquer print posterior falhou com ValueError I/O operation on closed file
confianca: alta
ocorrencias: 1
ttl: permanente
aplica_se_a: [global]
resumo: Registra que import deve expor definicoes sem reconfigurar stdout, ambiente, logging ou outro recurso global; configuracao pertence ao entrypoint que possui o processo.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: nao-exigida
---

# Configuracao de processo fica na borda

## A licao

Importar modulo nao autoriza tomar posse de `stdout`, variaveis de ambiente, logging ou
outro recurso global. Quem possui o processo e o **entrypoint**; biblioteca oferece funcao.

## A evidencia, medida

Em `A-130`, um modulo fazia novo `TextIOWrapper` no import. Quando o wrapper anterior perdeu
referencia, seu fechamento levou junto o buffer compartilhado. Importar o grafo bastava
para quebrar qualquer `print()` posterior com `ValueError`.

## A condicao fina

Inicializacao imutavel e local do modulo continua permitida. A regra alcança mutacao cujo
efeito vaza para importadores ou depende da ordem de imports. Em processo standalone, a
mesma configuracao pode ocorrer sob `if __name__ == "__main__"`.

## Acao com dono

Modulos do Corpo ficam import-safe; configuracao de I/O e ambiente mora nos entrypoints
(`DEP-ENG`). Teste importa o mesmo componente em processo que ja configurou o recurso e
prova que ele permanece utilizavel (`DEP-QAR`).

## Gatilho de refutacao

Uma plataforma em que o modulo seja formalmente o unico entrypoint e possua o recurso pode
configura-lo; essa propriedade deve ser contratual, nao inferida pela execucao atual.
