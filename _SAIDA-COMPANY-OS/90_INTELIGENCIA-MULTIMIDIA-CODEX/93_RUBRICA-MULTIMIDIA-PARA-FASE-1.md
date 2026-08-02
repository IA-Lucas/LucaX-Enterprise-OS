> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO

# 93 — RUBRICA MULTIMÍDIA PARA INTEGRAÇÃO NA FASE 1

## Níveis de legibilidade

| Nível | Evidência disponível | Afirmação permitida |
|---|---|---|
| LV0 | arquivo ilegível | nenhuma |
| LV1 | metadados técnicos | duração, formato, tamanho, presença de áudio |
| LV2 | descrição anterior | apenas “o catálogo afirma” |
| LV3-V | quadros-chave revisados | texto e fatos visuais, sem atribuir fala |
| LV3-A | transcrição automática bruta | fala provável, com confiança e ressalvas |
| LV4 | transcrição revisada + quadros | conteúdo multimodal sustentado |
| LV5 | conteúdo reproduzido/confirmado | afirmação confirmada por fonte independente |

## Campos obrigatórios por vídeo

- ID estável do manifesto.
- Hash, duração e caminho.
- Método de extração.
- Idioma detectado.
- Transcrição com timestamps, quando existir.
- Confiança e trechos inaudíveis.
- Quadros-chave e instante de captura.
- Texto visual separado da fala.
- Ferramentas ou repositórios citados.
- Alegações do autor.
- Fatos observados.
- Inferências separadas.
- Possível duplicidade visual ou semântica.

## Regras de pontuação

1. Vídeo em LV0–LV2 recebe **ND** em conteúdo, não zero.
2. LV3-V permite pontuar apenas evidência visual.
3. LV3-A não autoriza citação exata sem revisão.
4. Qualidade técnica da mídia não mede qualidade da ideia.
5. Descrição do catálogo é avaliada separadamente da fonte.
6. Alegação numérica sem fonte recebe “não verificada”.
7. Ausência de transcrição impede síntese normativa.
8. Um vídeo duplicado herda a ficha do original e mantém rastreabilidade.

## Handoff para Claude

Claude deve consumir cada entrega citando o ID do vídeo e o ID do handoff.
Nenhum resumo multimídia substitui a evidência original e nenhuma conclusão
é automaticamente incorporada ao LucaX.
