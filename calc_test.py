import unittest
import calc


class Test_batch(unittest.TestCase):
    def setUp(self):
        self.Calc = calc.Calc()

    def test_add_success(self):
        self.assertEqual(4, self.Calc.add(2, 2))

    def test_add_float_success(self):
        self.assertEqual(4.5, self.Calc.add(2.25, 2.25))

    def test_add_strings(self):
        self.assertRaises(TypeError, self.Calc.add, "a", "b")

    def test_sub_success(self):
        self.assertEqual(0, self.Calc.sub(2, 2))

    def test_sub_strings(self):
        self.assertRaises(TypeError, self.Calc.sub, "a", "b")

    def test_mul_success(self):
        self.assertEqual(4, self.Calc.mul(2, 2))

    def test_mul_strings(self):
        self.assertRaises(TypeError, self.Calc.mul, "a", "b")

    def test_div_success(self):
        self.assertEqual(1, self.Calc.div(2, 2))

    def test_div_strings(self):
        self.assertRaises(TypeError, self.Calc.div, "a", "b")

    def test_div_zero(self):
        self.assertRaises(TypeError, self.Calc.div, 5, 0)


if __name__ == "__main__":
    unittest.main()
