import sqlite3
from sqlite3 import Error

def executar_comando_bd(conn, comando):
    try:
        c = conn.cursor()
        c.execute(comando)
    except Error as e:
        print(e)

def criar_conexao(caminho):
    conn = None
    try:
        conn = sqlite3.connect(caminho)
        print("Conexao com banco de dados criada com sucesso!")
    except Error as e:
        print(e)
    return conn

def criar_tabelas(conn):
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
    
    sql_criar_tabela_multas = """CREATE TABLE IF NOT EXISTS multas (
                                    id integer PRIMARY KEY,
                                    id_usuario integer,
                                    valor float NOT NULL,
                                    status text NOT NULL,
                                    FOREIGN KEY (id_usuario)
                                        REFERENCES usuarios (id) 
                                );"""
    
    sql_criar_tabela_alugueis = """CREATE TABLE IF NOT EXISTS alugueis (
                                    id integer PRIMARY KEY,
                                    data DATETIME DEFAULT CURRENT_TIMESTAMP,
                                    vencimento text NOT NULL,
                                    status text NOT NULL,
                                    id_usuario integer,
                                    id_livro integer,
                                    FOREIGN KEY (id_usuario)
                                        REFERENCES usuarios (id),
                                    FOREIGN KEY (id_usuario)
                                        REFERENCES usuarios (id) 
                                );"""
    
    executar_comando_bd(conn, sql_criar_tabela_livros)
    print("Tabela de livros carregada com sucesso!")
    executar_comando_bd(conn, sql_criar_tabela_usuarios)
    print("Tabela de usuarios carregada com sucesso!")
    #executar_comando_bd(sql_criar_tabela_multas)
    #print("Tabela de multas carregada com sucesso!")
    executar_comando_bd(conn, sql_criar_tabela_alugueis)
    print("Tabela de alugueis carregada com sucesso!")

if __name__ == '__main__':
    conn = criar_conexao("./biblioteca.db")
    criar_tabelas(conn)