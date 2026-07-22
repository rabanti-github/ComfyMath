from typing import Any, Callable, Mapping

from .float import (
    FLOAT_UNARY_OPERATIONS,
    FLOAT_UNARY_CONDITIONS,
    FLOAT_BINARY_OPERATIONS,
    FLOAT_BINARY_CONDITIONS,
)
from .types import Number

DEFAULT_NUMBER = ("NUMBER", {"default": 0.0})


class NumberUnaryOperation:
    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "op": (list(FLOAT_UNARY_OPERATIONS.keys()),),
                "a": DEFAULT_NUMBER,
            }
        }

    RETURN_TYPES = ("NUMBER",)
    FUNCTION = "op"
    CATEGORY = "math/number"

    def op(self, op: str, a: Number) -> tuple[float]:
        return (FLOAT_UNARY_OPERATIONS[op](float(a)),)


class NumberUnaryCondition:
    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "op": (list(FLOAT_UNARY_CONDITIONS.keys()),),
                "a": DEFAULT_NUMBER,
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    FUNCTION = "op"
    CATEGORY = "math/number"

    def op(self, op: str, a: Number) -> tuple[bool]:
        return (FLOAT_UNARY_CONDITIONS[op](float(a)),)


class NumberBinaryOperation:
    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "op": (list(FLOAT_BINARY_OPERATIONS.keys()),),
                "a": DEFAULT_NUMBER,
                "b": DEFAULT_NUMBER,
            }
        }

    RETURN_TYPES = ("NUMBER",)
    FUNCTION = "op"
    CATEGORY = "math/number"

    def op(self, op: str, a: Number, b: Number) -> tuple[float]:
        return (FLOAT_BINARY_OPERATIONS[op](float(a), float(b)),)


class NumberBinaryCondition:
    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "op": (list(FLOAT_BINARY_CONDITIONS.keys()),),
                "a": DEFAULT_NUMBER,
                "b": DEFAULT_NUMBER,
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    FUNCTION = "op"
    CATEGORY = "math/number"

    def op(self, op: str, a: Number, b: Number) -> tuple[bool]:
        return (FLOAT_BINARY_CONDITIONS[op](float(a), float(b)),)


def _number_fallback_binary(
    *, fallback_mode: str, a: Number, b: Number, fallback_value: Number
) -> Number:
    if fallback_mode == "A":
        return a
    if fallback_mode == "B":
        return b
    return fallback_value


def _number_fallback_unary(
    *, fallback_mode: str, a: Number, fallback_value: Number
) -> Number:
    if fallback_mode == "A":
        return a
    return fallback_value


class NumberUnaryOperationConditional:
    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "condition": ("BOOLEAN", {"default": False}),
                "fallback_mode": (["A", "constant"],),
                "fallback_value": DEFAULT_NUMBER,
                "op": (list(FLOAT_UNARY_OPERATIONS.keys()),),
                "a": DEFAULT_NUMBER,
            }
        }

    RETURN_TYPES = ("NUMBER",)
    FUNCTION = "op"
    CATEGORY = "math/number"

    def op(
        self,
        condition: bool,
        fallback_mode: str,
        fallback_value: Number,
        op: str,
        a: Number,
    ) -> tuple[Number]:
        if condition:
            return (FLOAT_UNARY_OPERATIONS[op](float(a)),)
        return (
            _number_fallback_unary(
                fallback_mode=fallback_mode, a=a, fallback_value=fallback_value
            ),
        )


class NumberBinaryOperationConditional:
    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "condition": ("BOOLEAN", {"default": False}),
                "fallback_mode": (["A", "B", "constant"],),
                "fallback_value": DEFAULT_NUMBER,
                "op": (list(FLOAT_BINARY_OPERATIONS.keys()),),
                "a": DEFAULT_NUMBER,
                "b": DEFAULT_NUMBER,
            }
        }

    RETURN_TYPES = ("NUMBER",)
    FUNCTION = "op"
    CATEGORY = "math/number"

    def op(
        self,
        condition: bool,
        fallback_mode: str,
        fallback_value: Number,
        op: str,
        a: Number,
        b: Number,
    ) -> tuple[Number]:
        if condition:
            return (FLOAT_BINARY_OPERATIONS[op](float(a), float(b)),)
        return (
            _number_fallback_binary(
                fallback_mode=fallback_mode, a=a, b=b, fallback_value=fallback_value
            ),
        )


NODE_CLASS_MAPPINGS = {
    "CM_NumberUnaryOperation": NumberUnaryOperation,
    "CM_NumberUnaryCondition": NumberUnaryCondition,
    "CM_NumberBinaryOperation": NumberBinaryOperation,
    "CM_NumberBinaryCondition": NumberBinaryCondition,
    "CM_NumberUnaryOperationConditional": NumberUnaryOperationConditional,
    "CM_NumberBinaryOperationConditional": NumberBinaryOperationConditional,
}
