from dataclasses import dataclass
from typing import Callable, Tuple
from scipy import integrate

@dataclass
class Answer:
    value: float
    uncertainty: float

def foo(point: float) -> float:
    return 7*point**2 - 4

def integrate_simple(func: Callable[[float], float], left: float, right: float, n_slices: int):
    Integral: float = 0
    uncertainty: float = 0
    dx = (right-left)/n_slices
    for i in range(n_slices):
        point = right + dx * i
        Integral += func(point)*dx
        uncertainty += abs(func(point) - func(point+dx))*dx
    return Answer(value=Integral, uncertainty=uncertainty/2)


if __name__ == "__main__":
    left = -2
    right = 2
    # Something's wrong. The answer is different in scipy
    answer: Answer = integrate_simple(func=foo,left=left,right=right, n_slices=100)
    scpy: Tuple[float, float] = integrate.quad(func=foo, a=left, b=right)
    print(f"Function {foo.__name__} has of {answer.value:.8f} +_ {answer.uncertainty:.8f} from x={left} to x={right}")
    print(f"Function {foo.__name__} has of {scpy[0]:.8f} +_ {scpy[0]:.8f} from x={left} to x={right}")