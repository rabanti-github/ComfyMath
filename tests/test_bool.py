import unittest

from src.comfymath.bool import BoolBinaryOperation, BoolUnaryOperation


class BoolUnaryOperationTest(unittest.TestCase):
    def test_not_true_returns_false(self) -> None:
        self.assertEqual(BoolUnaryOperation().op("Not", True), (False,))

    def test_not_false_returns_true(self) -> None:
        self.assertEqual(BoolUnaryOperation().op("Not", False), (True,))


class BoolBinaryOperationTest(unittest.TestCase):
    def test_and_true_false_returns_false(self) -> None:
        self.assertEqual(BoolBinaryOperation().op("And", True, False), (False,))

    def test_and_false_true_returns_false(self) -> None:
        self.assertEqual(BoolBinaryOperation().op("And", False, True), (False,))

    def test_and_false_false_returns_false(self) -> None:
        self.assertEqual(BoolBinaryOperation().op("And", False, False), (False,))

    def test_and_true_true_returns_true(self) -> None:
        self.assertEqual(BoolBinaryOperation().op("And", True, True), (True,))


    def test_or_true_false_returns_true(self) -> None:
        self.assertEqual(BoolBinaryOperation().op("Or", True, False), (True,))

    def test_or_false_true_returns_true(self) -> None:
        self.assertEqual(BoolBinaryOperation().op("Or", False, True), (True,))

    def test_or_false_false_returns_false(self) -> None:
        self.assertEqual(BoolBinaryOperation().op("Or", False, False), (False,))


if __name__ == "__main__":
    unittest.main()
