import unittest
import datetime
from unittest.mock import patch
from unittest.mock import MagicMock
import sys
sys.path.append('..')
from aluguel_controller import AlugueisController

class TestAlugueisController(unittest.TestCase):
    @patch('builtins.print')
    def test_criar_aluguel(self, mock_output):
        mock_conn = MagicMock()
        sql = ''' INSERT INTO alugueis(data,vencimento,status,id_usuario,id_livro)
              VALUES(datetime('now', 'localtime'),datetime('now', '+7 day', 'localtime'),?,?,?) '''
        aluguel_exemplo = (1, '2023-02-12 16:30:00', '2023-02-19 16:30:00', 'pendente', 1, 1)
        mock_conn.cursor.return_value.lastrowid = 1
        mock_conn.cursor.return_value.execute.return_value.fetchall.return_value = []
        alugueis_controller = AlugueisController(mock_conn)
        
        self.assertEqual(alugueis_controller.criar_aluguel(aluguel_exemplo), 1)
        mock_conn.commit.assert_called_once_with()
        #mock_conn.cursor.return_value.execute.assert_called_once_with(sql, aluguel_exemplo)

    @patch('builtins.print')
    def test_checar_se_aluguel_vencido_true(self, mock_output):
        mock_conn = MagicMock()
        aluguel_exemplo = (1, '2023-02-12 16:30:00', '2023-02-19 16:30:00', 'pendente', 1, 1)
        alugueis_controller = AlugueisController(mock_conn)
        
        self.assertEqual(alugueis_controller.checar_se_aluguel_vencido(aluguel_exemplo, 1), True)

    @patch('builtins.print')
    def test_checar_se_aluguel_vencido_false(self, mock_output):
        data_exemplo = datetime.datetime.now() + datetime.timedelta(days=7)
        aluguel_exemplo = (1, 1, data_exemplo.strftime("%Y-%m-%d %H:%M:%S"))
        alugueis_controller = AlugueisController([])
        
        self.assertEqual(alugueis_controller.checar_se_aluguel_vencido(aluguel_exemplo, 1), False)
    
    @patch('builtins.print')
    def test_renovar_aluguel(self, mock_output):
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

    @patch('builtins.print')
    def test_listar_alugueis_do_usuario(self, mock_output):
        mock_conn = MagicMock()
        sql = "SELECT * FROM alugueis WHERE id_usuario=?"
        retorno = [(1, '2023-02-12 16:30:00', '2023-02-19 16:30:00', 'pendente', 1, 1)]
        mock_conn.cursor.return_value.fetchall.return_value = retorno
        alugueis_controller = AlugueisController(mock_conn)
        
        self.assertEqual(alugueis_controller.listar_alugueis_do_usuario(1), retorno)
        mock_conn.cursor.return_value.execute.assert_called_once_with(sql, (1,))

    def test_listar_aluguel_por_id(self):
        mock_conn = MagicMock()
        sql = "SELECT * FROM alugueis WHERE id=?"
        retorno = [(1, '2023-02-12 16:30:00', '2023-02-19 16:30:00', 'pendente', 1, 1)]
        mock_conn.cursor.return_value.fetchall.return_value = retorno
        alugueis_controller = AlugueisController(mock_conn)
        
        self.assertEqual(alugueis_controller.listar_aluguel_por_id(1), retorno[0])
        mock_conn.cursor.return_value.execute.assert_called_once_with(sql, (1))
