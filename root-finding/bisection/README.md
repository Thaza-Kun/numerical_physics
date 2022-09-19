# Root by Bisection

Root finding using the bisection method uses a repeated bisection within a defined interval.
It assumes that the root of the function is contained in the interval, else it is trapped in an infinite loop.

## Strategy

1. Initialize an interval with the `left` and `right` argument.
2. Find the `midpoint` of the interval to form a bisection.
3. Check the left part of the interval if there is a sign change.
   1. If there is a sign change, that means the root is somewhere within the left part of the interval.
   2. Else, that means the root is somewhere within the right part of the interval.
4. Set a new interval based on the result of (3).
5. Repeat steps (2) - (4) until `interval` is less than `tolerance`.

## Advantages

It is simple and very robust. If there is a root between the two initial guesses, bisection will find it.

## Disadvantages

1. Bisection is not particularly fast. Each step improves the accuracy only by a factor of two,
   so if you start with a and b separated by something on the order of 1, and
   you have a desired tolerance on the order of 10−6, it will take roughly 20 steps.

2. If the root is not between the initial guesses, then it will NOT find the root.
