import sqlite3

# Conecta ao banco de dados
conexao = sqlite3.connect('biblioteca.db')

cursor = conexao.cursor()

# Criação da tabela de livros
cursor.execute('''
CREATE TABLE livros(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER,
    disponivel INTEGER
);
''')

# Criação da tabela de usuários
cursor.execute('''
CREATE TABLE usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);
''')

# Cadastro dos livros iniciais
cursor.execute(
'''
INSERT INTO livros (titulo, autor, ano, disponivel)
VALUES (?,?,?,?);
''',
('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954, 1)
)

cursor.execute(
'''
INSERT INTO livros (titulo, autor, ano, disponivel)
VALUES (?,?,?,?);
''',
('1984', 'George Orwell', 1949, 1)
)

cursor.execute(
'''
INSERT INTO livros (titulo, autor, ano, disponivel)
VALUES (?,?,?,?);
''',
('O Iluminado', 'Stephen King', 1977, 0)
)

# Salva as alterações no banco
conexao.commit()

# Fecha a conexão
conexao.close()
