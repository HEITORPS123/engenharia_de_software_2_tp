import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
from unittest.mock import call
import sys
sys.path.append('..')
from multa_controller import MultaController

class TestMultaController(unittest.TestCase):
    def test_criar_multa(self):
        mock_conn = MagicMock()
        sql = ''' INSERT INTO multas(id_usuario,valor,status)
              VALUES(?,?,?) '''
        multa_exemplo = (1, 100, 'pendente')
        mock_conn.cursor.return_value.lastrowid = 1
        multa_controller = MultaController(mock_conn)
        
        self.assertEqual(multa_controller.criar_multa(multa_exemplo), 1)
        mock_conn.commit.assert_called_once_with()
        mock_conn.cursor.return_value.execute.assert_called_once_with(sql, multa_exemplo)

    @patch('builtins.print')
    def test_listar_multas_por_id(self, mock_output):
        mock_conn = MagicMock()
        sql = ''' SELECT * FROM multas 
            WHERE id_usuario = ? ''' 
        retorno_multas = [(1, 100, 'pendente')]
        mock_conn.cursor.return_value.fetchall.return_value = retorno_multas
        multa_controller = MultaController(mock_conn)
        id_multa = 1
        
        self.assertEqual(multa_controller.listar_multas_por_id(id_multa), retorno_multas)
        mock_conn.commit.assert_called_once_with()
        mock_conn.cursor.return_value.execute.assert_called_once_with(sql, (id_multa, ))

    @patch('builtins.print')    
    def test_resolver_multa(self, mock_output):    
        mock_conn = MagicMock()    
        sql = ''' UPDATE multas SET status = ? WHERE id = ? '''
        id_multa = 1    
        multa_controller = MultaController(mock_conn)    

        mock_conn.cursor.return_value.fetchone.return_value = ('some', 'row')
        self.assertEqual(multa_controller.resolver_multa(id_multa), 0) 
        mock_conn.commit.assert_called_once_with()    
        mock_conn.cursor.return_value.execute.assert_has_calls([
            call("SELECT * FROM multas WHERE id = ?", (id_multa,)),
            call(sql, ('paga', id_multa))
        ])
