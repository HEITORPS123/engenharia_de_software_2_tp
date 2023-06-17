import unittest
from unittest.mock import MagicMock
import sys
sys.path.append('..')
from adm_controller import AdmController

class TestAdmController(unittest.TestCase):
    def test_criar_usuario(self):
        mock_conn = MagicMock()
        sql = ''' INSERT INTO usuarios(login,senha,permissoes)
              VALUES(?,?,?) '''
        usuario_exemplo = ('login', 'senha', 'rw+')
        mock_conn.cursor.return_value.lastrowid = 1
        adm_controller = AdmController(mock_conn)
        
        self.assertEqual(adm_controller.criar_usuario(usuario_exemplo, mock_conn), 1)
        mock_conn.cursor.return_value.execute.assert_called_once_with(sql, usuario_exemplo)

    def test_excluir_usuario(self):
        mock_conn = MagicMock()
        sql = 'DELETE FROM usuarios WHERE id=?'
        adm_controller = AdmController(mock_conn)
        
        self.assertEqual(adm_controller.excluir_usuario(1, mock_conn), 0)
        mock_conn.cursor.return_value.execute.assert_called_once_with(sql, (1,))

if __name__ == '__main__':
    unittest.main()