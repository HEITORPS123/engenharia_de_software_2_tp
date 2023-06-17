import unittest
import datetime
from unittest.mock import MagicMock
import sys
sys.path.append('..')
from aluguel_controller import AlugueisController

class TestAlugueisController(unittest.TestCase):
    def test_criar_aluguel(self):
        mock_conn = MagicMock()
        sql = ''' INSERT INTO alugueis(data,vencimento,status,id_usuario,id_livro)
              VALUES(datetime('now', 'localtime'),datetime('now', '+7 day', 'localtime'),?,?,?) '''
        aluguel_exemplo = ('', '', '')
        mock_conn.cursor.return_value.lastrowid = 1
        mock_conn.cursor.return_value.execute.return_value.fetchall.return_value = []
        alugueis_controller = AlugueisController(mock_conn)
        
        self.assertEqual(alugueis_controller.criar_aluguel(aluguel_exemplo), 1)
        mock_conn.commit.assert_called_once_with()
        #mock_conn.cursor.return_value.execute.assert_called_once_with(sql, aluguel_exemplo)

    def test_checar_se_aluguel_vencido_true(self):
        mock_conn = MagicMock()
        aluguel_exemplo = (1, 1, '2023-02-12 16:30:00')
        alugueis_controller = AlugueisController(mock_conn)
        
        self.assertEqual(alugueis_controller.checar_se_aluguel_vencido(aluguel_exemplo, aluguel_exemplo), True)

    def test_checar_se_aluguel_vencido_false(self):
        data_exemplo = datetime.datetime.now() + datetime.timedelta(days=7)
        aluguel_exemplo = (1, 1, data_exemplo.strftime("%Y-%m-%d %H:%M:%S"))
        alugueis_controller = AlugueisController([])
        
        self.assertEqual(alugueis_controller.checar_se_aluguel_vencido(aluguel_exemplo, aluguel_exemplo), False)

    def test_renovar_aluguel(self):
        mock_conn = MagicMock()
        sql = ''' UPDATE alugueis
              SET vencimento = ? 
              WHERE id = ?'''
        alugueis_controller = AlugueisController(mock_conn)

        id_aluguel = 1
        novo_vencimento = datetime.datetime.now() + datetime.timedelta(days=7)
        
        self.assertEqual(alugueis_controller.renovar_aluguel(id_aluguel, novo_vencimento), 0)
        mock_conn.commit.assert_called_once_with()
        mock_conn.cursor.return_value.execute.assert_called_once_with(sql, (novo_vencimento, id_aluguel))

    def test_listar_alugueis_do_usuario(self):
        mock_conn = MagicMock()
        sql = "SELECT * FROM alugueis WHERE id_usuario=?"
        retorno = [(1, 1, '2023-02-12 16:30:00')]
        mock_conn.cursor.return_value.fetchall.return_value = retorno
        alugueis_controller = AlugueisController(mock_conn)
        
        self.assertEqual(alugueis_controller.listar_alugueis_do_usuario(1), retorno)
        mock_conn.cursor.return_value.execute.assert_called_once_with(sql, (1,))

    def test_listar_aluguel_por_id(self):
        mock_conn = MagicMock()
        sql = "SELECT * FROM alugueis WHERE id=?"
        retorno = [(1, 1, '2023-02-12 16:30:00')]
        mock_conn.cursor.return_value.fetchall.return_value = retorno
        alugueis_controller = AlugueisController(mock_conn)
        
        self.assertEqual(alugueis_controller.listar_aluguel_por_id(1), retorno[0])
        mock_conn.cursor.return_value.execute.assert_called_once_with(sql, (1))

if __name__ == '__main__':
    unittest.main()