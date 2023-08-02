from connection import DatabaseConnection
from livro import Livro
from pessoa import Pessoa


def create_tables(connection):
    try:
        cursor = connection.cursor()

        # Criação da tabela Livro
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Livro (
                ID SERIAL PRIMARY KEY,
                Titulo VARCHAR(100) NOT NULL,
                Altura NUMERIC NOT NULL,
                Largura NUMERIC NOT NULL
            )
        ''')

        # Criação da tabela Pessoa
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Pessoa (
                CPF VARCHAR(14) PRIMARY KEY,
                Nome VARCHAR(100) NOT NULL,
                Rua VARCHAR(100) NOT NULL,
                Numero INTEGER NOT NULL,
                Apartamento VARCHAR(10)
            )
        ''')

        # Criação da tabela Emprestimo
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Emprestimo (
                Data DATE NOT NULL,
                Livro_ID INTEGER REFERENCES Livro(ID),
                Pessoa_CPF VARCHAR(14) REFERENCES Pessoa(CPF),
                PRIMARY KEY (Data, Livro_ID, Pessoa_CPF)
            )
        ''')

        connection.commit()

    except (Exception, Error) as e:
        print('Error while creating tables', e)


def populate_tables(connection):
    try:
        cursor = connection.cursor()

        # Populando a tabela Livro
        cursor.execute('''
            INSERT INTO Livro (Titulo, Altura, Largura)
            VALUES ('Livro A', 20, 15),
                   ('Livro B', 18, 12),
                   ('Livro C', 25, 20)
        ''')

        # Populando a tabela Pessoa
        cursor.execute('''
            INSERT INTO Pessoa (CPF, Nome, Rua, Numero, Apartamento)
            VALUES ('111.111.111-11', 'João da Silva', 'Rua das Flores', 123, '15A'),
                   ('222.222.222-22', 'Maria Souza', 'Av. Principal', 456, '22B')
        ''')

        # Populando a tabela Emprestimo
        cursor.execute('''
            INSERT INTO Emprestimo (Data, Livro_ID, Pessoa_CPF)
            VALUES ('2023-07-30', 1, '111.111.111-11'),
                   ('2023-07-31', 2, '222.222.222-22')
        ''')

        connection.commit()

    except (Exception, Error) as e:
        print('Error while populating tables', e)


if __name__ == '__main__':
    db = DatabaseConnection(
        user='postgres',
        password='Softex2023',
        host='localhost',
        port='5432',
        database='postgres'
    )
    db.connect()

    create_tables(db.connection)
    populate_tables(db.connection)

    db.close()
