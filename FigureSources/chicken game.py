import numpy as np
import matplotlib.pyplot as plt
R, S, T, P = 3, 1, 5, 0
def replicator_dynamics(x):
    f_C = x * R + (1 - x) * S  
    f_D = x * T + (1 - x) * P  
    return x * (1 - x) * (f_C - f_D)
x_values = np.linspace(0, 1, 100)
dx_dt = replicator_dynamics=(x_values)
plt.figure(figsize=(8, 5))
plt.plot(x_values, dx_dt, label=r'$\frac{dx}{dt} = x(1-x)(f_C - f_D)$', color='b')
plt.axhline(0, color='black', linestyle='--', linewidth=1)
plt.axvline(1/3, color='red', linestyle='--', label=r'$x^* = \frac{1}{3}$')
plt.scatter([0, 1], [0, 0], color='red', zorder=3, label='Equilibria')
plt.xlabel("Fraction of population playing Swerve (C)")
plt.ylabel("Rate of change $dx/dt$")
plt.title("Replicator Dynamics for the Chicken Game")
plt.legend()
plt.grid()
plt.show()
