import numpy as np
import matplotlib.pyplot as plt


fa_values = [2, 6, 10, 14]
fb_values = [1, 4, 10,18]

x = np.linspace(0, 1, 100)  

plt.figure(figsize=(8, 6))


for fa, fb in zip(fa_values, fb_values):
    f_diff = fa - fb
    y = x * (1 - x) * f_diff  
    label = f"fa={fa}, fb={fb}"
    plt.plot(x, y, label=label)

plt.axhline(0, color='black', linewidth=0.5, linestyle='--') 
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')  
plt.xlabel("x")
plt.ylabel("x(1-x)(fa - fb)")
plt.title("Plot of x(1-x)(fa - fb) for different fa and fb values")
plt.legend()
plt.grid()
plt.show()


