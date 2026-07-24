from abc import ABC, abstractmethod
import math
from typing import Any, Mapping, Sequence, Tuple

ResolutionPreset = Tuple[int, int, float]

ASPECT_RATIOS = (
    "1:1",
    "16:9",
    "9:16",
    "4:3",
    "3:4",
    "3:2",
    "2:3",
    "4:5",
    "5:4",
    "21:9",
    "9:21",
)


def _with_aspect_ratios(
    resolutions: Sequence[Tuple[int, int]],
) -> list[ResolutionPreset]:
    return [(width, height, width / height) for width, height in resolutions]


SDXL_SUPPORTED_RESOLUTIONS = _with_aspect_ratios(
    [
        (1024, 1024),
        (1152, 896),
        (896, 1152),
        (1216, 832),
        (832, 1216),
        (1344, 768),
        (768, 1344),
        (1536, 640),
        (640, 1536),
    ]
)

SDXL_EXTENDED_RESOLUTIONS = _with_aspect_ratios(
    [
        (512, 2048),
        (512, 1984),
        (512, 1920),
        (512, 1856),
        (576, 1792),
        (576, 1728),
        (576, 1664),
        (640, 1600),
        (640, 1536),
        (704, 1472),
        (704, 1408),
        (704, 1344),
        (768, 1344),
        (768, 1280),
        (832, 1216),
        (832, 1152),
        (896, 1152),
        (896, 1088),
        (960, 1088),
        (960, 1024),
        (1024, 1024),
        (1024, 960),
        (1088, 960),
        (1088, 896),
        (1152, 896),
        (1152, 832),
        (1216, 832),
        (1280, 768),
        (1344, 768),
        (1408, 704),
        (1472, 704),
        (1536, 640),
        (1600, 640),
        (1664, 576),
        (1728, 576),
        (1792, 576),
        (1856, 512),
        (1920, 512),
        (1984, 512),
        (2048, 512),
    ]
)


def _round_to_multiple(value: float, multiple: int) -> int:
    if multiple <= 0:
        raise ValueError("multiple must be greater than zero")
    return max(multiple, math.floor(value / multiple + 0.5) * multiple)


def _calculate_resolution(
    aspect_ratio: float, megapixels: float, multiple: int
) -> tuple[int, int]:
    if not math.isfinite(aspect_ratio) or aspect_ratio <= 0:
        raise ValueError("aspect ratio must be finite and greater than zero")
    if not math.isfinite(megapixels) or megapixels <= 0:
        raise ValueError("megapixels must be finite and greater than zero")
    if multiple <= 0:
        raise ValueError("multiple must be greater than zero")

    target_pixels = megapixels * 1024 * 1024
    ideal_width = math.sqrt(target_pixels * aspect_ratio)
    ideal_height = math.sqrt(target_pixels / aspect_ratio)
    return (
        _round_to_multiple(ideal_width, multiple),
        _round_to_multiple(ideal_height, multiple),
    )


class Resolution(ABC):
    @classmethod
    @abstractmethod
    def resolutions(cls) -> Sequence[ResolutionPreset]:
        ...

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "resolution": ([f"{res[0]}x{res[1]}" for res in cls.resolutions()],)
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "op"
    CATEGORY = "math/graphics"
    DESCRIPTION = (
        "Selects one of the standard or extended SDXL width/height presets."
    )

    def op(self, resolution: str) -> tuple[int, int]:
        width, height = resolution.split("x")
        return (int(width), int(height))


class NearestResolution(ABC):
    @classmethod
    @abstractmethod
    def resolutions(cls) -> Sequence[ResolutionPreset]:
        ...

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {"required": {"image": ("IMAGE",)}}

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "op"
    CATEGORY = "math/graphics"
    DESCRIPTION = (
        "Chooses the standard or extended SDXL preset whose aspect ratio is "
        "nearest to the input image."
    )

    def op(self, image: Any) -> tuple[int, int]:
        image_size = image.size()
        image_width = image_size[2]
        image_height = image_size[1]
        if image_width <= 0 or image_height <= 0:
            raise ValueError("image dimensions must be greater than zero")

        resolutions = self.resolutions()
        if not resolutions:
            return (1024, 1024)

        image_ratio = image_width / image_height
        nearest = min(
            resolutions,
            key=lambda resolution: abs(
                image_ratio - resolution[0] / resolution[1]
            ),
        )
        return (nearest[0], nearest[1])


class SDXLResolution(Resolution):
    @classmethod
    def resolutions(cls) -> Sequence[ResolutionPreset]:
        return SDXL_SUPPORTED_RESOLUTIONS


class SDXLExtendedResolution(Resolution):
    @classmethod
    def resolutions(cls) -> Sequence[ResolutionPreset]:
        return SDXL_EXTENDED_RESOLUTIONS


class NearestSDXLResolution(NearestResolution):
    @classmethod
    def resolutions(cls) -> Sequence[ResolutionPreset]:
        return SDXL_SUPPORTED_RESOLUTIONS


class NearestSDXLExtendedResolution(NearestResolution):
    @classmethod
    def resolutions(cls) -> Sequence[ResolutionPreset]:
        return SDXL_EXTENDED_RESOLUTIONS


class AspectRatioResolution:
    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "aspect_ratio": (list(ASPECT_RATIOS),),
                "megapixels": (
                    "FLOAT",
                    {"default": 1.0, "min": 0.01, "step": 0.05, "round": False},
                ),
                "multiple": ("INT", {"default": 16, "min": 1, "max": 512}),
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "op"
    CATEGORY = "math/graphics"
    DESCRIPTION = (
        "Calculates a resolution from an aspect ratio, target megapixels, and "
        "pixel multiple."
    )

    def op(
        self, aspect_ratio: str, megapixels: float, multiple: int
    ) -> tuple[int, int]:
        ratio_width, ratio_height = aspect_ratio.split(":")
        width = float(ratio_width)
        height = float(ratio_height)
        if width <= 0 or height <= 0:
            raise ValueError("aspect ratio components must be greater than zero")
        return _calculate_resolution(width / height, megapixels, multiple)


class ImageAspectResolution:
    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "image": ("IMAGE",),
                "megapixels": (
                    "FLOAT",
                    {"default": 1.0, "min": 0.01, "step": 0.05, "round": False},
                ),
                "multiple": ("INT", {"default": 16, "min": 1, "max": 512}),
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "op"
    CATEGORY = "math/graphics"
    DESCRIPTION = (
        "Calculates a resolution from an image aspect ratio, target megapixels, "
        "and pixel multiple."
    )

    def op(self, image: Any, megapixels: float, multiple: int) -> tuple[int, int]:
        image_size = image.size()
        image_width = image_size[2]
        image_height = image_size[1]
        if image_width <= 0 or image_height <= 0:
            raise ValueError("image dimensions must be greater than zero")
        return _calculate_resolution(image_width / image_height, megapixels, multiple)


NODE_CLASS_MAPPINGS = {
    "CM_SDXLResolution": SDXLResolution,
    "CM_NearestSDXLResolution": NearestSDXLResolution,
    "CM_SDXLExtendedResolution": SDXLExtendedResolution,
    "CM_NearestSDXLExtendedResolution": NearestSDXLExtendedResolution,
    "CM_AspectRatioResolution": AspectRatioResolution,
    "CM_ImageAspectResolution": ImageAspectResolution,
}
