from datetime import timedelta
from time import sleep

from interface import InterfacePrints
from livros_controller import LivrosController
from multa_controller import MultaController
from aluguel_controller import AlugueisController

class UserController:
    def __init__(self, conn):
        self.conn = conn
        self.user = None
        
    def login(self):
        
        login = input("Login: ")
        senha = input("Senha: ")
        
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT * FROM usuarios WHERE login = ? AND senha = ?", (login, senha))
        if cursor.fetchone() is None:
            return
        print(cursor.fetchone())
        
        self.user = cursor.fetchone()
        if self.user is None:
            InterfacePrints.print_invalid_login()
            return
        print("Login efetuado com sucesso.")
        sleep(1)
        self.run
        
    def run(self):

        InterfacePrints.print_user_menu()
        try:
            escolha = int(input())
        except:
            InterfacePrints.print_invalid_option()
            self.run()
            return

        self.executar_escolha(escolha)

    def executar_escolha(self, escolha):
        
        if escolha == 1:
            AlugueisController.criar_aluguel()
        elif escolha == 2:
            nome = input("Nome do livro: ")
            LivrosController.pesquisar_livro(nome, self.conn)
        elif escolha == 3:
            nome = input("Nome do livro: ")
            LivrosController.get_livro_info(nome, self.conn)
        elif escolha == 4:
            id_usuario = input("Id do usuario: ")
            # AlugueisController.listar_alugueis_do_usuario(id_usuario, self.conn)
        elif escolha == 5:
            id_aluguel = input("Id do aluguel: ")
            self.renovar_aluguel(id_aluguel)
        elif escolha == 6:
            id_usuario = input("Id do usuario: ")
            MultaController.listar_multas_por_id(id_usuario, self.conn)
        elif escolha == 0:
            InterfacePrints.print_exiting_msg()
            return
        else:
            InterfacePrints.print_invalid_option()
            self.run()

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
        nova_data = data_vencimento + timedelta(days=7)
        nova_data = 0
        aluguel_controller.renovar_aluguel(id_aluguel, nova_data,self.conn)