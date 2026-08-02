> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO

# Relatório de inspeção da planilha — AC-10-PLA-001

**Item:** `_construcao-civil/maiscontrole-dossie-jul2026.xlsx`  
**Área:** 10 — Aplicações de negócio  
**Hash reconferido:** `9B35BF396C57A0D4F6842E98060E2017FE6E91C15254C7863C9A3A0BB2520921`  
**Hash do manifesto:** `9B35BF396C57A0D4` — confere  
**LV:** LV4 — conteúdo das dez abas inspecionado diretamente  
**Estado do catálogo:** PARCIAL  
**Fonte modificada:** não

## Cobertura técnica

| Aba | Intervalo usado | Conteúdo |
|---|---|---|
| 01 Resumo | A1:C26 | perfil, preços, stack, integrações, tração e veredito |
| 02 Planos e Precos | A1:F21 | planos, adicionais e conta cheia |
| 03 Modulos | A1:E18 | 12 módulos e Venda Reajustada |
| 04 Mapa Funcional | A1:D18 | domínios e rotas |
| 05 Stack Tecnica | A1:F32 | tecnologias, status e leitura competitiva |
| 06 Integracoes | A1:D32 | presença/ausência declarada |
| 07 Vulnerabilidades | A1:E21 | lacunas comerciais ranqueadas |
| 08 Concorrentes | A1:G12 | comparação de seis alternativas |
| 09 Backlog MVP | A1:F37 | 32 itens de paridade/diferenciação |
| 10 Fontes | A1:D21 | 16 fontes e uma linha de não cobertura |

Estrutura observada: 10 abas, 10 tabelas, nenhuma fórmula, nenhum gráfico e nenhum erro de fórmula. A ausência de erros não comprova os cálculos: todos os resultados derivados foram gravados como valores ou texto estático.

## Fidelidade do `_CONTEUDO.md`

O catálogo acerta:

- dez abas e seus temas;
- 12 módulos declarados;
- preço de entrada de R$ 269/mês;
- conta cheia de R$ 1.126/mês e implantação de R$ 1.250;
- AngularJS 1.5.7, migração parcial para React e alegação de 131 rotas;
- ausência declarada de API pública, webhooks, BIM/IFC e IA embarcada;
- Vobi como ameaça classificada pela própria planilha;
- transformação das lacunas em backlog P0–P2.

O estado é **PARCIAL** porque o catálogo reproduz contagens e conclusões como fatos sem registrar inconsistências internas, natureza estática dos cálculos e limites do método.

## Reconciliações objetivas

### 1. Preços

- `499 + 60 + 60 + 60 + 69 + 90 + 90 + 99 + 99 = 1.126`: correto.
- `1.126 × 12 + 1.250 = 14.762`: correto.
- `1.126 ÷ 269 = 4,185...`: arredondamento para 4,2× é coerente.

Os três resultados estão hardcoded; não existem fórmulas nem células de premissa ligadas aos totais.

### 2. Módulos

A aba 03 lista quatro módulos “Plano inicial” e oito linhas “Adicional”, porém:

- `Aplicativo` aparece como adicional com preço “embutido”;
- `Venda Reajustada`, fora dos 12 cards, custa R$ 90;
- a conta cheia usa oito itens pagos incluindo Venda Reajustada, não o Aplicativo.

Logo, “12 módulos, 8 pagos à parte” precisa de definição mais rigorosa: oito são rotulados como adicionais, mas um é embutido; existe ainda um adicional pago sem card.

### 3. Rotas

As 13 quantidades da aba 04 somam:

`11+6+14+6+17+12+8+6+10+13+10+10+5 = 128`.

O título afirma 131. A nota diz que duas rotas foram capturadas parcialmente, o que levaria a 130, não 131. A diferença não é reconciliada.

### 4. Integrações

A contagem direta da aba 06 resulta em:

- **13 PRESENTE**: 8 bancos, 2 fiscais, 2 serviços públicos e 1 integração de engenharia;
- **14 AUSENTE**.

