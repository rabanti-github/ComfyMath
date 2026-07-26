import importlib.util
import json
import pathlib
import sys
import unittest
from typing import Any


REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
NODE_LIST_PATH = REPO_ROOT / "node_list.json"


def load_root_node_class_mappings() -> dict[str, Any]:
    parent = str(REPO_ROOT.parent)
    if parent not in sys.path:
        sys.path.insert(0, parent)

    spec = importlib.util.spec_from_file_location(
        "ComfyMath",
        REPO_ROOT / "__init__.py",
        submodule_search_locations=[str(REPO_ROOT)],
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load root ComfyMath package")

    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module.NODE_CLASS_MAPPINGS


def reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate node_list.json key: {key}")
        result[key] = value
    return result


class NodeListValidationTest(unittest.TestCase):
    def test_node_list_matches_effective_root_node_class_mappings(self) -> None:
        with NODE_LIST_PATH.open(encoding="utf-8") as node_list_file:
            node_list = json.load(
                node_list_file, object_pairs_hook=reject_duplicate_keys
            )

        self.assertIs(type(node_list), dict)
        for node_key, description in node_list.items():
            with self.subTest(node_key=node_key):
                self.assertIs(type(node_key), str)
                self.assertIs(type(description), str)
                self.assertTrue(description.strip())

        registered_nodes = load_root_node_class_mappings()

        self.assertEqual(list(node_list), list(registered_nodes))
        self.assertEqual(set(node_list), set(registered_nodes))
        self.assertEqual(len(node_list), len(registered_nodes))


if __name__ == "__main__":
    unittest.main()
