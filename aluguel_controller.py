class AlugueisController:
    def __init__(self):
        self.a = 0

    def criar_aluguel(self, aluguel, conn):
        sql = ''' INSERT INTO aluguel(data,vencimento,status,id_usuario,id_livro)
              VALUES(?,?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, aluguel)
        conn.commit()
        return cur.lastrowid
    
    def resolver_aluguel(self, id_aluguel,conn):
        sql = ''' UPDATE alugueis
              SET status = ? ,
              WHERE id = ?'''
        cur = conn.cursor()

        cur.execute(sql, ('devolvido',id_aluguel))
        return 0
    
    def listar_alugueis_do_usuario(self, id_usuario,conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM alugueis WHERE id_usuario=?", (id_usuario,))

        rows = cur.fetchall()
        return rows