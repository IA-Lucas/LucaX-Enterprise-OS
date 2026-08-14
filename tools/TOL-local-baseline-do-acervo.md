---
id: TOL-local-baseline-do-acervo
titulo: Baseline canônica do acervo — reprodução read-only por lista fechada positiva
tipo: ferramenta
versao: 1.1.0
status: ativo
camada_memoria: tecnica
autor: DEP-TLS
proprietario: DEP-TLS
aprovador: DEP-EXE
criado_em: 2026-08-14
atualizado_em: 2026-08-14
revisao_prevista: 2027-02-14
decisoes_relacionadas: [ADR-0041, ADR-0044, MSG-2026-0015]
substitui: []
substituido_por: null
resumo: Mede artefatos, linhas e impressão digital do acervo por lista fechada positiva, recusando raiz não declarada, sem escrever nada.
perfil_contexto: sob-demanda
confidencialidade: interno
revisor: DEP-QAR
ratificacao: ratificada
capabilities: [CAP-governanca]
classe: local
dado_trafegado: nenhum
custo: zero — medido, não estimado (ver §12)
criticidade: média
---

# Baseline canônica do acervo (`TOL-local-baseline-do-acervo`)

## Propósito
Reproduzir a contagem de artefatos, a contagem de linhas e a impressão digital do acervo
da Mente, por lista fechada positiva, para que qualquer sessão possa conferir — antes e
depois de escrever — que o estado medido bate com o estado declarado no lease de escrita.

## Escopo
| Item | Definição |
|---|---|
| Usos autorizados | Medir o acervo da Mente antes de adquirir um lease de escrita (`estado_fenceado`); medir depois de escrever, na pós-verificação; conferir reprodutibilidade sobre cópia datada, para prova de inércia ao emendar o próprio instrumento |
| Usos **não** autorizados | Medir qualquer árvore fora do acervo da Mente como se fosse a baseline canônica; usar o resultado como prova de integridade byte a byte (a impressão cobre conteúdo dos artefatos listados, não detecta edição fora da lista — ver §6); invocar em automação sem revisão humana do `EXIT` code |
| Quem pode usar | Qualquer Departamento — a capacidade não pertence a agente algum, mesmo princípio de `SK-02` |

## Responsáveis
| Papel | Quem |
|---|---|
| Proprietário | `DEP-TLS` |
| Avaliação de risco | `DEP-QAR` |
| Aprovador | `DEP-EXE` |

## 1. Finalidade
Antes desta ficha, o instrumento (`_sincronizacao-2026-08-10/ferramentas/baseline.sh`)
já era invocado repetidamente em toda escrita sob lease da Mente — sete gerações
(`IR-BL/1` a `IR-BL/7`), citado em mais de vinte tokens de lease — mas nunca tinha ficha
própria de Ferramenta: vivia só como script e como prosa no `CLAUDE.md` e no catálogo
mestre. Esta ficha registra a capacidade formalmente, sem mover o script nem alterar seu
comportamento.

## 2. Alternativas avaliadas
| Alternativa | Por que não foi escolhida |
|---|---|
| Não usar ferramenta alguma — conferir "de olho" | É exatamente o defeito que `RD-53`/`RD-81` mediram repetidas vezes: leitura sem instrumento erra contagem e não detecta drift de conteúdo |
| Mover o script para dentro do acervo (`governance/`) | O próprio instrumento se mediria, o que o tornaria autorreferente — [[baseline-medicao-autorreferente]]. Vive fora **deliberadamente** (§2 do catálogo mestre: *"script dentro da raiz seria invisível à medição que ele executa"*) |
| Adotar ferramenta de terceiro (ex.: hash de diretório de mercado) | Nenhuma candidata avaliada reproduz o portão de raiz por lista fechada positiva nem a distinção `ACERVO`/`NAO_ACERVO` — teria de ser envolvida por script equivalente de qualquer forma |

