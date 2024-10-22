import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.colors as colors

# Set up the grid
n = 128
grid = np.zeros((n, n), dtype=int)

# Create bendy riverbed
def create_riverbed(n):
    x = np.arange(n)
    y = np.sin(x / 10) * 20 + np.sin(x / 20) * 10 + n // 2
    riverbed = np.zeros((n, n), dtype=int)
    for i in range(n):
        riverbed[max(0, int(y[i])-15):min(n, int(y[i])+16), i] = 1
    return riverbed

riverbed = create_riverbed(n)

# Initialize cells only on the left edge of the screen
left_edge = np.where(riverbed[:, 0] == 1)[0]
grid[left_edge[len(left_edge)//2:len(left_edge)//2+1], 0] = 1

def update(frame):
    global grid
    new_grid = grid.copy()
    for i in range(n):
        for j in range(1, n):  # Start from 1 to avoid modifying the left edge
            if riverbed[i, j] == 0:
                new_grid[i, j] = 0  # Cells outside riverbed always die
                continue
            
            # Count live neighbors, with more weight to the left (upstream)
            total = int((grid[i, j-1] * 2 +  # Left neighbor counts double
                         grid[i, (j+1)%n] + 
                         grid[(i-1)%n, j] + 
                         grid[(i+1)%n, j] + 
                         grid[(i-1)%n, j-1] + 
                         grid[(i-1)%n, (j+1)%n] + 
                         grid[(i+1)%n, j-1] + 
                         grid[(i+1)%n, (j+1)%n]))
            
            if grid[i, j] == 1:
                if (total < 3) or (total > 5):
                    new_grid[i, j] = 0
            else:
                if total >= 3 or (total == 2 and np.random.random() < 0.3):
                    new_grid[i, j] = 1

    # Ensure continuous flow from left edge of the screen
    new_grid[left_edge[len(left_edge)//2-7:len(left_edge)//2+8], 0] = 1

    grid = new_grid
    mat.set_data(grid)
    return [mat]

# Set up the figure and animation
fig, ax = plt.subplots(figsize=(10, 10))

# Create a custom colormap: white for dead cells, blue for live cells
cmap = colors.ListedColormap(['white', 'blue'])
bounds = [0, 0.5, 1]
norm = colors.BoundaryNorm(bounds, cmap.N)

mat = ax.matshow(grid, cmap=cmap, norm=norm)
ani = FuncAnimation(fig, update, frames=200, interval=50, save_count=50)
plt.show()