import time

import pygame

class Obstacle:

    def __init__(self, pos: tuple[int, int], color: tuple[int, int, int], size: tuple[int, int], special: bool):
        x, y = pos
        w, h =  size
        self.rect  = pygame.Rect(x, y, w, h)
        self.color = color if not special else (50, 220, 100)
        self.active = True
        self.special = special

    @staticmethod
    def update_timer(start_time: float, amount: int):
        if start_time + amount > time.time():
            return time.time()

        return start_time + amount

    def hit(self, start_time):
        self.active = False
        if self.special:
            return self.update_timer(start_time, 10)
        return start_time

    def draw(self, surface: pygame.Surface):
        if self.active:
            pygame.draw.rect(surface, self.color, self.rect, border_radius=4)