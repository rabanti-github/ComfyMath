import unittest

from src.comfymath.convert import (
    BoolToInt,
    BreakoutVec2,
    BreakoutVec3,
    BreakoutVec4,
    ComposeVec2,
    ComposeVec3,
    ComposeVec4,
    FillVec2,
    FillVec3,
    FillVec4,
    FloatToInt,
    FloatToNumber,
    IntToBool,
    IntToFloat,
    IntToNumber,
    NumberToFloat,
    NumberToInt,
)


class ScalarConversionTest(unittest.TestCase):
    def test_bool_to_int(self) -> None:
        cases = [(False, 0), (True, 1)]
        operation = BoolToInt()

        for given, expected in cases:
            with self.subTest(given=given, expected=expected):
                result = operation.op(given)
                self.assertEqual(result, (expected,))
                self.assertIs(type(result[0]), int)

    def test_int_to_bool(self) -> None:
        cases = [
            (0, False),
            (1, True),
            (-1, True),
            (99, True),
            (-99, True),
        ]
        operation = IntToBool()

        for given, expected in cases:
            with self.subTest(given=given, expected=expected):
                result = operation.op(given)
                self.assertEqual(result, (expected,))
                self.assertIs(type(result[0]), bool)

    def test_float_to_int_truncates_towards_zero(self) -> None:
        cases = [
            (0.0, 0),
            (1.0, 1),
            (-1.0, -1),
            (1.99, 1),
            (-1.99, -1),
            (99.75, 99),
        ]
        operation = FloatToInt()

        for given, expected in cases:
            with self.subTest(given=given, expected=expected):
                result = operation.op(given)
                self.assertEqual(result, (expected,))
                self.assertIs(type(result[0]), int)

    def test_float_to_int_rejects_non_finite_values(self) -> None:
        cases = [
            (float("nan"), ValueError),
            (float("inf"), OverflowError),
            (float("-inf"), OverflowError),
        ]
        operation = FloatToInt()

        for given, expected_exception in cases:
            with self.subTest(given=given, expected_exception=expected_exception):
                with self.assertRaises(expected_exception):
                    operation.op(given)

    def test_int_to_float(self) -> None:
        cases = [(0, 0.0), (1, 1.0), (-1, -1.0), (99, 99.0), (-99, -99.0)]
        operation = IntToFloat()

        for given, expected in cases:
            with self.subTest(given=given, expected=expected):
                result = operation.op(given)
                self.assertEqual(result, (expected,))
                self.assertIs(type(result[0]), float)

    def test_int_to_number_preserves_integer_value_and_type(self) -> None:
        cases = [0, 1, -1, 99, -99]
        operation = IntToNumber()

        for given in cases:
            with self.subTest(given=given):
                result = operation.op(given)
                self.assertEqual(result, (given,))
                self.assertIs(type(result[0]), int)

    def test_number_to_int_truncates_float_values(self) -> None:
        cases = [
            (0, 0),
            (1, 1),
            (-1, -1),
            (99, 99),
            (1.99, 1),
            (-1.99, -1),
        ]
        operation = NumberToInt()

        for given, expected in cases:
            with self.subTest(given=given, expected=expected):
                result = operation.op(given)
                self.assertEqual(result, (expected,))
                self.assertIs(type(result[0]), int)

    def test_number_to_int_rejects_non_finite_values(self) -> None:
        cases = [
            (float("nan"), ValueError),
            (float("inf"), OverflowError),
            (float("-inf"), OverflowError),
        ]
        operation = NumberToInt()

        for given, expected_exception in cases:
            with self.subTest(given=given, expected_exception=expected_exception):
                with self.assertRaises(expected_exception):
                    operation.op(given)

    def test_float_to_number_preserves_float_value_and_type(self) -> None:
        cases = [0.0, 1.0, -1.0, 99.75, -99.75]
        operation = FloatToNumber()

        for given in cases:
            with self.subTest(given=given):
                result = operation.op(given)
                self.assertEqual(result, (given,))
                self.assertIs(type(result[0]), float)

    def test_number_to_float(self) -> None:
        cases = [
            (0, 0.0),
            (1, 1.0),
            (-1, -1.0),
            (99, 99.0),
            (1.25, 1.25),
            (-1.25, -1.25),
        ]
        operation = NumberToFloat()

        for given, expected in cases:
            with self.subTest(given=given, expected=expected):
                result = operation.op(given)
                self.assertEqual(result, (expected,))
                self.assertIs(type(result[0]), float)


