> EVIDÊNCIA EXTERNA
> PROVISÓRIO
> NÃO NORMATIVO
> CANDIDATO À AVALIAÇÃO

> **RETIRADO COMO CONCLUSÃO:** este artefato excedeu o adiamento definido em `00_GOVERNANCA-DA-PESQUISA.md §9`. Não usar sua recomendação. O registro neutro autorizado está em `125_REGISTRO-DE-CRITERIOS-PARA-DEBATE-FUTURO.md`.

# Debate provisório — núcleo próprio versus frameworks externos

**Momento de decisão:** somente após a conclusão e aplicação dos Frameworks oficiais 1.11–1.19  
**Estado:** questão aberta; nenhuma escolha arquitetural é feita aqui

## A pergunta correta

Não é “colocar tudo dentro” versus “terceirizar tudo”. Para cada capacidade, decidir entre:

1. **núcleo canônico** — responsabilidade essencial e estável;
2. **serviço interno isolado** — propriedade da empresa, mas fora do núcleo;
3. **framework externo encapsulado** — especialista substituível chamado por contrato;
4. **uso humano assistido** — ferramenta sem integração autônoma;
5. **rejeitar/postergar** — valor ou segurança insuficiente.

## Modelo “agências especializadas” — frameworks fora

### Vantagens potenciais

- substituição e atualização mais fáceis;
- falha e privilégio contidos;
- núcleo menor e contexto mais barato;
- especialistas evoluem independentemente;
- teste A/B entre fornecedores;
- menor acoplamento a uma moda ou linguagem.

### Custos e riscos

- integração, latência e observabilidade distribuídas;
- versões, licenças e supply chain multiplicadas;
- semântica e memória podem fragmentar;
- contratos de interface tornam-se parte crítica;
- dados atravessam mais fronteiras;
- dependência de fornecedor e indisponibilidade externa;
- debugging ponta a ponta fica mais difícil.

## Modelo “multinacional dentro da máquina” — tudo internalizado

### Vantagens potenciais

- identidade, dados, logs e políticas unificados;
- chamadas locais e menor dependência externa;
- contexto compartilhado quando realmente necessário;
- maior controle sobre experiência e evolução;
- conhecimento crítico permanece interno.

### Custos e riscos

- acoplamento, bloat e contexto permanente;
- concentração de credenciais e blast radius;
- manutenção de capacidades commodity;
- atualizações coordenadas e mais lentas;
- uma falha de governança pode atingir todos os setores;
- confusão entre capacidade disponível e capacidade autorizada.

## Critérios de colocação

| Critério | Puxa para dentro | Puxa para fora/isolado |
|---|---|---|
| Diferenciação estratégica | É parte do valor único do produto | É commodity ou facilmente substituível |
| Sensibilidade dos dados | Exige controle direto e residência definida | Pode operar com dados mínimos/sintéticos |
| Autoridade/efeito | Transação central, governada e auditável | Trabalho episódico, reversível ou somente leitura |
| Frequência/latência | Uso contínuo e baixa latência | Uso raro ou assíncrono |
| Estabilidade | Domínio estável e bem compreendido | Tecnologia volátil e especializada |
| Acoplamento | Muitos consumidores internos e semântica central | Interface estreita e contrato claro |
| Competência interna | Conhecimento deve compor patrimônio | Especialidade cara e não diferenciadora |
| Reversibilidade | Migração aceitável e plano de saída | Fácil trocar, desligar ou comparar |
| Evidência operacional | Evals, logs e suporte maduros | Ainda experimental; manter sandbox |

## Hipótese a testar — não decisão

O padrão mais consistente do acervo favorece uma **federação governada**:

- um núcleo pequeno cuidaria de identidade, autorização, política, evidência, auditoria, catálogo de capacidades, roteamento e portas de aprovação;
- capacidades especializadas permaneceriam isoladas, substituíveis e chamadas por contratos;
- dados, memória e efeitos seriam concedidos por tarefa, não herdados globalmente;
- frameworks externos nunca receberiam credibilidade por popularidade, repetição ou “open source”.

Esta hipótese precisa ser comparada com os Frameworks oficiais. Não deve ser convertida em diagrama, ADR, organograma, Spec ou implementação nesta fase.

## Perguntas para o debate oficial

1. Que capacidades constituem propriedade intelectual do LucaX?
2. Quais dados jamais podem sair do perímetro controlado?
3. Qual autoridade máxima cada capacidade pode receber?
4. Que falhas precisam ficar isoladas?
5. Qual latência e disponibilidade são realmente necessárias?
6. Como trocar um fornecedor sem perder memória, evidência ou histórico?
7. Quem mantém, testa, atualiza e desliga cada capacidade?
8. Qual é o custo total: licença + tokens + integração + observabilidade + incidentes + migração?
9. Qual teste prova que internalizar é melhor que encapsular — ou vice-versa?
10. Qual capacidade pode continuar sendo ferramenta humana, sem virar agente?

## Forma segura de decidir depois

Para cada capacidade, produzir uma ficha comparativa com opções internas/externas, dados acessados, autoridade, SLA, custo, risco, licença, manutenção, plano de saída e experimento reversível. Só então promover uma colocação por decisão oficial.

O acervo informa o LucaX Enterprise OS, mas não determina sua arquitetura.
