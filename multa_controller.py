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
        cur.execute(sql, id_usuario)
        self.conn.commit()
        return cur.lastrowid
    
    def resolver_multa(self, id_multa):
        sql = ''' UPDATE multas
              SET status = ? 
              WHERE id = ? '''
        cur = self.conn.cursor()

        cur.execute(sql, ('paga', id_multa))
        self.conn.commit()
        return 0
    