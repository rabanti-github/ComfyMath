import math
import random

from typing import Any, Callable, Mapping

INT_MIN = -9223372036854775808
INT_MAX = 9223372036854775807

DEFAULT_INT = ("INT", {"default": 0})
RANDOM_INT_VALUE = ("INT", {"default": 0, "min": INT_MIN, "max": INT_MAX})
RANDOM_INT_MIN = ("INT", {"default": -1, "min": INT_MIN, "max": INT_MAX})
RANDOM_INT_MAX = ("INT", {"default": 1, "min": INT_MIN, "max": INT_MAX})

RANDOM_INT_CONSTRAINTS = [
    "Full range",
    "1 to max Int",
    "0 to max Int",
    "Min int to -1",
    "Min int to 0",
    "Custom min/max",
]
RANDOM_INT_CONTROLS = ["Fixed", "Increment", "Decrement", "Randomize"]

INT_UNARY_OPERATIONS: Mapping[str, Callable[[int], int]] = {
    "Abs": lambda a: abs(a),
    "Neg": lambda a: -a,
    "Inc": lambda a: a + 1,
    "Dec": lambda a: a - 1,
    "Sqr": lambda a: a * a,
    "Cube": lambda a: a * a * a,
    "Not": lambda a: ~a,
    "Factorial": lambda a: math.factorial(a),
}

INT_UNARY_CONDITIONS: Mapping[str, Callable[[int], bool]] = {
    "IsZero": lambda a: a == 0,
    "IsNonZero": lambda a: a != 0,
    "IsPositive": lambda a: a > 0,
    "IsNegative": lambda a: a < 0,
    "IsEven": lambda a: a % 2 == 0,
    "IsOdd": lambda a: a % 2 == 1,
}

INT_BINARY_OPERATIONS: Mapping[str, Callable[[int, int], int]] = {
    "Add": lambda a, b: a + b,
    "Sub": lambda a, b: a - b,
    "Mul": lambda a, b: a * b,
    "Div": lambda a, b: a // b,
    "Mod": lambda a, b: a % b,
    "Pow": lambda a, b: a**b,
    "And": lambda a, b: a & b,
    "Nand": lambda a, b: ~(a & b),
    "Or": lambda a, b: a | b,
    "Nor": lambda a, b: ~(a | b),
    "Xor": lambda a, b: a ^ b,
    "Xnor": lambda a, b: ~(a ^ b),
    "Shl": lambda a, b: a << b,
    "Shr": lambda a, b: a >> b,
    "Max": lambda a, b: max(a, b),
    "Min": lambda a, b: min(a, b),
}

INT_BINARY_CONDITIONS: Mapping[str, Callable[[int, int], bool]] = {
    "Eq": lambda a, b: a == b,
    "Neq": lambda a, b: a != b,
    "Gt": lambda a, b: a > b,
    "Lt": lambda a, b: a < b,
    "Geq": lambda a, b: a >= b,
    "Leq": lambda a, b: a <= b,
}


def _random_int_bounds(constraint: str, minimum: int, maximum: int) -> tuple[int, int]:
    if constraint == "Custom min/max":
        return (minimum, maximum) if minimum <= maximum else (maximum, minimum)
    if constraint == "1 to max Int":
        return 1, INT_MAX
    if constraint == "0 to max Int":
        return 0, INT_MAX
    if constraint == "Min int to -1":
        return INT_MIN, -1
    if constraint == "Min int to 0":
        return INT_MIN, 0
    return INT_MIN, INT_MAX


def _clamp_int(value: int, minimum: int, maximum: int) -> int:
    return max(minimum, min(value, maximum))


class IntUnaryOperation:
    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {"op": (list(INT_UNARY_OPERATIONS.keys()),), "a": DEFAULT_INT}
        }

    RETURN_TYPES = ("INT",)
    FUNCTION = "op"
    CATEGORY = "math/int"
    DESCRIPTION = (
        "Applies a unary (one input) integer operation. Operations: Abs, Neg, Inc, Dec, Sqr, Cube, bitwise Not, Factorial."
    )

    def op(self, op: str, a: int) -> tuple[int]:
        return (INT_UNARY_OPERATIONS[op](a),)


class IntUnaryCondition:
    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {"op": (list(INT_UNARY_CONDITIONS.keys()),), "a": DEFAULT_INT}
        }

    RETURN_TYPES = ("BOOLEAN",)
    FUNCTION = "op"
    CATEGORY = "math/int"
    DESCRIPTION = (
        "Tests one integer value. Conditions: zero/non-zero, positive/negative, even/odd."
    )

    def op(self, op: str, a: int) -> tuple[bool]:
        return (INT_UNARY_CONDITIONS[op](a),)


class IntBinaryOperation:
    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "op": (list(INT_BINARY_OPERATIONS.keys()),),
                "a": DEFAULT_INT,
                "b": DEFAULT_INT,
            }
        }

    RETURN_TYPES = ("INT",)
    FUNCTION = "op"
    CATEGORY = "math/int"
    DESCRIPTION = (
        "Applies a binary (two inputs) integer operation. Operations include arithmetic, bitwise logic, shifts, Max, and Min."
    )


    def op(self, op: str, a: int, b: int) -> tuple[int]:
        return (INT_BINARY_OPERATIONS[op](a, b),)


