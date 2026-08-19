import sqlite3


def cadastrar_um_livro():
    livro = input('Digite o nome do livro que deseja cadastrar: ').strip()
    autor = input('Digite o nome do autor do livro que está cadastrando: ').strip()
    try:
        ano = int(input('Digite o ano de publicação do livro que está sendo cadastrado: ').strip())
    except ValueError:
        print('Digite apenas números.')
        return

    conexao = sqlite3.connect('biblioteca.db')

    cursor = conexao.cursor()

    cursor.execute('''
    INSERT INTO livros (titulo, autor, ano, disponivel) 
    VALUES (?,?,?,?);
    ''',
    (livro,autor,ano,1)
    )

    conexao.commit() 

    cursor.execute('''
    SELECT * FROM livros WHERE titulo=?;
    ''',
    (livro,)
    )

    livro_cadastrado = cursor.fetchone()

    if livro_cadastrado:
        print(f'O livro {livro_cadastrado[1]}, do autor: {livro_cadastrado[2]}, ano: {livro_cadastrado[3]}, foi cadastrado com sucesso e agora está disponível.')

    conexao.close()

    return

def listar_livros():
    conexao = sqlite3.connect('biblioteca.db')

    cursor = conexao.cursor()

    cursor.execute('''
    SELECT * FROM livros; 
    ''')

    livros = cursor.fetchall()

    for livro in livros:
        if livro[4] == 1:
            status = 'disponível'
        else:
            status = 'emprestado'

        print(f'O livro: {livro[1]} está {status}.')
        print(f'Seu autor é {livro[2]} e seu ano de publicação é {livro[3]}.\n')

    conexao.close()

def buscar_livro():
    livro_busca = input('Digite o nome do livro que deseja buscar no sistema: ').strip()

    conexao = sqlite3.connect('biblioteca.db')

    cursor = conexao.cursor()

    cursor.execute('''
    SELECT * FROM livros WHERE titulo=?;
    ''',(livro_busca,)
    )

    livro = cursor.fetchone()

    if livro:
        print(f'O livro {livro[1]} está cadastrado no sistema.')

    else:
        print('O livro procurado não está cadastrado no sistema.')

    conexao.close()

def cadastrar_usuario():
    nome_usuario = input('Digite o nome do usuário que deseja cadastrar no sistema da biblioteca: ').strip()
    email = input('Digite o email que deseja cadastrar pelo usuário: ').strip()

    conexao = sqlite3.connect('biblioteca.db')
    cursor = conexao.cursor()

    cursor.execute('''
    SELECT * FROM usuarios WHERE email=?;
    ''', (email,)
    )

    usuarios = cursor.fetchone()

    if usuarios:
        print('Email já cadastrado no sistema.')
        conexao.close()
        return

    cursor.execute('''
    INSERT INTO usuarios (nome, email)
    VALUES (?,?);
    ''', (nome_usuario, email)
    )

    conexao.commit()

    cursor.execute('''
        SELECT * FROM usuarios WHERE email=?;
        ''', (email,)
        )

    usuario_cadastrado = cursor.fetchone()

    print(f'Usuário: {usuario_cadastrado[1]} cadastrado.')

    conexao.close()


def listar_usuarios_cadastrados():

    conexao = sqlite3.connect('biblioteca.db')

    cursor = conexao.cursor()

    cursor.execute('''
    SELECT * FROM usuarios;
    '''
    )

    usuarios = cursor.fetchall()

    if not usuarios:
        print('Nenhum usuário cadastrado no sistema.')
        return

    for usuario in usuarios:
        print(f'Usuário: {usuario[1]} cadastrado com o email: {usuario[2]}.')

    conexao.close()

def realizar_emprestimo():
    livro_emprestar = input('Digite o nome do livro que deseja pegar emprestado da biblioteca: ').strip()

    conexao = sqlite3.connect('biblioteca.db')

    cursor = conexao.cursor()

    cursor.execute('''
    SELECT * FROM livros WHERE titulo=?
    ''',(livro_emprestar,)
    )

    livro_emprestado = cursor.fetchone()

    if livro_emprestado:
        if livro_emprestado[4] == 1:
            cursor.execute('''
            UPDATE livros SET disponivel=? WHERE titulo=?;
            ''', (0, livro_emprestar)
            )

            print(f'Parabéns, seu empréstimo do livro: {livro_emprestado[1]} foi realizado.')
            conexao.commit()
            conexao.close()
        else:
            print(f'O livro: {livro_emprestado[1]} já está emprestado.')
            conexao.close()

    else:
        print('O livro procurado não está cadastrado nesta biblioteca.')
        conexao.close()

def listar_emprestimos():
    conexao = sqlite3.connect('biblioteca.db')

    cursor = conexao.cursor()

    cursor.execute('''
    SELECT * FROM livros WHERE disponivel =?; 
    ''', (0,)
    )

    emprestados = cursor.fetchall()

    if emprestados:
        for livro in emprestados:
            print(f'O livro {livro[1]} está emprestado no momento.')

        conexao.close()
    else: 
        print('Nenhum livro emprestado.')
        conexao.close()

def realizar_devolucao():
    livro_devolucao = input('Digite o nome do livro que deseja remover: ').strip()

    conexao = sqlite3.connect('biblioteca.db')

    cursor = conexao.cursor()

    cursor.execute('''
    SELECT * FROM livros WHERE titulo=?;
    ''', (livro_devolucao,)
    )

    livro = cursor.fetchone()

    if livro:

        if livro[4] == 0:
            cursor.execute('''
            UPDATE livros SET disponivel = ? WHERE titulo=?;
            ''', (1, livro_devolucao)
            )

            conexao.commit()

            print(f'Livro: {livro_devolucao} devolvido com sucesso.')

            conexao.close()

        else:
            print('O livro em questão não está emprestado.')
            conexao.close()

    else:
        print('O livro em questão não está cadastrado no sistema.')
        conexao.close()


def encerrar_programa():
    print('Encerrando o programa.')

def menu():
    while True:
        print('==== MENU DO SISTEMA DA BIBLIOTECA ====\n')
        print('1. Cadastrar um livro no sistema')
        print('2. Listar livros cadastrados no sistema.')
        print('3. Buscar livro')
        print('4. Cadastrar usuário no sistema da biblioteca')
        print('5. Listar usuários cadastrados no sistema')
        print('6. Realizar empréstimo de um livro')
        print('7. Listar empréstimos')
        print('8. Realizar devolução')
        print('9. Encerrar')
        try:
            opcao = int(input('Digite o número da opção que deseja selecionar: ').strip())
        except ValueError:
            print('Digite apenas o número de uma das opções disponíveis.')
            continue
        if opcao == 1:
            cadastrar_um_livro()
        elif opcao == 2:
            listar_livros()
        elif opcao == 3:
            buscar_livro()
        elif opcao == 4:
            cadastrar_usuario()
        elif opcao == 5:
            listar_usuarios_cadastrados()
        elif opcao == 6:
            realizar_emprestimo()
        elif opcao == 7:
            listar_emprestimos()
        elif opcao == 8:
            realizar_devolucao()
        elif opcao ==9:
            encerrar_programa()
            break
        else:
            print('Opção inexistente. Digite apenas um número entre as opções apresentadas.')

menu()