import sqlite3
from sqlite3 import Error

def executar_comando_bd(conn, comando):
    try:
        c = conn.cursor()
        c.execute(comando)
    except Error as e:
        print(e)

def criar_conexao(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Conexao com banco de dados criada com sucesso!")
    except Error as e:
        print(e)
    return conn

def criar_tabelas():
    sql_criar_tabela_livros = """ CREATE TABLE IF NOT EXISTS livros (
                                        id integer PRIMARY KEY,
                                        nome text NOT NULL,
                                        descricao text
                                    ); """

    sql_criar_tabela_usuarios = """CREATE TABLE IF NOT EXISTS usuarios (
                                    id integer PRIMARY KEY,
                                    login text NOT NULL,
                                    senha text NOT NULL,
                                    permissoes integer
                                );"""
    
    executar_comando_bd(sql_criar_tabela_livros)
    print("Tabela de livros carregada com sucesso!")
    executar_comando_bd(sql_criar_tabela_usuarios)
    print("Tabela de usuarios carregada com sucesso!")

if __name__ == '__main__':
    criar_conexao("/home/heitor/Desktop/pythonsqlite.db")
    criar_tabelas()