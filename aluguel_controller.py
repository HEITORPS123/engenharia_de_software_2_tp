import datetime
from time import sleep
from interface import InterfacePrints
from multa_controller import MultaController


class AlugueisController:
    def __init__(self, conn):
        self.conn = conn

    def criar_aluguel(self, aluguel):
        cur = self.conn.cursor()
        # Verificando se essa entrada já não existe na tabela de alugueis
        # aluguel[1] -> id_user
        # aluguel[2] -> id_livro
        aux = cur.execute("SELECT * FROM alugueis WHERE id_usuario = ? AND id_livro = ?", (aluguel[0], aluguel[1]))
        auxInfo = aux.fetchall()
        if(auxInfo == None):
            ultimoAluguel = auxInfo[-1] # Ultimo aluguel feito pelo usuário
            if(ultimoAluguel[3] == 'ativo'):
                print("O usuário já está com esse livro alugado")
                InterfacePrints.waiting_key_msg()
                return -1
        

        sql = ''' INSERT INTO alugueis(data,vencimento,status,id_usuario,id_livro)
              VALUES(datetime('now', 'localtime'),datetime('now', '+7 day', 'localtime'),?,?,?) '''
        
        cur.execute(sql, ('ativo', aluguel[0], aluguel[1]))
        self.conn.commit()
        
        print("Aluguel realizado com sucesso!")
        
        return cur.lastrowid
    
    def resolver_aluguel(self, id_aluguel):
        cur = self.conn.cursor()
        
        cur.execute("SELECT * FROM alugueis WHERE id = ?", (id_aluguel))
        aluguel = cur.fetchone()
        if(aluguel == None):
            print("Aluguel não encontrado")
            InterfacePrints.waiting_key_msg()
            return -1
        self.checar_se_aluguel_vencido(aluguel, aluguel[4])
        
        sql = ''' UPDATE alugueis
              SET status = ? 
              WHERE id = ?'''

        cur.execute(sql, ('devolvido', id_aluguel))
        self.conn.commit()
        print('Livro devolvido com sucesso!')
        
        return 0
    
    def checar_se_aluguel_vencido(self, aluguel, id_usuario):
        data_vencimento = datetime.datetime.strptime(aluguel[2], "%Y-%m-%d %H:%M:%S")
        data_atual = datetime.datetime.now()
        
        if data_atual > data_vencimento:
            print("Aluguel vencido!")
            valorMulta = (data_atual - data_vencimento).days * 2
            MultaController(self.conn).criar_multa((id_usuario, valorMulta, 'aberta'))
            return True
        return False
    
    def renovar_aluguel(self, id_aluguel, novo_vencimento):
        sql = ''' UPDATE alugueis
              SET vencimento = ? 
              WHERE id = ?'''
        cur = self.conn.cursor()

        cur.execute(sql, (novo_vencimento, id_aluguel))
        self.conn.commit()
        print("Aluguel renovado com sucesso")
        return 0
    
    def listar_alugueis_do_usuario(self, id_usuario):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM alugueis WHERE id_usuario=?", (id_usuario,))

        alugueis = cur.fetchall()
        InterfacePrints._clear()
        for aluguel in alugueis:
            print('Id: ', aluguel[0])
            print('Data do aluguel: ', aluguel[1])
            print('Data de vencimento: ', aluguel[2])
            print('Status: ', aluguel[3])
            print('Id do usuário: ', aluguel[4])
            print('Id do livro: ', aluguel[5])
            print('--------------------------')
        return alugueis
    
    def listar_aluguel_por_id(self, id_aluguel):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM alugueis WHERE id=?", (id_aluguel))

        rows = cur.fetchall()
        return rows[0]