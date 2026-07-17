from typing import Any, Mapping


class ChooseInt:
    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "condition": ("BOOLEAN", {"default": False}),
                "a": ("INT", {"default": 0}),
                "b": ("INT", {"default": 0}),
            }
        }

    RETURN_TYPES = ("INT",)
    FUNCTION = "op"
    CATEGORY = "math/control"

    def op(self, condition: bool, a: int, b: int) -> tuple[int]:
        return (a if condition else b,)


class ChooseFloat:
    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "condition": ("BOOLEAN", {"default": False}),
                "a": ("FLOAT", {"default": 0.0, "step": 0.001, "round": False}),
                "b": ("FLOAT", {"default": 0.0, "step": 0.001, "round": False}),
            }
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "op"
    CATEGORY = "math/control"

    def op(self, condition: bool, a: float, b: float) -> tuple[float]:
        return (a if condition else b,)


NODE_CLASS_MAPPINGS: Mapping[str, Any] = {
    "CM_ChooseInt": ChooseInt,
    "CM_ChooseFloat": ChooseFloat,
}