## 3. Capabilities habilitadas
| Capability | Como esta ferramenta habilita |
|---|---|
| [`CAP-governanca`](../capabilities/CAP-governanca.md) — `ativo`, custódio `DEP-GOV` | É o instrumento de medição que sustenta o protocolo de lease de escrita da Mente (`CLAUDE.md` §LEASE): sem ele, `estado_fenceado` não é medível e a aquisição de lease não tem base |

## 4. Dado que trafega
| Tipo de dado | Sensibilidade | Sai do ambiente do Soberano? | Autorização correspondente |
|---|---|---|---|
| Caminho e conteúdo de arquivos `.md` do acervo da Mente | `interno` (a árvore governada, não dado pessoal) | Não — execução 100% local, `stdlib`/`coreutils` (`sh`, `find`, `wc`, `sha256sum`, `sort`, `xargs`), sem rede | Não se aplica — não há exposição a terceiro |

> Envio de dado a serviço externo é ato de exposição e exigiria autorização específica
> (`EX-03`, `LV-08`). **Não ocorre aqui**: `0` chamadas de rede no script.

## 5. Autorização de exposição
Não aplicável — este instrumento não envia dado a Ferramenta externa nem a terceiro. Sua
única saída são quatro linhas de texto (`artefatos`, `linhas`, `manifesto`, `impressão
digital`) impressas em `stdout` para quem o invocou.

## 6. Acesso e segredo
| Campo | Conteúdo |
|---|---|
| Nome da variável de ambiente | Não aplicável — não usa credencial alguma |
| Onde a credencial é guardada | Não aplicável |
| Quem pode rotacionar | Não aplicável |

> Nenhuma credencial jamais aparece nesta ficha nem é usada pelo instrumento (`PI-08`,
> `LV-02`).

## 7. Isolamento e sandbox
| Eixo | Alcance declarado |
|---|---|
| Leitura | A árvore inteira do caminho passado como argumento (`$1`), restrita aos diretórios listados em `ACERVO`/`NAO_ACERVO` — arquivos fora dessas listas **recusam a medição inteira** (portão de raiz), nunca são lidos parcialmente |
| Escrita | **Nenhuma.** `set -e`, sem redirecionamento a arquivo, sem `mv`/`cp`/`rm`. Declarado no próprio cabeçalho: *"Não escreve nada. Read-only"* |
| Execução | Só os binários POSIX que invoca (`find`, `wc`, `xargs`, `sha256sum`, `sort`) sobre a lista de artefatos já resolvida — não invoca interpretador de conteúdo dos arquivos (não executa `.md` como código) |

> `TF-18` declara que eixo não declarado conta como irrestrito — aqui os três estão
> declarados, e o eixo de escrita é declarado **vazio por desenho**, não por omissão.

## 8. Custo
| Campo | Conteúdo |
|---|---|
| Modelo de cobrança | Nenhum — execução local, sem provedor pago envolvido |
| Custo recorrente | Zero, medido: tempo de CPU/IO local da máquina que invoca (não medido em unidade monetária porque não há) |
| Limite definido | Nenhum limite externo; o único limite é o portão de split (`§ código`), que recusa se `wc -l` fragmentar a chamada em mais de um lote — proteção estrutural, não teto de uso |
| Quem monitora | `DEP-EXE` (função Recursos), por convenção do template — não há custo recorrente a monitorar hoje |

## 9. Dependência e risco
| Campo | Conteúdo |
|---|---|
| Criticidade | **Média.** Não crítica no sentido de causar dano se cair — o modo de falha é **recusar medir** (fail-closed), nunca medir errado em silêncio. É média porque, sem ela, nenhuma sessão consegue declarar `estado_fenceado` de um lease com prova — o protocolo de escrita da Mente inteiro depende dela |
| O que quebra se a ferramenta cair | Nenhuma escrita sob lease pode ser corretamente instrumentada; sessões teriam de declarar `estado_fenceado` sem medição, violando o próprio protocolo de lease do `CLAUDE.md` |
| Plano de contingência | Reconstituir de cópia datada anterior (o script fica versionado por comentário de geração, `IR-BL/1` a `IR-BL/7`, dentro do próprio arquivo) |
| Lock-in criado | Nenhum — `sh` POSIX puro, sem dependência de provedor; portável para qualquer máquina com `coreutils` |

