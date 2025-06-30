import numpy as np
import matplotlib.pyplot as plt
import mpltern
from scipy.integrate import odeint


def dxdt(x,t):
    A=np.array([[0,1,-1],
            [-1,0,1],
            [1,-1,0]]) #payoff
    f_i= np.dot(A,x) #average fitness of a strategy
    avg_f= np.dot(f_i,x) #average fitness of a population
    dxdt= x*(f_i-avg_f)
    return dxdt  # replicator dynamics


x_0=np.array([0.4,0.3,0.3]) # initial trajectory points
t=np.linspace(0,150,1000) # time
traj=odeint(dxdt,x_0,t) # solving the replicator dynamics
internal_eq=np.array([1/3,1/3,1/3]) # internal equilibrium


fig = plt.figure(figsize=(6, 6))
ax = plt.subplot(projection='ternary')


ax.set_tlabel('Rock') #labels
ax.set_llabel('Paper')
ax.set_rlabel('Scissors') 

ax.plot([internal_eq[0]],[internal_eq[1]], [internal_eq[2]],'bo') # plotting the internal equilibrium
ax.plot(traj[:,0],traj[:,1],traj[:, 2],color='green') # plotting the trajectory

plt.grid(True)
plt.show()
