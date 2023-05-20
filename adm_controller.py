class AdmController:
    def __init__(self):
        self.a = 0

    def criar_usuario(self, usuario, conn):
        sql = ''' INSERT INTO usuarios
              VALUES(?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, usuario)
        conn.commit()
        return cur.lastrowid
    
    def excluir_usuario(self, id_usuario, conn):
        sql = 'DELETE FROM usuarios WHERE id=?'
        cur = conn.cursor()
        cur.execute(sql, (id_usuario,))
        conn.commit()
        return 0
    
    def editar_usuario(self, usuario,conn):
        sql = ''' UPDATE usuarios
              SET login = ? ,
                  senha = ?
              WHERE id = ?'''
        cur = conn.cursor()
        cur.execute(sql, usuario)
        return 0
    
    def listar_usuarios(self, conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM usuarios")

        rows = cur.fetchall()
        return rows