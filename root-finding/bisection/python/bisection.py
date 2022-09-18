# Root by bisection
from dataclasses import dataclass
from typing import Callable

@dataclass
class PhysicalValue:
    value: float
    uncertainty: float

def foo(point: float) -> float:
    """This is the arbitrary function that we want to know the root of.
    """
    ## Use this to set illegal values
    # if point == 0.:
    #     raise ValueError(f'Value {point} is illegal')
    return point**2 - 4

def root_by_bisection(func: Callable[[float], float], left: float, right: float, tolerance: float = 1.0e-6) -> PhysicalValue:
    interval = abs(right-left)
    
    while interval > tolerance:
        midpoint = (left-right)/2.
        
        # Check if func(first) and func(mid) is on opposite sign 
        if (func(left)*func(midpoint)) < 0:
            # If opposite sign a*b => - (root is between first and midpoint)
            right = midpoint
        else:
            # If same sign a*b => + (root is not between first and midpoint)
            left = midpoint
        #  Repeat loop with updated points and interval
        interval = abs(right-left)
    
    return PhysicalValue(value=midpoint, uncertainty=interval/2)


if __name__ == "__main__":
    answer: PhysicalValue = root_by_bisection(guess=(0,6),func=foo)
    print(f"Function {foo.__name__} has root at {answer.value:.8f} +_ {answer.uncertainty:.8f}")