import numpy as np

class Grid:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.grid = np.full((self.grid_size, self.grid_size), '.', dtype=str)

    # Draw the grid
    def draw(self):
        print("\n")
        for row in self.grid:
            for cell in row:
                print(f"{cell}   ", end = "")
            print("\n")

    # Update the grid with the next move
    def update(self, move, symbol):
        self.grid[move[0]][move[1]] = symbol

    # Checks if the grid is true to the win condition
    def check_win(self, symbol):
        for i in range(self.grid_size):
            if all(self.grid[i, j] == symbol for j in range(self.grid_size)) or all(self.grid[j, i] == symbol for j in range(self.grid_size)):
                return True
            
            if all(self.grid[i, i] == symbol for i in range(self.grid_size)) or all(self.grid[i, self.grid_size-i-1] == symbol for i in range(self.grid_size)):
                return True
            
        return False