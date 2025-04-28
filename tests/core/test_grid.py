import pytest
import numpy as np
from game_of_life.core.grid import Grid

def test_grid_initialization():
    """Test that the grid is initialized correctly."""
    grid = Grid(width=10, height=15)
    
    # Then dimensions should match
    assert grid.width == 10
    assert grid.height == 15
    assert grid.cells.shape == (10, 15)
    
    # Then all cells should be dead
    assert np.all(grid.cells == 0)
    
def test_set_cell_state():
    """Test setting cell state."""
    # Given a grid
    grid = Grid(width=10, height=10)
    
    # When we set a cell to alive
    grid.set_cell(x=5, y=5, alive=True)
    
    # Then the cell should be alive
    assert grid.is_alive(x=5, y=5) == True
    
    # When we set a cell to dead
    grid.set_cell(x=5, y=5, alive=False)
    
    # Then the cell should be dead
    assert grid.is_alive(x=5, y=5) == False
    
def test_count_neighbors():
    """Test counting neighbors of a cell."""
    # Given a grid with a pattern
    grid = Grid(width=3, height=3)
    # Create a pattern:
    # 1 1 0
    # 0 0 0
    # 0 1 1
    grid.set_cell(x=0, y=0, alive=True)
    grid.set_cell(x=0, y=1, alive=True)
    grid.set_cell(x=2, y=1, alive=True)
    grid.set_cell(x=2, y=2, alive=True)
    
    # When we count neighbors
    # Then each cell should have correct neighbor count
    # 1   0 1 1   0
    #    - - - -
    # 0 | 1 1 0 | 1
    # 0 | 0 0 0 | 0
    # 1 | 0 1 1 | 0
    #    - - - -
    # 0   1 1 0   1
    assert grid.count_neighbors(x=0, y=0) == 3
    assert grid.count_neighbors(x=0, y=1) == 3
    assert grid.count_neighbors(x=0, y=2) == 4
    assert grid.count_neighbors(x=1, y=0) == 4
    assert grid.count_neighbors(x=1, y=1) == 4
    assert grid.count_neighbors(x=1, y=2) == 4
    assert grid.count_neighbors(x=2, y=0) == 4
    assert grid.count_neighbors(x=2, y=1) == 3
    assert grid.count_neighbors(x=2, y=2) == 3