import numpy as np
import matplotlib.pyplot as plt
R, S, T, P = 3, 0, 5, 1  
def f_C(x):  
    return R * x + S * (1 - x)  
def f_D(x):  
    return T * x + P * (1 - x) s
def replicator_eq(x):
    f_avg = x * f_C(x) + (1 - x) * f_D(x)  
    return x * (f_C(x) - f_avg)  
x_values = np.linspace(0, 1, 100)
dx_dt_values = replicator_eq(x_values)
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
