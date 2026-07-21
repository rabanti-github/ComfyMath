import unittest

from src.comfymath.bool import BoolBinaryOperation, BoolUnaryOperation

# Bool Unary Operation Tests
class BoolUnaryOperationTest(unittest.TestCase):
    def test_true_condition_applies_operation(self) -> None:
        cases = [
            ("Not", True, False),
            ("Not", False, True),
        ]
        operation = BoolUnaryOperation()
        for operator, given, expected in cases:
            with self.subTest(operator=operator, given=given, expected=expected,):
                result = operation.op(operator, given)
                self.assertEqual(result, (expected,))


# Bool Binary Operation Tests
class BoolBinaryOperationTest(unittest.TestCase):
    def test_true_condition_applies_operation(self) -> None:
        cases = [
            ("And", True, False, False),
            ("And", False, True, False),
            ("And", False, False, False),
            ("And", True, True, True),
            ("Or", True, False, True),
            ("Or", False, True, True),
            ("Or", False, False, False),
        ]
        operation = BoolBinaryOperation()
        for operator, givenA, givenB, expected in cases:
            with self.subTest(operator=operator, givenA=givenA, givenB=givenB, expected=expected,):
                result = operation.op(operator, givenA, givenB)
                self.assertEqual(result, (expected,))

if __name__ == "__main__":
    unittest.main()
