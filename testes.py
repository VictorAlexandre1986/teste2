import unittest
from calculadora import soma

class TestCalculdora(unittest.TestCase):
    def test_soma_5_mais_5_igual_10(self):
        self.assertEqual(soma(5,5),10)

    def test_soma_0_mais_0_igual_0(self):
        self.assertEqual(soma(0,0),0)
    
    def test_string_mais_5_igual_10(self):
        self.assertEqual(soma('5',5),10)

    def test_5negativo_mais_5_igual_0(self):
        self.assertEqual(soma(-5,5),0)
    
    def test_verificar_se_é_um_numero_interiro(self):
        self.assertIsInstance(5,int)

unittest.main(verbosity=2)