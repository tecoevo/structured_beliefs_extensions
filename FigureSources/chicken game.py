import numpy as np
import matplotlib.pyplot as plt
R, S, T, P = 3, 1, 5, 0
def replicator_dynamics(x, t):
    """
    Replicator equation for the Chicken Game.
    x: Fraction of population playing Swerve (Cooperate)
    t: Time variable 
    """
    f_C = R * x + S * (1 - x)  
    f_D = T * x + P * (1 - x)  
    avg_payoff = x * f_C + (1 - x) * f_D
    dx_dt = x * (f_C - avg_payoff)
    return dx_dt
t = np.linspace(0, 10, 100)
x_vals = np.linspace(0, 1, 100)  
x_dot = [replicator_dynamics(x, 0) for x in x_vals]
plt.figure(figsize=(8, 5))
plt.plot(x_vals, x_dot, label="dx/dt", color='blue')
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)  
plt.axvline(1/3, color='red', linestyle='dashed', label="$x^* = 1/3$ (Equilibrium)")
plt.xlabel("Fraction of Swerve (Cooperate), x")
plt.ylabel("dx/dt (Rate of Change of x)")
plt.title("Replicator Dynamics of the Chicken Game")
plt.legend()
plt.grid()
plt.show()
