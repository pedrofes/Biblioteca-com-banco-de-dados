# Sistema de Biblioteca com SQLite

## Sobre o projeto

O projeto em questão é um sistema de biblioteca baseado em Python e SQLite. O sistema em questão foi desenvolvido como parte de um esquema de estudos para integração de Python com Banco de Dados. Neste sistema, usuários podem cadastrar livros, visualizar livros cadastrados, cadastrar usuários, listar usuários cadastrados, realizar empréstimos de livros, realizar devoluções e listar livros emprestados.

## Funcionalidades

- Cadastrar livro
- Listar livros cadastrados
- Buscar livro entre os títulos cadastrados
- Cadastrar usuário
- Listar usuários cadastrados
- Realizar empréstimo de um livro
- Listar os livros emprestados, segundo o sistema
- Realizar a devolução de um livro emprestado
- Encerrar o programa

## Tecnologias utilizadas

- Python
- SQLite

## Conceitos praticados

- Integração entre Python e SQLite
- Criação e manipulação de banco de dados
- Operações SQL com `SELECT`, `INSERT` e `UPDATE`
- Consultas parametrizadas
- Uso de `fetchone()` e `fetchall()`
- Persistência e gerenciamento de dados
- Validação de entradas e tratamento de erros em Python

## Estrutura do banco de dados

Tabelas do banco de dados estruturadas da seguinte forma (base dos comandos SQL):

TABLE livros(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER,
    disponivel INTEGER)

TABLE usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE)

### Tabela `livros`

A tabela 'livros' registra dados sobre todos os títulos listados no sistema. Estes incluem:

- Código único de cada livro cadastrado, gerado pelo próprio sistema
- Nome da obra (título)
- Autor da obra
- Ano de publicação
- Status do título no sistema, disponível para empréstimo ou não

### Tabela `usuarios`

A tabela usuário registra dados referentes aos usuários cadastrados no sistema da biblioteca. São estes os dados em questão:

- Nome do usuário
- E-mail do usuário, que deve ser único

## Como executar

É necessário contar com Python instalado no computador.

Baixe o projeto e primeiro execute o arquivo criarbanco.py para a criação do banco de dados que será utilizado. Em seguida, rode o programa biblioteca.py.

O sistema conta com execução simples. O usuário deve apenas selecionar uma das opções disponibilizadas através das opções numéricas que vão de 1 a 9.

## Status do projeto

Projeto finalizado. Tempo de desenvolvimento: 2 dias.

## Autor

Pedro Fonseca Esperidião Silva