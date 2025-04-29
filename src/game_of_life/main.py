from game_of_life.core.grid import Grid
from game_of_life.core.game import Game
from game_of_life.ui.renderer import PygameRenderer

def main():
    """Main entry point for the Game of Life application."""
    # Create a grid with appropriate dimensions
    grid = Grid(width=80, height=60)
    
    # Initialize the game
    game = Game(grid)
    
    # Initialize and run the renderer
    renderer = PygameRenderer(game, cell_size=10)
    print("Game of Life controls:")
    print("- Click on cells to toggle their state")
    print("- Space: Pause/resume simulation")
    print("- R: Randomize grid")
    print("- C: Clear grid")
    renderer.run(fps=10)

if __name__ == "__main__":
    main()