class IntBinaryCondition:
    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "op": (list(INT_BINARY_CONDITIONS.keys()),),
                "a": DEFAULT_INT,
                "b": DEFAULT_INT,
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    FUNCTION = "op"
    CATEGORY = "math/int"
    DESCRIPTION = (
        "Compares two integer values. Conditions: Eq, Neq, Gt, Lt, Geq, Leq."
    )

    def op(self, op: str, a: int, b: int) -> tuple[bool]:
        return (INT_BINARY_CONDITIONS[op](a, b),)


class RandomInt:
    _rng = random.SystemRandom()

    def __init__(self) -> None:
        self._last_value: int | None = None
        self._last_input_value: int | None = None

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "value": RANDOM_INT_VALUE,
                "constraint": (RANDOM_INT_CONSTRAINTS,),
                "min": RANDOM_INT_MIN,
                "max": RANDOM_INT_MAX,
                "control_after_generation": (
                    RANDOM_INT_CONTROLS,
                    {"default": "Randomize"},
                ),
            }
        }

    RETURN_TYPES = ("INT",)
    FUNCTION = "op"
    CATEGORY = "math/int"
    DESCRIPTION = (
        "Returns a fixed, incremented, decremented, or randomized integer within the selected range constraint."
    )

    @classmethod
    def IS_CHANGED(
        cls,
        value: int,
        constraint: str,
        min: int,
        max: int,
        control_after_generation: str,
    ) -> float | bool:
        if control_after_generation == "Fixed":
            return False
        return float("NaN")

    def op(
        self,
        value: int,
        constraint: str,
        min: int,
        max: int,
        control_after_generation: str,
    ) -> dict[str, Any]:
        minimum, maximum = _random_int_bounds(constraint, min, max)
        provided_value = int(value)
        last_value = self._last_value

        if last_value is None or provided_value != self._last_input_value:
            last_value = provided_value
            self._last_input_value = provided_value

        if control_after_generation == "Fixed":
            next_value = provided_value
        elif control_after_generation == "Increment":
            next_value = _clamp_int(last_value + 1, minimum, maximum)
        elif control_after_generation == "Decrement":
            next_value = _clamp_int(last_value - 1, minimum, maximum)
        else:
            next_value = self._rng.randint(minimum, maximum)

        self._last_value = next_value
        return {"ui": {"value": [next_value]}, "result": (next_value,)}


def _int_fallback_binary(
    *, fallback_mode: str, a: int, b: int, fallback_value: int
) -> int:
    if fallback_mode == "A":
        return a
    if fallback_mode == "B":
        return b
    return fallback_value


def _int_fallback_unary(*, fallback_mode: str, a: int, fallback_value: int) -> int:
    if fallback_mode == "A":
        return a
    return fallback_value


class IntUnaryOperationConditional:
    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "condition": ("BOOLEAN", {"default": False}),
                "fallback_mode": (["A", "constant"],),
                "fallback_value": DEFAULT_INT,
                "op": (list(INT_UNARY_OPERATIONS.keys()),),
                "a": DEFAULT_INT,
            }
        }

    RETURN_TYPES = ("INT",)
    FUNCTION = "op"
    CATEGORY = "math/int"
    DESCRIPTION = (
        "Applies a unary (one int input, one fallback input) integer operation only when condition is true; otherwise returns a or fallback_value."
    )

    def op(
        self,
        condition: bool,
        fallback_mode: str,
        fallback_value: int,
        op: str,
        a: int,
    ) -> tuple[int]:
        if condition:
            return (INT_UNARY_OPERATIONS[op](a),)
        return (
            _int_fallback_unary(
                fallback_mode=fallback_mode, a=a, fallback_value=fallback_value
            ),
        )


class IntBinaryOperationConditional:
    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "condition": ("BOOLEAN", {"default": False}),
                "fallback_mode": (["A", "B", "constant"],),
                "fallback_value": DEFAULT_INT,
                "op": (list(INT_BINARY_OPERATIONS.keys()),),
                "a": DEFAULT_INT,
                "b": DEFAULT_INT,
            }
        }

    RETURN_TYPES = ("INT",)
    FUNCTION = "op"
    CATEGORY = "math/int"
    DESCRIPTION = (
        "Applies a binary (two int inputs, one fallback input) integer operation only when condition is true; otherwise returns a, b, or fallback_value."
    )

    def op(
        self,
        condition: bool,
        fallback_mode: str,
        fallback_value: int,
        op: str,
        a: int,
        b: int,
    ) -> tuple[int]:
        if condition:
            return (INT_BINARY_OPERATIONS[op](a, b),)
        return (
            _int_fallback_binary(
                fallback_mode=fallback_mode, a=a, b=b, fallback_value=fallback_value
            ),
        )


NODE_CLASS_MAPPINGS = {
    "CM_IntUnaryOperation": IntUnaryOperation,
    "CM_IntUnaryCondition": IntUnaryCondition,
    "CM_IntBinaryOperation": IntBinaryOperation,
    "CM_IntBinaryCondition": IntBinaryCondition,
    "CM_IntRandomNumber": RandomInt,
    "CM_IntUnaryOperationConditional": IntUnaryOperationConditional,
    "CM_IntBinaryOperationConditional": IntBinaryOperationConditional,
}
