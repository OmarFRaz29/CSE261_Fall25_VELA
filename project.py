print("Welcome to our project!")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 

print("CTCS Vibrating String Simulation Started") 
L = 1.0; c = 1.0; T = 2.0 
Nx = 50; Nt = 200 


# Mamber 3 salman islam Tonmoy:
x = np.linspace(0, L, Nx) 
t = np.linspace(0, T, Nt) 
u = np.zeros((Nt, Nx))


# member 2 Fahim Islam Prithy:
dx = L / (Nx - 1); dt = T / (Nt - 1) 
r = (c * dt / dx) ** 2 
print("CFL number:", r)

#Member 4:
px = 0.3; ph = 0.1 
for i in range(Nx): 
 if x[i] <= px: 
  u[0, i] = ph * x[i] / px 
 else: 
  u[0, i] = ph * (L - x[i]) / (L - px) 
  u[0, 0] = 0.0; u[0, -1] = 0.0

# member 5 Mehedi Hasan Dipu:
for i in range(1, Nx - 1): 
    u[1, i] = u[0, i] + 0.5 * r * (u[0, i+1] - 2*u[0, i] + u[0, i-1])
    
     
u[1, 0] = 0.0
u[1, -1] = 0.0


for n in range(1, Nt - 1):
    for i in range(1, Nx - 1):
        u[n+1, i] = 2*u[n, i] - u[n-1, i] + r*(u[n, i+1] - 2*u[n, i] + u[n, i-1])
    u[n+1, 0] = 0.0
    u[n+1, -1] = 0.0




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

#Omar:
steps = [0, 40, 80, 120, 160, 199] 
for s in steps: 
     plt.figure(figsize=(8,4)) 
     plt.plot(x, u[s], linewidth=3) 
     plt.fill_between(x, 0, u[s], alpha=0.3) 
     plt.title("Time = " + str(round(t[s], 3))) 
     plt.xlabel("Position"); plt.ylabel("Displacement") 
     plt.ylim(-0.15, 0.15); plt.grid(True) 
     plt.show() 



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