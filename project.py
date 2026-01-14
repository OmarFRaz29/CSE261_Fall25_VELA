print("Welcome to our project!")

import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D 
print("CTCS Vibrating String Simulation Started")













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