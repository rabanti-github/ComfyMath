import unittest

from src.comfymath.control import ChooseFloat, ChooseInt


class ChooseIntTest(unittest.TestCase):
    def test_selects_expected_integer(self) -> None:
        cases = [
            (True, 0, 1, 0),
            (False, 0, 1, 1),
            (True, 1, -1, 1),
            (False, 1, -1, -1),
            (True, 99, -99, 99),
            (False, 99, -99, -99),
            (True, -1, -1, -1),
            (False, 0, 0, 0),
        ]
        operation = ChooseInt()

        for condition, a, b, expected in cases:
            with self.subTest(condition=condition, a=a, b=b, expected=expected):
                result = operation.op(condition, a, b)
                self.assertEqual(result, (expected,))
                self.assertIs(type(result[0]), int)

    def test_missing_required_argument_raises_type_error(self) -> None:
        operation = ChooseInt()

        with self.assertRaises(TypeError):
            operation.op(True, 1)  # type: ignore[call-arg]


class ChooseFloatTest(unittest.TestCase):
    def test_selects_expected_float(self) -> None:
        cases = [
            (True, 0.0, 1.0, 0.0),
            (False, 0.0, 1.0, 1.0),
            (True, 1.0, -1.0, 1.0),
            (False, 1.0, -1.0, -1.0),
            (True, 99.25, -99.25, 99.25),
            (False, 99.25, -99.25, -99.25),
            (True, -1.5, -1.5, -1.5),
            (False, 0.0, 0.0, 0.0),
        ]
        operation = ChooseFloat()

        for condition, a, b, expected in cases:
            with self.subTest(condition=condition, a=a, b=b, expected=expected):
                result = operation.op(condition, a, b)
                self.assertEqual(result, (expected,))
                self.assertIs(type(result[0]), float)

    def test_missing_required_argument_raises_type_error(self) -> None:
        operation = ChooseFloat()

        with self.assertRaises(TypeError):
            operation.op(False, 1.0)  # type: ignore[call-arg]


class ControlNodeMetadataTest(unittest.TestCase):
    def test_input_types_expose_all_operation_arguments_as_required(self) -> None:
        cases = [ChooseInt, ChooseFloat]

        for node_class in cases:
            with self.subTest(node_class=node_class.__name__):
                input_types = node_class.INPUT_TYPES()
                self.assertEqual(set(input_types), {"required"})
                self.assertEqual(
                    set(input_types["required"]), {"condition", "a", "b"}
                )


if __name__ == "__main__":
    unittest.main()
