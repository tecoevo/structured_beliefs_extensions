import numpy as np
import matplotlib.pyplot as plt

R, S, T, P = 3, 0, 5, 1  
def replicator_dynamics(x):
    f_C = x * R + (1 - x) * S  
    f_D = x * T + (1 - x) * P  
    return x * (1 - x) * (f_C - f_D)
x_values = np.linspace(0, 1, 100)
dx_dt_values = replicator_eq=(x_values)
plt.figure(figsize=(8, 5))
plt.plot(x_values, dx_dt_values, label=r'$\frac{dx}{dt} = x(1-x)(f_C - f_D)$', color='b')
plt.axhline(0, color='black', linestyle='--', linewidth=1)  
plt.scatter([0, 1], [0, 0], color='red', zorder=3, label='Equilibria')
for x in np.linspace(0.1, 0.9, 5):
    plt.arrow(x, replicator_eq(x), 0.02, replicator_eq(x) * 0.1, head_width=0.02, color='black')
plt.xlabel("Fraction of Cooperators (x)")
plt.ylabel("Rate of Change (dx/dt)")
plt.title("Replicator Dynamics in Prisoner's Dilemma")
plt.legend()
plt.grid(True)
plt.show()
