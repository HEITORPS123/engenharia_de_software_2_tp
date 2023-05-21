from datetime import datetime, timedelta
import datetime
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
        user = cursor.fetchone()
        if user is None:
            InterfacePrints.print_invalid_login()
            return
        
        self.user = user
        print("Login efetuado com sucesso.")
        sleep(1)
        self.run()
        
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
        
        InterfacePrints._clear()
        
        if escolha == 1:
            id_livro = input("Id do livro: ")
            AlugueisController(self.conn).criar_aluguel((self.user[0], id_livro))
        elif escolha == 2:
            nome = input("Nome do livro: ")
            LivrosController(self.conn).pesquisar_livro(nome)
            self.run()
        elif escolha == 3:
            nome = input("Nome do livro: ")
            LivrosController(self.conn).get_livro_info(nome)
        elif escolha == 4:
            id_usuario = self.user[0]
            AlugueisController(self.conn).listar_alugueis_do_usuario(id_usuario)
        elif escolha == 5:
            id_aluguel = input("Id do aluguel: ")
            self.renovar_aluguel(id_aluguel)
        elif escolha == 6:
            id_usuario = self.user[0]
            MultaController(self.conn).listar_multas_por_id(id_usuario)
        elif escolha == 0:
            InterfacePrints.print_exiting_msg()
            return
        else:
            InterfacePrints.print_invalid_option()
            self.run()
            
        self.run()

    def listar_multas_pendentes(self, id_usuario):
        multa_controller = MultaController()
        multas = multa_controller.listar_multas_por_id(id_usuario, self.conn)
        multas_pendentes = list()
        for multa in multas:
            if multa[3] == 'PENDENTE':
                multas_pendentes.append(multa)

        return multas_pendentes
    
    def renovar_aluguel(self, id_aluguel):
        aluguel_controller = AlugueisController(self.conn)
        aluguel = aluguel_controller.listar_aluguel_por_id(id_aluguel)
        data_vencimento = datetime.datetime.strptime(aluguel[2], "%Y-%m-%d %H:%M:%S")
        nova_data = data_vencimento + timedelta(days=7)
        aluguel_controller.renovar_aluguel(id_aluguel, nova_data)