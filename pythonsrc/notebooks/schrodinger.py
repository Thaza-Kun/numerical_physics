# %%
import numpy as np
from numpy import ndarray
import matplotlib.pyplot as plt
from matplotlib import animation

from scipy import sparse, integrate


# %%
# Set x range
dx: float = 0.02
x: ndarray = np.arange(0, 10, dx)

# Wave properties
k_x: float = 0.1  # Wave number
m: float = 1.0  # Mass of wave

# Wave packet initialization
wave_w: float = 0.1  # Width of initial gaussian wave packet
wave_x: float = 3.0  # Center of initial gaussian wave packet

A: float = 1.0 / (wave_w * np.sqrt(np.pi))  # Normalization constant

# %%
# Potential function
V_height = 50
V = np.zeros(x.shape)
for i, _x in enumerate(x):
    if _x >= 4.5 and _x <= 5.5:
        V[i] = V_height

# %%
# Laplace Operator
D2: sparse.dia_matrix = (
    sparse.diags([1, -2, 1], [-1, 0, 1], shape=(x.size, x.size)) / dx**2
)
D2.toarray() * dx**2

# %%
psi_0: ndarray = (
    np.exp(-((x - wave_x) ** 2) / (2.0 * wave_w**2))
    * np.exp(1j * k_x * x)
    * np.sqrt(A)
)

# %%
# Defining the Schrodinger wave function

hbar: float = 1.0


def psi_t(t: ndarray, psi: ndarray, potential: ndarray) -> ndarray:
    return -1j * ((-0.5 * hbar / m) * D2.dot(psi) + (potential / hbar) * psi)


# %%
# We will use scipy to solve the equations

dt: float = 0.005  # time interval for snapshots
t0: float = 0.0  # initial time
tf: float = 1.0  # final time
t_eval: ndarray = np.arange(t0, tf, dt)  # recorded time shots

# Solve the Initial Value Problem
sol = integrate.solve_ivp(
    psi_t, t_span=[t0, tf], y0=psi_0, t_eval=t_eval, method="RK23", args=(V,)
)

# %%
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

# %%
anim.save(f"sho_v{V_height}.mp4", fps=15, extra_args=["-vcodec", "libx264"], dpi=300)

# %%