## 10. Comportamento em falha
| Natureza | Como se manifesta | Como se detecta |
|---|---|---|
| Indisponível | Caminho inexistente ou sem permissão de leitura | Erro do shell, `EXIT` não-zero, mensagem do sistema de arquivos |
| Lenta além do limite | Não observado — árvore medida (299 artefatos) resolve em menos de 1s | Não aplicável hoje; se a árvore crescer muito, seria observável por tempo de parede |
| Resposta inválida | Lista de hashes com contagem diferente da lista de artefatos | **Portão de cobertura** (linha do código): recusa com `EXIT=5` nomeando a divergência, nunca deixa passar impressão parcial |
| **Resposta plausível e errada** *(a que se esquece — `TF-28` exige declarar)* | O instrumento mediria um conjunto diferente do que a lista `ACERVO`/`NAO_ACERVO` realmente declara, produzindo número "válido" mas errado | **Detectado por `TESTE`** (`SF-14`): as quatro provas de inércia executadas a cada nova geração (`IR-BL/4` a `IR-BL/7`) — árvore sem a entrada nova reproduz o valor da geração anterior; árvore com a entrada nova move o valor pelo conteúdo real; entrada não declarada continua recusando; desfeita a linha, a recusa volta. **Medido em `IR-BL/7`: 4 de 4 provas passaram antes do uso** |

## 11. Observabilidade
| Campo | Conteúdo |
|---|---|
| O que se registra | As quatro linhas de saída (`artefatos`, `linhas`, `manifesto`, `impressão digital`) e o `EXIT` code — nada além disso é emitido pelo próprio instrumento |
| Onde | `stdout`/`stderr` da invocação; a sessão que invoca transcreve o resultado no lease (`estado_fenceado`/`estado_no_fechamento`) como registro persistente |
| Por quanto tempo | O instrumento não retém nada; a persistência é do **lease** (`_leases/LucaX-Enterprise-OS.lease`), fora do escopo desta ficha |
| Quem lê | Quem adquire ou libera lease de escrita na Mente, e qualquer sessão que retome uma missão em curso (`WFL-GOV-migracao-por-ondas-do-legado.md` §16, Retomada) |

> Nenhum dado `sensivel` passa pelo registro — as quatro linhas são contagens e hashes de
> conteúdo público do acervo, nunca segredo.

## 12. Limites de uso
| Limite | Valor | Consequência de ultrapassar |
|---|---|---|
| Portão de split | Exatamente uma linha `total` na saída de `wc -l` | `EXIT=4` — a baseline não é medida; evita soma parcial se `xargs` fragmentar a chamada |
| Portão de cobertura | Número de hashes obtidos == número de artefatos listados | `EXIT=5` — a baseline não é medida; evita impressão digital sobre conjunto incompleto |
| Portão de raiz | Toda entrada de topo do acervo precisa estar em `ACERVO` ou `NAO_ACERVO` | `EXIT=2` — a baseline não é medida; é o portão que motivou `IR-BL/7` a acrescentar `workflows` |

## 13. Critério de descarte
| Condição | Sinal observável | Substituto previsto |
|---|---|---|
| O versionador (`git`) passar a ser ponto de retorno confiável o bastante para dispensar hash de conteúdo próprio | Nenhum sinal observado até hoje — `git` já é usado para `HEAD`/commits no lease, mas a impressão digital de conteúdo (`IR-BL/4`+) continua sendo o que detecta edição que preserva contagem de linha | `git` puro, com `.gitattributes` como fonte de verdade |
| Um instrumento equivalente, mais barato de manter, entrar em operação | Nenhum candidato avaliado (§2) cobre a mesma lista fechada positiva hoje | Esse instrumento, se e quando existir |
| **Se nenhum substituto existir** | — | A organização deixa de ter medição instrumentada do acervo, e isso é **decisão**, não omissão |

