class AlugueisController:
    def __init__(self):
        self.a = 0

    def criar_aluguel(self, aluguel, conn):
        cur = conn.cursor()
        # Verificando se essa entrada já não existe na tabela de alugueis
        # aluguel[1] -> id_user
        # aluguel[2] -> id_livro
        aux = cur.execute("SELECT * FROM alugueis WHERE id_usuario = ? AND id_livro = ?", (aluguel[1],aluguel[2]))
        if(aux.fetchall() != []):
            print("O usuário já está com esse livro alugado")
            return
        

        sql = ''' INSERT INTO alugueis(data,vencimento,status,id_usuario,id_livro)
              VALUES(datetime('now', 'localtime'),datetime('now', '+7 day', 'localtime'),?,?,?) '''
        
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
    
    def renovar_aluguel(self, id_aluguel, novo_vencimento,conn):
        sql = ''' UPDATE alugueis
              SET vencimento = ? ,
              WHERE id = ?'''
        cur = conn.cursor()

        cur.execute(sql, (novo_vencimento,id_aluguel))
        return 0
    
    def listar_alugueis_do_usuario(self, id_usuario,conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM alugueis WHERE id_usuario=?", (id_usuario,))

        rows = cur.fetchall()
        return rows
    
    def listar_aluguel_por_id(self, id_aluguel,conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM alugueis WHERE id=?", (id_aluguel,))

        rows = cur.fetchall()
        return rows[0]