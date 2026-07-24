import math
import unittest
import warnings
from numbers import Real

import numpy

from src.comfymath.vec import (
    NODE_CLASS_MAPPINGS,
    Vec2BinaryCondition,
    Vec2BinaryOperation,
    Vec2ScalarOperation,
    Vec2ToScalarBinaryOperation,
    Vec2ToScalarUnaryOperation,
    Vec2UnaryCondition,
    Vec2UnaryOperation,
    Vec3BinaryCondition,
    Vec3BinaryOperation,
    Vec3ScalarOperation,
    Vec3ToScalarBinaryOperation,
    Vec3ToScalarUnaryOperation,
    Vec3UnaryCondition,
    Vec3UnaryOperation,
    Vec4BinaryCondition,
    Vec4BinaryOperation,
    Vec4ScalarOperation,
    Vec4ToScalarBinaryOperation,
    Vec4ToScalarUnaryOperation,
    Vec4UnaryCondition,
    Vec4UnaryOperation,
)


UNARY_OPERATION_NODES = [
    (Vec2UnaryOperation, 2),
    (Vec3UnaryOperation, 3),
    (Vec4UnaryOperation, 4),
]

TO_SCALAR_UNARY_OPERATION_NODES = [
    (Vec2ToScalarUnaryOperation, 2),
    (Vec3ToScalarUnaryOperation, 3),
    (Vec4ToScalarUnaryOperation, 4),
]

UNARY_CONDITION_NODES = [
    (Vec2UnaryCondition, 2),
    (Vec3UnaryCondition, 3),
    (Vec4UnaryCondition, 4),
]

BINARY_OPERATION_NODES = [
    (Vec2BinaryOperation, 2),
    (Vec3BinaryOperation, 3),
    (Vec4BinaryOperation, 4),
]

TO_SCALAR_BINARY_OPERATION_NODES = [
    (Vec2ToScalarBinaryOperation, 2),
    (Vec3ToScalarBinaryOperation, 3),
    (Vec4ToScalarBinaryOperation, 4),
]

BINARY_CONDITION_NODES = [
    (Vec2BinaryCondition, 2),
    (Vec3BinaryCondition, 3),
    (Vec4BinaryCondition, 4),
]

SCALAR_OPERATION_NODES = [
    (Vec2ScalarOperation, 2),
    (Vec3ScalarOperation, 3),
    (Vec4ScalarOperation, 4),
]


class VectorTestCase(unittest.TestCase):
    def assertVectorAlmostEqual(
        self, actual: tuple[float, ...], expected: tuple[float, ...]
    ) -> None:
        self.assertEqual(len(actual), len(expected))
        for actual_component, expected_component in zip(actual, expected):
            self.assertAlmostEqual(actual_component, expected_component, places=12)


class VecUnaryOperationTest(VectorTestCase):
    def test_negates_vectors(self) -> None:
        cases = [
            (Vec2UnaryOperation, (0.0, 99.0), (-0.0, -99.0)),
            (Vec3UnaryOperation, (0.0, 1.0, -1.0), (-0.0, -1.0, 1.0)),
            (
                Vec4UnaryOperation,
                (0.0, 1.0, -1.0, 99.0),
                (-0.0, -1.0, 1.0, -99.0),
            ),
        ]

        for node_class, given, expected in cases:
            with self.subTest(node_class=node_class.__name__, given=given):
                self.assertEqual(node_class().op("Neg", given), (expected,))

    def test_normalizes_vectors(self) -> None:
        cases = [
            (Vec2UnaryOperation, (3.0, 4.0), (0.6, 0.8)),
            (Vec3UnaryOperation, (0.0, 3.0, 4.0), (0.0, 0.6, 0.8)),
            (Vec4UnaryOperation, (0.0, 0.0, 3.0, 4.0), (0.0, 0.0, 0.6, 0.8)),
        ]

        for node_class, given, expected in cases:
            with self.subTest(node_class=node_class.__name__, given=given):
                result = node_class().op("Normalize", given)
                self.assertVectorAlmostEqual(result[0], expected)

    def test_normalizing_zero_vector_returns_non_finite_components(self) -> None:
        for node_class, dimensions in UNARY_OPERATION_NODES:
            given = (0.0,) * dimensions
            with self.subTest(node_class=node_class.__name__):
                with numpy.errstate(divide="ignore", invalid="ignore"):
                    result = node_class().op("Normalize", given)
                self.assertTrue(all(math.isnan(component) for component in result[0]))


