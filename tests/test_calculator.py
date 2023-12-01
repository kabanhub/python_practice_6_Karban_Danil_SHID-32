import pytest
from app.calculator import Calculator

class TestCalculator(pytest.TestCase):
    def test_addition(self):
        calc = Calculator(3, 4)
        result = calc.addition()
        self.assertEqual(result, 7)

    def test_subtraction(self):
        calc = Calculator(5, 2)
        result = calc.subtraction()
        self.assertEqual(result, 3)

    def test_multiplication(self):
        calc = Calculator(2, 6)
        result = calc.multiplication()
        self.assertEqual(result, 12)

    def test_division(self):
        calc = Calculator(8, 4)
        result = calc.division()
        self.assertEqual(result, 2)

    def test_exponentiation(self):
        calc = Calculator(2, 3)
        result = calc.exponentiation()
        self.assertEqual(result, 8)

    def test_random_number(self):
        random_num = Calculator.random_number(1, 10)
        self.assertTrue(1 <= random_num <= 10)

if __name__ == '__main__':
    pytest.main()
