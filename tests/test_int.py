import unittest

from src.comfymath.int import (
    IntBinaryCondition,
    IntBinaryOperation,
    IntBinaryOperationConditional,
    IntUnaryCondition,
    IntUnaryOperation,
    IntUnaryOperationConditional,
)


class IntUnaryOperationTest(unittest.TestCase):
    def test_abs_negative_returns_positive(self) -> None:
        self.assertEqual(IntUnaryOperation().op("Abs", -7), (7,))


class IntUnaryConditionTest(unittest.TestCase):
    def test_is_even_returns_true_for_even_integer(self) -> None:
        self.assertEqual(IntUnaryCondition().op("IsEven", 8), (True,))

    def test_is_even_returns_false_for_odd_integer(self) -> None:
        self.assertEqual(IntUnaryCondition().op("IsEven", 7), (False,))


class IntBinaryOperationTest(unittest.TestCase):
    def test_div_uses_floor_division(self) -> None:
        self.assertEqual(IntBinaryOperation().op("Div", 7, 2), (3,))

    def test_div_by_zero_raises_zero_division_error(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            IntBinaryOperation().op("Div", 7, 0)


class IntBinaryConditionTest(unittest.TestCase):
    def test_greater_than_returns_true(self) -> None:
        self.assertEqual(IntBinaryCondition().op("Gt", 9, 4), (True,))

    def test_less_than_returns_true(self) -> None:
        self.assertEqual(IntBinaryCondition().op("Lt", 4, 9), (True,))


class IntUnaryOperationConditionalTest(unittest.TestCase):
    def test_true_condition_applies_operation(self) -> None:
        self.assertEqual(
            IntUnaryOperationConditional().op(True, "constant", 99, "Neg", 5),
            (-5,),
        )

    def test_false_condition_returns_fallback_value(self) -> None:
        self.assertEqual(
            IntUnaryOperationConditional().op(False, "constant", 99, "Neg", 5),
            (99,),
        )


class IntBinaryOperationConditionalTest(unittest.TestCase):
    def test_true_condition_applies_operation(self) -> None:
        self.assertEqual(
            IntBinaryOperationConditional().op(True, "constant", 99, "Mul", 3, 4),
            (12,),
        )

    def test_false_condition_returns_selected_input(self) -> None:
        self.assertEqual(
            IntBinaryOperationConditional().op(False, "B", 99, "Mul", 3, 4),
            (4,),
        )


if __name__ == "__main__":
    unittest.main()
