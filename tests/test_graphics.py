import math
import unittest
from typing import Sequence

from src.comfymath.graphics import (
    ASPECT_RATIOS,
    NODE_CLASS_MAPPINGS,
    SDXL_EXTENDED_RESOLUTIONS,
    SDXL_SUPPORTED_RESOLUTIONS,
    AspectRatioResolution,
    ImageAspectResolution,
    NearestResolution,
    NearestSDXLExtendedResolution,
    NearestSDXLResolution,
    ResolutionPreset,
    SDXLExtendedResolution,
    SDXLResolution,
)


class FakeImage:
    def __init__(self, width: int, height: int) -> None:
        self._size = (1, height, width, 3)

    def size(self) -> tuple[int, int, int, int]:
        return self._size


class EmptyNearestResolution(NearestResolution):
    @classmethod
    def resolutions(cls) -> Sequence[ResolutionPreset]:
        return []


class TieNearestResolution(NearestResolution):
    @classmethod
    def resolutions(cls) -> Sequence[ResolutionPreset]:
        return [(100, 100, 99.0), (200, 100, -99.0)]


class ResolutionPresetTest(unittest.TestCase):
    def test_preset_invariants(self) -> None:
        cases = [
            ("standard", SDXL_SUPPORTED_RESOLUTIONS),
            ("extended", SDXL_EXTENDED_RESOLUTIONS),
        ]

        for preset_name, presets in cases:
            with self.subTest(preset_name=preset_name):
                dimensions = [(width, height) for width, height, _ in presets]
                self.assertEqual(len(dimensions), len(set(dimensions)))
                for width, height, aspect_ratio in presets:
                    self.assertGreater(width, 0)
                    self.assertGreater(height, 0)
                    self.assertEqual(width % 64, 0)
                    self.assertEqual(height % 64, 0)
                    self.assertEqual(aspect_ratio, width / height)

    def test_selector_input_types_preserve_preset_order(self) -> None:
        cases = [
            (SDXLResolution, SDXL_SUPPORTED_RESOLUTIONS),
            (SDXLExtendedResolution, SDXL_EXTENDED_RESOLUTIONS),
        ]

        for node_class, presets in cases:
            expected = [f"{width}x{height}" for width, height, _ in presets]
            with self.subTest(node_class=node_class.__name__):
                choices = node_class.INPUT_TYPES()["required"]["resolution"][0]
                self.assertEqual(choices, expected)

    def test_selector_parses_every_preset(self) -> None:
        cases = [
            (SDXLResolution(), SDXL_SUPPORTED_RESOLUTIONS),
            (SDXLExtendedResolution(), SDXL_EXTENDED_RESOLUTIONS),
        ]

        for operation, presets in cases:
            for width, height, _ in presets:
                resolution = f"{width}x{height}"
                with self.subTest(
                    node_class=type(operation).__name__, resolution=resolution
                ):
                    self.assertEqual(operation.op(resolution), (width, height))

    def test_selector_rejects_malformed_resolutions(self) -> None:
        cases = ["", "1024", "1024x", "x1024", "axb", "1x2x3"]
        operation = SDXLResolution()

        for resolution in cases:
            with self.subTest(resolution=resolution):
                with self.assertRaises(ValueError):
                    operation.op(resolution)


class NearestResolutionTest(unittest.TestCase):
    def test_selects_nearest_standard_resolution(self) -> None:
        cases = [
            (1024, 1024, (1024, 1024)),
            (400, 300, (1152, 896)),
            (300, 400, (896, 1152)),
            (2400, 1000, (1536, 640)),
            (1000, 2400, (640, 1536)),
        ]
        operation = NearestSDXLResolution()

        for width, height, expected in cases:
            with self.subTest(width=width, height=height):
                self.assertEqual(operation.op(FakeImage(width, height)), expected)

    def test_selects_nearest_extended_resolution(self) -> None:
        cases = [
            (1024, 960, (1024, 960)),
            (512, 1984, (512, 1984)),
            (2048, 512, (2048, 512)),
            (1408, 704, (1408, 704)),
        ]
        operation = NearestSDXLExtendedResolution()

        for width, height, expected in cases:
            with self.subTest(width=width, height=height):
                self.assertEqual(operation.op(FakeImage(width, height)), expected)

    def test_uses_dimensions_instead_of_stored_ratio(self) -> None:
        operation = TieNearestResolution()

        self.assertEqual(operation.op(FakeImage(100, 100)), (100, 100))
        self.assertEqual(operation.op(FakeImage(200, 100)), (200, 100))

    def test_tie_selects_first_resolution(self) -> None:
        operation = TieNearestResolution()

        self.assertEqual(operation.op(FakeImage(3, 2)), (100, 100))

    def test_empty_resolution_list_uses_square_fallback(self) -> None:
        operation = EmptyNearestResolution()

        self.assertEqual(operation.op(FakeImage(16, 9)), (1024, 1024))

    def test_rejects_non_positive_image_dimensions(self) -> None:
        cases = [(0, 1), (1, 0), (-1, 1), (1, -1)]
        operation = NearestSDXLResolution()

        for width, height in cases:
            with self.subTest(width=width, height=height):
                with self.assertRaises(ValueError):
                    operation.op(FakeImage(width, height))


