# Root by bisection
from typing import Callable

def func(x: int | float) -> int|float:
    """This is the arbitrary function that we want to know the root of.
    """
    return x**2 - 4

def root_by_bisection(func: Callable[[int|float], int|float], guess: tuple[int|float], tolerance: float = 1.0e-6) -> tuple[float, float]:
    left = guess[0]
    right = guess[1]
    dx = abs(right-left)
    
    while dx > tolerance:
        midpoint = (left-right)/2.
        
        # Check if func(first) and func(mid) is on opposite sign 
        if (func(left)*func(midpoint)) < 0:
            # If opposite sign a*b => - (root is between first and midpoint)
            right = midpoint
        else:
            # If same sign a*b => + (root is not between first and midpoint)
            left = midpoint
        #  Repeat loop with updated points and interval
        dx = abs(right-left)
    
    return midpoint, dx


if __name__ == "__main__":
    x, uncertainty = root_by_bisection(guess=(0,6),func=func)
    print(f"Function {func.__name__} has root at {x:.8f} +_ {uncertainty:.8f}")