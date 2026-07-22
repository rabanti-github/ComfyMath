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

#### Operators

| Operator | Applicable for | Description | Exmaple |
| --- | --- | --- | --- |
| `Not` | `BoolUnaryOperation` | Inverts the input value. | `Not True` → `False` |
| `Nor` | `BoolBinaryOperation` | True only when both inputs are false. | `True Nor False` → `False` |
| `Xor` | `BoolBinaryOperation` | True when the inputs differ. | `True Xor False` → `True` |
| `Nand` | `BoolBinaryOperation` | False only when both inputs are true. | `True Nand True` → `False` |
| `And` | `BoolBinaryOperation` | True only when both inputs are true. | `True And False` → `False` |
| `Xnor` | `BoolBinaryOperation` | True when the inputs are equal. | `True Xnor True` → `True` |
| `Or` | `BoolBinaryOperation` | True when either input is true. | `False Or True` → `True` |
| `Eq` | `BoolBinaryOperation` | Tests whether the inputs are equal. | `True Eq False` → `False` |
| `Neq` | `BoolBinaryOperation` | Tests whether the inputs differ. | `True Neq False` → `True` |

### Integer Nodes

| Node | Purpose | Inputs | Outputs |
| --- | --- | --- | --- |
| `IntUnaryOperation` | Applies a unary integer operation. Operations: `Abs`, `Neg`, `Inc`, `Dec`, `Sqr`, `Cube`, bitwise `Not`, `Factorial`. | `op`, `a: INT` | `INT` |
| `IntUnaryCondition` | Tests one integer value. Conditions: zero/non-zero, positive/negative, even/odd. | `op`, `a: INT` | `BOOLEAN` |
| `IntBinaryOperation` | Applies a binary integer operation. Operations include arithmetic, bitwise logic, shifts, `Max`, and `Min`. | `op`, `a: INT`, `b: INT` | `INT` |
| `IntBinaryCondition` | Compares two integer values. Conditions: `Eq`, `Neq`, `Gt`, `Lt`, `Geq`, `Leq`. | `op`, `a: INT`, `b: INT` | `BOOLEAN` |
| `IntUnaryOperationConditional` | Applies a unary integer operation only when `condition` is true; otherwise returns `a` or `fallback_value`. | `condition: BOOLEAN`, `fallback_mode`, `fallback_value: INT`, `op`, `a: INT` | `INT` |
| `IntBinaryOperationConditional` | Applies a binary integer operation only when `condition` is true; otherwise returns `a`, `b`, or `fallback_value`. | `condition: BOOLEAN`, `fallback_mode`, `fallback_value: INT`, `op`, `a: INT`, `b: INT` | `INT` |

#### Operators