class AspectRatioResolutionTest(unittest.TestCase):
    def test_input_types_expose_expected_ratios_and_defaults(self) -> None:
        required = AspectRatioResolution.INPUT_TYPES()["required"]

        self.assertEqual(required["aspect_ratio"][0], list(ASPECT_RATIOS))
        self.assertEqual(required["megapixels"][1]["default"], 1.0)
        self.assertEqual(required["multiple"][1]["default"], 16)

    def test_calculates_resolution(self) -> None:
        cases = [
            ("1:1", 1.0, 16, (1024, 1024)),
            ("16:9", 1.0, 16, (1360, 768)),
            ("9:16", 1.0, 16, (768, 1360)),
            ("1:1", 1.0, 64, (1024, 1024)),
            ("1:1", 0.000001, 16, (16, 16)),
        ]
        operation = AspectRatioResolution()

        for aspect_ratio, megapixels, multiple, expected in cases:
            with self.subTest(
                aspect_ratio=aspect_ratio,
                megapixels=megapixels,
                multiple=multiple,
            ):
                self.assertEqual(
                    operation.op(aspect_ratio, megapixels, multiple), expected
                )

    def test_rounds_half_up(self) -> None:
        megapixels = 24**2 / 1024**2

        self.assertEqual(
            AspectRatioResolution().op("1:1", megapixels, 16), (32, 32)
        )

    def test_rejects_invalid_aspect_ratios(self) -> None:
        cases = ["", "1", "1:2:3", "a:b", "0:1", "1:0", "-1:1", "inf:1"]
        operation = AspectRatioResolution()

        for aspect_ratio in cases:
            with self.subTest(aspect_ratio=aspect_ratio):
                with self.assertRaises(ValueError):
                    operation.op(aspect_ratio, 1.0, 16)

    def test_rejects_invalid_megapixels(self) -> None:
        cases = [0.0, -1.0, math.inf, -math.inf, math.nan]
        operation = AspectRatioResolution()

        for megapixels in cases:
            with self.subTest(megapixels=megapixels):
                with self.assertRaises(ValueError):
                    operation.op("1:1", megapixels, 16)

    def test_rejects_invalid_multiples(self) -> None:
        cases = [0, -1, -99]
        operation = AspectRatioResolution()

        for multiple in cases:
            with self.subTest(multiple=multiple):
                with self.assertRaises(ValueError):
                    operation.op("1:1", 1.0, multiple)


class ImageAspectResolutionTest(unittest.TestCase):
    def test_input_types_expose_expected_defaults(self) -> None:
        required = ImageAspectResolution.INPUT_TYPES()["required"]

        self.assertEqual(required["image"], ("IMAGE",))
        self.assertEqual(required["megapixels"][1]["default"], 1.0)
        self.assertEqual(required["multiple"][1]["default"], 16)

    def test_calculates_resolution_from_image_aspect(self) -> None:
        cases = [
            (FakeImage(1, 1), 1.0, 16, (1024, 1024)),
            (FakeImage(16, 9), 1.0, 16, (1360, 768)),
            (FakeImage(9, 16), 1.0, 16, (768, 1360)),
            (FakeImage(1, 1), 0.000001, 16, (16, 16)),
        ]
        operation = ImageAspectResolution()

        for image, megapixels, multiple, expected in cases:
            with self.subTest(
                image_size=image.size(),
                megapixels=megapixels,
                multiple=multiple,
            ):
                self.assertEqual(operation.op(image, megapixels, multiple), expected)

    def test_rejects_non_positive_image_dimensions(self) -> None:
        cases = [(0, 1), (1, 0), (-1, 1), (1, -1)]
        operation = ImageAspectResolution()

        for width, height in cases:
            with self.subTest(width=width, height=height):
                with self.assertRaises(ValueError):
                    operation.op(FakeImage(width, height), 1.0, 16)

    def test_rejects_invalid_megapixels_and_multiples(self) -> None:
        cases = [(0.0, 16), (-1.0, 16), (1.0, 0), (1.0, -1)]
        operation = ImageAspectResolution()

        for megapixels, multiple in cases:
            with self.subTest(megapixels=megapixels, multiple=multiple):
                with self.assertRaises(ValueError):
                    operation.op(FakeImage(1, 1), megapixels, multiple)


class GraphicsNodeRegistrationTest(unittest.TestCase):
    def test_all_graphics_nodes_are_registered(self) -> None:
        expected = {
            "CM_SDXLResolution": SDXLResolution,
            "CM_NearestSDXLResolution": NearestSDXLResolution,
            "CM_SDXLExtendedResolution": SDXLExtendedResolution,
            "CM_NearestSDXLExtendedResolution": NearestSDXLExtendedResolution,
            "CM_AspectRatioResolution": AspectRatioResolution,
            "CM_ImageAspectResolution": ImageAspectResolution,
        }

        self.assertEqual(NODE_CLASS_MAPPINGS, expected)
        for mapping_name, node_class in NODE_CLASS_MAPPINGS.items():
            with self.subTest(mapping_name=mapping_name):
                self.assertTrue(node_class.DESCRIPTION)


if __name__ == "__main__":
    unittest.main()
