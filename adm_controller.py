from ast import In
from interface import InterfacePrints
from livros_controller import LivrosController
from aluguel_controller import AlugueisController
from multa_controller import MultaController

class AdmController:
    def __init__(self, conn):
        self.conn = conn
        self.livros_controller = LivrosController(conn)
        self.alugueis_controller = AlugueisController(conn)
        self.multa_controller = MultaController(conn)

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
            self.administrar_livros()

        # Usuarios
        elif escolha == 2:
            self.administrar_usuarios()

        elif escolha == 3:
            self.listar_usuarios()
            
        elif escolha == 4:
            self.listar_livros()

        elif escolha == 5:
            id_aluguel = input("Id do aluguel: ")
            self.alugueis_controller.resolver_aluguel(id_aluguel)

        elif escolha == 6:
            id_multa = input("Id da multa: ")
            self.multa_controller.resolver_multa(id_multa)
            InterfacePrints.waiting_key_msg()

        elif escolha == 0:
            InterfacePrints.print_exiting_msg()
            return
        else:
            InterfacePrints.print_invalid_option()
            self.run()
            
        self.run()

    def administrar_livros(self):
        InterfacePrints.print_add_remove_edit()
        auxEscolha = int(input())
        if auxEscolha == 1:
            nome = input("Nome: ")
            descricao = input("Descricao: ")
            self.livros_controller.criar_livro((nome, descricao))
        elif auxEscolha == 2:
            id_livro = input("Id do livro: ")
            self.livros_controller.excluir_livro(id_livro)
        elif auxEscolha == 3:
            id_livro = input("Id do livro: ")
            nome = input("Nome: ")
            descricao = input("Descricao: ")
            self.livros_controller.editar_livro((nome, descricao, id_livro))
        elif auxEscolha == 0:
            self.run()
        else:
            InterfacePrints.print_invalid_option()
            self.run()

    def administrar_usuarios(self):
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
            id_usr = input("Id do usuario: ")
            login = input("Login: ")
            senha = input("Senha: ")
            permissao = input("Permissao: ")
            self.editar_usuario((login, senha, permissao ,id_usr), self.conn)
        elif auxEscolha == 0:
            self.run()
        else:
            InterfacePrints.print_invalid_option()
            self.run()


    def criar_usuario(self, usuario, conn):
        sql = ''' INSERT INTO usuarios(login,senha,permissoes)
              VALUES(?,?,?) '''
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
        conn.commit()
        return 0

    def listar_usuarios(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM usuarios")

        usuarios = cur.fetchall()
        InterfacePrints._clear()
        for usuario in usuarios:
            print('Id: ', usuario[0])
            print('Usuario: ', usuario[1])
            print('Senha: ', usuario[2])
            print('Permissao: ', usuario[3])
            print('=======================')
        InterfacePrints.waiting_key_msg()
        return usuarios

    def listar_livros(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM livros")

        livros = cur.fetchall()
        InterfacePrints._clear()
        for livro in livros:
            print('Id: ', livro[0])
            print('Nome: ', livro[1])
            print('Descricao:: ', livro[2])
            print('=======================')
            
        InterfacePrints.waiting_key_msg()
        return livros

    def pesquisar_usuario_por_login(self, conn, login):
        sql = 'SELECT * FROM livros WHERE login=?'
        cur = conn.cursor()
        cur.execute(sql, [login])
        rows = cur.fetchall()
        return rows
