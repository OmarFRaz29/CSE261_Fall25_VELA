print("Welcome to our project!")

import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D 
print("CTCS Vibrating String Simulation Started")


# Mamber 3 salman islam Tonmoy:
x = np.linspace(0, L, Nx) 
t = np.linspace(0, T, Nt) 
u = np.zeros((Nt, Nx))




# member 2 Fahim Islam Prithy:
dx = L / (Nx - 1); dt = T / (Nt - 1) 
r = (c * dt / dx) ** 2 
print("CFL number:", r)



# member 5 Mehedi Hasan Dipu:
for i in range(1, Nx - 1): 
    u[1, i] = u[0, i] + 0.5 * r * (u[0, i+1] - 2*u[0, i] + u[0, i-1])
    
     
u[1, 0] = 0.0
u[1, -1] = 0.0




# member 7 Rakibul Hasan Rakib:
energy = np.zeros(Nt)
for n in range(Nt - 1):
    ke = 0.0
    pe = 0.0
    for i in range(1, Nx - 1):
        v = (u[n+1, i] - u[n, i]) / dt
        g = (u[n, i+1] - u[n, i-1]) / (2*dx)
        ke += 0.5 * v*v * dx
        pe += 0.5 * c*c * g*g * dx
    energy[n] = ke + pe
print("Initial Energy:", energy[0])
print("Final Energy:", energy[Nt-2])


# member 9 Abyaj ahmed asif: 
X, TT = np.meshgrid(x, t) 
fig = plt.figure(figsize=(10,7)) 
ax = fig.add_subplot(111, projection='3d') 
ax.plot_surface(X, TT, u, cmap='viridis') 
ax.set_xlabel("Position"); 
ax.set_ylabel("Time"); 
ax.set_zlabel("Displacement") 
ax.set_title("3D Vibrating String Motion") 
plt.show() 
print("Simulation Completed Successfully")