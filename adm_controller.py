from ast import In
from aluguel_controller import AlugueisController
from interface import InterfacePrints
from livros_controller import LivrosController
from multa_controller import MultaController


class AdmController:
    def __init__(self, conn):
        self.conn = conn

    def login(self):
        
        login = input("Login: ")
        senha = input("Senha: ")

        if login != 'admin' or senha != 'admin':
            InterfacePrints.print_invalid_login()
            return
        self.run()

    def run(self):

        InterfacePrints.print_adm_menu()
        try:
            escolha = int(input())
        except:
            InterfacePrints.print_invalid_option()
            self.run()
            return

        self.executar_escolha(escolha)

    def executar_escolha(self, escolha):

        # Livros
        if escolha == 1:
            InterfacePrints.print_add_remove_edit()
            auxEscolha = int(input())
            if auxEscolha == 1:
                nome = input("Nome: ")
                descricao = input("Descricao: ")
                self.livros_controller.criar_livro((nome, descricao))
            elif auxEscolha == 2:
                id_livro = input("Id do livro: ")
                LivrosController.excluir_livro(id_livro, self.conn)
            elif auxEscolha == 3:
                nome = input("Nome: ")
                descricao = input("Descricao: ")
                LivrosController.editar_livro((nome, descricao), self.conn)
            elif auxEscolha == 0:
                self.run()
            else:
                InterfacePrints.print_invalid_option()
                self.run()

        # Usuarios
        elif escolha == 2:
            InterfacePrints.print_add_remove_edit()
            auxEscolha = int(input())
            if auxEscolha == 1:
                login = input("Login: ")
                senha = input("Senha: ")
                # input with 0 or 1
                permissao = input("Permissao: ")
                self.criar_usuario((login, senha, permissao), self.conn)
            elif auxEscolha == 2:
                id_usr = input("Id do usuario: ")
                self.excluir_usuario(id_usr, self.conn)
            elif auxEscolha == 3:
                login = input("Login: ")
                senha = input("Senha: ")
                permissao = input("Permissao: ")
                self.editar_usuario((login, senha, permissao), self.conn)
            elif auxEscolha == 0:
                self.run()
            else:
                InterfacePrints.print_invalid_option()
                self.run()

        elif escolha == 3:
            self.listar_usuarios()

        elif escolha == 4:
            id_aluguel = input("Id do aluguel: ")
            # AlugueisController.resolver_aluguel(id_aluguel, self.conn)

        elif escolha == 5:
            id_aluguel = input("Id do aluguel: ")
            # MultaController.resolver_multa(id_aluguel, self.conn)

        elif escolha == 0:
            InterfacePrints.print_exiting_msg()
            return
        else:
            InterfacePrints.print_invalid_option()
            self.run()
            
        self.run()

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

    def editar_usuario(self, usuario, conn):
        sql = ''' UPDATE usuarios
              SET login = ? ,
                  senha = ? ,
                  permissoes = ?
              WHERE id = ?'''
        cur = conn.cursor()
        cur.execute(sql, usuario)
        return 0

    def listar_usuarios(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM usuarios")

        usuarios = cur.fetchall()
        for usuario in usuarios:
            print(usuario)
        InterfacePrints.waiting_key_msg()
        return usuarios

    def pesquisar_usuario_por_login(self, conn, login):
        sql = 'SELECT * FROM livros WHERE login=?'
        cur = conn.cursor()
        cur.execute(sql, [login])
        rows = cur.fetchall()
        return rows
