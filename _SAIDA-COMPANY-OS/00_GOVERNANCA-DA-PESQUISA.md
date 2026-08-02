> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO

# 00 — GOVERNANÇA DA PESQUISA

**Frente:** Programa de Inteligência do Acervo
**Fase corrente:** Fase 0 — Governança e Inventário
**Abertura:** 2026-07-29

---

## 1. Regra central

> **O acervo informa o LucaX Enterprise OS, mas não determina sua arquitetura.**

Esta frente produz **evidência**, não decisão. Nenhum artefato produzido aqui adquire força normativa por existir, por estar bem argumentado ou por ser conveniente. A passagem de evidência para norma só pode ocorrer por avaliação explícita dos Frameworks oficiais 1.11–1.19, fora desta frente.

## 2. O que esta frente é

Uma trilha **paralela e isolada** de pesquisa sobre um acervo de material de terceiros — 43 repositórios públicos, 93 capturas de tela, 142 vídeos e 1 planilha — coletado para estudo de sistemas de IA e agentes.

O objetivo é responder, com procedência rastreável: *o que existe lá dentro, em que estado, e com que grau de confiança*.

## 3. O que esta frente não é

Esta frente **não pode**, em nenhuma fase, produzir:

| Categoria proibida | |
|---|---|
| Carta | Framework oficial |
| ADR | Spec |
| Skill | Agente ou subagente |
| Command | Workflow |
| Política | Arquitetura ou organograma |
| Componente canônico | Roadmap de implementação |
| Decisão oficial | Antecipação de decisão normativa |

Qualquer aplicação possível ao LucaX Enterprise OS é registrada exclusivamente como **candidato à avaliação futura**, com essa etiqueta literal.

## 4. Classificação obrigatória

Todo arquivo desta frente abre com o bloco:

```
> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO
```

Um arquivo sem esse bloco não pertence a esta frente e não deve ser lido como produto dela.

## 5. Isolamento

### 5.1 Área de saída

Tudo que esta frente produz vive em:

```
E:\LucasIA\Projetos\LucaX Enterprise OS\_SAIDA-COMPANY-OS\
```

**Justificativa do local.** A frente serve ao LucaX Enterprise OS e precisa ser retomável por outra IA no mesmo workspace. O prefixo `_` mantém a pasta fora da hierarquia canônica (`foundation/`, `governance/`, `decisions/`, `capabilities/`, `departments/`, `rfcs/`, `memory/`), que não foi tocada. Nenhum arquivo canônico foi lido para escrita, alterado ou renomeado.

### 5.2 Restrições sobre o acervo de origem

Durante a Fase 0, sobre `C:\Users\IA Lucas\OneDrive\Área de Trabalho\POJETOS\Para criar um novo projeto\Mais material`:

| Restrição | Cumprimento na Fase 0 |
|---|---|
| Não mover ou renomear fontes | Cumprido — nenhuma operação de escrita |
| Não alterar arquivos originais | Cumprido — apenas leitura e cálculo de hash |
| Não executar repositórios | Cumprido — nenhum processo iniciado a partir do acervo |
| Não instalar dependências | Cumprido |
| Não importar código ou componentes | Cumprido — nada copiado para o repositório canônico |
| Não modificar Frameworks 1.11–1.19 | Cumprido — não acessados |

Operações realizadas sobre o acervo, exaustivamente: enumeração de diretórios, leitura de arquivos de catálogo (`INDICE-COMPLETO.md`, `LEIA-PRIMEIRO.md`, `_CONTEUDO.md`), cálculo de SHA-256, leitura dos 12 primeiros bytes de cada mídia para conferir assinatura de formato, e leitura de `xl/workbook.xml` da planilha para contar abas.

## 6. Regras de evidência

1. **Não inferir conteúdo de vídeo pelo nome do arquivo.** Um vídeo sem transcrição é uma lacuna declarada, não um conteúdo presumido. O acervo tem 142 vídeos e **zero** arquivos de transcrição ou legenda.
2. **Não converter popularidade, opinião ou marketing em fato técnico.** Contagem de estrelas, alegação de README e frase de divulgação são registradas como *alegação do autor*, nunca como *fato observado*.
3. **Não afirmar número não contado.** Toda contagem neste corpo de documentos foi produzida por varredura de ferramenta, não de memória.
4. **Descrição prévia não é validação.** O acervo chegou com catálogo próprio, escrito por terceiro. O estado `JÁ DESCRITO` registra a existência dessa descrição — não a sua veracidade.
5. **Divergência se expõe, não se resolve em silêncio.** Quando o catálogo e o sistema de arquivos discordam, ambos são registrados.

## 7. Separação de camadas de afirmação

Da Fase 2 em diante, toda afirmação recebe uma destas etiquetas. A Fase 0 usa apenas as duas primeiras:

| Camada | Definição | Usada na Fase 0 |
|---|---|---|
| Fato observado | Verificado diretamente no sistema de arquivos ou no conteúdo | sim |
| Alegação do autor | Afirmada por README, catálogo ou material de terceiro, sem verificação independente | sim |
| Inferência | Derivada por raciocínio a partir de fatos observados | não |
| Hipótese | Formulada para teste futuro | não |
| Candidato à avaliação | Possível aplicação ao LucaX, sujeita a avaliação oficial | não |

## 8. Estrutura de artefatos da frente

| Arquivo | Fase | Estado |
|---|---|---|
| `00_GOVERNANCA-DA-PESQUISA.md` | 0 | criado |
| `01_ESTADO-DA-ANALISE.md` | 0 | criado — atualizado continuamente |
| `02_MANIFESTO-DAS-FONTES.md` | 0 | criado |
| `03_RELATORIO-DO-INVENTARIO.md` | 0 | criado |
| `03_RUBRICA-DE-AVALIACAO.md` | 1 | não criado — fora do escopo desta fase |
| `04_FICHAS-DE-EVIDENCIA/` | 3 | não criado |
| `05_SINTESES-DAS-11-AREAS/` | 4 | não criado |
| `06_CATALOGO-DE-CANDIDATOS.md` | 4 | não criado |
| `07_CONFLITOS-E-LACUNAS.md` | 4 | não criado |
| `08_RELATORIO-DA-FASE.md` | 4 | não criado |

Nenhum artefato foi criado fora de `_SAIDA-COMPANY-OS/`.

## 9. Debate adiado

O debate **internalizar versus contratar como agência** não é conduzido nesta frente. Evidências úteis a ele são registradas quando aparecem, sem tomar lado e sem estruturar o argumento.

Registro da Fase 0 relevante ao debate futuro: dos 43 repositórios, **4 não possuem arquivo de licença na raiz efetiva** (`ai-orchestrator-starter`, `second-brain-skills-main`, `andrej-karpathy-skills-main`, `frontend-design-main`). Licença ausente é fato observado com consequência jurídica em qualquer cenário de internalização. Nenhuma conclusão é extraída disso aqui.

## 10. Condição de encerramento da frente

A Fase 0 não encerra a frente. A frente permanece aberta e **não normativa** até que os Frameworks oficiais 1.11–1.19 avaliem explicitamente cada candidato. Enquanto isso não ocorrer, nada aqui vincula o LucaX Enterprise OS.
