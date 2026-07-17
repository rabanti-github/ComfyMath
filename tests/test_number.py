import unittest

from src.comfymath.number import (
    NumberBinaryCondition,
    NumberBinaryOperation,
    NumberUnaryCondition,
    NumberUnaryOperation,
)


class NumberUnaryOperationTest(unittest.TestCase):
    def test_abs_returns_positive_number(self) -> None:
        self.assertEqual(NumberUnaryOperation().op("Abs", -4), (4.0,))

    def test_sqrt_negative_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            NumberUnaryOperation().op("Sqrt", -1)


class NumberUnaryConditionTest(unittest.TestCase):
    def test_is_positive_returns_true_for_positive_number(self) -> None:
        self.assertEqual(NumberUnaryCondition().op("IsPositive", 2), (True,))


class NumberBinaryOperationTest(unittest.TestCase):
    def test_div_returns_true_division_result(self) -> None:
        self.assertEqual(NumberBinaryOperation().op("Div", 7, 2), (3.5,))

    def test_div_by_zero_raises_zero_division_error(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            NumberBinaryOperation().op("Div", 7, 0)


class NumberBinaryConditionTest(unittest.TestCase):
    def test_lte_returns_true_for_lower_value(self) -> None:
        self.assertEqual(NumberBinaryCondition().op("Lte", 2, 3), (True,))


if __name__ == "__main__":
    unittest.main()
