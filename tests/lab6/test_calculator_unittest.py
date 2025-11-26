# test_calculator_unittest.py
import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        """Выполняется перед каждым тестом"""
        self.calc = Calculator()

    # Тесты для метода add
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_add_mixed_numbers(self):
        self.assertEqual(self.calc.add(-2, 5), 3)

    def test_add_with_zero(self):
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(5, 0), 5)

    # Тесты для метода divide
    def test_divide_normal_cases(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(10, 3), 10/3)

    def test_divide_negative_numbers(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(10, -2), -5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError) as context:
            self.calc.divide(10, 0)
        self.assertEqual(str(context.exception), "Деление на ноль невозможно")

    # Тесты для метода is_prime_number
    def test_is_prime_number_primes(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for prime in primes:
            with self.subTest(prime=prime):
                self.assertTrue(self.calc.is_prime_number(prime))

    def test_is_prime_number_composites(self):
        composites = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18]
        for composite in composites:
            with self.subTest(composite=composite):
                self.assertFalse(self.calc.is_prime_number(composite))

    def test_is_prime_number_special_cases(self):
        self.assertFalse(self.calc.is_prime_number(1))
        self.assertFalse(self.calc.is_prime_number(0))
        self.assertFalse(self.calc.is_prime_number(-5))


if __name__ == '__main__':
    unittest.main()
