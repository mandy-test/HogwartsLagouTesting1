import unittest

from python.calc import Calc


class TestCalc(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calc()
        self.calc.add(1,2)

    def test_add(self):
        calc = Calc()
        self.assertEqual(3, calc.add(1, 2))

    def test_add_2(self):
        calc = Calc()
        self.assertEqual(0.03, calc.add(0.01, 0.02))

if __name__ == '__main__':
    unittest.main()