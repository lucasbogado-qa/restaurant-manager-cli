# 🍽️ Restaurant Manager CLI

Sistema de linha de comando (CLI) para cadastro e gerenciamento de restaurantes, desenvolvido em Python puro como projeto de estudo de lógica de programação e backend.

```
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
```

## 📋 Sobre o projeto

O **Restaurant Manager CLI** é um sistema interativo via terminal que permite cadastrar, listar e alternar o status (ativo/inativo) de restaurantes. Foi desenvolvido como projeto de estudo, com foco em:

- Estruturação de código em funções com responsabilidade única
- Manipulação de listas e dicionários como estrutura de dados em memória
- Tratamento de exceções (`try/except`)
- Fluxo de navegação em menu interativo (CLI)

> Este é um projeto **em memória**: os dados não são persistidos em banco de dados ou arquivo. Ao encerrar o programa, as informações cadastradas são perdidas (exceto os restaurantes pré-carregados no código).

## ✨ Funcionalidades

- ✅ Cadastrar novo restaurante (nome + categoria)
- ✅ Listar todos os restaurantes cadastrados, com nome, categoria e status
- ✅ Alternar o status de um restaurante entre **ativado** e **desativado**
- ✅ Tratamento de opções inválidas e entradas incorretas
- ✅ Menu interativo que retorna automaticamente após cada ação

## 🛠️ Tecnologias

- **Python 3** (biblioteca padrão apenas — sem dependências externas)
- Módulo `os` para limpar o terminal entre as telas

## 📁 Estrutura do projeto

```
restaurant-manager-cli/
├── app.py          # Código principal da aplicação
└── README.md       # Este arquivo
```

## 🚀 Como executar

### Pré-requisitos

- Python 3.6 ou superior instalado ([python.org](https://www.python.org/downloads/))

### Passo a passo

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/restaurant-manager-cli.git
   cd restaurant-manager-cli
   ```

2. Execute o programa:
   ```bash
   python app.py
   ```
   ou, dependendo do seu sistema:
   ```bash
   python3 app.py
   ```

3. Navegue pelo menu digitando o número da opção desejada e pressionando Enter.

## 🎮 Como usar

Ao iniciar, o sistema exibe o menu principal:

```
1. Cadastrar restaurante
2. Listar restaurantes
3. Alternar estado do restaurante
4. Sair
```

- **Opção 1** — solicita nome e categoria do novo restaurante e o adiciona à lista, já cadastrado como **desativado**.
- **Opção 2** — exibe todos os restaurantes cadastrados em formato de tabela, com nome, categoria e status atual.
- **Opção 3** — solicita o nome de um restaurante existente e alterna seu status (de ativado para desativado, ou vice-versa).
- **Opção 4** — encerra a aplicação.

Após cada ação, o programa aguarda uma tecla para retornar ao menu principal.

## 🗂️ Dados de exemplo

O sistema já inicia com três restaurantes pré-cadastrados para facilitar os testes:

| Nome | Categoria | Status |
|---|---|---|
| Praça | Japonesa | Desativado |
| Pizza Suprema | Pizza | Ativado |
| Cantina | Italiano | Desativado |

## 🧭 Possíveis evoluções futuras

- [ ] Persistência de dados em arquivo (JSON) ou banco de dados (SQLite)
- [ ] Validação de nome de restaurante duplicado no cadastro
- [ ] Opção de remover restaurante
- [ ] Busca de restaurante por categoria
- [ ] Migração para uma API REST (Flask ou FastAPI)
- [ ] Testes automatizados (pytest)

## 👤 Autor

Desenvolvido por **Lucas Bogado** como parte dos estudos em backend com Python.

[LinkedIn](https://www.linkedin.com/in/lucas-bogado-182245245/)

## 📄 Licença

Este projeto está sob a licença MIT — sinta-se livre para usar, estudar e modificar.
