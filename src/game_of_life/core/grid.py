# src/game_of_life/core/grid.py
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
        self.cells = np.zeros((height, width), dtype=np.int8)
        
    def set_cell(self, x: int, y: int, alive: bool) -> None:
        """Set the state of a cell.
        
        Args:
            x: X coordinate (column)
            y: Y coordinate (row)
            alive: True for alive, False for dead
        """
        self.cells[y, x] = 1 if alive else 0
        
    def is_alive(self, x: int, y: int) -> bool:
        """Check if a cell is alive.
        
        Args:
            x: X coordinate (column)
            y: Y coordinate (row)
            
        Returns:
            True if the cell is alive, False otherwise
        """
        return self.cells[y, x] == 1
        
    def count_neighbors(self, x: int, y: int) -> int:
        """Count the number of live neighbors for a cell.
        
        Args:
            x: X coordinate (column)
            y: Y coordinate (row)
            
        Returns:
            Number of live neighbors (0-8)
        """
        count = 0
        
        # Check all 8 neighbors with wrapping
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                # Skip the cell itself
                if dx == 0 and dy == 0:
                    continue
                    
                # Calculate neighbor position with wrapping
                nx = (x + dx) % self.width
                ny = (y + dy) % self.height
                
                if self.is_alive(nx, ny):
                    count += 1
                    
        return count
