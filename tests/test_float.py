import unittest, math

from src.comfymath.float import (
    FloatBinaryCondition,
    FloatBinaryOperation,
    FloatBinaryOperationConditional,
    FloatUnaryCondition,
    FloatUnaryOperation,
    FloatUnaryOperationConditional,
)

# Float Unary Operation Tests
class FloatUnaryOperationTest(unittest.TestCase):
    def test_true_condition_applies_operation(self) -> None:
        cases = [
            ("Neg", 1.0, -1.0),
            ("Neg", -2.0, 2.0),
            ("Inc", -1.0, 0.0),
            ("Inc", 10, 11.0),
            ("Dec", -1.0, -2.0),
            ("Dec", 2.0, 1.0),
            ("Abs", 5.7, 5.7),
            ("Abs", -12.0, 12.0),
            ("Abs", 0.0, 0.0),
            ("Sqr", 2.0, 4.0),
            ("Sqr", -3.0, 9.0),
            ("Sqr", 0.0, 0.0),
            ("Sqr", 1.0, 1.0),
            ("Cube", 2.0, 8.0),
            ("Cube", -3.0, -27.0),
            ("Cube", 0.0, 0.0),
            ("Cube", 1.0, 1.0),
            ("Cube", -1.0, -1.0),
            ("Sqrt", 9.0, 3.0),
            ("Sqrt", 16.0, 4.0),
            ("Sqrt", 0.0, 0.0),
            ("Sqrt", 1.0, 1.0),
            ("Log10", 100, 2),
            # Ln -> see approx function
            ("Log2", 4.0, 2.0),
            ("Log2", 8.0, 3.0),
            ("Sin", 0.0, 0.0),
            ("Cos", 0.0, 1.0),
            ("Tan", 0.0, 0.0),
            ("Asin", 0.0, 0.0),
            ("Acos", 1.0, 0.0),
            ("Atan", 0.0, 0.0),
            ("Sinh", 0.0, 0.0),
            ("Cosh", 0.0, 1.0),
            ("Tanh", 0.0, 0.0),
            ("Asinh", 0.0, 0.0),
            ("Acosh", 1.0, 0.0),
            ("Atanh", 0.0, 0.0),
            ("Round", 0.0, 0.0),
            ("Round", 1.1, 1.0),
            ("Round", -1.1, -1.0),
            ("Round", 1.5, 2.0),
            ("Round", -1.6, -2.0),
            ("Round", 0.0001, 0.0),
            ("Floor", 1.1, 1.0),
            ("Floor", 1.6, 1.0),
            ("Floor", -1.5, -2.0),
            ("Ceil", 1.1, 2.0),
            ("Ceil", 1.6, 2.0),
            ("Ceil", -1.1, -1.0),
            ("Trunc", 1.1, 1.0),
            ("Trunc", 4.6, 4.0),
            ("Trunc", -3.5, -3.0),
            ("Erf", 0.0, 0.0),
            ("Erf", 6.0, 1.0),
            ("Erf", -6.0, -1.0),
            ("Erfc", 0.0, 1.0),
            ("Erfc", -6.0, 2.0),
            ("Gamma", 1.0, 1.0),
            ("Gamma", 8.0, 5040.0),
            ("Radians", 0.0, 0.0),
            ("Degrees", 0.0, 0.0),
        ]
        operation = FloatUnaryOperation()
        for operator, given, expected in cases:
            with self.subTest(operator=operator, given=given, expected=expected,):
                result = operation.op(operator, given)
                self.assertEqual(result, (expected,))

# Float Unary Operation Tests with Approximation
class FloatUnaryApproxOperationTest(unittest.TestCase):
    def test_true_condition_applies_operation(self) -> None:
        cases = [
            ("Ln", math.e, 1.0),
            ("Sin", math.pi/2.0, 1.0),
            ("Cos", (math.pi)*-1, -1.0),
            ("Cos", math.pi, -1.0),
            ("Tan", math.pi/4, 1.0),
            ("Asin", 1.0, math.pi/2.0),
            ("Asin", -1.0, math.pi/-2.0),
            ("Acos", 0.0, math.pi/2.0),
            ("Acos", -1.0, math.pi),
            ("Atan", 1.0, math.pi/4.0),
            ("Sinh", 1.0,  1.1752011936438014),
            ("Cosh", 1.0,  1.5430806348152437),
            ("Tanh", 1.0,  0.7615941559557649),
            ("Asinh",1.0, 0.881373587019543),
            ("Acosh", 2.0, 1.3169578969248166),
            ("Atanh", 0.99, 2.6466524123622457),
            ("Erf", 0.5, 0.5204998778130465),
            ("Erfc", 0.5, 0.4795001221869535),
            ("Radians", 180, math.pi),
            ("Degrees", 1.0, 57.29577951308232),
        ]
        operation = FloatUnaryOperation()
        for operator, given, expected in cases:
            with self.subTest(operator=operator, given=given, expected=expected,):
                result = operation.op(operator, given)
                self.assertEqual(len(result), 1)
                self.assertAlmostEqual(result[0], expected, places=12,)

