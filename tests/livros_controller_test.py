import unittest
from unittest.mock import MagicMock
import sys
sys.path.append('..')
from livros_controller import LivrosController

class TestLivrosController(unittest.TestCase):
    def test_criar_livro(self):
        mock_conn = MagicMock()
        sql = ''' INSERT INTO livros(nome,descricao)
              VALUES(?,?) '''
        livro_exemplo = ('A culpa é das estrelas', 'Romance')
        mock_conn.cursor.return_value.lastrowid = 1
        livros_controller = LivrosController(mock_conn)
        
        self.assertEqual(livros_controller.criar_livro(livro_exemplo), 1)
        mock_conn.commit.assert_called_once_with()
        mock_conn.cursor.return_value.execute.assert_called_once_with(sql, livro_exemplo)

    def test_excluir_livro(self):
        mock_conn = MagicMock()
        sql = 'DELETE FROM livros WHERE id=?'
        livros_controller = LivrosController(mock_conn)
        
        self.assertEqual(livros_controller.excluir_livro(1), 0)
        mock_conn.commit.assert_called_once_with()
        mock_conn.cursor.return_value.execute.assert_called_once_with(sql, (1,))

    def test_editar_livro(self):
        mock_conn = MagicMock()
        sql = ''' UPDATE livros
              SET nome = ? ,
                  descricao = ?
              WHERE id = ?'''
        livro_exemplo_a_editar = ('A culpa é das estrelas', 'Romance', 1)
        livros_controller = LivrosController(mock_conn)
        
        self.assertEqual(livros_controller.editar_livro(livro_exemplo_a_editar), 0)
        mock_conn.commit.assert_called_once_with()
        mock_conn.cursor.return_value.execute.assert_called_once_with(sql, livro_exemplo_a_editar)

    def test_listar_livros(self):
        mock_conn = MagicMock()
        sql = "SELECT * FROM livros"
        retorno = [('A culpa é das estrelas', 'Romance', 1)]
        mock_conn.cursor.return_value.fetchall.return_value = retorno
        livros_controller = LivrosController(mock_conn)
        
        self.assertEqual(livros_controller.listar_livros(), retorno)
        mock_conn.cursor.return_value.execute.assert_called_once_with(sql)

    def test_get_livro_info(self):
        mock_conn = MagicMock()
        sql = "SELECT * FROM livros"
        retorno = [('A culpa é das estrelas', 'Romance', 1)]
        mock_conn.cursor.return_value.fetchall.return_value = retorno
        livros_controller = LivrosController(mock_conn)
        
        self.assertEqual(livros_controller.listar_livros(), retorno)
        mock_conn.cursor.return_value.execute.assert_called_once_with(sql)


if __name__ == '__main__':
    unittest.main()