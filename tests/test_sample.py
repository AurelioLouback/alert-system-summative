import unittest  # Biblioteca para testes

# Função de exemplo para testar
def soma(a, b):
    return a + b

# Classe de testes (herda de unittest.TestCase)
class TestCalculadora(unittest.TestCase):
    def test_soma(self):  # Método de teste
        self.assertEqual(soma(2, 3), 5)  # Verifica se 2+3=5
        self.assertEqual(soma(-1, 1), 0)  # Verifica se -1+1=0

# Executa os testes se o arquivo for rodado diretamente
if __name__ == '__main__':
    unittest.main()
def test_soma_decimais(self):
    self.assertEqual(soma(1.5, 2.5), 4.0)