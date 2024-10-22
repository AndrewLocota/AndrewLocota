import numpy as np
import time
import os

# Constants
ALIVE = 1
DEAD = 0

# Function to print the grid
def print_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        for cell in row:
            print('█' if cell == ALIVE else ' ', end=' ')
        print()
    print()

# Function to count live neighbors
def count_live_neighbors(grid, x, y):
    rows, cols = grid.shape
    live_neighbors = 0
    
    # Iterate over the 8 neighboring cells
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue  # Skip the cell itself
            neighbor_x = (x + i) % rows
            neighbor_y = (y + j) % cols
            live_neighbors += grid[neighbor_x, neighbor_y]
    
    return live_neighbors

# Function to apply the Game of Life rules
def game_of_life_step(grid):
    new_grid = np.copy(grid)
    rows, cols = grid.shape
    
    for x in range(rows):
        for y in range(cols):
            live_neighbors = count_live_neighbors(grid, x, y)
            
            if grid[x, y] == ALIVE:
                # Rule 1 and 3: underpopulation or overpopulation
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[x, y] = DEAD
            else:
                # Rule 4: reproduction
                if live_neighbors == 3:
                    new_grid[x, y] = ALIVE
    
    return new_grid

# Main function to run the simulation
def run_game_of_life(rows=20, cols=40, steps=100, delay=0.1):
    # Random initial grid
    grid = np.random.choice([ALIVE, DEAD], size=(rows, cols))
    
    for _ in range(steps):
        print_grid(grid)
        grid = game_of_life_step(grid)
        time.sleep(delay)

# Run the Game of Life simulation
if __name__ == "__main__":
    run_game_of_life()