## 14. Avaliação `PI-11`
| Campo | Conteúdo |
|---|---|
| Por que esta é a melhor opção **para a tarefa** | A tarefa é medir reprodutibilidade de um acervo versionado em Markdown por lista fechada positiva com portão de raiz — nenhuma ferramenta de mercado avaliada faz exatamente isso sem envolvimento equivalente |
| Custo declarado como restrição | Zero — não é critério de escolha, é constatação (`TF-21`: proibido estimar; aqui não há o que estimar) |
| Qualidade que se ganha em relação à alternativa | Reprodutibilidade byte a byte da lista declarada, com quatro portões distintos (raiz, split, cobertura) que falham fechado — contra a alternativa de conferência manual, que já errou contagem múltiplas vezes na história do acervo (família `RD-32`) |

## 15. Autorização por consumidor
| Consumidor | Uso autorizado | Nível de dado |
|---|---|---|
| `DEP-GOV` | Medir `estado_fenceado`/`estado_no_fechamento` em toda aquisição e liberação de lease de escrita na Mente | `interno` |
| Qualquer Departamento que adquira lease de escrita na Mente (`CLAUDE.md` §LEASE) | Mesmo uso acima, por papel — não por identidade | `interno` |

> `TF-30`: autorização não se herda por composição. Uma `SKL`/`WFL` que invoque este
> instrumento como parte de sua própria etapa (ex.: `WFL-GOV-migracao-por-ondas-do-legado.md`
> §16) precisa estar ela mesma autorizada a operar sob lease — o consumidor aqui é o papel
> que adquire o lease, nunca "todos os Workflows".

## 16. Rastreabilidade
| Campo | Conteúdo |
|---|---|
| ADR de adoção | [`ADR-0044`](../decisions/ADR-0044-adocao-da-baseline-como-ferramenta.md) — `ativo` · `ratificada` |
| Ratificação do Soberano (data) | **2026-08-14** — [`MSG-2026-0015`](../memory/operacional/MSG-2026-0015-ato-soberano-ratificacao-adr-0044.md), *"Ratifico o ADR-0044 em 2026-08-14"* |
| Revisão prevista | `2027-02-14`, ou na primeira falha *plausível e errada* observada (`L4` de `ADR-0041`), o que ocorrer primeiro |

## 17. Não-proliferação (`FND-04 §6.1`), respondida por escrito
1. **Já existe em outra forma?** Sim, como script — mas nunca como Ferramenta registrada
   (`TOL`); o script já era invocado repetidamente sem ficha, e é exatamente essa lacuna
   que esta ficha fecha, sem mover ou reescrever o script.
2. **Cabe em componente existente sem distorcê-lo?** Não: por `TF-01`/`TF-02`, capacidade
   externa ao sistema que o procedimento *chama* é `TOL`, nunca `SKL`/`WFL` — descrevê-la
   como procedimento seria invadir a fronteira que `TF-02` proíbe.
3. **Qual ganho de `PI-14`, com sinal já observado?** Formalizar sob autoridade derivada
   (`TF-10`) um instrumento já citado em mais de vinte tokens de lease e em sete gerações
   (`IR-BL/1` a `IR-BL/7`) — sinal observado, não previsto.
4. **Como se vai saber que deixou de ser necessário?** Ver §13 (Critério de descarte).

## Histórico
| Versão | Data | Autor | Mudança |
|---|---|---|---|
| 1.0.0 | 2026-08-14 | DEP-TLS | Criação — primeira Ferramenta registrada do acervo. `status: rascunho`, `ratificacao: pendente`: a proposta existe, a adoção aguarda ato do Soberano (`TF-10`). `0` bytes do script alterados; a ficha registra a capacidade, não move nem reescreve o instrumento. |
| 1.1.0 | 2026-08-14 | DEP-GOV | **RATIFICADA** — `ADR-0044` → `MSG-2026-0015`, *"Ratifico o ADR-0044 em 2026-08-14"*. `status: ativo`, `ratificacao: ratificada`. Primeira Ferramenta vigente do acervo. `0` bytes do script alterados. |