| Operator | Applicable for | Description | Exmaple |
| --- | --- | --- | --- |
| `Abs` | `IntUnaryOperation`, `IntUnaryOperationConditional` | Returns the absolute value. | `Abs -12` → `12` |
| `Neg` | `IntUnaryOperation`, `IntUnaryOperationConditional` | Negates the input. | `Neg 1` → `-1` |
| `Inc` | `IntUnaryOperation`, `IntUnaryOperationConditional` | Adds one. | `Inc 10` → `11` |
| `Dec` | `IntUnaryOperation`, `IntUnaryOperationConditional` | Subtracts one. | `Dec 2` → `1` |
| `Sqr` | `IntUnaryOperation`, `IntUnaryOperationConditional` | Squares the input. | `Sqr -3` → `9` |
| `Cube` | `IntUnaryOperation`, `IntUnaryOperationConditional` | Cubes the input. | `Cube -3` → `-27` |
| `Not` | `IntUnaryOperation`, `IntUnaryOperationConditional` | Applies bitwise NOT. | `Not 4` → `-5` |
| `Factorial` | `IntUnaryOperation`, `IntUnaryOperationConditional` | Returns the factorial. | `Factorial 5` → `120` |
| `IsZero` | `IntUnaryCondition` | Tests whether the input is zero. | `IsZero 0` → `True` |
| `IsNonZero` | `IntUnaryCondition` | Tests whether the input is not zero. | `IsNonZero 4` → `True` |
| `IsPositive` | `IntUnaryCondition` | Tests whether the input is positive. | `IsPositive 4` → `True` |
| `IsNegative` | `IntUnaryCondition` | Tests whether the input is negative. | `IsNegative -4` → `True` |
| `IsEven` | `IntUnaryCondition` | Tests whether the input is even. | `IsEven 2` → `True` |
| `IsOdd` | `IntUnaryCondition` | Tests whether the input is odd. | `IsOdd 1` → `True` |
| `Add` | `IntBinaryOperation`, `IntBinaryOperationConditional` | Adds both inputs. | `20 Add 80` → `100` |
| `Sub` | `IntBinaryOperation`, `IntBinaryOperationConditional` | Subtracts the second input. | `20 Sub 80` → `-60` |
| `Mul` | `IntBinaryOperation`, `IntBinaryOperationConditional` | Multiplies both inputs. | `20 Mul 80` → `1600` |
| `Div` | `IntBinaryOperation`, `IntBinaryOperationConditional` | Performs floor division. | `80 Div 20` → `4` |
| `Mod` | `IntBinaryOperation`, `IntBinaryOperationConditional` | Returns the division remainder. | `100 Mod 80` → `20` |
| `Pow` | `IntBinaryOperation`, `IntBinaryOperationConditional` | Raises the first input to the second. | `2 Pow 2` → `4` |
| `And` | `IntBinaryOperation`, `IntBinaryOperationConditional` | Applies bitwise AND. | `2 And 3` → `2` |
| `Nand` | `IntBinaryOperation`, `IntBinaryOperationConditional` | Applies bitwise NAND. | `10 Nand 3` → `-3` |
| `Or` | `IntBinaryOperation`, `IntBinaryOperationConditional` | Applies bitwise OR. | `4 Or 6` → `6` |
| `Nor` | `IntBinaryOperation`, `IntBinaryOperationConditional` | Applies bitwise NOR. | `4 Nor 6` → `-7` |
| `Xor` | `IntBinaryOperation`, `IntBinaryOperationConditional` | Applies bitwise XOR. | `4 Xor 6` → `2` |
| `Xnor` | `IntBinaryOperation`, `IntBinaryOperationConditional` | Applies bitwise XNOR. | `4 Xnor 6` → `-3` |
| `Shl` | `IntBinaryOperation`, `IntBinaryOperationConditional` | Shifts bits left. | `4 Shl 4` → `64` |
| `Shr` | `IntBinaryOperation`, `IntBinaryOperationConditional` | Shifts bits right. | `-1 Shr 2` → `-1` |
| `Max` | `IntBinaryOperation`, `IntBinaryOperationConditional` | Returns the larger input. | `20 Max 80` → `80` |
| `Min` | `IntBinaryOperation`, `IntBinaryOperationConditional` | Returns the smaller input. | `20 Min 80` → `20` |
| `Eq` | `IntBinaryCondition` | Tests whether the inputs are equal. | `4 Eq 4` → `True` |
| `Neq` | `IntBinaryCondition` | Tests whether the inputs differ. | `4 Neq 5` → `True` |
| `Gt` | `IntBinaryCondition` | Tests whether the first input is greater. | `9 Gt 4` → `True` |
| `Lt` | `IntBinaryCondition` | Tests whether the first input is smaller. | `4 Lt 9` → `True` |
| `Geq` | `IntBinaryCondition` | Tests whether the first input is greater or equal. | `4 Geq 4` → `True` |
| `Leq` | `IntBinaryCondition` | Tests whether the first input is smaller or equal. | `4 Leq 9` → `True` |

### Float Nodes

| Node | Purpose | Inputs | Outputs |
| --- | --- | --- | --- |
| `FloatUnaryOperation` | Applies a unary float operation. Operations include arithmetic helpers, roots/logs, trig/hyperbolic functions, rounding, error/gamma functions, and radians/degrees conversion. | `op`, `a: FLOAT` | `FLOAT` |
| `FloatUnaryCondition` | Tests one float value. Conditions include zero/non-zero, sign, finite/infinite, NaN, even, and odd. | `op`, `a: FLOAT` | `BOOLEAN` |
| `FloatBinaryOperation` | Applies a binary float operation. Operations: `Add`, `Sub`, `Mul`, `Div`, `Mod`, `Pow`, `FloorDiv`, `Max`, `Min`, `Log`, `Atan2`. | `op`, `a: FLOAT`, `b: FLOAT` | `FLOAT` |
| `FloatBinaryCondition` | Compares two float values. Conditions: `Eq`, `Neq`, `Gt`, `Gte`, `Lt`, `Lte`. | `op`, `a: FLOAT`, `b: FLOAT` | `BOOLEAN` |
| `FloatUnaryOperationConditional` | Applies a unary float operation only when `condition` is true; otherwise returns `a` or `fallback_value`. | `condition: BOOLEAN`, `fallback_mode`, `fallback_value: FLOAT`, `op`, `a: FLOAT` | `FLOAT` |
| `FloatBinaryOperationConditional` | Applies a binary float operation only when `condition` is true; otherwise returns `a`, `b`, or `fallback_value`. | `condition: BOOLEAN`, `fallback_mode`, `fallback_value: FLOAT`, `op`, `a: FLOAT`, `b: FLOAT` | `FLOAT` |

