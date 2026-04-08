import math
import pygame

from model.game_model import GameModel
from view.game_view import (
    GameView,
    hole_center,
    HOLE_RADIUS,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
)


class GameController:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.model = GameModel()
        self.view = GameView(self.screen)

    def _hole_at(self, pos: tuple[int, int]) -> int | None:
        for i in range(self.model.NUM_HOLES):
            center = hole_center(i)
            distance = math.dist(pos, center)

            if distance <= HOLE_RADIUS:
                return i

        return None

    def _handle_click(self, pos: tuple[int, int]) -> None:
        index = self._hole_at(pos)

        if index is not None:
            self.model.toggle_hole(index)

    def run(self) -> None:
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self._handle_click(event.pos)

            self.view.draw(self.model)
            self.clock.tick(60)
