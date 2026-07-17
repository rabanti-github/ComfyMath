# ComfyMath

ComfyMath provides math and utility nodes for [ComfyUI](https://github.com/comfyanonymous/ComfyUI).

The package currently registers **59 custom nodes** under the `math/...` categories. Most operation nodes expose an `op` dropdown, so one node can perform several related operations.

## Features

Provides nodes for:

* Boolean logic
* Integer, float, and generic number arithmetic
* Numeric comparisons and conditions
* Conditional value selection and conditional arithmetic fallbacks
* Vec2, Vec3, and Vec4 arithmetic, scalar operations, and vector checks
* Type conversion and vector compose/breakout helpers
* SDXL resolution helpers

## Installation

From the `custom_nodes` directory in your ComfyUI installation, run:

```sh
git clone https://github.com/rabanti-github/ComfyMath.git
```

Restart ComfyUI after installation. Nodes are displayed without the internal `CM_` prefix.

## Node Reference

### Boolean Nodes

| Node | Purpose | Inputs | Outputs |
| --- | --- | --- | --- |
| `BoolUnaryOperation` | Applies a unary boolean operation. Operations: `Not`. | `op`, `a: BOOLEAN` | `BOOLEAN` |
| `BoolBinaryOperation` | Applies a binary boolean operation. Operations: `Nor`, `Xor`, `Nand`, `And`, `Xnor`, `Or`, `Eq`, `Neq`. | `op`, `a: BOOLEAN`, `b: BOOLEAN` | `BOOLEAN` |

### Integer Nodes

| Node | Purpose | Inputs | Outputs |
| --- | --- | --- | --- |
| `IntUnaryOperation` | Applies a unary integer operation. Operations: `Abs`, `Neg`, `Inc`, `Dec`, `Sqr`, `Cube`, bitwise `Not`, `Factorial`. | `op`, `a: INT` | `INT` |
| `IntUnaryCondition` | Tests one integer value. Conditions: zero/non-zero, positive/negative, even/odd. | `op`, `a: INT` | `BOOLEAN` |
| `IntBinaryOperation` | Applies a binary integer operation. Operations include arithmetic, bitwise logic, shifts, `Max`, and `Min`. | `op`, `a: INT`, `b: INT` | `INT` |
| `IntBinaryCondition` | Compares two integer values. Conditions: `Eq`, `Neq`, `Gt`, `Lt`, `Geq`, `Leq`. | `op`, `a: INT`, `b: INT` | `BOOLEAN` |
| `IntUnaryOperationConditional` | Applies a unary integer operation only when `condition` is true; otherwise returns `a` or `fallback_value`. | `condition: BOOLEAN`, `fallback_mode`, `fallback_value: INT`, `op`, `a: INT` | `INT` |
| `IntBinaryOperationConditional` | Applies a binary integer operation only when `condition` is true; otherwise returns `a`, `b`, or `fallback_value`. | `condition: BOOLEAN`, `fallback_mode`, `fallback_value: INT`, `op`, `a: INT`, `b: INT` | `INT` |

### Float Nodes

| Node | Purpose | Inputs | Outputs |
| --- | --- | --- | --- |
| `FloatUnaryOperation` | Applies a unary float operation. Operations include arithmetic helpers, roots/logs, trig/hyperbolic functions, rounding, error/gamma functions, and radians/degrees conversion. | `op`, `a: FLOAT` | `FLOAT` |
| `FloatUnaryCondition` | Tests one float value. Conditions include zero/non-zero, sign, finite/infinite, NaN, even, and odd. | `op`, `a: FLOAT` | `BOOLEAN` |
| `FloatBinaryOperation` | Applies a binary float operation. Operations: `Add`, `Sub`, `Mul`, `Div`, `Mod`, `Pow`, `FloorDiv`, `Max`, `Min`, `Log`, `Atan2`. | `op`, `a: FLOAT`, `b: FLOAT` | `FLOAT` |
| `FloatBinaryCondition` | Compares two float values. Conditions: `Eq`, `Neq`, `Gt`, `Gte`, `Lt`, `Lte`. | `op`, `a: FLOAT`, `b: FLOAT` | `BOOLEAN` |
| `FloatUnaryOperationConditional` | Applies a unary float operation only when `condition` is true; otherwise returns `a` or `fallback_value`. | `condition: BOOLEAN`, `fallback_mode`, `fallback_value: FLOAT`, `op`, `a: FLOAT` | `FLOAT` |
| `FloatBinaryOperationConditional` | Applies a binary float operation only when `condition` is true; otherwise returns `a`, `b`, or `fallback_value`. | `condition: BOOLEAN`, `fallback_mode`, `fallback_value: FLOAT`, `op`, `a: FLOAT`, `b: FLOAT` | `FLOAT` |

### Number Nodes

`NUMBER` accepts integer or float-like values and runs the same operation sets as the float nodes after converting inputs to `float`.

| Node | Purpose | Inputs | Outputs |
| --- | --- | --- | --- |
| `NumberUnaryOperation` | Applies a float-style unary operation to a generic number. | `op`, `a: NUMBER` | `NUMBER` |
| `NumberUnaryCondition` | Tests a generic number with the float-style unary conditions. | `op`, `a: NUMBER` | `BOOLEAN` |
| `NumberBinaryOperation` | Applies a float-style binary operation to two generic numbers. | `op`, `a: NUMBER`, `b: NUMBER` | `NUMBER` |
| `NumberBinaryCondition` | Compares two generic numbers with the float-style binary conditions. | `op`, `a: NUMBER`, `b: NUMBER` | `BOOLEAN` |

### Vector Nodes

The same node families are provided for `VEC2`, `VEC3`, and `VEC4`.

| Node Pattern | Purpose | Inputs | Outputs |
| --- | --- | --- | --- |
| `VecNUnaryOperation` | Applies vector unary operations. Operations: `Neg`, `Normalize`. | `op`, `a: VECN` | `VECN` |
| `VecNToScalarUnaryOperation` | Converts one vector to a scalar. Operations: `Norm`. | `op`, `a: VECN` | `FLOAT` |
| `VecNUnaryCondition` | Tests one vector. Conditions: zero/non-zero and normalized/not normalized. | `op`, `a: VECN` | `BOOLEAN` |
| `VecNBinaryOperation` | Applies vector binary operations. Operations: `Add`, `Sub`, `Cross`. **Note**: `Cross` is currently only usable as a Vec3 operation; NumPy returns a scalar for Vec2, which does not match this node output conversion, and Vec4 is invalid. | `op`, `a: VECN`, `b: VECN` | `VECN` |
| `VecNToScalarBinaryOperation` | Converts two vectors to a scalar. Operations: `Dot`, `Distance`. | `op`, `a: VECN`, `b: VECN` | `FLOAT` |
| `VecNBinaryCondition` | Compares two vectors. Conditions: `Eq`, `Neq`. | `op`, `a: VECN`, `b: VECN` | `BOOLEAN` |
| `VecNScalarOperation` | Applies scalar multiplication or division to a vector. Operations: `Mul`, `Div`. | `op`, `a: VECN`, `b: FLOAT` | `VECN` |

Registered vector node names replace `N` with `2`, `3`, or `4`, for example `Vec2UnaryOperation`, `Vec3ScalarOperation`, and `Vec4ToScalarBinaryOperation`.

### Conversion Nodes

| Node | Purpose | Inputs | Outputs |
| --- | --- | --- | --- |
| `BoolToInt` | Converts `False`/`True` to `0`/`1`. | `a: BOOLEAN` | `INT` |
| `IntToBool` | Converts `0` to `False` and any other integer to `True`. | `a: INT` | `BOOLEAN` |
| `FloatToInt` | Converts a float to an integer using Python `int()` truncation. | `a: FLOAT` | `INT` |
| `IntToFloat` | Converts an integer to a float. | `a: INT` | `FLOAT` |
| `IntToNumber` | Passes an integer as a generic number. | `a: INT` | `NUMBER` |
| `NumberToInt` | Converts a generic number to an integer using Python `int()` truncation. | `a: NUMBER` | `INT` |
| `FloatToNumber` | Passes a float as a generic number. | `a: FLOAT` | `NUMBER` |
| `NumberToFloat` | Converts a generic number to a float. | `a: NUMBER` | `FLOAT` |
| `ComposeVec2` | Builds a Vec2 from component floats. | `x: FLOAT`, `y: FLOAT` | `VEC2` |
| `ComposeVec3` | Builds a Vec3 from component floats. | `x: FLOAT`, `y: FLOAT`, `z: FLOAT` | `VEC3` |
| `ComposeVec4` | Builds a Vec4 from component floats. | `x: FLOAT`, `y: FLOAT`, `z: FLOAT`, `w: FLOAT` | `VEC4` |
| `BreakoutVec2` | Splits a Vec2 into component floats. | `a: VEC2` | `FLOAT`, `FLOAT` |
| `BreakoutVec3` | Splits a Vec3 into component floats. | `a: VEC3` | `FLOAT`, `FLOAT`, `FLOAT` |
| `BreakoutVec4` | Splits a Vec4 into component floats. | `a: VEC4` | `FLOAT`, `FLOAT`, `FLOAT`, `FLOAT` |

### Control Nodes

| Node | Purpose | Inputs | Outputs |
| --- | --- | --- | --- |
| `ChooseInt` | Returns `a` when `condition` is true, otherwise returns `b`. | `condition: BOOLEAN`, `a: INT`, `b: INT` | `INT` |
| `ChooseFloat` | Returns `a` when `condition` is true, otherwise returns `b`. | `condition: BOOLEAN`, `a: FLOAT`, `b: FLOAT` | `FLOAT` |

### Graphics Nodes

| Node | Purpose | Inputs | Outputs |
| --- | --- | --- | --- |
| `SDXLResolution` | Selects one of the standard SDXL width/height presets. | `resolution` | `width: INT`, `height: INT` |
| `NearestSDXLResolution` | Chooses the standard SDXL preset whose aspect ratio is nearest to the input image. | `image: IMAGE` | `width: INT`, `height: INT` |
| `SDXLExtendedResolution` | Selects one of the extended SDXL width/height presets. | `resolution` | `width: INT`, `height: INT` |
| `NearestSDXLExtendedResolution` | Chooses the extended SDXL preset whose aspect ratio is nearest to the input image. | `image: IMAGE` | `width: INT`, `height: INT` |

## Limitations

* Math errors are not caught. Examples: division by zero, invalid logarithm/square-root domains, invalid factorial input, and normalizing a zero vector may raise errors or produce non-finite values.
* Float equality uses exact Python comparison; vector equality uses NumPy `allclose`.
* Integer `Div` uses floor division (`//`), not true division. Use `IntToFloat` first, then a float or number division node when a fractional result is needed.
* `FloatToInt` and `NumberToInt` truncate toward zero.
* `FillVec2`, `FillVec3`, and `FillVec4` classes exist in `convert.py`, but are not referenced elsewhere or registered in `NODE_CLASS_MAPPINGS`. They are currently orphaned/unexposed convenience helpers for creating vectors with all components set to the same value.

## Further References

* ComfyUI custom nodes: <https://github.com/comfyanonymous/ComfyUI>
* Python `math` module behavior: <https://docs.python.org/3/library/math.html>
* NumPy vector operations used by vector nodes: <https://numpy.org/doc/stable/reference/routines.linalg.html>

## Credits

This repo was originally cloned from <https://github.com/evanspearman/ComfyMath>.

Additional features were added, according to a PR proposal of [dnnagy](https://github.com/evanspearman/ComfyMath/pull/15).

