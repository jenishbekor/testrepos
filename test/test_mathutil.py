import unittest

from mathutil import MathUtil


class TestMathUtil(unittest.TestCase):

    def test_sum(self):

        self.assertEqual(7, MathUtil.sum(3,4) )
        self.assertEqual(5, MathUtil.sum(2,3))


    def test_even(self):
        self.assertTrue( MathUtil.is_even(27))
        self.assertFalse( MathUtil.is_even(25))

    def test_prime(self):
        self.assertTrue( MathUtil.is_prime(29))
        self.assertFalse( MathUtil.is_prime(27))
        self.assertTrue( MathUtil.is_prime(97))


    def test_div(self):
        self.assertEqual( 5 , MathUtil.div(10, 2))
        self.assertAlmostEqual(3.333, MathUtil.div(10, 3), delta=0.0001)