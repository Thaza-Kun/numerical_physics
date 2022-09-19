# Root by Newton

Newton's method uses a both the function and its derivative to find a root of a function.

## Strategy

1. Choose a single `initial` point within the function domain.
2. Find the point at which the `derivative` intercepts $y=0$. This point can be found using
   $$x_{\text{intercept}} = x - \frac{f(x)}{f^\prime(x)}$$
3. Set that point as the new `initial`.
4. Repeat steps (2) - (3) until `interval` is less than `tolerance`.

## Advantages

It is faster than root by bisection.

## Disadvantages

- It requires `initial` guess close to the actual root for best performance.
- It requires knowledge of `derivative`.
