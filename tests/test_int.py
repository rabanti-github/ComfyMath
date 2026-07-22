import unittest

from src.comfymath.int import (
    IntBinaryCondition,
    IntBinaryOperation,
    IntBinaryOperationConditional,
    IntUnaryCondition,
    IntUnaryOperation,
    IntUnaryOperationConditional,
)


# Int Unary Operation Tests
class IntUnaryOperationTest(unittest.TestCase):
    def test_true_condition_applies_operation(self) -> None:
        cases = [
            ("Neg", 1, -1),
            ("Neg", -2, 2),
            ("Inc", -1, 0),
            ("Inc", 10, 11),
            ("Dec", -1, -2),
            ("Dec", 2, 1),
            ("Abs", 5, 5),
            ("Abs", -12, 12),
            ("Abs", 0, 0),
            ("Sqr", 2, 4),
            ("Sqr", -3, 9),
            ("Sqr", 0, 0),
            ("Sqr", 1, 1),
            ("Cube", 2, 8),
            ("Cube", -3, -27),
            ("Cube", 0, 0),
            ("Cube", 1, 1),
            ("Cube", -1, -1),
            ("Not", -1, 0),
            ("Not", 1, -2),
            ("Not", 4, -5),
            ("Not", -4, 3),
            ("Factorial", 0, 1),
            ("Factorial", 1, 1),
            ("Factorial", 2, 2),
            ("Factorial", 3, 6),
            ("Factorial", 5, 120),
        ]
        operation = IntUnaryOperation()
        for operator, given, expected in cases:
            with self.subTest(operator=operator, given=given, expected=expected,):
                result = operation.op(operator, given)
                self.assertEqual(result, (expected,))

# Int Unary Condition Tests
class IntUnaryConditionTest(unittest.TestCase):
    def test_true_condition_applies_operation(self) -> None:
        cases = [
            ("IsPositive", 0, False),
            ("IsPositive", 4, True),
            ("IsPositive", -4, False),
            ("IsNegative", 0, False),
            ("IsNegative", 4, False),
            ("IsNegative", -4, True),
            ("IsZero", 0, True),
            ("IsZero", 4, False),
            ("IsZero", -4, False),
            ("IsNonZero", 0, False),
            ("IsNonZero", 4, True),
            ("IsNonZero", -4, True),
            ("IsEven", 0, True),
            ("IsEven", 1, False),
            ("IsEven", 2, True),
            ("IsEven", -2, True),
            ("IsOdd", 0, False),
            ("IsOdd", 1, True),
            ("IsOdd", 2, False),
            ("IsOdd", -2, False),
            ("IsOdd", -4, False),
        ]
        operation = IntUnaryCondition()
        for operator, given, expected in cases:
            with self.subTest(operator=operator, given=given, expected=expected,):
                result = operation.op(operator, given)
                self.assertEqual(result, (expected,))

# Int Binary Operation Tests
class IntBinaryOperationTest(unittest.TestCase):
    def test_true_condition_applies_operation(self) -> None:
        cases = [
            ("Add", 1, -1, 0),
            ("Add", 0, 0, 0),
            ("Add", -1, -1, -2),
            ("Add", 1, 0, 1),
            ("Add", 20, 80, 100),
            ("Sub", 1, -1, 2),
            ("Sub", 0, 0, 0),
            ("Sub", -1, -1, 0),
            ("Sub", 1, 0, 1),
            ("Sub", 20, 80, -60),
            ("Mul", 1, -1, -1),
            ("Mul", 0, 0, 0),
            ("Mul", -2, -2, 4),
            ("Mul", 1, 0, 0),
            ("Mul", 20, 80, 1600),
            ("Div", 1, -1, -1),
            ("Div", -2, -2, 1),
            ("Div", 20, 80, 0),
            ("Div", 80, 20, 4),
            ("Mod", 1, 4, 1),
            ("Mod", 100, 80, 20),
            ("Mod", -100, 80, 60),
            ("Mod", -100, -80, -20),
            ("Pow", 1, 0, 1),
            ("Pow", 1, 1, 1),
            ("Pow", 1, 2, 1),
            ("Pow", -1, 2, 1),
            ("Pow", 2, 0, 1),
            ("Pow", 2, 1, 2),
            ("Pow", 2, 2, 4),
            ("Pow", -2, 2, 4),
            ("And", 0, 0, 0),
            ("And", 1, 0, 0 ),
            ("And", 1, 1, 1 ),
            ("And", 2, 2, 2 ),
            ("And", 2, 3, 2 ),
            ("And", -2, 5, 4 ),
            ("And", 10, 4, 0 ),
            ("Nand", 0, 0, -1 ),
            ("Nand", 0, 1, -1 ),
            ("Nand", 1, 1, -2 ),
            ("Nand", -2, 4, -5 ),
            ("Nand", 10, 3, -3 ),
            ("Or", 0, 0, 0 ),
            ("Or", 0, 1, 1 ),
            ("Or", -1, 2, -1 ),
            ("Or", 4, 4, 4 ),
            ("Or", 4, 6, 6 ),
            ("Nor", 0, 0, -1 ),
            ("Nor", 0, 1, -2 ),
            ("Nor", -1, 2, 0 ),
            ("Nor", 4, 4, -5 ),
            ("Nor", 4, 6, -7 ),
            ("Xor", 0, 0, 0 ),
            ("Xor", 0, 1, 1 ),
            ("Xor", -1, 2, -3 ),
            ("Xor", 4, 4, 0 ),
            ("Xor", 4, 6, 2 ),
            ("Xnor", 0, 0, -1 ),
            ("Xnor", 0, 1, -2 ),
            ("Xnor", -1, 2, 2 ),
            ("Xnor", 4, 4, -1 ),
            ("Xnor", 4, 6, -3 ),
            ("Shl", 0, 0, 0 ),
            ("Shl", 0, 1, 0 ),
            ("Shl", -1, 2, -4 ),
            ("Shl", 4, 4, 64 ),
            ("Shl", 4, 6, 256 ),
            ("Shr", 0, 0, 0 ),
            ("Shr", 0, 1, 0 ),
            ("Shr", -1, 2, -1 ),
            ("Shr", 4, 4, 0 ),
            ("Shr", 4, 6, 0 ),
            ("Min", 20, 80, 20),
            ("Min", -60, 20, -60),
            ("Min", 80, 20, 20),
            ("Min", 20, -60, -60),
            ("Max", 20, 80, 80),
            ("Max", -60, 20, 20),
            ("Max", 80, 20, 80),
            ("Max", 20, -60, 20),
        ]
        operation = IntBinaryOperation()
        for operator, givenA, givenB, expected in cases:
            with self.subTest(operator=operator, givenA=givenA, givenB=givenB, expected=expected,):
                result = operation.op(operator, givenA, givenB)
                self.assertEqual(result, (expected,))

