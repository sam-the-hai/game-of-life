import pytest
from game_of_life.core.grid import Grid
from game_of_life.core.game import Game

def test_game_step():
    """Test that the game correctly applies the rules for one step."""
    # Given a grid with a specific pattern (blinker)
    grid = Grid(width=5, height=5)
    # Create a horizontal line:
    # 0 0 0 0 0
    # 0 0 0 0 0
    # 0 1 1 1 0
    # 0 0 0 0 0
    # 0 0 0 0 0
    grid.set_cell(1, 2, True)
    grid.set_cell(2, 2, True)
    grid.set_cell(3, 2, True)
    
    game = Game(grid)
    
    # When we update the grid
    game.step()
    
    # Then the grid should show a vertical line (blinker oscillator)
    # 0 0 0 0 0
    # 0 0 1 0 0
    # 0 0 1 0 0
    # 0 0 1 0 0
    # 0 0 0 0 0
    assert game.grid.is_alive(1, 2) == False
    assert game.grid.is_alive(2, 2) == True
    assert game.grid.is_alive(3, 2) == False
    assert game.grid.is_alive(2, 1) == True
    assert game.grid.is_alive(2, 3) == True
    
    # When we update again
    game.step()
    
    # Then we should be back to the horizontal line
    assert game.grid.is_alive(1, 2) == True
    assert game.grid.is_alive(2, 2) == True
    assert game.grid.is_alive(3, 2) == True
    assert game.grid.is_alive(2, 1) == False
    assert game.grid.is_alive(2, 3) == False

    