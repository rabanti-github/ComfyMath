import unittest, math

from src.comfymath.number import (
    NumberBinaryCondition,
    NumberBinaryOperation,
    NumberBinaryOperationConditional,
    NumberUnaryCondition,
    NumberUnaryOperation,
    NumberUnaryOperationConditional,
)

# Number Unary Operation Tests
class NumberUnaryOperationTest(unittest.TestCase):
    def test_true_condition_applies_operation(self) -> None:
        cases = [
            ("Neg", 1.0, -1.0),
            ("Neg", -2.0, 2.0),
            ("Inc", -1.0, 0.0),
            ("Inc", 10.12, 11.12),
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
        operation = NumberUnaryOperation()
        for operator, given, expected in cases:
            with self.subTest(operator=operator, given=given, expected=expected,):
                result = operation.op(operator, given)
                self.assertEqual(result, (expected,))

# Number Unary Operation Tests with Approximation
class NumberUnaryApproxOperationTest(unittest.TestCase):
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
        operation = NumberUnaryOperation()
        for operator, given, expected in cases:
            with self.subTest(operator=operator, given=given, expected=expected,):
                result = operation.op(operator, given)
                self.assertEqual(len(result), 1)
                self.assertAlmostEqual(result[0], expected, places=12,)

# Number Failing Unary Operation Tests
class NumberFailingUnaryOperationTest(unittest.TestCase):
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
        operation = NumberUnaryOperation()
        for operator, given in cases:
            with self.subTest(operator=operator, given=given):
                with self.assertRaises(ValueError):
                    operation.op(operator,given)
                    

# Number Unary Condition Tests
class NumberUnaryConditionTest(unittest.TestCase):
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
        operation = NumberUnaryCondition()
        for operator, given, expected in cases:
            with self.subTest(operator=operator, given=given, expected=expected,):
                result = operation.op(operator, given)
                self.assertEqual(result, (expected,))

# Number Unary Operation Tests
class NumberBinaryOperationTest(unittest.TestCase):
    def test_true_condition_applies_operation(self) -> None:
        cases = [
            ("Add", 1.0, -1.0, 0.0),
            ("Add", 0.0, 0.0, 0.0),
            ("Add", -1.0, -1.0, -2.0),
            ("Add", 1.1, 0.1, 1.2),
            ("Add", 20.0, 80.0, 100.0),
            ("Sub", 1.0, -1.0, 2.0),
            ("Sub", 0.0, 0.0, 0.0),
            ("Sub", -1.0, -1.0, 0.0),
            ("Sub", 1.1, 0.1, 1.0),
            ("Sub", 20.0, 80.0, -60.0),
            ("Mul", 1.0, -1.0, -1.0),
            ("Mul", 0.0, 0.0, 0.0),
            ("Mul", -2.0, -2.0, 4.0),
            ("Mul", 1.1, 0.1, 0.11),
            ("Mul", 20.0, 80.0, 1600),
            ("Div", 1.0, -1.0, -1.0),
            ("Div", -2.0, -2.0, 1.0),
            ("Div", 1.1, 0.1, 11.0),
            ("Div", 20.0, 80.0, 0.25),
            ("Mod", 1.0, 4.0, 1.0),
            ("Mod", 100.0, 80.0, 20.0),
            ("Mod", -100.0, 80.0, 60.0),
            ("Mod", -100.0, -80.0, -20.0),
            ("Pow", 1.0, 0.0, 1.0),
            ("Pow", 1.0, 1.0, 1.0),
            ("Pow", 1.0, 2.0, 1.0),
            ("Pow", -1.0, 2.0, 1.0),
            ("Pow", 2.0, 0.0, 1.0),
            ("Pow", 2.0, 1.0, 2.0),
            ("Pow", 2.0, 2.0, 4.0),
            ("Pow", -2.0, 2.0, 4.0),
            ("FloorDiv", 10.0, 5.0, 2.0),
            ("FloorDiv", -10.0, 5.0, -2.0),
            ("FloorDiv", 20.0, 80.0, 0.0),
            ("Min", 20.0, 80.0, 20.0),
            ("Min", -60.0, 20.0, -60.0),
            ("Min", 80.0, 20.0, 20.0),
            ("Min", 20.0, -60.0, -60.0),
            ("Max", 20.0, 80.0, 80.0),
            ("Max", -60.0, 20.0, 20.0),
            ("Max", 80.0, 20.0, 80.0),
            ("Max", 20.0, -60.0, 20.0),
            ("Log", 8.0, 2.0, 3.0),
            ("Log", 100.0, 10.0, 2.0),
            ("Log", 0.25, 2.0, -2.0),
            ("Log", 27.0, 3.0, 3.0),
            ("Atan2", 0.0, 0.0, 0.0),
            ("Atan2", 0.0, -1.0, math.pi),
            ("Atan2", 0.0, 1.0, 0.0),
            ("Atan2", 1.0, 1.0, 0.7853981633974483),
            ("Atan2", 1.0, 0.0, math.pi/2),
            ("Atan2", 0.5, 0.5, 0.7853981633974483),
        ]
        operation = NumberBinaryOperation()
        for operator, givenA, givenB, expected in cases:
            with self.subTest(operator=operator, givenA=givenA, givenB=givenB, expected=expected,):
                result = operation.op(operator, givenA, givenB)
                self.assertTrue(math.isclose(result[0], expected, rel_tol=1e-12, abs_tol=1e-12)
)

# Number Unary Operation Zero-Division Tests
class NumberBinaryOperationZeroDivTest2(unittest.TestCase):
    def test_div_by_zero_raises_zero_division_error(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            NumberBinaryOperation().op("Div", 7.0, 0.0)


# Number Binary Condition Tests
class NumberBinaryConditionTest(unittest.TestCase):
    def test_true_condition_applies_operation(self) -> None:
        cases = [
            ("Gt", 9.0, 4.0, True),
            ("Gt", 3.0, 4.0, False),
            ("Gt", 4.0, 4.0, False),
            ("Gte", 4.0, 4.0, True),
            ("Gte", 4.1, 4.0, True),
            ("Gte", 3.9, 4.0, False),
            ("Lt", 4.0, 9.0, True),
            ("Lt", 4.0, 4.0, False),
            ("Lt", 9.0, 4.0, False),
            ("Lte", 4.0, 9.0, True),
            ("Lte", 4.0, 4.0, True),
            ("Lte", 9.0, 4.0, False),
            ("Eq", 4.0, 4.0, True),
            ("Eq", 4.0, 5.0, False),
            ("Neq", 4.0, 5.0, True),
            ("Neq", 4.0, 4.0, False),
        ]
        operation = NumberBinaryCondition()
        for operator, givenA, givenB, expected in cases:
            with self.subTest(operator=operator, givenA=givenA, givenB=givenB, expected=expected,):
                result = operation.op(operator, givenA, givenB)
                self.assertEqual(result, (expected,))


# Unary Number Tests (Conditional Operation)
class NumberUnaryOperationConditionalTest(unittest.TestCase):
    def test_true_condition_applies_operation(self) -> None:
        from src.comfymath.float import FLOAT_UNARY_OPERATIONS

        operation_cases = {
            "Neg": (2.5, -2.5),
            "Inc": (2.5, 3.5),
            "Dec": (2.5, 1.5),
            "Abs": (-2.5, 2.5),
            "Sqr": (3.0, 9.0),
            "Cube": (-3.0, -27.0),
            "Sqrt": (9.0, 3.0),
            "Exp": (1.0, math.e),
            "Ln": (math.e, 1.0),
            "Log10": (100.0, 2.0),
            "Log2": (8.0, 3.0),
            "Sin": (math.pi / 2.0, 1.0),
            "Cos": (math.pi, -1.0),
            "Tan": (math.pi / 4.0, 1.0),
            "Asin": (1.0, math.pi / 2.0),
            "Acos": (0.0, math.pi / 2.0),
            "Atan": (1.0, math.pi / 4.0),
            "Sinh": (1.0, 1.1752011936438014),
            "Cosh": (1.0, 1.5430806348152437),
            "Tanh": (1.0, 0.7615941559557649),
            "Asinh": (1.0, 0.881373587019543),
            "Acosh": (2.0, 1.3169578969248166),
            "Atanh": (0.5, 0.5493061443340548),
            "Round": (1.6, 2.0),
            "Floor": (1.6, 1.0),
            "Ceil": (1.1, 2.0),
            "Trunc": (-3.5, -3.0),
            "Erf": (0.0, 0.0),
            "Erfc": (0.0, 1.0),
            "Gamma": (8.0, 5040.0),
            "Radians": (180.0, math.pi),
            "Degrees": (math.pi, 180.0),
        }
        cases = []
        for operator in FLOAT_UNARY_OPERATIONS:
            given, expected = operation_cases[operator]
            cases.append((True, "constant", 99.0, operator, given, expected))
            cases.append((False, "constant", 99.0, operator, given, 99.0))

        operation = NumberUnaryOperationConditional()
        for condition, fallback_mode, fallback_value, operator, given, expected in cases:
            with self.subTest(
                condition=condition, operator=operator, given=given, expected=expected
            ):
                result = operation.op(
                    condition, fallback_mode, fallback_value, operator, given
                )
                self.assertTrue(
                    math.isclose(result[0], expected, rel_tol=1e-12, abs_tol=1e-12)
                )

class NumberBinaryOperationConditionalTest(unittest.TestCase):
    def test_true_condition_applies_operation(self) -> None:
        from src.comfymath.float import FLOAT_BINARY_OPERATIONS

        operation_cases = {
            "Add": (20.0, 80.0, 100.0),
            "Sub": (20.0, 80.0, -60.0),
            "Mul": (2.5, 4.0, 10.0),
            "Div": (20.0, 80.0, 0.25),
            "Mod": (-100.0, 80.0, 60.0),
            "Pow": (-2.0, 2.0, 4.0),
            "FloorDiv": (20.0, 80.0, 0.0),
            "Max": (-60.0, 20.0, 20.0),
            "Min": (-60.0, 20.0, -60.0),
            "Log": (8.0, 2.0, 3.0),
            "Atan2": (1.0, 1.0, math.pi / 4.0),
        }
        cases = []
        for operator in FLOAT_BINARY_OPERATIONS:
            given_a, given_b, expected = operation_cases[operator]
            cases.append(
                (True, "constant", 99.0, operator, given_a, given_b, expected)
            )
            cases.append(
                (False, "constant", 99.0, operator, given_a, given_b, 99.0)
            )

        operation = NumberBinaryOperationConditional()
        for (
            condition,
            fallback_mode,
            fallback_value,
            operator,
            given_a,
            given_b,
            expected,
        ) in cases:
            with self.subTest(
                condition=condition,
                operator=operator,
                given_a=given_a,
                given_b=given_b,
                expected=expected,
            ):
                result = operation.op(
                    condition,
                    fallback_mode,
                    fallback_value,
                    operator,
                    given_a,
                    given_b,
                )
                self.assertTrue(
                    math.isclose(result[0], expected, rel_tol=1e-12, abs_tol=1e-12)
                )


if __name__ == "__main__":
    unittest.main()
