from interface import InterfacePrints


class AlugueisController:
    def __init__(self, conn):
        self.conn = conn

    def criar_aluguel(self, aluguel):
        cur = self.conn.cursor()
        # Verificando se essa entrada já não existe na tabela de alugueis
        # aluguel[1] -> id_user
        # aluguel[2] -> id_livro
        aux = cur.execute("SELECT * FROM alugueis WHERE id_usuario = ? AND id_livro = ?", (aluguel[0], aluguel[1]))
        if(aux.fetchall() != []):
            print("O usuário já está com esse livro alugado")
            return
        

        sql = ''' INSERT INTO alugueis(data,vencimento,status,id_usuario,id_livro)
              VALUES(datetime('now', 'localtime'),datetime('now', '+7 day', 'localtime'),?,?,?) '''
        
        cur.execute(sql, ('ativo', aluguel[0], aluguel[1]))
        self.conn.commit()
        
        print("Aluguel realizado com sucesso")
        
        return cur.lastrowid
    
    def resolver_aluguel(self, id_aluguel):
        sql = ''' UPDATE alugueis
              SET status = ? 
              WHERE id = ?'''
        cur = self.conn.cursor()

        cur.execute(sql, ('devolvido', id_aluguel))
        self.conn.commit()
        return 0
    
    def renovar_aluguel(self, id_aluguel, novo_vencimento):
        sql = ''' UPDATE alugueis
              SET vencimento = ? 
              WHERE id = ?'''
        cur = self.conn.cursor()

        cur.execute(sql, (novo_vencimento, id_aluguel))
        self.conn.commit()
        print("Aluguel renovado com sucesso")
        InterfacePrints.waiting_key_msg()
        return 0
    
    def listar_alugueis_do_usuario(self, id_usuario):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM alugueis WHERE id_usuario=?", (id_usuario,))

        alugueis = cur.fetchall()
        for aluguel in alugueis:
            print(aluguel)
        InterfacePrints.waiting_key_msg()
        return alugueis
    
    def listar_aluguel_por_id(self, id_aluguel):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM alugueis WHERE id=?", (id_aluguel))

        rows = cur.fetchall()
        return rows[0]