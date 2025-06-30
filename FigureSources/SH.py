import numpy as np
import matplotlib.pyplot as plt
a_1,a_0,b_1,b_0=4,1,3,3 # payoff values
x=np.linspace(0,1,1000)

def f_A(x): 
     return x*a_1 + (1-x)*a_0 # fitness of strategy A
def f_B(x):
     return x*b_1 + (1-x)*b_0 # fitness of strategy B
def dxdt(x):
     return x*(1-x)*(f_A(x)-f_B(x)) # replicator dynamics

numerator= b_0-a_0
denominator= a_1-a_0-b_1+b_0 # finding the internal equilibria


if denominator !=0:
    internal_eq = numerator / denominator
else:
    internal_eq = None 
if internal_eq is not None and 0<internal_eq<1:
     plt.plot(internal_eq,0,'bo')
     plt.text(internal_eq,0.04,'$f_A=f_B$',va='bottom',ha='center') # plotting the internal equilibria


plt.plot(x,dxdt(x),color='green', linewidth=1) # plotting the dynamics
plt.plot(0,0,'ro')
plt.text(0,0.01,'0',va='bottom',ha='left')

plt.plot(1,0,'ro')
plt.text(1,0.01,'1',va='bottom',ha='center')

plt.axhline(0,0, color='black', linewidth=1)
plt.axvline(0,0, color='black', linewidth=1)

plt.fill_between(x, dxdt(x), where=(dxdt(x) >= 0), color='orange')
plt.fill_between(x, dxdt(x), where=(dxdt(x) <= 0), color='yellow')

plt.xlabel("$x$", fontsize=13)
plt.ylabel("$x*(1-x)*(f_A-f_B)$",fontsize=13)

plt.grid(True)
plt.show()



