# Simple Integration

## Strategy

1.

## Advantages

It is simple and very robust. If there is a root between the two initial guesses, bisection will find it.

## Disadvantages

1. Bisection is not particularly fast. Each step improves the accuracy only by a factor of two,
   so if you start with a and b separated by something on the order of 1, and
   you have a desired tolerance on the order of 10−6, it will take roughly 20 steps.

2. If the root is not between the initial guesses, then it will NOT find the root.
