import filecmp
import os
from shutil import rmtree
from unittest import TestCase
from main import criar_conexao, criar_tabelas

from main_controller import MainController

class SystemTest(TestCase):
    
    def setUp(self):
        
        self.current_dir = os.path.dirname(__file__)
        if os.path.exists(self.current_dir + "/../databaseTest.db"):
            print("removendo databaseTest.db")
            os.remove(self.current_dir + "/../databaseTest.db")
        file = open(self.current_dir + "/../databaseTest.db", "w")
        file.close()
        
        self.inputs = os.path.join(self.current_dir, 'inputs')
        self.outputs = os.path.join(self.current_dir, 'outputs')
        self.temp = os.path.join(self.current_dir, 'temp')
        if os.path.exists(self.temp):
            rmtree(self.temp)
        os.mkdir(self.temp)

        
    def run_test(self, in_file, out_file):
        conn = criar_conexao(self.current_dir + "/../databaseTest.db")
        criar_tabelas(conn)        
        main_controller = MainController(conn)
        main_controller.run(
            from_file=True,
            file_path=os.path.join(self.inputs, in_file),
            to_file=True,
            outfile_path=os.path.join(self.temp, out_file)
        )

        result = filecmp.cmp(
            os.path.join(self.temp, out_file),
            os.path.join(self.outputs, out_file)
        )

        return result
    
    def test_logar_usuario_e_sair(self):
        result = self.run_test('1.in', '1.out')
        self.assertTrue(result)