from dataclasses import dataclass
from typing import Any, List, Tuple, Union
import numpy as np
from scipy import sparse, integrate

import matplotlib.pyplot as plt
from matplotlib import animation

# Define Constants
## Fundamental constants
hbar: float = 1.0

## Canvas constants
dx: float = 0.02
x: np.ndarray = np.arange(0, 10, dx)

## Time constants
dt: float = 0.005  # time interval for snapshots
t0: float = 0.0  # initial time
tf: float = 1.005  # final time
t_eval: np.ndarray = np.arange(t0, tf, dt)  # recorded time shots


## Wave properties
k_x: float = 0.1  # Wave number
m: float = 1.0  # Mass of wave

## Wave packet initialization
wave_w: float = 0.1  # Width of initial gaussian wave packet
wave_x: float = 2.0  # Center of initial gaussian wave packet

A: float = 1.0 / (wave_w * np.sqrt(np.pi))  # Normalization constant

## Potential Function constants
V_height = 0.5 * A


@dataclass
class Laplacian:
    determinant: float
    shape: int

    def __post_init__(self) -> None:
        self.adjoint: sparse.dia_matrix = sparse.diags(
            diagonals=[1, -2, 1], offsets=[-1, 0, 1], shape=(self.shape, self.shape)
        )
        self.matrix: sparse.dia_matrix = self.adjoint / self.determinant**2

    def dot(self, other) -> Any:
        return self.matrix.dot(other)


# Potential function
def step_potential(
    walls: List[float], canvas: np.ndarray, height: float = V_height
) -> np.ndarray:
    for wall in walls:
        if wall > canvas[-1] or wall < canvas[0]:
            raise ValueError("Wall value is not within canvas")
    _walls_copy = walls.copy()

    def _get_bounds(walls) -> Union[Tuple[float, float], Tuple[float]]:
        # For recursive behaviour i.e. when animating the same function
        # if len(walls) == 0:
        #     walls = _walls_copy.copy()
        left: float = walls.pop(0)
        try:
            right: float = walls.pop(0)
            return (left, right)
        except IndexError:
            return (left,)

    V = np.zeros(len(canvas))
    bounds: Union[Tuple[float, float], Tuple[float]] = _get_bounds(walls)
    for i, _x in enumerate(canvas):
        if len(bounds) == 1:
            if _x >= bounds[0]:
                V[i] = height
        elif len(bounds) == 2:
            if _x >= bounds[0] and _x <= bounds[1]:
                V[i] = height
            if _x > bounds[1]:
                if len(walls) > 0:
                    bounds = _get_bounds(walls)
    return V


psi_0: np.ndarray = (
    np.exp(-((x - wave_x) ** 2) / (2.0 * wave_w**2))
    * np.exp(1j * k_x * x)
    * np.sqrt(A)
)


def psi_t(
    t: np.ndarray,
    psi: np.ndarray,
    potential: np.ndarray,
    canvas: np.ndarray = x,
    determinant: float = dx,
) -> np.ndarray:
    laplacian: Laplacian = Laplacian(determinant=dx, shape=canvas.size)
    return -1j * ((-0.5 * hbar / m) * laplacian.dot(psi) + (potential / hbar) * psi)


def run():
    # TODO Output in appropriate file
    V = step_potential(walls=[3, 4, 5], canvas=x)

    sol = integrate.solve_ivp(
        psi_t, t_span=[t0, tf], y0=psi_0, t_eval=t_eval, method="RK23", args=(V,)
    )
    fig = plt.figure()
    ax1 = plt.subplot(1, 1, 1)
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 6)
    title = ax1.set_title("")
    (line1,) = ax1.plot([], [], "k--")
    (line2,) = ax1.plot([], [])

    def init():
        line1.set_data(x, V)
        return (line1,)

    def animate(i):
        line2.set_data(x, np.abs(sol.y[:, i]) ** 2)
        title.set_text("Time = {0:1.3f}".format(sol.t[i]))
        return (line1,)

    anim = animation.FuncAnimation(
        fig, animate, init_func=init, frames=len(sol.t), interval=50, blit=True
    )

    anim.save(
        f"sho_v{V_height:.3f}.mp4", fps=15, extra_args=["-vcodec", "libx264"], dpi=300
    )


if __name__ == "__main__":
    run()
