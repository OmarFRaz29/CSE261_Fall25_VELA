print("Welcome to our project!")

import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D 
print("CTCS Vibrating String Simulation Started")





# member 5 Mehedi Hasan Dipu:
for i in range(1, Nx - 1): 
    u[1, i] = u[0, i] + 0.5 * r * (u[0, i+1] - 2*u[0, i] + u[0, i-1])
    
     
u[1, 0] = 0.0
u[1, -1] = 0.0







# member 8 Abyaj ahmed asif: 
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