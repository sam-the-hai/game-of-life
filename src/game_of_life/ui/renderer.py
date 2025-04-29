import pygame
import sys
from game_of_life.core.grid import Grid
from game_of_life.core.game import Game

class PygameRenderer:
    """Pygame-based renderer for the Game of Life."""
    
    def __init__(self, game: Game, cell_size: int = 10):
        """Initialize the renderer.
        
        Args:
            game: The game to render
            cell_size: The size of each cell in pixels
        """
        self.game = game
        self.cell_size = cell_size
        self.width = game.grid.width * cell_size
        self.height = game.grid.height * cell_size
        
        # Initialize pygame
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Game of Life")
        self.clock = pygame.time.Clock()
        
    def run(self, fps: int = 10):
        """Run the game loop.
        
        Args:
            fps: Frames per second (controls simulation speed)
        """
        running = True
        paused = False
        
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        paused = not paused
                    elif event.key == pygame.K_r:
                        # Randomize the grid
                        self._randomize_grid()
                    elif event.key == pygame.K_c:
                        # Clear the grid
                        self._clear_grid()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Toggle cell state on click
                    pos = pygame.mouse.get_pos()
                    x, y = pos[0] // self.cell_size, pos[1] // self.cell_size
                    self.game.grid.set_cell(x, y, not self.game.grid.is_alive(x, y))
            
            # Update game state (if not paused)
            if not paused:
                self.game.step()
            
            # Render the grid
            self._render()
            
            # Control game speed
            self.clock.tick(fps)
        
        pygame.quit()
        
    def _render(self):
        """Render the current state of the grid."""
        # Clear the screen
        self.screen.fill((0, 0, 0))
        
        # Draw each cell
        for y in range(self.game.grid.height):
            for x in range(self.game.grid.width):
                if self.game.grid.is_alive(x, y):
                    rect = pygame.Rect(
                        x * self.cell_size, 
                        y * self.cell_size,
                        self.cell_size,
                        self.cell_size
                    )
                    pygame.draw.rect(self.screen, (255, 255, 255), rect)
        
        # Draw grid lines
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, (50, 50, 50), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, (50, 50, 50), (0, y), (self.width, y))
            
        # Update the display
        pygame.display.flip()
        
    def _randomize_grid(self):
        """Fill the grid with random cells."""
        import numpy as np
        self.game.grid.cells = np.random.choice([0, 1], size=(self.game.grid.height, self.game.grid.width), p=[0.8, 0.2])
    
    def _clear_grid(self):
        """Clear all cells in the grid."""
        self.game.grid.cells.fill(0)
