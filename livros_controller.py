from interface import InterfacePrints


class LivrosController:
    def __init__(self, conn):
        self.conn = conn

    def criar_livro(self, livro):
        sql = ''' INSERT INTO livros(nome,descricao)
              VALUES(?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, livro)
        self.conn.commit()
        return cur.lastrowid
    
    def excluir_livro(self, id_livro):
        sql = 'DELETE FROM livros WHERE id=?'
        cur = self.conn.cursor()
        cur.execute(sql, (id_livro,))
        self.conn.commit()
        return 0
    
    def editar_livro(self, livro):
        sql = ''' UPDATE livros
              SET nome = ? ,
                  descricao = ?
              WHERE id = ?'''
        cur = self.conn.cursor()
        cur.execute(sql, livro)
        self.conn.commit()
        return 0
    
    def listar_livros(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM livros")

        rows = cur.fetchall()
        return rows

    def pesquisar_livro(self, nome_livro):
        sql = 'SELECT * FROM livros WHERE nome=?'
        cur = self.conn.cursor()
        cur.execute(sql, [nome_livro])
        rows = cur.fetchall()
        if len(rows) == 0:
            InterfacePrints.print_no_result()
            InterfacePrints.waiting_key_msg()
            return
        print(rows)
        InterfacePrints.waiting_key_msg()
        return rows

    def get_livro_info(self, nome_livro):
        livro = self.pesquisar_livro(nome_livro)
        
        if livro is None:
            return
        
        id = livro[0][0]
        nome = livro[0][1]
        descricao = livro[0][2]

        print(f"Id: {id}")
        print(f"Nome: {nome}")
        print(f"Descrição: {descricao}")
        return (id, nome, descricao)