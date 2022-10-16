# main.py
# Root by Secant

from dataclasses import dataclass
from typing import Callable

@dataclass
class Answer:
    value: float
    uncertainty: float

def foo(point: float) -> float:
    return point**2 - 4

def root_by_secant(func: Callable[[float], float], first: float, second: float, tolerance: float = 1.0e-6, limit: int = 100) -> Answer:
    interval: float = abs(second - first)

    def slope(first: float, second: float) -> float:
        x_diff = second - first
        y_diff = func(second) - func(first)
        try:
            _slope = y_diff/x_diff
        except ZeroDivisionError:
            _slope = 0
        return _slope
        

    run: int = 0
    while interval > tolerance:
        y_intercept = func(first) - slope(first, second)*first
        x_intercept = -y_intercept / slope(first, second)
        interval = abs(first - x_intercept)
        # check if the first interval is smaller than second interval
        if interval < (candidate_interval:=abs(second - x_intercept)):
            second = first
        else:
            interval = candidate_interval
        first = x_intercept
        run += 1
        if run == limit: raise ValueError(f'Loop has run {limit} times and no answer was found. Consider using other interval.')

    
    return Answer(value=x_intercept, uncertainty=interval/2)

if __name__ == "__main__":
    answer: Answer = root_by_secant(func=foo, first=0, second=0.1)
    print(f"Function {foo.__name__} has root at {answer.value:.8f} +_ {answer.uncertainty:.8f}")