class VecToScalarUnaryOperationTest(unittest.TestCase):
    def test_calculates_norm(self) -> None:
        cases = [
            (Vec2ToScalarUnaryOperation, (0.0, 0.0), 0.0),
            (Vec2ToScalarUnaryOperation, (3.0, 4.0), 5.0),
            (Vec3ToScalarUnaryOperation, (0.0, 3.0, 4.0), 5.0),
            (Vec4ToScalarUnaryOperation, (0.0, 0.0, 3.0, 4.0), 5.0),
            (Vec4ToScalarUnaryOperation, (99.0, 0.0, 0.0, 0.0), 99.0),
        ]

        for node_class, given, expected in cases:
            with self.subTest(node_class=node_class.__name__, given=given):
                result = node_class().op("Norm", given)
                self.assertEqual(result, (expected,))
                self.assertIsInstance(result[0], Real)


class VecUnaryConditionTest(unittest.TestCase):
    def test_evaluates_unary_conditions(self) -> None:
        for node_class, dimensions in UNARY_CONDITION_NODES:
            zero = (0.0,) * dimensions
            unit = (1.0,) + (0.0,) * (dimensions - 1)
            non_unit = (99.0,) + (0.0,) * (dimensions - 1)
            cases = [
                ("IsZero", zero, True),
                ("IsZero", unit, False),
                ("IsNotZero", zero, False),
                ("IsNotZero", non_unit, True),
                ("IsNormalized", unit, True),
                ("IsNormalized", non_unit, False),
                ("IsNotNormalized", unit, False),
                ("IsNotNormalized", non_unit, True),
            ]

            for operator, given, expected in cases:
                with self.subTest(
                    node_class=node_class.__name__, operator=operator, given=given
                ):
                    self.assertEqual(node_class().op(operator, given), (expected,))


class VecBinaryOperationTest(unittest.TestCase):
    def test_adds_and_subtracts_vectors(self) -> None:
        cases = [
            (
                Vec2BinaryOperation,
                (0.0, 99.0),
                (1.0, -1.0),
                (1.0, 98.0),
                (-1.0, 100.0),
            ),
            (
                Vec3BinaryOperation,
                (0.0, 1.0, -1.0),
                (99.0, -1.0, 1.0),
                (99.0, 0.0, 0.0),
                (-99.0, 2.0, -2.0),
            ),
            (
                Vec4BinaryOperation,
                (0.0, 1.0, -1.0, 99.0),
                (1.0, -1.0, 99.0, 0.0),
                (1.0, 0.0, 98.0, 99.0),
                (-1.0, 2.0, -100.0, 99.0),
            ),
        ]

        for node_class, a, b, expected_add, expected_sub in cases:
            for operator, expected in [("Add", expected_add), ("Sub", expected_sub)]:
                with self.subTest(node_class=node_class.__name__, operator=operator):
                    self.assertEqual(node_class().op(operator, a, b), (expected,))

    def test_vec3_cross_product(self) -> None:
        cases = [
            ((1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0)),
            ((1.0, -1.0, 0.0), (0.0, 1.0, -1.0), (1.0, 1.0, 1.0)),
            ((0.0, 0.0, 0.0), (99.0, -1.0, 1.0), (0.0, 0.0, -0.0)),
        ]
        operation = Vec3BinaryOperation()

        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(operation.op("Cross", a, b), (expected,))

    def test_cross_product_rejects_unsupported_dimensions(self) -> None:
        cases = [
            (Vec2BinaryOperation(), (1.0, 0.0), (0.0, 1.0), IndexError),
            (
                Vec4BinaryOperation(),
                (1.0, 0.0, 0.0, 0.0),
                (0.0, 1.0, 0.0, 0.0),
                ValueError,
            ),
        ]

        for operation, a, b, expected_exception in cases:
            with self.subTest(node_class=type(operation).__name__):
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore", DeprecationWarning)
                    with self.assertRaises(expected_exception):
                        operation.op("Cross", a, b)


