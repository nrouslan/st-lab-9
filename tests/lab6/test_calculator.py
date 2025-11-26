# test_calculator.py
import pytest
from calculator import Calculator


class TestCalculator:

    def setup_method(self):
        """Выполняется перед каждым тестом"""
        self.calc = Calculator()

    # Тесты для метода add
    @pytest.mark.parametrize("a, b, expected", [
        (2, 3, 5),           # положительные числа
        (-2, -3, -5),        # отрицательные числа
        (0, 5, 5),           # ноль + положительное
        (5, 0, 5),           # положительное + ноль
        (-2, 5, 3),          # отрицательное + положительное
        (2.5, 3.5, 6.0),     # дробные числа
        (0, 0, 0),           # два нуля
    ])
    def test_add(self, a, b, expected):
        """Тестирование метода сложения с различными наборами данных"""
        result = self.calc.add(a, b)
        assert result == expected, f"Ожидалось {expected}, получено {result}"

    # Тесты для метода divide
    @pytest.mark.parametrize("a, b, expected", [
        (10, 2, 5),          # целое деление
        (10, 3, 10/3),       # дробное деление
        (-10, 2, -5),        # отрицательное делимое
        (10, -2, -5),        # отрицательный делитель
        (0, 5, 0),           # ноль в делимом
        (2.5, 0.5, 5.0),     # дробные числа
        (1, 1, 1),           # деление на единицу
    ])
    def test_divide(self, a, b, expected):
        """Тестирование метода деления с различными наборами данных"""
        result = self.calc.divide(a, b)
        assert result == expected, f"Ожидалось {expected}, получено {result}"

    def test_divide_by_zero(self):
        """Тестирование исключения при делении на ноль"""
        with pytest.raises(ValueError, match="Деление на ноль невозможно"):
            self.calc.divide(10, 0)

    # Тесты для метода is_prime_number
    @pytest.mark.parametrize("n, expected", [
        (2, True),           # наименьшее простое число
        (3, True),           # простое число
        (17, True),          # простое число
        (19, True),          # простое число
        (4, False),          # составное число
        (9, False),          # составное число
        (15, False),         # составное число
        (1, False),          # 1 не является простым
        (0, False),          # 0 не является простым
        (-5, False),         # отрицательные числа не являются простыми
        (97, True),          # большое простое число
        (100, False),        # большое составное число
    ])
    def test_is_prime_number(self, n, expected):
        """Тестирование проверки простых чисел с различными наборами данных"""
        result = self.calc.is_prime_number(n)
        assert result == expected, f"Число {n}: ожидалось {expected}, получено {result}"
