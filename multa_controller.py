from interface import InterfacePrints


class MultaController:
    def __init__(self, conn):
        self.conn = conn

    def criar_multa(self, multa):
        sql = ''' INSERT INTO multas(id_usuario,valor,status)
              VALUES(?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, multa)
        self.conn.commit()
        return cur.lastrowid

    def listar_multas_por_id(self, id_usuario):
        sql = ''' SELECT * FROM multas 
            WHERE id_usuario = ? ''' 
        cur = self.conn.cursor()
        cur.execute(sql, (id_usuario,))
        multas = cur.fetchall()
        for multa in multas:
            print(multa)
        InterfacePrints.waiting_key_msg()
        self.conn.commit()
        return multas
    
    def resolver_multa(self, id_multa):
        sql = ''' UPDATE multas
              SET status = ? 
              WHERE id = ? '''
        cur = self.conn.cursor()

        cur.execute(sql, ('paga', id_multa))
        print('Multa paga com sucesso!')
        InterfacePrints.waiting_key_msg()
        self.conn.commit()
        return 0
    