class VectorConversionTest(unittest.TestCase):
    def test_compose_vec2(self) -> None:
        cases = [
            ((0.0, 0.0), ((0.0, 0.0),)),
            ((1.0, -1.0), ((1.0, -1.0),)),
            ((99.5, -99.5), ((99.5, -99.5),)),
        ]
        operation = ComposeVec2()

        for given, expected in cases:
            with self.subTest(given=given, expected=expected):
                self.assertEqual(operation.op(*given), expected)

    def test_fill_vec2(self) -> None:
        cases = [(0.0, ((0.0, 0.0),)), (1.0, ((1.0, 1.0),)), (-99.5, ((-99.5, -99.5),))]
        operation = FillVec2()

        for given, expected in cases:
            with self.subTest(given=given, expected=expected):
                self.assertEqual(operation.op(given), expected)

    def test_breakout_vec2(self) -> None:
        cases = [((0.0, 0.0), (0.0, 0.0)), ((1.0, -1.0), (1.0, -1.0)), ((99.5, -99.5), (99.5, -99.5))]
        operation = BreakoutVec2()

        for given, expected in cases:
            with self.subTest(given=given, expected=expected):
                self.assertEqual(operation.op(given), expected)

    def test_compose_vec3(self) -> None:
        cases = [
            ((0.0, 0.0, 0.0), ((0.0, 0.0, 0.0),)),
            ((1.0, -1.0, 99.0), ((1.0, -1.0, 99.0),)),
        ]
        operation = ComposeVec3()

        for given, expected in cases:
            with self.subTest(given=given, expected=expected):
                self.assertEqual(operation.op(*given), expected)

    def test_fill_vec3(self) -> None:
        cases = [(0.0, ((0.0, 0.0, 0.0),)), (1.0, ((1.0, 1.0, 1.0),)), (-99.5, ((-99.5, -99.5, -99.5),))]
        operation = FillVec3()

        for given, expected in cases:
            with self.subTest(given=given, expected=expected):
                self.assertEqual(operation.op(given), expected)

    def test_breakout_vec3(self) -> None:
        cases = [
            ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
            ((1.0, -1.0, 99.0), (1.0, -1.0, 99.0)),
        ]
        operation = BreakoutVec3()

        for given, expected in cases:
            with self.subTest(given=given, expected=expected):
                self.assertEqual(operation.op(given), expected)

    def test_compose_vec4(self) -> None:
        cases = [
            ((0.0, 0.0, 0.0, 0.0), ((0.0, 0.0, 0.0, 0.0),)),
            ((1.0, -1.0, 99.0, -99.0), ((1.0, -1.0, 99.0, -99.0),)),
        ]
        operation = ComposeVec4()

        for given, expected in cases:
            with self.subTest(given=given, expected=expected):
                self.assertEqual(operation.op(*given), expected)

    def test_fill_vec4(self) -> None:
        cases = [
            (0.0, ((0.0, 0.0, 0.0, 0.0),)),
            (1.0, ((1.0, 1.0, 1.0, 1.0),)),
            (-99.5, ((-99.5, -99.5, -99.5, -99.5),)),
        ]
        operation = FillVec4()

        for given, expected in cases:
            with self.subTest(given=given, expected=expected):
                self.assertEqual(operation.op(given), expected)

    def test_breakout_vec4(self) -> None:
        cases = [
            ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)),
            ((1.0, -1.0, 99.0, -99.0), (1.0, -1.0, 99.0, -99.0)),
        ]
        operation = BreakoutVec4()

        for given, expected in cases:
            with self.subTest(given=given, expected=expected):
                self.assertEqual(operation.op(given), expected)

    def test_breakout_rejects_vectors_with_too_few_components(self) -> None:
        cases = [
            (BreakoutVec2(), (1.0,)),
            (BreakoutVec3(), (1.0, 2.0)),
            (BreakoutVec4(), (1.0, 2.0, 3.0)),
        ]

        for operation, given in cases:
            with self.subTest(operation=type(operation).__name__, given=given):
                with self.assertRaises(IndexError):
                    operation.op(given)  # type: ignore[arg-type]


class ConversionNodeMetadataTest(unittest.TestCase):
    def test_input_types_expose_all_operation_arguments_as_required(self) -> None:
        cases = [
            (BoolToInt, {"a"}),
            (IntToBool, {"a"}),
            (FloatToInt, {"a"}),
            (IntToFloat, {"a"}),
            (IntToNumber, {"a"}),
            (NumberToInt, {"a"}),
            (FloatToNumber, {"a"}),
            (NumberToFloat, {"a"}),
            (ComposeVec2, {"x", "y"}),
            (FillVec2, {"a"}),
            (BreakoutVec2, {"a"}),
            (ComposeVec3, {"x", "y", "z"}),
            (FillVec3, {"a"}),
            (BreakoutVec3, {"a"}),
            (ComposeVec4, {"x", "y", "z", "w"}),
            (FillVec4, {"a"}),
            (BreakoutVec4, {"a"}),
        ]

        for node_class, expected_arguments in cases:
            with self.subTest(node_class=node_class.__name__):
                input_types = node_class.INPUT_TYPES()
                self.assertEqual(set(input_types), {"required"})
                self.assertEqual(set(input_types["required"]), expected_arguments)


if __name__ == "__main__":
    unittest.main()
