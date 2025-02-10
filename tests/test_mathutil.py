import unittest
from mathutil import Mathutil

class TestMathutil(unittest.TestCase):

    def test_even(self):
        self.assertTrue(Mathutil.is_even(24))
        self.assertFalse(Mathutil.is_even(23))


    def test_prime(self):
        self.assertEqual(Mathutil.is_prime(25), False)
        self.assertEqual(Mathutil.is_prime(29), True)
        self.assertEqual(Mathutil.is_prime(2), True)