# Float Failing Unary Operation Tests
class FloatFailingUnaryOperationTest(unittest.TestCase):
    def test_fail_condition_applies_operation(self) -> None:
        cases = [
            ("Sqrt", -9.0),
            ("Sqrt", -0.0001),
            ("Ln", 0.0),
            ("Ln", -2.0),
            ("Log10", 0.0),
            ("Log10", -2.0),
            ("Log2", 0.0),
            ("Log2", -2.0),
            ("Gamma", 0.0),
        ]
        operation = FloatUnaryOperation()
        for operator, given in cases:
            with self.subTest(operator=operator, given=given):
                with self.assertRaises(ValueError):
                    operation.op(operator,given)
                    

# Float Unary Condition Tests
class FloatUnaryConditionTest(unittest.TestCase):
    def test_true_condition_applies_operation(self) -> None:
        cases = [
            ("IsFinite", 4.5, True),
            ("IsFinite", math.inf, False),
            ("IsFinite", float("nan"), False),
            ("IsPositive", 0.0, False),
            ("IsPositive", 4.5, True),
            ("IsPositive", -4.5, False),
            ("IsNegative", 0.0, False),
            ("IsNegative", 4.5, False),
            ("IsNegative", -4.5, True),
            ("IsNonZero", 0.0, False),
            ("IsNonZero", 4.5, True),
            ("IsNonZero", -4.5, True),
            ("IsPositiveInfinity", 0.0, False),
            ("IsPositiveInfinity", math.inf, True),
            ("IsPositiveInfinity", float("inf"), True),
            ("IsPositiveInfinity", float("-inf"), False),
            ("IsNegativeInfinity", 0.0, False),
            ("IsNegativeInfinity", math.inf, False),
            ("IsNegativeInfinity", float("inf"), False),
            ("IsNegativeInfinity", float("-inf"), True),
            ("IsNaN", float("nan"), True),
            ("IsNaN", 5.5, False),
            ("IsNaN", math.inf, False),
            ("IsFinite", 9999.9999, True),
            ("IsFinite", math.inf, False),
            ("IsFinite", float("-inf"), False),
            ("IsInfinite", 9999.9999, False),
            ("IsInfinite", math.inf, True),
            ("IsInfinite", float("-inf"), True),
            ("IsEven", 0.0, True),
            ("IsEven", 1.0, False),
            ("IsEven", 2.0, True),
            ("IsEven", -2.0, True),
            ("IsEven", 2.1, False),
            ("IsOdd", 0.0, False),
            ("IsOdd", 1.0, True),
            ("IsOdd", 2.0, False),
            ("IsOdd", -2.0, False),
            ("IsOdd", 2.1, True),
            ("IsOdd", -4.4, True),
        ]
        operation = FloatUnaryCondition()
        for operator, given, expected in cases:
            with self.subTest(operator=operator, given=given, expected=expected,):
                result = operation.op(operator, given)
                self.assertEqual(result, (expected,))

# Binary Float Tests (Operation)
class FloatBinaryOperationTest(unittest.TestCase):
    def test_div_returns_true_division_result(self) -> None:
        self.assertEqual(FloatBinaryOperation().op("Div", 7.0, 2.0), (3.5,))

    def test_div_by_zero_raises_zero_division_error(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            FloatBinaryOperation().op("Div", 7.0, 0.0)

# Binary Float Tests (Condition)
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

# Unary Float Tests (Conditional Operation)
class FloatUnaryOperationConditionalTest(unittest.TestCase):
    def test_true_condition_applies_neg_operation(self) -> None:
        self.assertEqual(FloatUnaryOperationConditional().op(True, "constant", 99.0, "Neg", 2.5), (-2.5,),)

    def test_false_condition_returns_fallback_value(self) -> None:
        self.assertEqual(FloatUnaryOperationConditional().op(False, "constant", 99.0, "Neg", 2.5), (99.0,),)

    def test_true_condition_applies_operation(self) -> None:
        self.assertEqual(FloatUnaryOperationConditional().op(True, "constant", 99.0, "Neg", 2.5), (-2.5,),)

    # TODO: Add more tests for FloatUnaryOperationConditional, including different operations.


class FloatBinaryOperationConditionalTest(unittest.TestCase):
    def test_true_condition_applies_operation(self) -> None:
        self.assertEqual(FloatBinaryOperationConditional().op(True, "constant", 99.0, "Mul", 2.5, 4.0), (10.0,),)

    def test_false_condition_returns_selected_input(self) -> None:
        self.assertEqual(FloatBinaryOperationConditional().op(False, "B", 99.0, "Mul", 2.5, 4.0), (4.0,),)


if __name__ == "__main__":
    unittest.main()
