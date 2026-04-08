import pygame

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

# Griglia
GRID_ROWS = 3
GRID_COLS = 3
HOLE_RADIUS = 60
GRID_MARGIN = 60

# Colori
COLOR_BG = (30, 30, 40)
COLOR_HOLE = (90, 90, 100)
COLOR_HOLE_ON = (230, 140, 40)


def hole_center(index: int) -> tuple[int, int]:
    """Restituisce le coordinate (x, y) del centro del buco i-esimo."""
    if index < 0 or index >= GRID_COLS * GRID_ROWS:
        raise ValueError("Indice non esistente")

    row = index // GRID_COLS
    col = index % GRID_COLS

    available_width = WINDOW_WIDTH - (2 * GRID_MARGIN)
    available_height = WINDOW_HEIGHT - (2 * GRID_MARGIN)

    cell_width = available_width // GRID_COLS
    cell_height = available_height // GRID_ROWS

    cx = GRID_MARGIN + (col * cell_width) + (cell_width // 2)
    cy = GRID_MARGIN + (row * cell_height) + (cell_height // 2)

    return (cx, cy)


class GameView:
    def __init__(self, screen) -> None:
        self.screen = screen

    def draw(self, model) -> None:
        self.screen.fill(COLOR_BG)

        for i, hole in enumerate(model.holes):
            center = hole_center(i)
            if hole.is_active:
                color = COLOR_HOLE_ON
            else:
                color = COLOR_HOLE

            pygame.draw.circle(self.screen, color, center, HOLE_RADIUS)

        pygame.display.flip()
