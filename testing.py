from palindromo import is_palindrome
import unittest

class TestPalindrome(unittest.TestCase):


    def test_aCa(self):
        resultado = is_palindrome("aCa")
        self.assertEqual(resultado, True)

    def test_ABBA(self):
        resultado = is_palindrome("ABBA")
        self.assertEqual(resultado, True)

    def test_juampi(self):
        resultado = is_palindrome("juampi")
        self.assertEqual(resultado, False)

    def test_computacion(self):
        resultado = is_palindrome("computacion")
        self.assertEqual(resultado, False)

    def test_neuquen(self):
        resultado = is_palindrome("neuq uen")
        self.assertEqual(resultado, True)

    def test_animoromina(self):
        resultado = is_palindrome("animo romina")
        self.assertEqual(resultado, True)

    def test_asado(self):
        resultado = is_palindrome("asado")
        self.assertEqual(resultado, False)

    def test_universidad(self):
        resultado = is_palindrome("universidad")
        self.assertEqual(resultado, False)

unittest.main()