# main.py
# Root by Newton's Method

from dataclasses import dataclass
from typing import Callable

@dataclass
class Answer:
    value: float
    uncertainty: float

def foo(point: float) -> float:
    return point**2 - 4

def deriv_foo(point: float) -> float:
    if 2*point == 0:
        raise ValueError(f"Illegal value on deriv_func: {point}")
    return 2*point

def root_by_newton(func: Callable[[float], float], deriv_func: Callable[[float], float], initial: float, tolerance: float = 1.0e-6, limit: int = 100) -> Answer:
    interval: float = 2*tolerance # initializes an interval
    point: float = initial # initializes an initial point

    run: int = 0
    while interval > tolerance:
        intercept = point - (func(point) / deriv_func(point))
        interval = abs(point - intercept)
        point = intercept
        run += 1
        if run == limit: raise ValueError(f'Loop has run {limit} times and no answer was found. Consider using other initial point.')

    
    return Answer(value=point, uncertainty=interval/2)

if __name__ == "__main__":
    answer: Answer = root_by_newton(func=foo, deriv_func=deriv_foo, initial=4)
    print(f"Function {foo.__name__} has root at {answer.value:.8f} +_ {answer.uncertainty:.8f}")