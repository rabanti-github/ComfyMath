import unittest

from src.comfymath.float import (
    FloatBinaryCondition,
    FloatBinaryOperation,
    FloatBinaryOperationConditional,
    FloatUnaryCondition,
    FloatUnaryOperation,
    FloatUnaryOperationConditional,
)


class FloatUnaryOperationTest(unittest.TestCase):
    def test_sqrt_returns_square_root(self) -> None:
        self.assertEqual(FloatUnaryOperation().op("Sqrt", 9.0), (3.0,))

    def test_sqrt_negative_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            FloatUnaryOperation().op("Sqrt", -1.0)


class FloatUnaryConditionTest(unittest.TestCase):
    def test_is_finite_returns_true_for_finite_value(self) -> None:
        self.assertEqual(FloatUnaryCondition().op("IsFinite", 4.5), (True,))


class FloatBinaryOperationTest(unittest.TestCase):
    def test_div_returns_true_division_result(self) -> None:
        self.assertEqual(FloatBinaryOperation().op("Div", 7.0, 2.0), (3.5,))

    def test_div_by_zero_raises_zero_division_error(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            FloatBinaryOperation().op("Div", 7.0, 0.0)


class FloatBinaryConditionTest(unittest.TestCase):

    def test_greater_than_returns_true(self) -> None:
        self.assertEqual(FloatBinaryCondition().op("Gt", 9.0, 4.0), (True,))

    def test_greater_than_returns_false(self) -> None:
        self.assertEqual(FloatBinaryCondition().op("Gt", 3.0, 4.0), (False,))

    def test_greater_than_returns_false_on_equal_values(self) -> None:
        self.assertEqual(FloatBinaryCondition().op("Gt", 4.0, 4.0), (False,))

    def test_gte_returns_true_for_equal_values(self) -> None:
        self.assertEqual(FloatBinaryCondition().op("Gte", 4.0, 4.0), (True,))

    def test_gte_returns_true(self) -> None:
        self.assertEqual(FloatBinaryCondition().op("Gte", 4.1, 4.0), (True,))

    def test_gte_returns_false(self) -> None:
        self.assertEqual(FloatBinaryCondition().op("Gte", 3.9, 4.0), (False,))

    def test_lt_returns_true(self) -> None:
        self.assertEqual(FloatBinaryCondition().op("Lt", 4.0, 9.0), (True,))

    def test_lt_returns_false_for_equal_values(self) -> None:
        self.assertEqual(FloatBinaryCondition().op("Lt", 4.0, 4.0), (False,))

    def test_lt_returns_false(self) -> None:
        self.assertEqual(FloatBinaryCondition().op("Lt", 9.0, 4.0), (False,))

    def test_lte_returns_true(self) -> None:
        self.assertEqual(FloatBinaryCondition().op("Lte", 4.0, 9.0), (True,))

    def test_lte_returns_true_for_equal_values(self) -> None:
        self.assertEqual(FloatBinaryCondition().op("Lte", 4.0, 4.0), (True,))

    def test_lte_returns_false(self) -> None:
        self.assertEqual(FloatBinaryCondition().op("Lte", 9.0, 4.0), (False,))

    def test_eq_returns_true_for_equal_values(self) -> None:
        self.assertEqual(FloatBinaryCondition().op("Eq", 4.0, 4.0), (True,))

    def test_eq_returns_false_for_unequal_values(self) -> None:
        self.assertEqual(FloatBinaryCondition().op("Eq", 4.0, 5.0), (False,))

    def test_neq_returns_true_for_unequal_values(self) -> None: 
        self.assertEqual(FloatBinaryCondition().op("Neq", 4.0, 5.0), (True,))

    def test_neq_returns_false_for_equal_values(self) -> None:
        self.assertEqual(FloatBinaryCondition().op("Neq", 4.0, 4.0), (False,))


class FloatUnaryOperationConditionalTest(unittest.TestCase):
    def test_true_condition_applies_operation(self) -> None:
        self.assertEqual(FloatUnaryOperationConditional().op(True, "constant", 99.0, "Neg", 2.5), (-2.5,),)

    def test_false_condition_returns_fallback_value(self) -> None:
        self.assertEqual(FloatUnaryOperationConditional().op(False, "constant", 99.0, "Neg", 2.5), (99.0,),)

    # TODO: Add more tests for FloatUnaryOperationConditional, including different operations.


class FloatBinaryOperationConditionalTest(unittest.TestCase):
    def test_true_condition_applies_operation(self) -> None:
        self.assertEqual(FloatBinaryOperationConditional().op(True, "constant", 99.0, "Mul", 2.5, 4.0), (10.0,),)

    def test_false_condition_returns_selected_input(self) -> None:
        self.assertEqual(FloatBinaryOperationConditional().op(False, "B", 99.0, "Mul", 2.5, 4.0), (4.0,),)


if __name__ == "__main__":
    unittest.main()
