# Repository Guidelines

## Project Structure & Module Organization

ComfyMath is a Python package that provides math nodes for ComfyUI. The root `__init__.py` registers node mappings for ComfyUI by importing modules from `src/comfymath/`.

- `src/comfymath/`: package source code for node groups such as `bool.py`, `int.py`, `float.py`, `vec.py`, `convert.py`, and `graphics.py`.
- `src/comfymath/types.py`: shared type definitions.
- `src/comfymath/py.typed`: marks the package as typed for static analysis.
- `README.md`: user-facing project overview and installation instructions.
- `pyproject.toml`: Poetry metadata and development tool configuration.
- `requirements.txt`: minimal runtime dependency list for ComfyUI-style installs.

There is no dedicated `tests/` directory yet.

## Build, Test, and Development Commands

Use Python 3.10 or newer.

- `poetry install`: install runtime and development dependencies from `pyproject.toml`.
- `poetry run black .`: format Python files with Black.
- `poetry run mypy src`: run static type checks against the package source.
- `python -m compileall src __init__.py`: quick syntax check without requiring ComfyUI.

For manual integration testing, clone or place this repository under a ComfyUI `custom_nodes` directory, start ComfyUI, and verify that the ComfyMath node categories load.

## Coding Style & Naming Conventions

Follow Black formatting defaults with 4-space indentation. Keep modules focused by node category; add new math node families as separate files under `src/comfymath/` when they do not naturally fit an existing module.

Node classes should use clear descriptive names, and ComfyUI mapping keys should retain the existing `CM_` prefix pattern. Keep `NODE_CLASS_MAPPINGS` local to each module, then export them through the root `__init__.py`.

Prefer type annotations for public functions, class methods, and shared helpers. Use `numpy` for numeric array behavior when it matches existing implementations.

## Testing Guidelines

Unit tests are not present yet. When adding tests, create a `tests/` directory and use focused cases for node input validation, numeric edge cases, and vector operations. Prefer deterministic examples, including divide-by-zero, boolean conversion, and mixed int/float behavior.

Until tests exist, run Black, mypy, and `compileall` before submitting changes, then perform a ComfyUI startup smoke test when node registration changes.

## Security & Configuration Tips

Do not commit local ComfyUI paths, generated caches, virtual environments, or machine-specific settings. Keep dependencies minimal and update both `pyproject.toml` and `requirements.txt` when runtime requirements change.
