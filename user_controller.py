from multa_controller import MultaController
from aluguel_controller import AlugueisController

class UserController:
    def __init__(self, conn):
        self.conn = conn

    def listar_multas_pendentes(self, id_usuario):
        multa_controller = MultaController()
        multas = multa_controller.listar_multas_por_id(id_usuario, self.conn)
        multas_pendentes = list()
        for multa in multas:
            if multa[3] == 'PENDENTE':
                multas_pendentes.append(multa)

        return multas_pendentes
    
    def renovar_aluguel(self,id_aluguel):
        aluguel_controller = AlugueisController()
        aluguel = aluguel_controller.listar_aluguel_por_id(id_aluguel)
        data_vencimento = aluguel[2]
        print(data_vencimento)
        nova_data = 0
        aluguel_controller.renovar_aluguel(id_aluguel, nova_data,self.conn)