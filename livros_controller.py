class LivrosController:
    def __init__(self):
        self.a = 0

    def criar_livro(self, livro, conn):
        sql = ''' INSERT INTO livro(nome,descricao)
              VALUES(?,?) '''
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