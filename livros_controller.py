class LivrosController:
    def __init__(self, conn):
        self.conn = conn

    def criar_livro(self, livro, conn):
        sql = ''' INSERT INTO livros(id,nome,descricao)
              VALUES(?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, livro)
        conn.commit()
        return cur.lastrowid
    
    def excluir_livro(self, id_livro, conn):
        sql = 'DELETE FROM livros WHERE id=?'
        cur = conn.cursor()
        cur.execute(sql, (id_livro,))
        conn.commit()
        return 0
    
    def editar_livro(self, livro,conn):
        sql = ''' UPDATE livros
              SET nome = ? ,
                  descricao = ?
              WHERE id = ?'''
        cur = conn.cursor()
        cur.execute(sql, livro)
        return 0
    
    def listar_livros(self, conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM livros")

        rows = cur.fetchall()
        return rows

    def pesquisar_livro(self, nome_livro, conn):
        sql = 'SELECT * FROM livros WHERE nome=?'
        cur = conn.cursor()
        cur.execute(sql, [nome_livro])
        rows = cur.fetchall()
        return rows

    def get_livro_info(self, nome_livro, conn):
        livro = self.pesquisar_livro(nome_livro, conn)
        id = livro[0][0]
        nome = livro[0][1]
        descricao = livro[0][2]

        print(f"Id: {id}")
        print(f"Nome: {nome}")
        print(f"Descrição: {descricao}")
        return (id, nome, descricao)