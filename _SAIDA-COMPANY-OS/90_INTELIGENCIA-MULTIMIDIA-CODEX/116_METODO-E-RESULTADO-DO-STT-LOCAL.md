> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO

# Método e resultado do STT local

## Objetivo e limite

Reduzir a lacuna auditiva dos 142 vídeos sem executar repositórios do acervo, sem enviar mídia a serviço externo e sem converter transcrição automática em decisão oficial. O áudio integral foi processado localmente. As fontes permaneceram somente leitura.

Cada resultado é **LV3-A bruto**: transcrição automática não revisada por humano. Os nove quadros já examinados por vídeo permanecem **LV3-V**. Somar LV3-A e LV3-V não produz LV4; nomes, marcas, números, pontuação e citações materiais exigem conferência humana no áudio.

## Ferramentas e integridade

- Motor: `whisper.cpp` v1.9.1, binário oficial CPU x64.
- Modelo: `ggml-small.bin`, multilingual small oficial.
- SHA-256 do arquivo distribuído do motor: `7D8BE46ECD31828E1EB7A2ECDD0D6B314FEAFD82163038AB6092594B0A063539`.
- SHA-256 do modelo: `1BE3A9B2063867B937E64E2EC7483364A79917E157FA98C5D94B5C1FFFEA987B`.
- Conversão: FFmpeg 8.1.2 para WAV mono, 16 kHz, PCM 16-bit.
- Execução: CPU local, oito threads; nenhum pacote foi instalado e nenhum vídeo foi enviado para fora da máquina.
- Porta V8: os 142 SHA-256 das fontes foram recalculados e conferidos contra `92_MANIFESTO-TECNICO-DOS-VIDEOS.md` antes do processamento.

## Piloto

O piloto usou três classes:

1. `AC-10-VID-003`: fala longa em português;
2. `AC-11-VID-001`: fala instrucional em português;
3. `AC-02-VID-008`: efeito sonoro sem narração.

As duas falas produziram texto coerente, com confiança média aproximada de 0,85 e 0,90. O terceiro arquivo produziu onomatopeias instáveis (`boop`/`POP`), demonstrando que probabilidade de token não distingue sozinha fala real de efeito sonoro. Por isso o lote recebeu revisão cruzada com os relatórios visuais.

## Resultado integral

| Métrica | Resultado |
|---|---:|
| Vídeos processados | 142/142 |
| Áudio | 4.020,9 s / 1,12 h |
| Segmentos brutos | 738 |
| Palavras brutas | 7.681 |
| Fala narrativa aproveitável como pista | 42 |
| Sem narração confiável | 99 |
| Letra/trilha musical, não narração | 1 |
| Alta confiança automática | 36 |
| Média confiança automática | 5 |
| Baixa, fala breve com música | 1 |
| Falha técnica de transcrição | 0 |
| Arquivo sem segmento produzido | 1 (`AC-05-VID-024`) |

Os 99 sem narração confiável incluem 93 classificados automaticamente por ausência de texto e seis corrigidos após revisão cruzada porque efeitos, música ou repetições incoerentes tinham sido confundidos com fala. A saída bruta foi preservada nesses seis casos para registrar o comportamento do reconhecedor, mas foi explicitamente proibida como evidência lexical.

## Regras de confiança

- `ALTA AUTOMÁTICA`: ao menos três palavras, texto não trivial, média de token ≥ 0,85 e até 10% dos tokens abaixo de 0,50.
- `MÉDIA AUTOMÁTICA`: média ≥ 0,72 e até 25% abaixo de 0,50.
- `BAIXA AUTOMÁTICA`: há texto, mas os limiares anteriores não foram atingidos.
- `SEM FALA LEXICAL CONFIÁVEL`: nenhum texto útil ou texto trivial.
- Revisão cruzada manual prevalece sobre a classificação numérica quando o conteúdo é claramente efeito, música, letra ou repetição incoerente.

Essas categorias medem utilidade operacional da transcrição, não veracidade do conteúdo falado.

## Erros e limitações observados

- Nomes próprios e produtos sofrem trocas: exemplos incluem `Claude/Cloud/Calde`, `Anthropic/entrópica` e nomes de ferramentas.
- Números, estrelas, preços, versões, licenças, popularidade e promessas continuam alegações não verificadas.
- Música pode gerar palavras ou frases inexistentes.
- Clipes promocionais usam superlativos e causalidades que o STT apenas registra.
- Um texto coerente pode ser letra de música, não narração.
- Não houve segunda pessoa revisora nem alinhamento fonético humano; nenhuma transcrição serve como citação exata.

## Artefatos

- 142 fichas em `TRANSCRICOES-BRUTAS-STT/<área>/AC-xx-VID-nnn_TRANSCRICAO-BRUTA.md`.
- Manifesto item a item em `117_MANIFESTO-TRANSCRICOES-BRUTAS-STT.md`.
- Síntese de contribuição do áudio em `118_RELATORIO-INTEGRADO-DO-AUDIO-DAS-11-AREAS.md`.

O acervo informa o LucaX Enterprise OS, mas não determina sua arquitetura.