class VecToScalarBinaryOperationTest(unittest.TestCase):
    def test_calculates_dot_product_and_distance(self) -> None:
        for node_class, dimensions in TO_SCALAR_BINARY_OPERATION_NODES:
            a = (1.0, -1.0) + (0.0,) * (dimensions - 2)
            b = (-1.0, 1.0) + (0.0,) * (dimensions - 2)
            cases = [("Dot", -2.0), ("Distance", math.sqrt(8.0))]

            for operator, expected in cases:
                with self.subTest(node_class=node_class.__name__, operator=operator):
                    result = node_class().op(operator, a, b)
                    self.assertAlmostEqual(result[0], expected, places=12)
                    self.assertIsInstance(result[0], Real)


class VecBinaryConditionTest(unittest.TestCase):
    def test_evaluates_binary_conditions(self) -> None:
        for node_class, dimensions in BINARY_CONDITION_NODES:
            a = (0.0, 1.0, -1.0, 99.0)[:dimensions]
            close = tuple(value + 1e-8 for value in a)
            different = tuple(value + 1.0 for value in a)
            cases = [
                ("Eq", a, a, True),
                ("Eq", a, close, True),
                ("Eq", a, different, False),
                ("Neq", a, a, False),
                ("Neq", a, different, True),
            ]

            for operator, left, right, expected in cases:
                with self.subTest(node_class=node_class.__name__, operator=operator):
                    self.assertEqual(
                        node_class().op(operator, left, right), (expected,)
                    )


class VecScalarOperationTest(unittest.TestCase):
    def test_multiplies_and_divides_by_scalar(self) -> None:
        cases = [
            (Vec2ScalarOperation, (99.0, -1.0)),
            (Vec3ScalarOperation, (0.0, 1.0, -1.0)),
            (Vec4ScalarOperation, (0.0, 1.0, -1.0, 99.0)),
        ]

        for node_class, given in cases:
            expected_mul = tuple(value * -1.0 for value in given)
            expected_div = tuple(value / 2.0 for value in given)
            operations = [("Mul", -1.0, expected_mul), ("Div", 2.0, expected_div)]

            for operator, scalar, expected in operations:
                with self.subTest(node_class=node_class.__name__, operator=operator):
                    self.assertEqual(
                        node_class().op(operator, given, scalar), (expected,)
                    )

    def test_dividing_by_zero_returns_non_finite_components(self) -> None:
        for node_class, dimensions in SCALAR_OPERATION_NODES:
            given = (1.0,) * dimensions
            with self.subTest(node_class=node_class.__name__):
                with numpy.errstate(divide="ignore", invalid="ignore"):
                    result = node_class().op("Div", given, 0.0)
                self.assertTrue(all(math.isinf(component) for component in result[0]))


class VecInvalidOperatorTest(unittest.TestCase):
    def test_unknown_operator_raises_key_error_for_every_node(self) -> None:
        unary_families = (
            UNARY_OPERATION_NODES
            + TO_SCALAR_UNARY_OPERATION_NODES
            + UNARY_CONDITION_NODES
        )
        binary_families = (
            BINARY_OPERATION_NODES
            + TO_SCALAR_BINARY_OPERATION_NODES
            + BINARY_CONDITION_NODES
        )

        for node_class, dimensions in unary_families:
            with self.subTest(node_class=node_class.__name__):
                with self.assertRaises(KeyError):
                    node_class().op("Unknown", (0.0,) * dimensions)

        for node_class, dimensions in binary_families:
            zero = (0.0,) * dimensions
            with self.subTest(node_class=node_class.__name__):
                with self.assertRaises(KeyError):
                    node_class().op("Unknown", zero, zero)

        for node_class, dimensions in SCALAR_OPERATION_NODES:
            with self.subTest(node_class=node_class.__name__):
                with self.assertRaises(KeyError):
                    node_class().op("Unknown", (0.0,) * dimensions, 1.0)


class VecNodeMetadataTest(unittest.TestCase):
    def test_input_types_for_every_registered_vector_node(self) -> None:
        self.assertEqual(len(NODE_CLASS_MAPPINGS), 21)

        for mapping_name, node_class in NODE_CLASS_MAPPINGS.items():
            with self.subTest(mapping_name=mapping_name):
                input_types = node_class.INPUT_TYPES()
                self.assertEqual(set(input_types), {"required"})
                self.assertIn("op", input_types["required"])
                self.assertIn("a", input_types["required"])


if __name__ == "__main__":
    unittest.main()