O rodapé declara 14 presentes e 13 ausentes. As duas contagens estão invertidas por uma unidade.

### 5. Backlog

A aba 09 contém 32 itens:

- 14 de PARIDADE e 18 DIFERENCIAIS;
- 15 P0, 13 P1 e 4 P2.

É um backlog opinativo, sem esforço, dependências, evidência de demanda, critério de aceite, risco, custo, responsável ou experimento. Não é roadmap validado.

## Forças do artefato

1. Organiza o problema em visão executiva, preço, produto, arquitetura, integrações, concorrência, backlog e fontes.
2. Distingue paridade obrigatória de diferenciação proposta.
3. Registra itens não cobertos.
4. Liga várias alegações a categorias de fonte.
5. Converte observações em hipóteses de produto, permitindo futura validação.
6. Expõe o raciocínio competitivo, inclusive premissas que podem ser contestadas.

## Limites e riscos

1. **Ausência no bundle não prova ausência no produto.** Back end, configuração, feature flag, serviço externo ou ambiente autenticado podem não aparecer no JavaScript público.
2. **“IA: nenhuma” e “API/webhooks ausentes” são conclusões fortes demais** sem inspeção do sistema autenticado e documentação completa.
3. **“Vulnerabilidades” são brechas comerciais**, não vulnerabilidades técnicas ou de segurança. A escala CRÍTICA/ALTA/MÉDIA/BAIXA mede oportunidade de ataque competitivo.
4. **Estimativas não demonstradas:** “cada feature custa 3×”, “metade do time”, “demo vende sozinha”, faixa R$ 599–699, first-load <300 KB e várias previsões de mercado.
5. **Comparação de concorrentes mistura dado, marketing e julgamento.** “IA: NÃO”, ameaça e posicionamento pedem evidência datada por linha.
6. **Fontes não têm proveniência por célula.** Há URLs e confiabilidade autoratribuída, mas não há captura arquivada, hash, trecho, timestamp individual nem vínculo claim→fonte.
7. **Engenharia reversa exige revisão jurídica e de termos** antes de uso operacional, comercial ou publicação.
8. **Dados de obra ampliam risco:** voz, foto, NF, pessoas, localização, finanças e documentos exigem minimização, acesso, retenção, consentimento/base legal e auditoria.
9. **Snapshot temporal:** preços, versões, avaliações, concorrentes e ofertas são retrato declarado de julho de 2026.

## Extrações candidatas

Estas ideias podem seguir para avaliação, nunca incorporação automática:

- modelo de dossiê em camadas: resumo→evidência→lacunas→concorrência→backlog→fontes;
- matriz **paridade × diferenciação**;
- registro explícito de não cobertura;
- reconciliação obrigatória de totais;
- cada alegação ligada a fonte, data, trecho e confiança;
- separação entre fato observado, inferência, marketing, cálculo e recomendação;
- portas de prova para preço, demanda, arquitetura e risco;
- backlog enriquecido com hipótese, métrica, experimento, custo, dependência, reversibilidade e critério de saída.

## Portas candidatas

- não usar 131 rotas nem 14/13 integrações sem reconciliação;
- não tratar ausência em bundle como prova de ausência sistêmica;
- não publicar comparação competitiva sem fonte primária datada e revisão jurídica;
- não transformar P0–P2 em roadmap oficial;
- não automatizar voz, imagem, nota fiscal ou dados de pessoas sem governança;
- não adotar preço, stack ou limite de performance sem experimento próprio;
- revalidar todas as alegações temporais antes de qualquer decisão.

Claude deve aplicar `05_GUIA-DE-APLICACAO-DA-RUBRICA.md`, mantendo NF, NC, RP e AA separados. LV4 autoriza avaliar o que a planilha demonstra sobre si; não eleva alegações externas a fatos confirmados nem produz LV5.

O acervo informa o LucaX Enterprise OS, mas não determina sua arquitetura.