# Int Failing Binary Operation Tests
class IntFailingBinaryOperationTest(unittest.TestCase):
    def test_fail_condition_applies_operation(self) -> None:
        cases = [
            ("Div", 1, 0),
        ]
        operation = IntBinaryOperation()
        for operator, givenA, givenB in cases:
            with self.subTest(operator=operator, givenA=givenA, givenB=givenB):
                with self.assertRaises(ZeroDivisionError):
                    operation.op(operator,givenA, givenB)

# Int Binary Condition Tests
class IntBinaryConditionTest(unittest.TestCase):
    def test_true_condition_applies_operation(self) -> None:
        cases = [
            ("Gt", 9, 4, True),
            ("Gt", 3, 4, False),
            ("Gt", 4, 4, False),
            ("Geq", 4, 4, True),
            ("Geq", 4, 3, True),
            ("Geq", 3, 4, False),
            ("Lt", 4, 9, True),
            ("Lt", 4, 4, False),
            ("Lt", 9, 4, False),
            ("Leq", 4, 9, True),
            ("Leq", 4, 4, True),
            ("Leq", 9, 4, False),
            ("Eq", 4, 4, True),
            ("Eq", 4, 5, False),
            ("Neq", 4, 5, True),
            ("Neq", 4, 4, False),
        ]
        operation = IntBinaryCondition()
        for operator, givenA, givenB, expected in cases:
            with self.subTest(operator=operator, givenA=givenA, givenB=givenB, expected=expected,):
                result = operation.op(operator, givenA, givenB)
                self.assertEqual(result, (expected,))


# Unary Int Tests (Conditional Operation)
class IntUnaryOperationConditionalTest(unittest.TestCase):
    def test_true_condition_applies_operation(self) -> None:
        from src.comfymath.int import INT_UNARY_OPERATIONS

        operation_cases = {
            "Neg": (2, -2),
            "Inc": (2, 3),
            "Dec": (2, 1),
            "Abs": (-2, 2),
            "Sqr": (3, 9),
            "Cube": (-3, -27),
            "Not": (4, -5),
            "Factorial": (5, 120),
        }
        cases = []
        for operator in INT_UNARY_OPERATIONS:
            given, expected = operation_cases[operator]
            cases.append((True, "constant", 99, operator, given, expected))
            cases.append((False, "constant", 99, operator, given, 99))

        operation = IntUnaryOperationConditional()
        for condition, fallback_mode, fallback_value, operator, given, expected in cases:
            with self.subTest(
                condition=condition, operator=operator, given=given, expected=expected
            ):
                result = operation.op(
                    condition, fallback_mode, fallback_value, operator, given
                )
                self.assertTrue(result, (expected,))  

#TODO fix tests
class IntBinaryOperationConditionalTest(unittest.TestCase):
    def test_true_condition_applies_operation(self) -> None:
        from src.comfymath.int import INT_BINARY_OPERATIONS

        operation_cases = {
            "Add": (20, 80, 100),
            "Sub": (20, 80, -60),
            "Mul": (2, 4, 10),
            "Div": (20, 80, 5),
            "Mod": (-100, 80, 60),
            "Pow": (-2, 2, 4),
            "Max": (-60, 20, 20),
            "Min": (-60, 20, -60),
            "And": (10, 4, 0 ),
            "Nand": (10, 3, -3 ),
            "Or": (4, 6, 6 ),
            "Nor": (4, 6, -7 ),
            "Xor": (-1, 2, -3 ),
            "Xnor": (4, 6, -3 ),
            "Shl": (4, 4, 64 ),
            "Shr": (-1, 2, -1 ),

            #TODO fix cases
        }
        cases = []
        for operator in INT_BINARY_OPERATIONS:
            given_a, given_b, expected = operation_cases[operator]
            cases.append(
                (True, "constant", 99, operator, given_a, given_b, expected)
            )
            cases.append(
                (False, "constant", 99, operator, given_a, given_b, 99)
            )

        operation = IntBinaryOperationConditional()
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
                self.assertTrue(result, (expected,))

if __name__ == "__main__":
    unittest.main()
