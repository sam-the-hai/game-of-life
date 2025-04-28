from game_of_life.core.grid import Grid
import numpy as np


class Game:
    """Game of Life simulation."""

    def __init__(self, grid: Grid):
        """Initialize the game with a grid.
        
        Args:
            grid: The grid to use for the simulation
        """
        self.grid = grid

    def step(self) -> None:
        """Advance the game by one generation."""
        
        # Create a copy of the current grid state
        new_cells = np.zeros_like(self.grid.cells)

        # Apply the rules to each cell
        for x in range(self.grid.width):
            for y in range(self.grid.height):
                neighbors = self.grid.count_neighbors(x, y)
                is_alive = self.grid.is_alive(x, y)
                
                # Apply Conway's rules (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
                # 1.Any live cell with fewer than two live neighbours dies, as if by underpopulation.
                # 2.Any live cell with two or three live neighbours lives on to the next generation.
                # 3.Any live cell with more than three live neighbours dies, as if by overpopulation.
                # 4.Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
                if is_alive and (neighbors < 2 or neighbors > 3):
                    # Cell dies (underpopulation or overpopulation)
                    new_cells[y, x] = 0
                elif is_alive and (neighbors == 2 or neighbors == 3):
                    # Cell survives
                    new_cells[y, x] = 1
                elif not is_alive and neighbors == 3:
                    # Cell becomes alive (reproduction)
                    new_cells[y, x] = 1
                else:
                    # Cell remains dead
                    new_cells[y, x] = 0

        # Update the grid with the new state
        self.grid.cells = new_cells
