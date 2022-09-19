# Root by bisection
from dataclasses import dataclass
from typing import Callable

@dataclass
class Answer:
    value: float
    uncertainty: float

def foo(point: float) -> float:
    """This is the arbitrary function that we want to know the root of.
    """
    ## Use this to set illegal values
    # if point == 0.:
    #     raise ValueError(f'Value {point} is illegal')
    return point**2 - 4

def root_by_bisection(func: Callable[[float], float], left: float, right: float, tolerance: float = 1.0e-6, limit: int = 100) -> Answer:
    interval = abs(right-left)
    
    run: int = 1
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
        run += 1
        if run == limit: raise ValueError(f'Loop has run {limit} times and no answer was found. Consider using other intervals.')
    
    return Answer(value=midpoint, uncertainty=interval/2)


if __name__ == "__main__":
    answer: Answer = root_by_bisection(func=foo,left=0,right=6)
    print(f"Function {foo.__name__} has root at {answer.value:.8f} +_ {answer.uncertainty:.8f}")