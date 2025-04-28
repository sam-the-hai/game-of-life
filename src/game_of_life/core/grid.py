import numpy as np
from typing import Tuple, List

class Grid:
    """Grid representing the Game of Life world."""
    
    def __init__(self, width: int, height: int):
        """Initialize a grid with the given dimensions.
        
        Args:
            width: The width of the grid
            height: The height of the grid
        """
        self.width = width
        self.height = height
        self.cells = np.zeros((width, height), dtype=np.int8)
        
    def set_cell(self, x: int, y: int, alive: bool) -> None:
        """Set the state of a cell.
        
        Args:
            x: X coordinate (row)
            y: Y coordinate (column)
            alive: True for alive, False for dead
        """
        self.cells[x, y] = 1 if alive else 0
        
    def is_alive(self, x: int, y: int) -> bool:
        """Check if a cell is alive.
        
        Args:
            x: X coordinate (row)
            y: Y coordinate (column)
            
        Returns:
            True if the cell is alive, False otherwise
        """
        return self.cells[x, y] == 1
        
    def count_neighbors(self, x: int, y: int) -> int:
        """Count the number of live neighbors for a cell.
        
        Args:
            x: X coordinate (row)
            y: Y coordinate (column)
            
        Returns:
            Number of live neighbors (0-8)
        """
        # Define neighbor coordinates (including wrapping)
        neighbors = [
            ((x-1) % self.width, (y-1) % self.height), # Top-left
            (x % self.width, (y-1) % self.height), # Top
            ((x+1) % self.width, (y-1) % self.height), # Top-right
            ((x-1) % self.width, y % self.height), # Left
            ((x+1) % self.width, y % self.height), # Right
            ((x-1) % self.width, (y+1) % self.height), # Bottom-left
            (x % self.width, (y+1) % self.height), # Bottom
            ((x+1) % self.width, (y+1) % self.height), # Bottom-right
        ]
        
        # Count live neighbors
        count = 0
        for nx, ny in neighbors:
            if self.is_alive(nx, ny):
                count += 1
                
        return count