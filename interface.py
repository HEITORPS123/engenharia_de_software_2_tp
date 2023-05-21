import os
from time import sleep
import settings


class InterfacePrints:

    @staticmethod
    def print_menu():
        InterfacePrints._clear()
        print("=======================")
        print("Bem-vindo!\n")
        print('1 - Cliente')
        print('2 - Administrador')
        print('0 - Sair')
        print("=======================")
        print("Opcao: ", end='')

    @staticmethod
    def print_user_menu():
        InterfacePrints._clear()
        print("=======================")
        print("Cliente\n")
        print('1 - Alugar livros')
        print('2 - Pesquisar livros')
        print('3 - Informacoes do livro')
        print('4 - Livros alugado')
        print('5 - Renovar livro')
        print('6 - Consultar multas pendentes')
        print('0 - Voltar')
        print("=======================")
        print("Opcao: ", end='')

    @staticmethod
    def print_adm_menu():
        InterfacePrints._clear()
        print("=======================")
        print("Administrador\n")
        print('1 - Alterar Livros')
        print('2 - Alterar Usuarios')
        print('3 - Listar Usuarios')
        print('4 - Registrar devolucao')
        print('5 - Quitacao de multa')
        print('0 - Voltar')
        print("=======================")
        print("Opcao: ", end='')

    @staticmethod
    def print_add_remove_edit():
        InterfacePrints._clear()
        print("=======================")
        print('1 - Adicionar')
        print('2 - Remover')
        print('3 - Editar')
        print('0 - Voltar')
        print("=======================")
        print("Opcao: ", end='')

    @staticmethod
    def print_invalid_option():
        print("Opcao invalida.")
        sleep(1)    
        
    @ staticmethod
    def print_invalid_login():
        print("Credenciais invalidas.")
        sleep(1)

    @staticmethod
    def waiting_key_msg():
        print("Aperte alguma tecla para continuar...")
        input()

    @staticmethod
    def print_exiting_msg():
        print("Saindo...")
        sleep(1)

    @staticmethod
    def _clear():
        if os.environ['DO_CLEAR'] == "True":
            os.system('cls' if os.name == 'nt' else 'clear')