#### Operators

| Operator | Applicable for | Description | Exmaple |
| --- | --- | --- | --- |
| `Neg` | `FloatUnaryOperation`, `FloatUnaryOperationConditional` | Negates the input. | `Neg 2.5` → `-2.5` |
| `Inc` | `FloatUnaryOperation`, `FloatUnaryOperationConditional` | Adds one. | `Inc 10.12` → `11.12` |
| `Dec` | `FloatUnaryOperation`, `FloatUnaryOperationConditional` | Subtracts one. | `Dec 2.0` → `1.0` |
| `Abs` | `FloatUnaryOperation`, `FloatUnaryOperationConditional` | Returns the absolute value. | `Abs -12.0` → `12.0` |
| `Sqr` | `FloatUnaryOperation`, `FloatUnaryOperationConditional` | Squares the input. | `Sqr -3.0` → `9.0` |
| `Cube` | `FloatUnaryOperation`, `FloatUnaryOperationConditional` | Cubes the input. | `Cube -3.0` → `-27.0` |
| `Sqrt` | `FloatUnaryOperation`, `FloatUnaryOperationConditional` | Returns the square root. | `Sqrt 9.0` → `3.0` |
| `Exp` | `FloatUnaryOperation`, `FloatUnaryOperationConditional` | Raises e to the input. | `Exp 1.0` → `2.718...` |
| `Ln` | `FloatUnaryOperation`, `FloatUnaryOperationConditional` | Returns the natural logarithm. | `Ln e` → `1.0` |
| `Log10` | `FloatUnaryOperation`, `FloatUnaryOperationConditional` | Returns the base-10 logarithm. | `Log10 100.0` → `2.0` |
| `Log2` | `FloatUnaryOperation`, `FloatUnaryOperationConditional` | Returns the base-2 logarithm. | `Log2 8.0` → `3.0` |
| `Sin` | `FloatUnaryOperation`, `FloatUnaryOperationConditional` | Returns the sine in radians. | `Sin (π / 2)` → `1.0` |
| `Cos` | `FloatUnaryOperation`, `FloatUnaryOperationConditional` | Returns the cosine in radians. | `Cos π` → `-1.0` |
| `Tan` | `FloatUnaryOperation`, `FloatUnaryOperationConditional` | Returns the tangent in radians. | `Tan (π / 4)` → `1.0` |
| `Asin` | `FloatUnaryOperation`, `FloatUnaryOperationConditional` | Returns the inverse sine. | `Asin 1.0` → `π / 2` |
| `Acos` | `FloatUnaryOperation`, `FloatUnaryOperationConditional` | Returns the inverse cosine. | `Acos 0.0` → `π / 2` |
| `Atan` | `FloatUnaryOperation`, `FloatUnaryOperationConditional` | Returns the inverse tangent. | `Atan 1.0` → `π / 4` |
| `Sinh` | `FloatUnaryOperation`, `FloatUnaryOperationConditional` | Returns the hyperbolic sine. | `Sinh 1.0` → `1.1752...` |
| `Cosh` | `FloatUnaryOperation`, `FloatUnaryOperationConditional` | Returns the hyperbolic cosine. | `Cosh 0.0` → `1.0` |
| `Tanh` | `FloatUnaryOperation`, `FloatUnaryOperationConditional` | Returns the hyperbolic tangent. | `Tanh 1.0` → `0.7615...` |
| `Asinh` | `FloatUnaryOperation`, `FloatUnaryOperationConditional` | Returns the inverse hyperbolic sine. | `Asinh 1.0` → `0.8813...` |
| `Acosh` | `FloatUnaryOperation`, `FloatUnaryOperationConditional` | Returns the inverse hyperbolic cosine. | `Acosh 1.0` → `0.0` |
| `Atanh` | `FloatUnaryOperation`, `FloatUnaryOperationConditional` | Returns the inverse hyperbolic tangent. | `Atanh 0.99` → `2.6466...` |
| `Round` | `FloatUnaryOperation`, `FloatUnaryOperationConditional` | Rounds to the nearest integer. | `Round 1.6` → `2.0` |
| `Floor` | `FloatUnaryOperation`, `FloatUnaryOperationConditional` | Rounds down. | `Floor 1.6` → `1.0` |
| `Ceil` | `FloatUnaryOperation`, `FloatUnaryOperationConditional` | Rounds up. | `Ceil 1.1` → `2.0` |
| `Trunc` | `FloatUnaryOperation`, `FloatUnaryOperationConditional` | Removes the fractional part. | `Trunc -3.5` → `-3.0` |
| `Erf` | `FloatUnaryOperation`, `FloatUnaryOperationConditional` | Returns the error function. | `Erf 0.0` → `0.0` |
| `Erfc` | `FloatUnaryOperation`, `FloatUnaryOperationConditional` | Returns the complementary error function. | `Erfc 0.0` → `1.0` |
| `Gamma` | `FloatUnaryOperation`, `FloatUnaryOperationConditional` | Returns the gamma function. | `Gamma 8.0` → `5040.0` |
| `Radians` | `FloatUnaryOperation`, `FloatUnaryOperationConditional` | Converts degrees to radians. | `Radians 180.0` → `π` |
| `Degrees` | `FloatUnaryOperation`, `FloatUnaryOperationConditional` | Converts radians to degrees. | `Degrees π` → `180.0` |
| `IsZero` | `FloatUnaryCondition` | Tests whether the input is zero. | `IsZero 0.0` → `True` |
| `IsPositive` | `FloatUnaryCondition` | Tests whether the input is positive. | `IsPositive 4.5` → `True` |
| `IsNegative` | `FloatUnaryCondition` | Tests whether the input is negative. | `IsNegative -4.5` → `True` |
| `IsNonZero` | `FloatUnaryCondition` | Tests whether the input is not zero. | `IsNonZero 4.5` → `True` |
| `IsPositiveInfinity` | `FloatUnaryCondition` | Tests for positive infinity. | `IsPositiveInfinity inf` → `True` |
| `IsNegativeInfinity` | `FloatUnaryCondition` | Tests for negative infinity. | `IsNegativeInfinity -inf` → `True` |
| `IsNaN` | `FloatUnaryCondition` | Tests for a NaN value. | `IsNaN nan` → `True` |
| `IsFinite` | `FloatUnaryCondition` | Tests for a finite value. | `IsFinite 4.5` → `True` |
| `IsInfinite` | `FloatUnaryCondition` | Tests for either infinity. | `IsInfinite inf` → `True` |
| `IsEven` | `FloatUnaryCondition` | Tests for an even whole value. | `IsEven 2.0` → `True` |
| `IsOdd` | `FloatUnaryCondition` | Tests for a non-even value. | `IsOdd 2.1` → `True` |
| `Add` | `FloatBinaryOperation`, `FloatBinaryOperationConditional` | Adds both inputs. | `20.0 Add 80.0` → `100.0` |
| `Sub` | `FloatBinaryOperation`, `FloatBinaryOperationConditional` | Subtracts the second input. | `20.0 Sub 80.0` → `-60.0` |
| `Mul` | `FloatBinaryOperation`, `FloatBinaryOperationConditional` | Multiplies both inputs. | `2.5 Mul 4.0` → `10.0` |
| `Div` | `FloatBinaryOperation`, `FloatBinaryOperationConditional` | Divides the first input by the second. | `20.0 Div 80.0` → `0.25` |
| `Mod` | `FloatBinaryOperation`, `FloatBinaryOperationConditional` | Returns the division remainder. | `100.0 Mod 80.0` → `20.0` |
| `Pow` | `FloatBinaryOperation`, `FloatBinaryOperationConditional` | Raises the first input to the second. | `2.0 Pow 2.0` → `4.0` |
| `FloorDiv` | `FloatBinaryOperation`, `FloatBinaryOperationConditional` | Divides and rounds down. | `20.0 FloorDiv 80.0` → `0.0` |
| `Max` | `FloatBinaryOperation`, `FloatBinaryOperationConditional` | Returns the larger input. | `20.0 Max 80.0` → `80.0` |
| `Min` | `FloatBinaryOperation`, `FloatBinaryOperationConditional` | Returns the smaller input. | `20.0 Min 80.0` → `20.0` |
| `Log` | `FloatBinaryOperation`, `FloatBinaryOperationConditional` | Returns a logarithm with the given base. | `8.0 Log 2.0` → `3.0` |
| `Atan2` | `FloatBinaryOperation`, `FloatBinaryOperationConditional` | Returns the angle from two coordinates. | `1.0 Atan2 1.0` → `π / 4` |
| `Eq` | `FloatBinaryCondition` | Tests whether the inputs are equal. | `4.0 Eq 4.0` → `True` |
| `Neq` | `FloatBinaryCondition` | Tests whether the inputs differ. | `4.0 Neq 5.0` → `True` |
| `Gt` | `FloatBinaryCondition` | Tests whether the first input is greater. | `9.0 Gt 4.0` → `True` |
| `Gte` | `FloatBinaryCondition` | Tests whether the first input is greater or equal. | `4.0 Gte 4.0` → `True` |
| `Lt` | `FloatBinaryCondition` | Tests whether the first input is smaller. | `4.0 Lt 9.0` → `True` |
| `Lte` | `FloatBinaryCondition` | Tests whether the first input is smaller or equal. | `4.0 Lte 9.0` → `True` |

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

