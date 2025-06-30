import numpy as np
import matplotlib.pyplot as plt
a_1,a_0,b_1,b_0=-3,4,0,2
x=np.linspace(0,1,1000)


def f_A(x): 
     return x*a_1 + (1-x)*a_0
def f_B(x):
     return x*b_1 + (1-x)*b_0
def dxdt(x):
     return x*(1-x)*(f_A(x)-f_B(x))


numerator= b_0-a_0
denominator= a_1-a_0-b_1+b_0


if denominator !=0:
    internal_eq = numerator / denominator
else:
    internal_eq = None
if internal_eq is not None and 0<internal_eq<1:
     plt.plot(internal_eq,0,'bo')
     plt.text(internal_eq,0,'$f_A=f_B$',va='bottom')


plt.plot(x,dxdt(x),color='green', linewidth=1)

plt.plot(0,0,'ro')
plt.text(0,0.01,'0',va='bottom',ha='right')

plt.plot(1,0,'ro')
plt.text(1,0.01,'1',va='bottom',ha='left')

plt.axhline(0,0,color='black', linewidth=1)
plt.axvline(0,0,color='black', linewidth=1)

plt.fill_between(x, dxdt(x), where=(dxdt(x) >= 0), color='orange')
plt.fill_between(x, dxdt(x), where=(dxdt(x) <= 0), color='yellow')

plt.xlabel("$x$", fontsize=16)
plt.ylabel("$x*(1-x)*(f_A-f_B)$",fontsize=16)

plt.grid(True)
plt.show()
