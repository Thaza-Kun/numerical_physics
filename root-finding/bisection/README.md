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
5. Repeat steps (2) - (4) until we find the answer.
