from connection import DatabaseConnection


def drop_tables(connection):
    try:
        cursor = connection.cursor()

        # Exclui a tabela Emprestimo
        cursor.execute('DROP TABLE IF EXISTS Emprestimo')

        # Exclui a tabela Livro
        cursor.execute('DROP TABLE IF EXISTS Livro')

        # Exclui a tabela Pessoa
        cursor.execute('DROP TABLE IF EXISTS Pessoa')

        connection.commit()

    except (Exception, Error) as e:
        print('Error while dropping tables', e)


if __name__ == '__main__':
    db = DatabaseConnection(
        user='postgres',
        password='Softex2023',
        host='localhost',
        port='5432',
        database='postgres'
    )
    db.connect()

    drop_tables(db.connection)

    db.close()
