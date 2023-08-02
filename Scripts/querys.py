from connection import DatabaseConnection


def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    except (Exception, Error) as e:
        print('Error while executing query', e)


if __name__ == '__main__':
    db = DatabaseConnection(
        user='postgres',
        password='Softex2023',
        host='localhost',
        port='5432',
        database='postgres'
    )
    db.connect()

    # Consultas
    query1 = 'SELECT COUNT(*) AS total_livros FROM Livro;'
    query2 = '''
        SELECT p.Nome AS pessoa_nome, l.Titulo AS livro_titulo
        FROM Emprestimo e
        JOIN Pessoa p ON e.Pessoa_CPF = p.CPF
        JOIN Livro l ON e.Livro_ID = l.ID;
    '''
    query3 = '''
        SELECT l.Titulo AS livro_titulo, p.Nome AS pessoa_nome, p.Rua AS rua, p.Numero AS numero, p.Apartamento AS apartamento
        FROM Emprestimo e
        JOIN Pessoa p ON e.Pessoa_CPF = p.CPF
        JOIN Livro l ON e.Livro_ID = l.ID
        WHERE l.Titulo = 'Livro A';
    '''

    result1 = execute_query(db.connection, query1)
    result2 = execute_query(db.connection, query2)
    result3 = execute_query(db.connection, query3)

    print('Quantidade total de livros:', result1[0][0])

    print('\nPessoas que pegaram livros:')
    for row in result2:
        print('Pessoa:', row[0], 'Livro:', row[1])

    print('\nLocalização do Livro A:')
    for row in result3:
        print('Livro:', row[0], 'Pessoa:', row[1], 'Endereço:', row[2], row[3], row[4])

    db.close()
