# Root by Secant

The secant method is a modification of Newton's method that doesn't require knowledge of its derivative.
It uses a calculated slope between two points to approximate the derivative of the function.

## Strategy

1. Choose two points, `first` and `second`. Ideally, these two points are near the root but the root is not necessarily in between.
2. Calculate the `slope` using `func(first)` and `func(second)`.
3. Find the `intercept`.
4. Calculate the `interval` of [`intercept`,`first`] and [`intercept`, `second`].
5. Set the new `first` and `second` using the points where the `interval` is shortest.
6. Repeat steps (2) - (5) until `interval` is less than `tolerance`.
