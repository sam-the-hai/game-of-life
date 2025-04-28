# tests/test_grid.py

import pytest
import numpy as np
from game_of_life.core.grid import Grid

def test_grid_initialization():
    """Test that the grid is initialized correctly."""
    grid = Grid(width=10, height=15)

    # Dimensions should match
    assert grid.width == 10
    assert grid.height == 15
    assert grid.cells.shape == (15, 10)

    # All cells should be dead initially
    assert np.all(grid.cells == 0)


def test_set_cell_state():
    """Test setting cell state."""
    grid = Grid(width=4, height=3)
    
    # Set a pattern:
    # (x = column, y = row)
    # Visualize the grid:
    # 
    #       x=0  x=1  x=2  x=3
    #       +----+----+----+----+
    # y=0   |  1 |  1 |  0 |  0 |
    #       +----+----+----+----+
    # y=1   |  0 |  0 |  0 |  0 |
    #       +----+----+----+----+
    # y=2   |  0 |  1 |  1 |  0 |
    #       +----+----+----+----+

    # (1 = alive, 0 = dead)

    # Wrapping: when x or y overflows, it wraps around.
    #
    grid.set_cell(x=0, y=0, alive=True)
    grid.set_cell(x=1, y=0, alive=True)
    grid.set_cell(x=1, y=2, alive=True)
    grid.set_cell(x=2, y=2, alive=True)

    # Validate the pattern
    expected = np.array([
        [1, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0],
    ], dtype=np.int8)

    np.testing.assert_array_equal(grid.cells, expected)


def test_count_neighbors():
    """Test counting neighbors with wrapping.

    Visualize the grid:
    
    x=0  x=1  x=2  x=3
    +----+----+----+----+
y=0 |  1 |  1 |  0 |  0 |
    +----+----+----+----+
y=1 |  0 |  0 |  0 |  0 |
    +----+----+----+----+
y=2 |  0 |  1 |  1 |  0 |
    +----+----+----+----+

    (1 = alive, 0 = dead)

    Wrapping: when x or y overflows, it wraps around.
    
     x=3   x=0  x=1  x=2  x=3 x=0
    +----+----+----+----+----+----+
y=2 |  0 |  0 |  1 |  1 |  0 |  0 |
    +----+----+----+----+----+----+
y=0 |  0 |  1 |  1 |  0 |  0 |  1 |
    +----+----+----+----+----+----+
y=1 |  0 |  0 |  0 |  0 |  0 |  0 |
    +----+----+----+----+----+----+
y=2 |  0 |  0 |  1 |  1 |  0 |  0 |
    +----+----+----+----+----+----+
y=0 |  0 |  1 |  1 |  0 |  0 |  1 |
    +----+----+----+----+----+----+
    """
    grid = Grid(width=4, height=3)
    grid.set_cell(x=0, y=0, alive=True)
    grid.set_cell(x=1, y=0, alive=True)
    grid.set_cell(x=1, y=2, alive=True)
    grid.set_cell(x=2, y=2, alive=True)

    # Now checking each cell's live neighbors
    assert grid.count_neighbors(x=0, y=0) == 2
    assert grid.count_neighbors(x=1, y=0) == 3
    assert grid.count_neighbors(x=2, y=0) == 3
    assert grid.count_neighbors(x=3, y=0) == 2

    assert grid.count_neighbors(x=0, y=1) == 3
    assert grid.count_neighbors(x=1, y=1) == 4
    assert grid.count_neighbors(x=2, y=1) == 3
    assert grid.count_neighbors(x=3, y=1) == 2

    assert grid.count_neighbors(x=0, y=2) == 3
    assert grid.count_neighbors(x=1, y=2) == 3
    assert grid.count_neighbors(x=2, y=2) == 2
    assert grid.count_neighbors(x=3, y=2) == 2
