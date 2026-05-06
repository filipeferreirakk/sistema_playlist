# Sistema de Playlist

Projeto desenvolvido para a disciplina de Estrutura de Dados — Fatec Rio Claro.

## Descrição

Sistema de gerenciamento de músicas via terminal. Permite cadastrar uma biblioteca pessoal de faixas, organizá-las em filas de reprodução por humor com base no BPM e acompanhar o histórico de reproduções.

As estruturas de dados foram implementadas do zero, sem uso de `list`, `deque` ou qualquer estrutura embutida do Python para a lista encadeada e as filas.

## Estruturas utilizadas

- **Lista encadeada simples** — armazena a biblioteca de músicas
- **Fila FIFO encadeada** — usada nas quatro filas de humor e no histórico

## Funcionalidades

1. Adicionar música à biblioteca
2. Remover música pelo ID
3. Buscar música por ID ou título
4. Listar biblioteca completa
5. Montar filas de reprodução por humor (baseado no BPM)
6. Reproduzir próxima música de uma fila
7. Exibir músicas de uma fila sem removê-las
8. Exibir histórico de reproduções
9. Estatísticas gerais
10. Sair

## Classificação por BPM

| Fila    | Humor        | BPM         |
|---------|--------------|-------------|
| Relaxar | tranquilo    | até 80      |
| Focar   | concentração | 81 a 120    |
| Animar  | agitado      | 121 a 160   |
| Treinar | intenso      | acima de 160|

## Como executar

Requer apenas Python 3. Sem dependências externas.

```bash
python main.py
```

## Estrutura do projeto

```
.
├── main.py
└── README.md
```
