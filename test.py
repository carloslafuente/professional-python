import unittest
from unittest import TestCase
from palindrome import is_palindrome
from prime_number import is_prime


class Test(TestCase):

    def test_is_palindrome(self):
        self.assertEqual(is_palindrome('Ligar es ser agil'), True)
        self.assertEqual(is_palindrome('Arepera'), True)
        self.assertEqual(is_palindrome('Esto no es un palindromo'), False)
        self.assertEqual(is_palindrome('ESto tampoco es un palindromo'), False)
        self.assertEqual(is_palindrome('Ana'), True)

    def test_is_prime(self):
        self.assertEqual(is_prime(100), False)
        self.assertEqual(is_prime(200), False)
        self.assertEqual(is_prime(53), True)
        self.assertEqual(is_prime(23), True)
        self.assertEqual(is_prime(45), False)
        self.assertEqual(is_prime(32), False)
        self.assertEqual(is_prime(142), False)


if __name__ == '__main__':
    unittest.main()
